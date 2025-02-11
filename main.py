from flask import Flask, json, jsonify
from flask import request
from flask_cors import CORS, cross_origin
from chatbot import respond
from corpus import inicialize_medium_corpus  # Corrected import
from career import return_career
from evaluation import evaluate
from dotenv import load_dotenv
import os
import stripe
import firebase_admin
from firebase_admin import firestore

firebase_admin.initialize_app(
    firebase_admin.credentials.Certificate(
        os.getenv("GOOGLE_APPLICATION_CREDENTIALS"),
    )
)
stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

# app config
app = Flask(__name__)
app.config["CORS_HEADERS"] = "Content-Type"
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
app.config["JWT_TOKEN_LOCATION"] = ["headers", "cookies", "json", "query_string"]

cors = CORS(app)

corpus = inicialize_medium_corpus()


@app.route("/")
def respond():
    return jsonify({"hello": "world"})


@app.route("/respond", methods=["POST"])
@cross_origin()
def respond_route():  # need to move the used question idx to the global scope
    request_data = request.get_json()
    history_in_req = request_data["history"]
    used_question_idx = request_data["used_question_idx"]

    respond(history_in_req, corpus, used_question_idx)

    return jsonify(
        {
            "history": history_in_req,
            "used_question_idx": used_question_idx,
        }
    )


@app.route("/career", methods=["POST"])
@cross_origin()
def career_route():
    request_data = request.get_json()
    history_in_req = request_data["history"]
    career = return_career(history_in_req)
    return jsonify({"career": career})


@app.route("/api/sign", methods=["POST"])
@cross_origin()
def sign_in():  # first check if the customer exists, then act accordingly
    request_data = request.get_json()
    user = request_data.get("user")

    if not user:
        return jsonify({"success": False, "error": "User not specified"}), 400

    try:
        db = firestore.client()
        user_ref = db.collection("users").document(user["uid"]).get()

        if not user_ref.exists:
            return (
                jsonify({"success": False, "error": "User not found"}),
                404,
            )

        user_data = user_ref.to_dict()
        stored_customer_id = user_data.get(
            "stripeCustomerId",
        )  # Correct way to get the field

        if stored_customer_id:
            return jsonify({"success": True, "error": None}), 200

        # Create Stripe customer
        customer = stripe.Customer.create(email=user["email"], name=user["name"])

        # Store Stripe customer ID in Firestore

        db.collection("users").document(user["uid"]).set(
            {"stripeCustomerId": customer.id}, merge=True
        )

        return jsonify({"success": True, "error": None}), 200

    except Exception as e:
        print(f"error in sign_in \n {e}")
        return jsonify({"success": False, "error": str(e)}), 500


@app.route("/api/create-subscription", methods=["POST"])
@cross_origin()
def create_subscription():
    data = request.json
    user_id = data["uid"]

    # Get user from Firestore
    db = firestore.client()
    user_ref = db.collection("users").document(user_id).get()
    if not user_ref.exists:
        return jsonify({"error": "User not found"}), 404

    user_data = user_ref.to_dict()
    stripe_customer_id = user_data["stripeCustomerId"]

    # Create a Stripe subscription
    try:
        subscription = stripe.Subscription.create(
            customer=stripe_customer_id,
            items=[
                {"price": "price_1QqF1UGg7dfr3NgwqDeBnb1T"}
            ],  # Set Stripe Price ID here
            payment_behavior="default_incomplete",
            expand=["latest_invoice.payment_intent"],
        )

        return jsonify(
            {
                "subscriptionId": subscription.id,
                "clientSecret": subscription.latest_invoice.payment_intent.client_secret,
            }
        )
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route("/api/cancel-subscription", methods=["POST"])
@cross_origin()
def cancel_subscription():
    data = request.json
    subscription_id = data["subscriptionId"]

    try:
        stripe.Subscription.delete(subscription_id)

        return jsonify({"message": "Subscription canceled successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400


endpoint_secret = os.getenv("STRIPE_ENDPOINT_SECRET")

print(endpoint_secret)


# @app.route("/webhook", methods=["POST"])
# def stripe_webhook():
#     payload = request.get_data(as_text=True)
#     sig_header = request.headers.get("Stripe-Signature")

#     try:
#         event = stripe.Webhook.construct_event(payload, sig_header, endpoint_secret)
#     except Exception as e:
#         return jsonify({"error": str(e)}), 400

#     print("got event")

#     if event["type"] == "invoice.payment_succeeded":

#         subscription_id = event["data"]["object"]["subscription"]
#         customer_id = event["data"]["object"]["customer"]

#         # Update user subscription status in Firestore
#         db = firestore.client()
#         users_ref = (
#             db.collection("users").where("stripeCustomerId", "==", customer_id).stream()
#         )

#         for user_doc in users_ref:
#             user_doc.reference.update(
#                 {"subscriptionActive": True, "subscriptionId": subscription_id}
#             )

#     elif event["type"] == "customer.subscription.deleted":
#         customer_id = event["data"]["object"]["customer"]

#         # Update subscription status as canceled
#         db = firestore.client()
#         users_ref = (
#             db.collection("users").where("stripeCustomerId", "==", customer_id).stream()
#         )

#         for user_doc in users_ref:
#             user_doc.reference.update({"subscriptionActive": False})

#     return jsonify({"status": "success"}), 200


@app.route("/webhook", methods=["POST"])
def webhook():
    event = None
    payload = request.data

    try:
        event = json.loads(payload)
    except json.decoder.JSONDecodeError as e:
        print("⚠️  Webhook error while parsing basic request." + str(e))
        return jsonify(success=False)
    if endpoint_secret:
        # Only verify the event if there is an endpoint secret defined
        # Otherwise use the basic event deserialized with json
        sig_header = request.headers.get("stripe-signature")
        try:
            event = stripe.Webhook.construct_event(payload, sig_header, endpoint_secret)
        except stripe.error.SignatureVerificationError as e:
            print("⚠️  Webhook signature verification failed." + str(e))
            return jsonify(success=False)

    # Handle the event
    if event["type"] == "invoice.payment_succeeded":

        subscription_id = event["data"]["object"]["subscription"]
        customer_id = event["data"]["object"]["customer"]

        # Update user subscription status in Firestore
        db = firestore.client()
        users_ref = (
            db.collection("users").where("stripeCustomerId", "==", customer_id).stream()
        )

        for user_doc in users_ref:
            user_doc.reference.update(
                {"subscriptionActive": True, "subscriptionId": subscription_id}
            )

    elif event["type"] == "customer.subscription.deleted":
        customer_id = event["data"]["object"]["customer"]

        # Update subscription status as canceled
        db = firestore.client()
        users_ref = (
            db.collection("users").where("stripeCustomerId", "==", customer_id).stream()
        )

        for user_doc in users_ref:
            user_doc.reference.update({"subscriptionActive": False})
    else:
        # Unexpected event type
        print("Unhandled event type {}".format(event["type"]))

    return jsonify(success=True)


if __name__ == "__main__":
    app.run()

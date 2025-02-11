import spacy
import random

nlp = spacy.load("en_core_web_md")


def check_sim(question_intents, response):
    max_similarity = -1
    most_similar_entry = None
    for entry in question_intents:
        # Create a doc for the Question_Text of each entry
        question_doc = nlp(entry)

        # Calculate similarity
        response_doc = nlp(response)
        response_no_stop_words = nlp(
            " ".join([str(t) for t in response_doc if not t.is_stop])
        )
        similarity = response_no_stop_words.similarity(question_doc)

        # Track the entry with the highest similarity score
        if similarity > max_similarity:
            max_similarity = similarity
            most_similar_entry = entry

    return most_similar_entry


def respond(history, corpus, used_question_idx):
    """
    Asks a question after the latest client response.

    Args:
        history: list of dicts, e.g., [{"bot": corpus[id], "client": "I like drawing"}, ...]
        corpus: List of question data, each with "Intent" and "following_intent".
        used_question_idx: List to keep track of used question indexes in the corpus.
    """
    if len(history) == 0:
        # Start the conversation with the first question in the corpus
        bot_content = {
            "Question_Text": corpus[0]["Question_Text"],
            "ID": corpus[0]["ID"],
        }
        history.append({"bot": bot_content, "client": None})
        used_question_idx.append(0)
    else:
        # Get the intent of the last bot question
        prev_question_data_id = history[-1]["bot"]["ID"]
        prev_questions_intents = None

        for question in corpus:
            if int(question["ID"]) == int(prev_question_data_id):
                prev_questions_intents = question["following_intent"]

        print(f"prev question intent:{prev_questions_intents}")
        # refactor the code to look for prev_questions_intents in corpus
        response = history[-1]["client"]

        # Find the most relevant intent based on the client's response
        most_similar_entry = check_sim(prev_questions_intents, response)
        print(f"Most similar entry: {most_similar_entry}")

        # Function to find a new question
        def find_new_question(intents_to_try):
            attempts = 0
            max_attempts = 5  # Limit to prevent infinite loops

            while attempts < max_attempts:
                for intent in intents_to_try:
                    similar_questions = [
                        question for question in corpus if question["Intent"] == intent
                    ]

                    for candidate_question in similar_questions:
                        question_idx_in_corpus = corpus.index(candidate_question)

                        if question_idx_in_corpus not in used_question_idx:
                            used_question_idx.append(question_idx_in_corpus)
                            return candidate_question

                attempts += 1
            return None

        # Try to find a question based on the most similar intent
        question = find_new_question([most_similar_entry])

        # If no question is found, try with all other intents
        if question is None:
            print(
                "No question found for the most similar intent. Broadening the search."
            )
            all_intents = set(q["Intent"] for q in corpus)
            other_intents = all_intents - {most_similar_entry}
            question = find_new_question(other_intents)

        # If a question is still not found, fallback action
        if question is None:
            print("No new questions are available.")
        else:
            bot_content = {
                "Question_Text": question["Question_Text"],
                "ID": question["ID"],
            }
            history.append({"bot": bot_content, "client": None})

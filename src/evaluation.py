import spacy

nlp = spacy.load("en_core_web_md")
# corpus = inicialize_medium_corpus()


def evaluate(history, corpus):
    """
    Evaluates the chatbot's performance based on the client's responses.
    Args:
        history: list of dicts, e.g., [{"bot": corpus[id], "client": "I like drawing"}, ...]
    Returns:
        A list of lists, each containing an intent and its score.
    """

    if len(history) == 0:
        return None
    responses = []
    question_intents = []

    scores = []
    intent_counts = {}  # Dictionary to count occurrences of each intent

    used_question_data = []

    for response in history:
        if response["client"]:
            responses.append(response["client"])
            question_intent = None
            found_question = None

            for question in corpus:
                if int(question["ID"]) == int(response["bot"]["ID"]):
                    found_question = question
                    break

            if found_question:
                used_question_data.append(found_question)
                print(f"the found_question is:{found_question}")
                question_intents.append(found_question["Intent"])
            else:
                print(
                    f"Warning: No matching question found for bot ID {response['bot']['ID']}"
                )

    iter = 0
    print(used_question_data)
    for response in responses:
        example_responses = used_question_data[iter]["example_responses"]
        question_intent = question_intents[iter]
        score = select_simlar(response, example_responses)
        found = False
        for record in scores:
            if record[0] == question_intent:
                record[1] += score
                found = True
                break
        if not found:
            scores.append([question_intent, score])

        # Count the occurrences of each intent
        if question_intent in intent_counts:
            intent_counts[question_intent] += 1
        else:
            intent_counts[question_intent] = 1

        iter += 1

    # Normalize the scores
    for record in scores:
        intent = record[0]
        record[1] /= intent_counts[intent]

    return scores


def select_simlar(response, example_responses):
    max_similarity = -1
    most_similar_response = None

    for example_response in example_responses.values():
        response_doc = nlp(response)
        response_no_stop_words = nlp(
            " ".join([str(t) for t in response_doc if not t.is_stop])
        )
        lemmatised_response = nlp(
            " ".join(
                [
                    str(t.lemma_.rstrip("."))
                    for t in response_no_stop_words
                    if not t.is_stop
                ]
            )
        )
        example_response_doc = nlp(example_response)
        example_response_no_stop_words = nlp(
            " ".join([str(t) for t in example_response_doc if not t.is_stop])
        )
        lemmatized_example_response = nlp(
            " ".join(
                [str(t.lemma_.rstrip(".")) for t in example_response_no_stop_words]
            )
        )
        similarity = lemmatised_response.similarity(lemmatized_example_response)
        if similarity > max_similarity:
            max_similarity = similarity
            most_similar_response = example_response

    key_of_most_similar_response = list(example_responses.keys())[
        list(example_responses.values()).index(most_similar_response)
    ]
    score = int(key_of_most_similar_response)
    return score

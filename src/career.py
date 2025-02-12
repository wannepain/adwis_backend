from src.chatbot import evaluate
from src.corpus import inicialize_medium_corpus

medium_careers = [
    {
        "ID": "1",
        "Career_Name": "Astronaut",
        "Description": "An astronaut is trained to travel and perform tasks in space.",
        "Scores": {
            "Work Environment": 5,
            "Personal Reflection": 5,
            "Interest Expansion": 5,
            "Value Identification": 5,
            "Strengths": 5,
        },
        "Starting_Salary": 65000,
    },
    {
        "ID": "2",
        "Career_Name": "Firefighter",
        "Description": "A firefighter is responsible for responding to fires and other emergencies.",
        "Scores": {
            "Work Environment": 4,
            "Personal Reflection": 3,
            "Interest Expansion": 4,
            "Value Identification": 4,
            "Strengths": 4,
        },
        "Starting_Salary": 45000,
    },
    {
        "ID": "3",
        "Career_Name": "Teacher",
        "Description": "A teacher is responsible for educating students in various subjects.",
        "Scores": {
            "Work Environment": 3,
            "Personal Reflection": 4,
            "Interest Expansion": 3,
            "Value Identification": 3,
            "Strengths": 3,
        },
        "Starting_Salary": 40000,
    },
    {
        "ID": "4",
        "Career_Name": "Software Developer",
        "Description": "A software developer is responsible for designing, coding, and maintaining software applications.",
        "Scores": {
            "Work Environment": 5,
            "Personal Reflection": 4,
            "Interest Expansion": 5,
            "Value Identification": 4,
            "Strengths": 5,
        },
        "Starting_Salary": 70000,
    },
    {
        "ID": "5",
        "Career_Name": "Doctor",
        "Description": "A doctor is responsible for diagnosing and treating patients.",
        "Scores": {
            "Work Environment": 4,
            "Personal Reflection": 4,
            "Interest Expansion": 4,
            "Value Identification": 5,
            "Strengths": 5,
        },
        "Starting_Salary": 120000,
    },
    {
        "ID": "6",
        "Career_Name": "Graphic Designer",
        "Description": "A graphic designer creates visual content to communicate messages.",
        "Scores": {
            "Work Environment": 3,
            "Personal Reflection": 4,
            "Interest Expansion": 4,
            "Value Identification": 5,
            "Strengths": 5,
        },
        "Starting_Salary": 45000,
    },
    {
        "ID": "7",
        "Career_Name": "Civil Engineer",
        "Description": "A civil engineer designs, constructs, and maintains infrastructure projects.",
        "Scores": {
            "Work Environment": 4,
            "Personal Reflection": 3,
            "Interest Expansion": 3,
            "Value Identification": 4,
            "Strengths": 4,
        },
        "Starting_Salary": 60000,
    },
    {
        "ID": "8",
        "Career_Name": "Chef",
        "Description": "A chef is responsible for preparing meals and managing kitchen staff.",
        "Scores": {
            "Work Environment": 4,
            "Personal Reflection": 4,
            "Interest Expansion": 4,
            "Value Identification": 4,
            "Strengths": 5,
        },
        "Starting_Salary": 35000,
    },
    {
        "ID": "9",
        "Career_Name": "Journalist",
        "Description": "A journalist researches, writes, and reports news stories.",
        "Scores": {
            "Work Environment": 3,
            "Personal Reflection": 4,
            "Interest Expansion": 4,
            "Value Identification": 4,
            "Strengths": 4,
        },
        "Starting_Salary": 40000,
    },
    {
        "ID": "10",
        "Career_Name": "Pilot",
        "Description": "A pilot operates aircraft to transport passengers and cargo.",
        "Scores": {
            "Work Environment": 5,
            "Personal Reflection": 4,
            "Interest Expansion": 4,
            "Value Identification": 4,
            "Strengths": 5,
        },
        "Starting_Salary": 80000,
    },
    {
        "ID": "11",
        "Career_Name": "Architect",
        "Description": "An architect designs buildings and oversees their construction.",
        "Scores": {
            "Work Environment": 4,
            "Personal Reflection": 4,
            "Interest Expansion": 4,
            "Value Identification": 5,
            "Strengths": 5,
        },
        "Starting_Salary": 65000,
    },
    {
        "ID": "12",
        "Career_Name": "Lawyer",
        "Description": "A lawyer provides legal advice and represents clients in legal matters.",
        "Scores": {
            "Work Environment": 5,
            "Personal Reflection": 3,
            "Interest Expansion": 4,
            "Value Identification": 4,
            "Strengths": 5,
        },
        "Starting_Salary": 90000,
    },
    {
        "ID": "13",
        "Career_Name": "Nurse",
        "Description": "A nurse provides medical care and support to patients.",
        "Scores": {
            "Work Environment": 4,
            "Personal Reflection": 4,
            "Interest Expansion": 4,
            "Value Identification": 5,
            "Strengths": 4,
        },
        "Starting_Salary": 55000,
    },
    {
        "ID": "14",
        "Career_Name": "Data Scientist",
        "Description": "A data scientist analyzes and interprets complex data to help organizations make decisions.",
        "Scores": {
            "Work Environment": 5,
            "Personal Reflection": 4,
            "Interest Expansion": 5,
            "Value Identification": 5,
            "Strengths": 5,
        },
        "Starting_Salary": 80000,
    },
    {
        "ID": "15",
        "Career_Name": "Pharmacist",
        "Description": "A pharmacist dispenses medications and provides information about their use.",
        "Scores": {
            "Work Environment": 4,
            "Personal Reflection": 3,
            "Interest Expansion": 4,
            "Value Identification": 4,
            "Strengths": 4,
        },
        "Starting_Salary": 70000,
    },
    {
        "ID": "16",
        "Career_Name": "Mechanical Engineer",
        "Description": "A mechanical engineer designs and develops mechanical systems.",
        "Scores": {
            "Work Environment": 4,
            "Personal Reflection": 3,
            "Interest Expansion": 3,
            "Value Identification": 4,
            "Strengths": 4,
        },
        "Starting_Salary": 65000,
    },
    {
        "ID": "17",
        "Career_Name": "Artist",
        "Description": "An artist creates visual art to express ideas and emotions.",
        "Scores": {
            "Work Environment": 3,
            "Personal Reflection": 5,
            "Interest Expansion": 5,
            "Value Identification": 5,
            "Strengths": 5,
        },
        "Starting_Salary": 30000,
    },
    {
        "ID": "18",
        "Career_Name": "Psychologist",
        "Description": "A psychologist studies mental processes and behavior, and provides therapy.",
        "Scores": {
            "Work Environment": 4,
            "Personal Reflection": 4,
            "Interest Expansion": 4,
            "Value Identification": 5,
            "Strengths": 4,
        },
        "Starting_Salary": 60000,
    },
    {
        "ID": "19",
        "Career_Name": "Marketing Manager",
        "Description": "A marketing manager develops strategies to promote products and services.",
        "Scores": {
            "Work Environment": 5,
            "Personal Reflection": 4,
            "Interest Expansion": 4,
            "Value Identification": 4,
            "Strengths": 5,
        },
        "Starting_Salary": 70000,
    },
    {
        "ID": "20",
        "Career_Name": "Environmental Scientist",
        "Description": "An environmental scientist studies the environment and develops solutions to environmental problems.",
        "Scores": {
            "Work Environment": 4,
            "Personal Reflection": 4,
            "Interest Expansion": 5,
            "Value Identification": 5,
            "Strengths": 4,
        },
        "Starting_Salary": 55000,
    },
]
medium_corpus = inicialize_medium_corpus()


def return_career(history, nlp):
    """
    Returns the career that best fits the user's responses
    Args:
        history: list of dicts, e.g., [{"bot": corpus[id], "client": "I like drawing"}, ...]
    Returns:
        The most similar career to the user's responses
    """

    scores = evaluate(history, medium_corpus, nlp)
    if scores is None:
        return None

    # Convert scores to a dictionary for easier comparison
    user_scores = {score[0]: score[1] for score in scores}

    def calculate_similarity(career_scores, user_scores):
        similarity = 0
        for intent, score in user_scores.items():
            if intent in career_scores:
                similarity += abs(career_scores[intent] - score)
        return similarity

    most_similar_career = None
    lowest_similarity = float("inf")

    for career in medium_careers:
        career_scores = career["Scores"]
        similarity = calculate_similarity(career_scores, user_scores)
        if similarity < lowest_similarity:
            lowest_similarity = similarity
            most_similar_career = career

    return most_similar_career

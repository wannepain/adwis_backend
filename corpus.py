small_corpus = [
    {
        "ID": "1",
        "Intent": "General",
        "Question_Text": "Hi! I’m here to help you explore your skills and interests. Ready to start?",
        "following_intent": [],  # add all categories
    },
    {
        "ID": "2",
        "Intent": "Interest Identification",
        "Question_Text": "What’s something you really enjoy doing in your free time?",
        "following_intent": [],
    },
    {
        "ID": "4",
        "Intent": "Skill Discovery",
        "Question_Text": "Have you ever been told you’re good at something? If so, what is it?",
        "following_intent": [],
    },
    {
        "ID": "6",
        "Intent": "Value Identification",
        "Question_Text": "What’s more important to you: creativity, logic, or helping others?",
        "following_intent": [],
    },
    {
        "ID": "7",
        "Intent": "Goal Setting",
        "Question_Text": "Do you have any goals for your future? If yes, can you describe one?",
        "following_intent": [],
    },
    {
        "ID": "8",
        "Intent": "Activity Preference",
        "Question_Text": "Do you prefer working on long-term projects or short, quick tasks?",
        "following_intent": [],
    },
    {
        "ID": "9",
        "Intent": "Personal Reflection",
        "Question_Text": "If you could choose any job without thinking about money, what would it be?",
        "following_intent": [],
    },
    {
        "ID": "10",
        "Intent": "Interest Expansion",
        "Question_Text": "Would you like to explore careers related to your interests or try something completely new?",
        "following_intent": [],
    },
    {
        "ID": "11",
        "Intent": "Learning Style",
        "Question_Text": "How do you prefer to learn new things?",
        "following_intent": [],
    },
]

medium_corpus = [
    {
        "ID": "1",
        "Intent": "General",
        "Question_Text": "Hi! I’m here to help you explore your skills and interests. Ready to start?",
        "following_intent": [],
        "example_responses": {"1": "no", "5": "yes"},
    },
    {
        "ID": "2",
        "Intent": "Interest Identification",
        "Question_Text": "What’s something you really enjoy doing in your free time?",
        "following_intent": [],
        "example_responses": {
            "1": "I have no hobbies or interests.",
            "2": "I sometimes watch TV.",
            "3": "I like reading occasionally.",
            "4": "I enjoy playing sports regularly.",
            "5": "I love painting and creating art whenever possible.",
        },
    },
    {
        "ID": "3",
        "Intent": "Interest Identification",
        "Question_Text": "Do you prefer working with people, technology, or ideas?",
        "following_intent": [],
        "example_responses": {
            "1": "I don't have a preference.",
            "2": "I prefer working with technology but not very often.",
            "3": "I enjoy working with ideas occasionally.",
            "4": "I often like working with people or ideas.",
            "5": "I love collaborating with people and exploring new technologies.",
        },
    },
    {
        "ID": "4",
        "Intent": "Skill Discovery",
        "Question_Text": "Have you ever been told you’re good at something? If so, what is it?",
        "following_intent": [],
        "example_responses": {
            "1": "No, I haven’t.",
            "2": "I’ve been told I’m okay at organizing things.",
            "3": "Some people say I’m good at cooking.",
            "4": "I’ve often been praised for my problem-solving skills.",
            "5": "I’m frequently told I’m a great leader and communicator.",
        },
    },
    {
        "ID": "5",
        "Intent": "Skill Discovery",
        "Question_Text": "Do you enjoy learning new skills or improving the ones you already have?",
        "following_intent": [],
        "example_responses": {
            "1": "Not really, I don’t focus on skills.",
            "2": "I occasionally learn something new.",
            "3": "I like improving my current skills.",
            "4": "I actively look for opportunities to learn.",
            "5": "I’m passionate about constantly learning and growing.",
        },
    },
    {
        "ID": "6",
        "Intent": "Value Identification",
        "Question_Text": "What’s more important to you: creativity, logic, or helping others?",
        "following_intent": [],
        "example_responses": {
            "1": "I don’t have a strong opinion.",
            "2": "I value creativity a little more.",
            "3": "Logic is somewhat important to me.",
            "4": "Helping others is very important to me.",
            "5": "All three are extremely important to me.",
        },
    },
    {
        "ID": "7",
        "Intent": "Goal Setting",
        "Question_Text": "Do you have any goals for your future? If yes, can you describe one?",
        "following_intent": [],
        "example_responses": {
            "1": "I don’t have any goals.",
            "2": "I want to do well in school.",
            "3": "I’m aiming to start a small business.",
            "4": "I have a detailed career plan in place.",
            "5": "I have multiple long-term goals, including personal and professional achievements.",
        },
    },
    {
        "ID": "8",
        "Intent": "Activity Preference",
        "Question_Text": "Do you prefer working on long-term projects or short, quick tasks?",
        "following_intent": [],
        "example_responses": {
            "1": "I don’t like either.",
            "2": "Short tasks are manageable sometimes.",
            "3": "I’m okay with both depending on the situation.",
            "4": "I enjoy long-term projects more.",
            "5": "I thrive on long-term projects and their challenges.",
        },
    },
    {
        "ID": "9",
        "Intent": "Personal Reflection",
        "Question_Text": "If you could choose any job without thinking about money, what would it be?",
        "following_intent": [],
        "example_responses": {
            "1": "I haven’t thought about it.",
            "2": "Maybe something simple like gardening.",
            "3": "A teacher or mentor role.",
            "4": "A career in art or music.",
            "5": "Running my own non-profit organization.",
        },
    },
    {
        "ID": "10",
        "Intent": "Interest Expansion",
        "Question_Text": "Would you like to explore careers related to your interests or try something completely new?",
        "following_intent": [],
        "example_responses": {
            "1": "I’m not interested in exploring careers.",
            "2": "I might try something new.",
            "3": "I’d like to explore a mix of both.",
            "4": "I’m keen on exploring careers related to my interests.",
            "5": "I’m determined to pursue my passion and interests in depth.",
        },
    },
    {
        "ID": "11",
        "Intent": "Learning Style",
        "Question_Text": "How do you prefer to learn new things?",
        "following_intent": [],
        "example_responses": {
            "1": "I don’t like learning new things.",
            "2": "I learn better when someone explains things to me.",
            "3": "I like learning through trial and error.",
            "4": "I prefer hands-on learning experiences.",
            "5": "I enjoy a mix of research, hands-on work, and structured classes.",
        },
    },
    {
        "ID": "12",
        "Intent": "Learning Style",
        "Question_Text": "Do you like working on your own or in groups?",
        "following_intent": [],
        "example_responses": {
            "1": "I don’t enjoy working much at all.",
            "2": "I prefer working alone most of the time.",
            "3": "I’m fine with either, depending on the task.",
            "4": "I enjoy collaborating in groups.",
            "5": "I thrive in group settings and love teamwork.",
        },
    },
    {
        "ID": "13",
        "Intent": "Learning Style",
        "Question_Text": "Do you prefer structured learning or more flexible, self-paced learning?",
        "following_intent": [],
        "example_responses": {
            "1": "I don’t prefer any learning style.",
            "2": "I like structured learning but not always.",
            "3": "I’m comfortable with both styles depending on the context.",
            "4": "I prefer flexible, self-paced learning.",
            "5": "I love self-paced learning as it allows me to focus deeply on my interests.",
        },
    },
    {
        "ID": "14",
        "Intent": "Personality",
        "Question_Text": "Do you enjoy fast-paced environments, or do you prefer working at your own pace?",
        "following_intent": [],
        "example_responses": {
            "1": "I don’t like working at all.",
            "2": "I prefer a slow pace but can adapt occasionally.",
            "3": "I can manage both, depending on the work.",
            "4": "I enjoy working at my own steady pace.",
            "5": "I thrive in fast-paced, high-pressure environments.",
        },
    },
    {
        "ID": "15",
        "Intent": "Personality",
        "Question_Text": "Would you describe yourself as more introverted or extroverted?",
        "following_intent": [],
        "example_responses": {
            "1": "I’m extremely introverted and avoid social interactions.",
            "2": "I’m slightly introverted and prefer smaller groups.",
            "3": "I’m balanced between introversion and extroversion.",
            "4": "I’m slightly extroverted and enjoy social settings.",
            "5": "I’m very extroverted and love being around people.",
        },
    },
    {
        "ID": "16",
        "Intent": "Work Environment",
        "Question_Text": "Do you thrive in a competitive or collaborative work environment?",
        "following_intent": [],
        "example_responses": {
            "1": "I don't like working in any environment.",
            "2": "I prefer collaborative environments.",
            "3": "I don't mind a mix of competitive and collaborative work.",
            "4": "I excel in collaborative work environments.",
            "5": "I thrive in highly competitive settings and love challenges.",
        },
    },
    {
        "ID": "17",
        "Intent": "Career Exploration",
        "Question_Text": "Have you explored different career paths before, or is this your first time thinking about it?",
        "following_intent": [],
        "example_responses": {
            "1": "I’ve never thought about career paths before.",
            "2": "I’ve considered one or two options briefly.",
            "3": "I’ve explored a few career paths but not deeply.",
            "4": "I’ve actively explored several career paths.",
            "5": "I’ve thoroughly researched and considered many career options.",
        },
    },
    {
        "ID": "18",
        "Intent": "Career Exploration",
        "Question_Text": "Are you interested in exploring careers that are in high demand or ones that allow for creativity and flexibility?",
        "following_intent": [],
        "example_responses": {
            "1": "I’m not interested in exploring careers.",
            "2": "I’d consider high-demand careers.",
            "3": "I’m open to either high-demand or creative careers.",
            "4": "I’m leaning toward creative and flexible career options.",
            "5": "I’m fully committed to exploring creative and flexible careers.",
        },
    },
    {
        "ID": "19",
        "Intent": "Career Exploration",
        "Question_Text": "Would you prefer a job that requires formal education or one where you can learn through experience?",
        "following_intent": [],
        "example_responses": {
            "1": "I don’t prefer either.",
            "2": "I’d choose experience-based learning if I had to.",
            "3": "I’m comfortable with both depending on the job.",
            "4": "I lean more toward jobs requiring formal education.",
            "5": "I strongly prefer formal education as a foundation for my career.",
        },
    },
    {
        "ID": "20",
        "Intent": "Strengths",
        "Question_Text": "What would you say is your greatest strength?",
        "following_intent": [],
        "example_responses": {
            "1": "I don’t think I have any strengths.",
            "2": "I’m decent at problem-solving.",
            "3": "I’m good at organizing tasks.",
            "4": "I’m great at leading teams.",
            "5": "I excel in creative thinking and innovation.",
        },
    },
    {
        "ID": "21",
        "Intent": "Challenges",
        "Question_Text": "What is something you find difficult or challenging in your work or studies?",
        "following_intent": [],
        "example_responses": {
            "1": "I find everything challenging and often feel overwhelmed.",
            "2": "I struggle with staying focused for long periods.",
            "3": "I find managing my time to be a bit difficult but manageable.",
            "4": "I occasionally find group work challenging, but I manage well.",
            "5": "I rarely find things difficult as I enjoy overcoming challenges.",
        },
    },
    {
        "ID": "22",
        "Intent": "Challenges",
        "Question_Text": "Do you feel more motivated by a challenge or prefer more straightforward tasks?",
        "following_intent": [],
        "example_responses": {
            "1": "I avoid challenges and prefer straightforward tasks.",
            "2": "I feel slightly motivated by challenges but prefer simplicity.",
            "3": "I’m neutral and can handle either type of task.",
            "4": "I enjoy challenges as they motivate me to improve.",
            "5": "I thrive on challenges and seek them out actively.",
        },
    },
    {
        "ID": "23",
        "Intent": "Lifestyle",
        "Question_Text": "Do you want a career that offers work-life balance or are you more focused on career growth?",
        "following_intent": [],
        "example_responses": {
            "1": "I want a stress-free life without thinking about work.",
            "2": "I slightly prefer work-life balance over career growth.",
            "3": "I want a mix of work-life balance and career growth.",
            "4": "I focus more on career growth but value balance when possible.",
            "5": "I’m fully focused on career growth and can prioritize work over personal life.",
        },
    },
    {
        "ID": "24",
        "Intent": "Goals",
        "Question_Text": "Do you see yourself staying in one job for a long time, or are you looking for variety?",
        "following_intent": [],
        "example_responses": {
            "1": "I don’t see myself working consistently in any job.",
            "2": "I’d prefer to stick to one job if it’s comfortable.",
            "3": "I’m open to either stability or variety in jobs.",
            "4": "I prefer variety and exploring different roles.",
            "5": "I strongly prefer variety and constant new opportunities.",
        },
    },
    {
        "ID": "25",
        "Intent": "Goals",
        "Question_Text": "What kind of impact do you want your work to have on the world or society?",
        "following_intent": [],
        "example_responses": {
            "1": "I don’t think my work needs to have an impact.",
            "2": "I want to make a small, positive difference in my field.",
            "3": "I aim to contribute positively but within a local scope.",
            "4": "I want my work to impact society in meaningful ways.",
            "5": "I strive to create a lasting, global impact with my work.",
        },
    },
    {
        "ID": "26",
        "Intent": "Values",
        "Question_Text": "Do you value financial security over job satisfaction or the other way around?",
        "following_intent": [],
        "example_responses": {
            "1": "Financial security is my only concern.",
            "2": "I slightly prioritize financial security over job satisfaction.",
            "3": "I value both financial security and job satisfaction equally.",
            "4": "I lean more toward job satisfaction but still value financial security.",
            "5": "Job satisfaction is far more important to me than financial security.",
        },
    },
    {
        "ID": "27",
        "Intent": "Values",
        "Question_Text": "Would you prefer a job that aligns with your personal values and purpose or one that offers greater opportunities for success?",
        "following_intent": [],
        "example_responses": {
            "1": "I don’t prioritize personal values in my work.",
            "2": "I slightly prefer opportunities for success over personal values.",
            "3": "I value both personal alignment and success equally.",
            "4": "I prefer a job that aligns with my personal values.",
            "5": "I strongly prefer a job that reflects my personal purpose and values.",
        },
    },
    {
        "ID": "28",
        "Intent": "Purpose",
        "Question_Text": "Do you see your work as a means to an end, or do you want it to reflect your passion and purpose?",
        "following_intent": [],
        "example_responses": {
            "1": "My work is only a means to an end.",
            "2": "I see work as a means to an end but enjoy it at times.",
            "3": "I like balancing practical work with personal passions.",
            "4": "I want my work to reflect my passions and purpose.",
            "5": "I need my work to align completely with my passions and purpose.",
        },
    },
    {
        "ID": "29",
        "Intent": "Flexibility",
        "Question_Text": "Would you prefer a job with flexible working hours or one that is more traditional?",
        "following_intent": [],
        "example_responses": {
            "1": "I prefer traditional hours and routine.",
            "2": "I lean slightly toward traditional working hours.",
            "3": "I’m okay with both flexible and traditional schedules.",
            "4": "I prefer flexible working hours to accommodate my needs.",
            "5": "I strongly prefer flexibility in my work schedule.",
        },
    },
    {
        "ID": "30",
        "Intent": "Location",
        "Question_Text": "Do you want to work remotely, in an office, or have a mix of both?",
        "following_intent": [],
        "example_responses": {
            "1": "I strongly prefer working in an office.",
            "2": "I prefer working in an office but don’t mind remote work occasionally.",
            "3": "I’m comfortable with both office and remote work.",
            "4": "I prefer remote work but can go to an office sometimes.",
            "5": "I strongly prefer working remotely.",
        },
    },
]


def inicialize_small_corpus():
    list_of_intents = []
    for question in small_corpus:
        list_of_intents.append(question["Intent"])

    for question in small_corpus:
        questions_intent = question["Intent"]
        for intent in list_of_intents:
            if not intent == questions_intent and not intent == "General":
                question["following_intent"].append(intent)

    return small_corpus


def inicialize_medium_corpus():
    """
    This function initializes the medium corpus with the following

    Args:
        None
    Output:
        medium_corpus: list of dictionaries
    """
    list_of_intents = []
    for question in medium_corpus:
        list_of_intents.append(question["Intent"])

    for question in medium_corpus:
        questions_intent = question["Intent"]
        for intent in list_of_intents:
            if not intent == questions_intent and not intent == "General":
                question["following_intent"].append(intent)

    return medium_corpus

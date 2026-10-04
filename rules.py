# ============================================================
# RULE-BASED CHATBOT RULES
# ============================================================

GREETING_RULES = {
    "hello": "Hello! 👋 How can I help you today?",
    "hi": "Hi there! 😊 What would you like to know?",
    "hey": "Hey! 👋 Nice to meet you.",
    "good morning": "Good morning! ☀️ How can I help you?",
    "good afternoon": "Good afternoon! 🌤️ How can I help you?",
    "good evening": "Good evening! 🌙 What can I do for you?"
}

THANKS_RULES = {
    "thank you": "You're very welcome! 😊",
    "thanks": "You're welcome! 👍",
    "thank": "Happy to help! 😊"
}

GOODBYE_RULES = {
    "bye": "Goodbye! 👋 Have a wonderful day!",
    "goodbye": "Goodbye! Take care! 😊",
    "see you": "See you later! 👋"
}

POSITIVE_WORDS = {
    "happy",
    "good",
    "great",
    "excellent",
    "awesome",
    "wonderful",
    "amazing",
    "love",
    "like",
    "nice",
    "fantastic",
    "best",
    "enjoy",
    "success"
}

NEGATIVE_WORDS = {
    "sad",
    "bad",
    "angry",
    "hate",
    "terrible",
    "worst",
    "awful",
    "poor",
    "problem",
    "fail",
    "failure",
    "difficult",
    "boring",
    "upset"
}

QUESTION_RULES = {
    "what": "I can answer basic questions using my predefined rules.",
    "why": "Why questions require predefined knowledge in a rule-based chatbot.",
    "how": "I can explain basic concepts using my predefined responses.",
    "who": "I can provide information about topics included in my rules.",
    "where": "Please provide more information so I can identify the appropriate rule."
}

NLP_RULES = {
    "what is nlp":
        "NLP stands for Natural Language Processing. It allows computers to process and understand human language.",

    "what is natural language processing":
        "Natural Language Processing, or NLP, is a field of AI that deals with interaction between computers and human language.",

    "what is chatbot":
        "A chatbot is a software application that communicates with users using text or speech.",

    "what is rule based chatbot":
        "A rule-based chatbot uses predefined rules, keywords, and patterns to determine how it should respond.",

    "what is sentiment analysis":
        "Sentiment analysis determines whether a piece of text expresses a positive, negative, or neutral opinion.",

    "what is text analysis":
        "Text analysis involves processing text to extract useful information such as words, sentences, sentiment, and keywords.",

    "what is tsa":
        "TSA can refer to Text and Speech Analysis. It involves analyzing textual and speech data using computational techniques.",

    "what is python":
        "Python is a high-level programming language widely used for web development, data science, automation, and AI.",

    "what is flask":
        "Flask is a lightweight Python web framework used to build web applications."
}
import re

from rules import (
    GREETING_RULES,
    THANKS_RULES,
    GOODBYE_RULES,
    NLP_RULES,
    POSITIVE_WORDS,
    NEGATIVE_WORDS
)


def clean_text(text):
    text = text.lower().strip()
    text = re.sub(r"[^\w\s?]", "", text)
    return text


def contains_keyword(text, keyword):
    pattern = r"\b" + re.escape(keyword) + r"\b"
    return re.search(pattern, text) is not None


def detect_intent(text):
    cleaned = clean_text(text)

    # Greeting
    for keyword in GREETING_RULES:
        if contains_keyword(cleaned, keyword):
            return "Greeting"

    # Thanks
    for keyword in THANKS_RULES:
        if contains_keyword(cleaned, keyword):
            return "Thank You"

    # Goodbye
    for keyword in GOODBYE_RULES:
        if contains_keyword(cleaned, keyword):
            return "Goodbye"

    # NLP knowledge
    for keyword in NLP_RULES:
        if keyword in cleaned:
            return "Information Request"

    # Question
    if "?" in text:
        return "Question"

    # Positive
    words = cleaned.split()

    if any(word in POSITIVE_WORDS for word in words):
        return "Positive Statement"

    # Negative
    if any(word in NEGATIVE_WORDS for word in words):
        return "Negative Statement"

    return "General Conversation"


def calculate_confidence(intent):
    confidence_values = {
        "Greeting": 98,
        "Thank You": 98,
        "Goodbye": 99,
        "Information Request": 96,
        "Question": 85,
        "Positive Statement": 82,
        "Negative Statement": 82,
        "General Conversation": 60
    }

    return confidence_values.get(intent, 50)


def get_response(text):
    cleaned = clean_text(text)

    # Exact knowledge rules
    for keyword, response in NLP_RULES.items():
        if keyword in cleaned:
            return (
                response,
                "Information Request",
                calculate_confidence("Information Request")
            )

    # Greetings
    for keyword, response in GREETING_RULES.items():
        if contains_keyword(cleaned, keyword):
            return (
                response,
                "Greeting",
                calculate_confidence("Greeting")
            )

    # Thanks
    for keyword, response in THANKS_RULES.items():
        if contains_keyword(cleaned, keyword):
            return (
                response,
                "Thank You",
                calculate_confidence("Thank You")
            )

    # Goodbye
    for keyword, response in GOODBYE_RULES.items():
        if contains_keyword(cleaned, keyword):
            return (
                response,
                "Goodbye",
                calculate_confidence("Goodbye")
            )

    # Positive response
    words = cleaned.split()

    if any(word in POSITIVE_WORDS for word in words):
        return (
            "That's great to hear! 😊 Tell me more.",
            "Positive Statement",
            calculate_confidence("Positive Statement")
        )

    # Negative response
    if any(word in NEGATIVE_WORDS for word in words):
        return (
            "I'm sorry to hear that. I hope things get better. 💙",
            "Negative Statement",
            calculate_confidence("Negative Statement")
        )

    # Question
    if "?" in text:
        return (
            "That's an interesting question. I can answer questions based on my predefined knowledge.",
            "Question",
            calculate_confidence("Question")
        )

    # Default
    return (
        "I understand your message. Could you provide a little more information?",
        "General Conversation",
        calculate_confidence("General Conversation")
    )
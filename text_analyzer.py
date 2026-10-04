import re


STOP_WORDS = {
    "the", "is", "a", "an", "and", "or", "to",
    "of", "in", "on", "for", "with", "this",
    "that", "it", "i", "am", "are", "was",
    "were", "be", "can", "you", "your"
}


POSITIVE_WORDS = {
    "happy", "good", "great", "excellent",
    "awesome", "wonderful", "amazing",
    "love", "like", "nice", "fantastic",
    "best", "enjoy", "success"
}


NEGATIVE_WORDS = {
    "sad", "bad", "angry", "hate",
    "terrible", "worst", "awful",
    "poor", "problem", "fail",
    "failure", "difficult", "boring",
    "upset"
}


def analyze_text(text):

    # Words
    words = re.findall(r"\b[\w']+\b", text)

    # Characters excluding spaces
    characters = len(text.replace(" ", ""))

    # Sentences
    sentences = re.split(r"[.!?]+", text)
    sentence_count = len([
        sentence for sentence in sentences
        if sentence.strip()
    ])

    # Vowels
    vowels = sum(
        1 for character in text.lower()
        if character in "aeiou"
    )

    # Consonants
    consonants = sum(
        1 for character in text.lower()
        if character.isalpha() and character not in "aeiou"
    )

    # Numbers
    numbers = sum(
        1 for character in text
        if character.isdigit()
    )

    # Uppercase
    uppercase = sum(
        1 for character in text
        if character.isupper()
    )

    # Lowercase
    lowercase = sum(
        1 for character in text
        if character.islower()
    )

    # Sentiment
    word_set = set(word.lower() for word in words)

    positive_count = len(word_set.intersection(POSITIVE_WORDS))
    negative_count = len(word_set.intersection(NEGATIVE_WORDS))

    if positive_count > negative_count:
        sentiment = "Positive 😊"
    elif negative_count > positive_count:
        sentiment = "Negative 😟"
    else:
        sentiment = "Neutral 😐"

    # Question
    question_detected = "Yes" if "?" in text else "No"

    # Keywords
    keywords = [
        word.lower()
        for word in words
        if word.lower() not in STOP_WORDS
        and len(word) > 2
    ]

    # Remove duplicates
    keywords = list(dict.fromkeys(keywords))

    return {
        "words": len(words),
        "characters": characters,
        "sentences": sentence_count,
        "vowels": vowels,
        "consonants": consonants,
        "numbers": numbers,
        "uppercase": uppercase,
        "lowercase": lowercase,
        "sentiment": sentiment,
        "question": question_detected,
        "keywords": keywords[:8]
    }
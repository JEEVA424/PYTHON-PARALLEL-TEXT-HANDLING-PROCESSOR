import re

positive_words = ["good", "excellent", "happy", "great"]
negative_words = ["bad", "terrible", "sad", "poor"]

def sentiment_score(text):
    score = 0
    
    for word in positive_words:
        if word in text.lower():
            score += 1

    for word in negative_words:
        if word in text.lower():
            score -= 1

    return score

def detect_pattern(text):
    matches = re.findall(r"\berror\b", text.lower())
    if matches:
        return "error_found"
    return "none"

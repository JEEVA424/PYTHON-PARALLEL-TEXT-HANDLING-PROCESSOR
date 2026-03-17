import re
from database import insert_result

positive_words = ["good","excellent","happy","great","amazing"]
negative_words = ["bad","terrible","sad","poor","worst"]

def sentiment_score(text):

    words = re.findall(r'\w+', text.lower())

    pos = sum(1 for w in words if w in positive_words)
    neg = sum(1 for w in words if w in negative_words)

    return pos - neg


def process_text(text):
    sentences = [s.strip() for s in text.split(".") if s.strip()]
    results = []

    for sentence in sentences:

        if sentence.strip() == "":
            continue

        score = sentiment_score(sentence)

        insert_result(sentence.strip(), score)

        results.append((sentence.strip(), score))

    return results
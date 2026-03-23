import re
import time
from concurrent.futures import ProcessPoolExecutor


POSITIVE_WORDS = {
    "good", "great", "excellent", "happy", "love", "nice", "best",
    "awesome", "amazing", "wonderful", "fast", "positive", "super",
    "clean", "smooth", "easy", "strong"
}

NEGATIVE_WORDS = {
    "bad", "worst", "sad", "hate", "terrible", "poor", "awful",
    "slow", "negative", "disappointing", "hard", "difficult", "weak",
    "error", "issue", "problem"
}


def split_sentences(text: str) -> list[str]:
    if not text:
        return []

    sentences = re.split(r"[.!?]\s+|\n+", text)
    return [s.strip() for s in sentences if s and s.strip()]


def sentiment_details(sentence: str) -> tuple[str, int, int, int, str]:
    words = re.findall(r"\w+", sentence.lower())

    pos_count = 0
    neg_count = 0

    i = 0
    while i < len(words):
        word = words[i]

        # "not good" -> negative
        if word == "not" and i + 1 < len(words):
            nxt = words[i + 1]
            if nxt in POSITIVE_WORDS:
                neg_count += 1
                i += 2
                continue
            if nxt in NEGATIVE_WORDS:
                pos_count += 1
                i += 2
                continue

        # "very good" -> strong positive
        if word == "very" and i + 1 < len(words):
            nxt = words[i + 1]
            if nxt in POSITIVE_WORDS:
                pos_count += 2
                i += 2
                continue
            if nxt in NEGATIVE_WORDS:
                neg_count += 2
                i += 2
                continue

        # repeated words count normally
        if word in POSITIVE_WORDS:
            pos_count += 1
        elif word in NEGATIVE_WORDS:
            neg_count += 1

        i += 1

    final_score = pos_count - neg_count

    if final_score > 0:
        final_sentiment = "Positive"
    elif final_score < 0:
        final_sentiment = "Negative"
    else:
        final_sentiment = "Neutral"

    return sentence, pos_count, neg_count, final_score, final_sentiment


def _parallel_worker(sentence: str):
    return sentiment_details(sentence)


def process_sequential(sentences: list[str]):
    start = time.time()
    results = [sentiment_details(s) for s in sentences if s.strip()]
    end = time.time()
    return results, end - start


def process_parallel(sentences: list[str], workers: int = 4):
    clean_sentences = [s for s in sentences if s.strip()]

    start = time.time()
    with ProcessPoolExecutor(max_workers=workers) as executor:
        results = list(executor.map(_parallel_worker, clean_sentences))
    end = time.time()

    return results, end - start


def repeated_query_analysis(query: str):
    words = re.findall(r"\w+", query.lower())

    if not words:
        return {
            "is_repeated": False,
            "repeated_word": "",
            "repeat_count": 0
        }

    first_word = words[0]
    if all(word == first_word for word in words):
        return {
            "is_repeated": True,
            "repeated_word": first_word,
            "repeat_count": len(words)
        }

    return {
        "is_repeated": False,
        "repeated_word": "",
        "repeat_count": 0
    }


def count_word_occurrences(text: str, word: str) -> int:
    words = re.findall(r"\w+", str(text).lower())
    return words.count(word.lower())

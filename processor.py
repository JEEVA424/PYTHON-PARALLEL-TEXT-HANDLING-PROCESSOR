import re
import time
from collections import Counter
from concurrent.futures import ProcessPoolExecutor


POSITIVE_WORDS = {
    "good", "great", "excellent", "happy", "love", "nice", "best",
    "awesome", "amazing", "wonderful", "fast", "positive", "super",
    "clean", "smooth", "easy", "strong", "useful", "efficient",
    "reliable", "stable", "smart", "accurate", "friendly", "beautiful",
    "cool", "fantastic", "brilliant", "outstanding", "perfect",
    "powerful", "impressive", "successful", "helpful", "safe",
    "quick", "responsive", "clear", "creative", "valuable", "effective"
}

NEGATIVE_WORDS = {
    "bad", "worst", "sad", "hate", "terrible", "poor", "awful",
    "slow", "negative", "disappointing", "hard", "difficult", "weak",
    "error", "issue", "problem", "bug", "broken", "confusing",
    "ugly", "unfriendly", "unsafe", "late", "boring", "messy",
    "annoying", "wrong", "failed", "failure", "crash", "crashed",
    "unstable", "inaccurate", "useless", "risky", "frustrating",
    "dirty", "laggy", "complicated", "harmful", "loss"
}


def split_sentences(text: str) -> list[str]:
    if not text:
        return []

    sentences = re.split(r"[.!?]\s+|\n+", text)
    return [s.strip() for s in sentences if s and s.strip()]


def tokenize(text: str) -> list[str]:
    return re.findall(r"\w+", text.lower())


def sentiment_details(sentence: str) -> tuple[str, int, int, int, str]:
    words = tokenize(sentence)

    pos_count = 0
    neg_count = 0

    i = 0
    while i < len(words):
        word = words[i]

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


def analyze_search_text(query: str):
    words = tokenize(query)
    counter = Counter(words)

    positive_found = [w for w in words if w in POSITIVE_WORDS]
    negative_found = [w for w in words if w in NEGATIVE_WORDS]

    repeated_positive = {
        word: count for word, count in counter.items()
        if word in POSITIVE_WORDS and count > 1
    }

    repeated_negative = {
        word: count for word, count in counter.items()
        if word in NEGATIVE_WORDS and count > 1
    }

    positive_count = len(positive_found)
    negative_count = len(negative_found)
    final_score = positive_count - negative_count

    if final_score > 0:
        final_sentiment = "Positive"
    elif final_score < 0:
        final_sentiment = "Negative"
    else:
        final_sentiment = "Neutral"

    return {
        "all_positive_words": positive_found,
        "all_negative_words": negative_found,
        "unique_positive_words": sorted(set(positive_found)),
        "unique_negative_words": sorted(set(negative_found)),
        "repeated_positive_words": repeated_positive,
        "repeated_negative_words": repeated_negative,
        "positive_count": positive_count,
        "negative_count": negative_count,
        "final_score": final_score,
        "final_sentiment": final_sentiment
    }

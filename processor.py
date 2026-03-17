import time
from concurrent.futures import ProcessPoolExecutor
from database import insert_result
import re


positive_words = ["good", "great", "excellent", "amazing", "love", "happy"]
negative_words = ["bad", "poor", "terrible", "hate", "sad"]


def analyze_sentiment(sentence):

    score = 0
    words = sentence.lower().split()

    for word in words:

        if word in positive_words:
            score += 1

        if word in negative_words:
            score -= 1

    return score


def process_sentence(sentence):

    score = analyze_sentiment(sentence)

    insert_result(sentence, score)

    return sentence, score


def process_text(text):

    start_time = time.time()

    sentences = [s.strip() for s in re.split(r'[.!?]', text) if s.strip()]

    with ProcessPoolExecutor(max_workers=4) as executor:

        results = list(executor.map(process_sentence, sentences))

    end_time = time.time()

    execution_time = end_time - start_time

    return results, execution_time

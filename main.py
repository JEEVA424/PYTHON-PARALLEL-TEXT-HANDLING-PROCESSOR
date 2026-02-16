from rule_engine import sentiment_score, detect_pattern
from database import insert_data

def run_parallel(chunks):
    for chunk in chunks:
        score = sentiment_score(chunk)
        tag = detect_pattern(chunk)
        insert_data(chunk, score, tag)

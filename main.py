"""
MAIN PROCESSOR
Python Parallel Text Handling Processor

Pipeline:
Load Text → Break into Chunks → Process in Parallel
→ Apply Rule Engine → Store Results → Display Summary
"""
import time
from concurrent.futures import ThreadPoolExecutor
from text_loader import load_txt
from rule_engine import sentiment_score, detect_pattern
from database import insert_data, create_table

# --------------------------------------------------
# CHUNKING FUNCTION
# --------------------------------------------------

def chunk_text(text, chunk_size=2500):
    """
    Break text into word-based chunks for scalable processing
    """
    words = text.split()
    chunks = []

    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)

    return chunks


# --------------------------------------------------
# PROCESS SINGLE CHUNK
# --------------------------------------------------

def process_chunk(chunk):
    """
    Apply rule engine and store results
    """
    score = sentiment_score(chunk)
    tag = detect_pattern(chunk)

    insert_data(chunk, score, tag)

    print("\n--- Chunk Processed ---")
    print("Score:", score)
    print("Tag:", tag)

    return score, tag


# --------------------------------------------------
# MAIN FUNCTION
# --------------------------------------------------

def main():
    start_time = time.time()
    print("\n==============================")
    print(" PARALLEL TEXT PROCESSOR")
    print("==============================\n")
    create_table()
    try:
        text = load_txt("sample_test.txt")

        if not text:
            print("No text found.")
            return

    except Exception as e:
        print("Error loading file:", e)
        return

    print("Text loaded successfully.")

    # ----------------------------------------------

    chunks = chunk_text(text)

    print("Total chunks created:", len(chunks))

    # ----------------------------------------------
    # PARALLEL PROCESSING
    # ----------------------------------------------

    results = []

    print("\nStarting parallel processing...\n")

    try:
        with ThreadPoolExecutor(max_workers=4) as executor:
            results = list(executor.map(process_chunk, chunks))

    except Exception as e:
        print("Parallel processing error:", e)
        return

    # ----------------------------------------------
    # SUMMARY REPORT
    # ----------------------------------------------

    total_chunks = len(chunks)
    total_score = sum(score for score, tag in results)

    pattern_count = sum(1 for score, tag in results if tag != "None")

    print("\n===================================")
    print("          PROCESS SUMMARY")
    print("===================================")

    print("Total Chunks Processed :", total_chunks)
    print("Total Sentiment Score  :", total_score)
    print("Patterns Detected      :", pattern_count)
    end_time = time.time()
    execution_time = end_time - start_time
    print("\nExecution Time:", round(execution_time, 3), "seconds")
    
    print("\nProcessing Complete.")
    
# --------------------------------------------------

if __name__ == "__main__":

    main()



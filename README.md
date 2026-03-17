# PYTHON PARALLEL TEXT HANDLING PROCESSOR

🚀 A Python-based system designed to **process large text files efficiently using parallel computing**.

This project splits text data into smaller units and processes them simultaneously using multiple CPU cores to improve performance.

The system provides an **interactive interface to upload text files, process them, store results, and visualize outputs.**

---

# Project Objective

Large text files require significant time when processed sequentially.
This project demonstrates how **parallel processing in Python** improves performance by distributing tasks across multiple processors.

The system:

* Reads text files
* Splits them into sentences
* Processes sentences in **parallel**
* Performs **sentiment analysis**
* Stores results in **SQLite database**
* Displays analysis in a **dashboard**

---

# Features

* Upload and process large text files
* Automatic sentence splitting
* Parallel text processing using **ProcessPoolExecutor**
* Sentiment classification (Positive / Negative / Neutral)
* Database storage using **SQLite**
* Interactive dashboard using **Streamlit**
* Export results to **CSV format**

---

# Technologies Used

| Technology         | Purpose                   |
| ------------------ | ------------------------- |
| Python             | Core programming language |
| Streamlit          | Web interface             |
| SQLite             | Data storage              |
| Pandas             | Data processing           |
| TextBlob / NLTK    | Sentiment analysis        |
| Concurrent Futures | Parallel processing       |

---

# System Architecture

```
                +----------------------+
                |   Text File Upload   |
                +----------+-----------+
                           |
                           v
                +----------------------+
                |  Streamlit Interface |
                +----------+-----------+
                           |
                           v
                +----------------------+
                | Sentence Splitting   |
                |        Module        |
                +----------+-----------+
                           |
                           v
                +------------------------------+
                | Parallel Processing Engine   |
                |    (ProcessPoolExecutor)     |
                +----------+-------------------+
                           |
                           v
                +----------------------+
                | Sentiment Analysis   |
                |        Engine        |
                +----------+-----------+
                           |
                           v
                +----------------------+
                | SQLite Database      |
                |   Store Results      |
                +----------+-----------+
                           |
                           v
                +----------------------+
                | Results Dashboard    |
                | + CSV Export         |
                +----------------------+
```

---

# Project Structure

```
PYTHON-PARALLEL-TEXT-HANDLING-PROCESSOR
│
├── app.py
├── processor.py
├── database.py
├── requirements.txt
├── sentiment_results.db
├── sample_text.txt
└── README.md
```

---

# Installation

### 1 Clone the Repository

```
git clone https://github.com/JEEVA424/PYTHON-PARALLEL-TEXT-HANDLING-PROCESSOR.git
```

### 2 Navigate to Project Folder

```
cd PYTHON-PARALLEL-TEXT-HANDLING-PROCESSOR
```

### 3 Install Required Libraries

```
pip install -r requirements.txt
```

---

# Run the Application

Start the Streamlit application:

```
streamlit run app.py
```

Then open your browser and go to:

```
http://localhost:8501
```

---

# How the System Works

1. User uploads a text file.
2. The system reads the file content.
3. The text is split into sentences.
4. Sentences are distributed across multiple processes.
5. Each process performs sentiment analysis.
6. Results are stored in SQLite database.
7. The dashboard displays the analysis results.

---

# Example Output

| Sentence            | Sentiment |
| ------------------- | --------- |
| I love this project | Positive  |
| This is very bad    | Negative  |
| It works fine       | Neutral   |

---

# Advantages of Parallel Processing

* Faster execution for large datasets
* Efficient CPU utilization
* Scalable processing architecture
* Reduced processing time

Parallel processing allows tasks to run simultaneously instead of sequentially, significantly improving performance when working with large text data.

---

# Future Improvements

* Real-time text processing
* Multi-language sentiment analysis
* Data visualization charts
* Cloud deployment
* REST API integration

---

# Author

Jeeva

GitHub:
https://github.com/JEEVA424

---

# License

This project is open-source and available for **educational and research purposes**.

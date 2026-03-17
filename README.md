# Python Parallel Text Handling Processor

## Overview

The **Python Parallel Text Handling Processor** is a mini data-processing system designed to efficiently analyze large text datasets using **parallel computing techniques**. The application allows users to upload text files, process sentences concurrently across multiple CPU cores, analyze sentiment scores, and visualize the results through an interactive dashboard.

This project demonstrates how **parallel processing improves performance in text analytics systems** by distributing tasks across multiple processors. The processed results are stored in a **SQLite database** and displayed through a **Streamlit-based dashboard**.

---

## Objectives

The main objectives of this project are:

* To demonstrate **parallel processing in Python**
* To efficiently process large text files by splitting them into sentences
* To apply **rule-based sentiment analysis**
* To store processed results using **SQLite database**
* To visualize analytics using a **Streamlit interactive dashboard**
* To export the processed data for further analysis

---

## Key Features

### Parallel Text Processing

The system uses Python's `ProcessPoolExecutor` to process multiple sentences simultaneously across different CPU cores.

### Sentiment Analysis

Each sentence is analyzed using a rule-based sentiment engine that calculates a **sentiment score** based on positive and negative keywords.

### Database Storage

All processed results are stored in a **SQLite database** for easy retrieval and visualization.

### Interactive Dashboard

The project uses **Streamlit** to build a web-based dashboard where users can:

* Upload text files
* View processing results
* Analyze sentiment metrics
* Search processed sentences
* Export results as CSV files

### Performance Measurement

The system also calculates **execution time** to demonstrate the efficiency of parallel processing.

---

## Technologies Used

| Technology         | Purpose                            |
| ------------------ | ---------------------------------- |
| Python             | Core programming language          |
| Streamlit          | Interactive dashboard interface    |
| Pandas             | Data analysis and visualization    |
| SQLite             | Database storage                   |
| Concurrent Futures | Parallel processing implementation |

---

## System Architecture

```
User Uploads Text File
        │
        ▼
Streamlit Web Interface
        │
        ▼
Sentence Splitting
        │
        ▼
Parallel Processing Engine
(ProcessPoolExecutor)
        │
        ▼
Rule-Based Sentiment Analysis
        │
        ▼
SQLite Database Storage
        │
        ▼
Interactive Dashboard & CSV Export
```

---

## Project Structure

```
PYTHON-PARALLEL-TEXT-HANDLING-PROCESSOR
│
├── app.py
├── processor.py
├── database.py
├── requirements.txt
├── README.md
│
└── sample_data
    └── sample_test.txt
```

---

## Installation and Setup

### Step 1: Clone the Repository

```
git clone https://github.com/JEEVA424/PYTHON-PARALLEL-TEXT-HANDLING-PROCESSOR
```

### Step 2: Navigate to Project Folder

```
cd PYTHON-PARALLEL-TEXT-HANDLING-PROCESSOR
```

### Step 3: Install Dependencies

```
pip install -r requirements.txt
```

If requirements file is not available:

```
pip install streamlit pandas
```

---

## Running the Application

Start the Streamlit dashboard:

```
python -m streamlit run app.py
```

The application will open automatically in your browser at:

```
http://localhost:8501
```

---

## Example Input

Example text file:

```
Python is amazing.
The weather is bad today.
This project is excellent.
The service was terrible.
I love programming.
```

---

## Output

After processing, the dashboard displays:

* Sentiment score for each sentence
* Total number of sentences processed
* Number of positive sentences
* Number of negative sentences
* Search functionality for text filtering
* CSV export for processed results

---

## Performance Optimization

The system improves processing speed by using **parallel execution**. Instead of analyzing sentences sequentially, the text is divided into multiple tasks which are processed simultaneously across CPU cores.

This significantly reduces execution time when processing large datasets.

---

## Future Improvements

Possible enhancements for this system include:

* Machine learning based sentiment analysis
* Real-time text streaming support
* Visualization charts and graphs
* Natural Language Processing integration
* Large dataset performance benchmarking

---

## Author

**Jeeva**

---

## Conclusion

The **Python Parallel Text Handling Processor** demonstrates how parallel computing can improve the efficiency of text processing systems. By combining multiprocessing, database storage, and interactive visualization, the project provides a complete pipeline for analyzing textual datasets efficiently.

# Python Parallel Text Handling Processor

## Overview

The **Python Parallel Text Handling Processor** is a text analysis application designed to efficiently process and analyze large text datasets using **parallel computing techniques in Python**. The system allows users to upload text files, split the content into sentences, analyze the sentiment of each sentence, and visualize the results through an interactive **Streamlit dashboard**.

The project demonstrates how **parallel processing can significantly improve performance when handling large volumes of textual data** by distributing tasks across multiple CPU cores.

---

## Problem Statement

Traditional text processing systems often process sentences sequentially, which can become inefficient when dealing with large datasets. Sequential processing increases computation time and reduces system performance.

This project addresses this issue by implementing **parallel sentence processing using Python's multiprocessing capabilities**, enabling multiple sentences to be analyzed simultaneously.

---

## Objectives

The primary objectives of this project are:

* To demonstrate the concept of **parallel processing in Python**
* To develop an efficient **text handling and processing system**
* To implement **rule-based sentiment analysis**
* To store and manage results using a **SQLite database**
* To visualize processed results using an **interactive dashboard**
* To measure system performance using **execution time analysis**

---

## Key Features

* Upload and process text files
* Sentence-level text analysis
* Parallel processing using multiple CPU cores
* Rule-based sentiment analysis system
* SQLite database integration
* Interactive Streamlit dashboard
* Search functionality for processed text
* CSV export for analysis results
* Automatic database reset for new processing tasks
* Execution time measurement to evaluate performance

---

## Technologies Used

| Technology         | Description                          |
| ------------------ | ------------------------------------ |
| Python             | Main programming language            |
| Streamlit          | Web-based dashboard interface        |
| Pandas             | Data analysis and data visualization |
| SQLite             | Lightweight relational database      |
| Concurrent Futures | Parallel computing implementation    |

---

## System Architecture

Text File Upload
↓
Streamlit User Interface
↓
Sentence Splitting Module
↓
Parallel Processing Engine (ProcessPoolExecutor)
↓
Sentiment Analysis Engine
↓
SQLite Database Storage
↓
Results Visualization Dashboard

---

## Workflow

1. The user uploads a text file through the Streamlit dashboard.
2. The system reads and previews the uploaded file.
3. The text is split into individual sentences.
4. Sentences are processed in parallel using multiple CPU cores.
5. Sentiment analysis is performed for each sentence using rule-based scoring.
6. Processed results are stored in a SQLite database.
7. The dashboard retrieves and displays the results.
8. Users can search sentences or export the results as a CSV file.

---

## Project Structure

```id="g4u7s3"
PYTHON-PARALLEL-TEXT-HANDLING-PROCESSOR
│
├── app.py
├── processor.py
├── database.py
├── requirements.txt
├── README.md
│
├── sample_data
│   └── sample_test.txt
```

### Module Description

**app.py**
This module implements the Streamlit dashboard. It handles file uploads, user interactions, and visualization of processed results.

**processor.py**
This module performs the main text processing operations. It splits sentences and processes them in parallel using Python's ProcessPoolExecutor.

**database.py**
This module manages database operations including table creation, data insertion, result retrieval, and database reset.

**sample_data/**
This directory contains example text files used to test and demonstrate the system.

---

## Parallel Processing Implementation

The project uses **Python's concurrent.futures.ProcessPoolExecutor** to implement parallel processing.

Instead of processing sentences sequentially, the system distributes sentences across multiple processes. Each process analyzes a sentence independently, allowing multiple tasks to run simultaneously.

Example concept:

```id="30d4m4"
CPU Core 1 → Sentence 1
CPU Core 2 → Sentence 2
CPU Core 3 → Sentence 3
CPU Core 4 → Sentence 4
```

This significantly improves processing efficiency for large text datasets.

---

## Installation

Clone the repository:

```id="qckhup"
git clone https://github.com/JEEVA424/PYTHON-PARALLEL-TEXT-HANDLING-PROCESSOR.git
```

Navigate to the project directory:

```id="g5d2fu"
cd PYTHON-PARALLEL-TEXT-HANDLING-PROCESSOR
```

Install required dependencies:

```id="r9o1af"
pip install -r requirements.txt
```

---

## Running the Application

Run the Streamlit application using the following command:

```id="ciulgl"
python -m streamlit run app.py
```

After executing the command, open the following address in your web browser:

```id="icofp7"
http://localhost:8501
```

---

## Example Input

```id="plkoyc"
Python is amazing.
The weather is bad today.
This project is excellent.
The service was terrible.
I love programming.
```

---

## Example Output

The application dashboard displays:

* Total number of processed sentences
* Number of positive sentences
* Number of negative sentences
* Sentiment score for each sentence
* Searchable text results
* Downloadable CSV file containing analysis results

---

## Performance Measurement

The system measures **processing execution time** to demonstrate the efficiency of parallel processing. Execution time is displayed after the processing task is completed.

---

## Future Improvements

Possible future enhancements include:

* Integrating machine learning models for advanced sentiment analysis
* Supporting large-scale datasets and distributed processing
* Implementing graphical analytics and charts
* Improving text preprocessing techniques
* Adding support for multiple languages

---

## Author

**Jeeva**

---

## Conclusion

The Python Parallel Text Handling Processor demonstrates how **parallel computing can improve the performance of text analysis systems**. By combining parallel processing, database storage, and interactive visualization, the project provides a scalable and efficient solution for handling textual data.

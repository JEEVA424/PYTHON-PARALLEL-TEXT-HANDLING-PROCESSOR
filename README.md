# 🚀 PYTHON PARALLEL TEXT HANDLING PROCESSOR

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Streamlit](https://img.shields.io/badge/Framework-Streamlit-red)
![Database](https://img.shields.io/badge/Database-SQLite-green)
![Parallel Processing](https://img.shields.io/badge/Processing-Parallel-orange)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

---

# 📌 Project Overview

This project is a **Parallel Text Processing System** built using Python that efficiently processes large text datasets using **multi-core parallel execution**.

The system allows users to:

* Upload large text files (TXT, CSV, Excel)
* Perform sentiment analysis
* Process data using parallel computing
* Store results in a database
* Visualize results through an interactive dashboard
* Search and analyze text dynamically

---

# ⚙️ Features Implemented

### 🔹 File Handling

* Upload TXT, CSV, XLSX files
* Supports large datasets (50K+ records)
* 1GB upload capability

### 🔹 Processing

* Sentence splitting
* Parallel processing using `ProcessPoolExecutor`
* Sequential vs Parallel comparison

### 🔹 Sentiment Analysis

* Rule-based sentiment detection
* Positive / Negative / Neutral classification
* Handles repeated words
* Handles:

  * `good good bad`
  * `not good`
  * `very good`

### 🔹 Dashboard

* Total records
* Positive / Negative / Neutral counts
* Pie chart visualization

### 🔹 Search Functionality

* Keyword search
* Case-insensitive matching
* Repeated word detection
* Search sentiment calculation
* Example:

  * `good good bad bad → Neutral`

### 🔹 Export & Reporting

* Download results as CSV
* Email report functionality

### 🔹 Performance Metrics

* Execution time display
* CPU core usage
* Speed comparison (Sequential vs Parallel)

---

# ⚡ Parallel Processing Logic

The system uses:

ProcessPoolExecutor(max_workers=n)

* Text is split into sentences
* Each sentence is processed independently
* Multiple CPU cores process simultaneously

Small dataset → slower
Large dataset → faster

---

# 🧠 Sentiment Analysis Implementation

Rule-based approach:

Final Score = Positive Count - Negative Count

* `not good → negative`
* `very good → strong positive`

---

# 📊 Dataset Details

* TXT / CSV / Excel files
* Large generated datasets (50K+ records)
* Mixed sentiment + repeated words

---

# ⏱️ Performance Comparison

Shows:

* Sequential time
* Parallel time
* Speedup
* CPU cores used

---

# ⚠️ Edge Cases Handled

* Empty input
* Invalid files
* No valid text
* Repeated words
* Large dataset
* No search results

---

# 🧩 Implementation Approach

* `app.py` → UI
* `processor.py` → logic
* `database.py` → storage

---

# 🏃 Steps to Run

git clone https://github.com/JEEVA424/PYTHON-PARALLEL-TEXT-HANDLING-PROCESSOR.git

cd PYTHON-PARALLEL-TEXT-HANDLING-PROCESSOR

pip install -r requirements.txt

python -m streamlit run app.py

---

# 🎯 Conclusion

* Parallel processing improves performance
* Handles large datasets efficiently
* Provides full UI + analytics

---

# 👨‍💻 Author

Jeeva M
https://github.com/JEEVA424

---

# 📜 License

Educational and research use

---

# ⭐ Final Note

Complete end-to-end system combining:

* Parallel computing
* Sentiment analysis
* Dashboard visualization

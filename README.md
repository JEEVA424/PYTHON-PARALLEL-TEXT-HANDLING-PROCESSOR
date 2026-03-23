PYTHON PARALLEL TEXT HANDLING PROCESSOR

🚀 A high-performance Python system designed to process large text datasets efficiently using parallel computing.

This project enables users to upload large files (TXT, CSV, Excel), perform sentiment analysis, and visualize results through an interactive dashboard with parallel execution optimization.

Project Objective

Processing large text data sequentially is slow and inefficient.
This project demonstrates how parallel processing using multiple CPU cores improves performance and scalability.

The system:

Reads large datasets (50K+ records)
Splits text into sentences
Processes data using parallel execution
Applies rule-based sentiment analysis
Stores results in a SQLite database
Displays analytics via a user-friendly dashboard
Features
Core Features

✔ Upload files (TXT, CSV, Excel)
✔ Parallel text processing using ProcessPoolExecutor
✔ Sentiment classification (Positive / Negative / Neutral)
✔ SQLite database storage
✔ Interactive Streamlit dashboard

Advanced Features

✔ Sequential vs Parallel execution comparison
✔ Execution time measurement
✔ CPU core selection (1–8 cores)
✔ Repeated-word sentiment handling
✔ Smart search (keyword + repeated word search)
✔ Pie chart visualization
✔ CSV export
✔ Email report generation
✔ Reset / clear data option
✔ Edge-case validation

Technologies Used
Technology	Purpose
Python	Core programming language
Streamlit	Interactive web interface
SQLite	Data storage
Pandas	Data processing & analysis
Matplotlib	Visualization (charts)
Concurrent Futures	Parallel processing engine
System Architecture
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
                +----------+-----------+
                           |
                           v
                +------------------------------+
                | Parallel Processing Engine   |
                |   (ProcessPoolExecutor)      |
                +----------+-------------------+
                           |
                           v
                +----------------------+
                | Sentiment Analysis   |
                +----------+-----------+
                           |
                           v
                +----------------------+
                | SQLite Database      |
                +----------+-----------+
                           |
                           v
                +----------------------+
                | Dashboard & Reports  |
                | (Charts, Search, CSV)|
                +----------------------+
Project Structure
PYTHON-PARALLEL-TEXT-HANDLING-PROCESSOR
│
├── app.py
├── processor.py
├── database.py
├── requirements.txt
├── results.db
├── README.md
│
└── .streamlit
     └── config.toml
Installation
1 Clone Repository
git clone https://github.com/JEEVA424/PYTHON-PARALLEL-TEXT-HANDLING-PROCESSOR.git
2 Navigate to Folder
cd PYTHON-PARALLEL-TEXT-HANDLING-PROCESSOR
3 Install Dependencies
pip install -r requirements.txt
Run the Application
python -m streamlit run app.py

Open browser:

http://localhost:8501
Application Workflow
User uploads a TXT / CSV / Excel file
System validates input (empty / invalid data)
Text is split into sentences
Sentences are processed in parallel
Sentiment is calculated using rule-based logic
Results are stored in database
Dashboard displays metrics, charts, and results
User can search, export, or email reports
Sentiment Scoring Logic

✔ Handles repeated words
Example:

good good bad → Positive = 2, Negative = 1

✔ Handles variations:

not good → Negative
very good → Strong Positive

✔ Output includes:

Positive Count
Negative Count
Final Score
Final Sentiment
Dashboard Features
Total records processed
Positive / Negative / Neutral counts
Pie chart visualization
Execution time display
CPU cores used
Search Functionality

Supports:

✔ Keyword search
✔ Case-insensitive matching
✔ Partial match search
✔ Repeated word search

Example:

good good good

Shows:

Repeated word = good
Query repetition count = 3
Occurrences in each sentence
Performance Analysis

The system compares:

Sequential execution time
Parallel execution time

✔ Shows performance improvement
✔ Demonstrates when parallel processing is beneficial

Edge Case Handling

The system handles:

✔ Empty input
✔ Invalid files
✔ Large datasets (50K+ records)
✔ Repeated words
✔ No valid text after preprocessing
✔ Search with no results

Export & Reporting

✔ Download results as CSV
✔ Send report via email
✔ Includes summary statistics

Advantages of Parallel Processing
Faster execution for large datasets
Efficient CPU utilization
Scalable architecture
Reduced processing time
Future Improvements
Machine learning-based sentiment analysis
Multi-language support
Real-time processing
Cloud deployment
API integration
Author

Jeeva

GitHub:
https://github.com/JEEVA424

License

This project is open-source and available for educational and research purposes.

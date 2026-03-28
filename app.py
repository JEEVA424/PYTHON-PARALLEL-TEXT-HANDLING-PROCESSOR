import io
import re
import smtplib
from email.message import EmailMessage

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

from database import create_table, get_all_results, insert_results, reset_database
from processor import (
    split_sentences,
    process_parallel,
    process_sequential,
    analyze_search_text
)
create_table()

st.set_page_config(
    page_title="Parallel Text Processing Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
.block-container {
    padding-top: 1.5rem;
    padding-bottom: 2rem;
}
.metric-card {
    padding: 0.8rem;
    border-radius: 12px;
    background: #111827;
    border: 1px solid #374151;
}
</style>
""", unsafe_allow_html=True)

st.title("Parallel Text Processing Dashboard")
st.caption("A user-friendly parallel text analyzer with processing, dashboard, search, export, and reporting.")

# ---------------- Sidebar ----------------
st.sidebar.header("Processing Settings")
workers = st.sidebar.slider("CPU Cores", 1, 8, 4)
compare_mode = st.sidebar.checkbox("Compare Sequential vs Parallel", value=True)
st.sidebar.write(f"Cores selected: {workers}")
st.sidebar.info("Upload supports TXT, CSV, XLSX. Actual limit is set to 1GB through Streamlit config.")

# ---------------- Helpers ----------------
def load_input_file(file):
    if file is None:
        return None, None, "No file uploaded."

    name = file.name.lower()

    try:
        if name.endswith(".txt"):
            raw = file.read()
            text = raw.decode("utf-8", errors="ignore")
            return text, None, None

        if name.endswith(".csv"):
            df = pd.read_csv(file)
            if df.empty:
                return None, None, "CSV file is empty."
            return None, df, None

        if name.endswith(".xlsx"):
            df = pd.read_excel(file)
            if df.empty:
                return None, None, "Excel file is empty."
            return None, df, None

        return None, None, "Unsupported file type."

    except Exception as e:
        return None, None, f"Invalid or unreadable file: {e}"


def extract_sentences_from_dataframe(df: pd.DataFrame):
    if df is None or df.empty:
        return []

    non_empty_columns = [col for col in df.columns if df[col].notna().any()]
    if not non_empty_columns:
        return []

    selected_col = non_empty_columns[0]
    values = df[selected_col].fillna("").astype(str).tolist()
    values = [v.strip() for v in values if v.strip()]
    return values


def render_pie_chart(positive_total, negative_total, neutral_total):
    fig, ax = plt.subplots()
    ax.pie(
        [positive_total, negative_total, neutral_total],
        labels=["Positive", "Negative", "Neutral"],
        autopct="%1.1f%%"
    )
    st.pyplot(fig)


def send_email_report(recipient, sender, password, df):
    csv_bytes = df.to_csv(index=False).encode("utf-8")

    total_records = len(df)
    positive_total = (df["Final Sentiment"] == "Positive").sum()
    negative_total = (df["Final Sentiment"] == "Negative").sum()
    neutral_total = (df["Final Sentiment"] == "Neutral").sum()

    msg = EmailMessage()
    msg["Subject"] = "Parallel Text Processing Report"
    msg["From"] = sender
    msg["To"] = recipient

    body = f"""
Parallel Text Processing Report

Total Records: {total_records}
Positive: {positive_total}
Negative: {negative_total}
Neutral: {neutral_total}
"""
    msg.set_content(body)
    msg.add_attachment(
        csv_bytes,
        maintype="text",
        subtype="csv",
        filename="processed_results.csv"
    )

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender, password)
        server.send_message(msg)


# ---------------- Tabs ----------------
tab1, tab2, tab3, tab4 = st.tabs([
    "Upload & Process",
    "Dashboard",
    "Search & Export",
    "Email Report"
])

# ---------------- Tab 1 ----------------
with tab1:
    st.subheader("Upload & Process")
    st.markdown("**Upload File (Limit: 1GB)**")

    uploaded_file = st.file_uploader(
        "Choose a TXT, CSV, or XLSX file",
        type=["txt", "csv", "xlsx"],
        key="main_uploader"
    )

    st.caption("Configured limit: 1GB • Supported files: TXT, CSV, XLSX")

    col1, col2 = st.columns([1, 1])

    with col1:
        if st.button("Start Processing", use_container_width=True):
            if uploaded_file is None:
                st.error("Please upload a file before processing.")
                st.stop()

            reset_database()

            text_data, df_data, error = load_input_file(uploaded_file)

            if error:
                st.error(error)
                st.stop()

            if text_data is not None:
                if not text_data.strip():
                    st.error("Empty input detected.")
                    st.stop()
                sentences = split_sentences(text_data)
            else:
                sentences = extract_sentences_from_dataframe(df_data)

            if not sentences:
                st.error("No valid text found after preprocessing.")
                st.stop()

            st.info(f"Uploaded file: {uploaded_file.name}")
            st.info(f"Number of files uploaded: 1")
            st.info(f"Total records detected: {len(sentences)}")

            preview_df = pd.DataFrame({"Preview Records": sentences[:10]})
            st.write("Preview of first 10 records:")
            st.dataframe(preview_df, use_container_width=True)

            progress = st.progress(0)

            sequential_time = None
            if compare_mode:
                progress.progress(20)
                _, sequential_time = process_sequential(sentences)
            else:
                progress.progress(35)

            progress.progress(60)
            parallel_results, parallel_time = process_parallel(sentences, workers=workers)

            progress.progress(85)
            insert_results(parallel_results)

            progress.progress(100)
            st.success("Processing completed successfully.")

            c1, c2, c3 = st.columns(3)
            c1.metric("Parallel Time (sec)", f"{parallel_time:.4f}")
            c2.metric("CPU Cores Used", workers)
            if sequential_time is not None:
                c3.metric("Sequential Time (sec)", f"{sequential_time:.4f}")
            else:
                c3.metric("Sequential Time (sec)", "Skipped")

            if sequential_time is not None:
                speedup = sequential_time / parallel_time if parallel_time > 0 else 0
                st.metric("Speedup", f"{speedup:.2f}x")
                st.info(
                    "Parallel processing can be slower for very small datasets because process creation adds overhead. "
                    "It becomes faster as the dataset size increases."
                )

    with col2:
        if st.button("Reset / Clear Data", use_container_width=True):
            reset_database()
            st.success("Database cleared successfully.")

# ---------------- Load Dashboard Data ----------------
data = get_all_results()
df = None

if data:
    df = pd.DataFrame(
        data,
        columns=["Text", "Positive Count", "Negative Count", "Final Score", "Final Sentiment"]
    )

# ---------------- Tab 2 ----------------
with tab2:
    st.subheader("Dashboard")

    if df is None or df.empty:
        st.info("No processed data available yet. Upload and process a file first.")
    else:
        total_records = len(df)
        positive_total = (df["Final Sentiment"] == "Positive").sum()
        negative_total = (df["Final Sentiment"] == "Negative").sum()
        neutral_total = (df["Final Sentiment"] == "Neutral").sum()

        a, b, c, d = st.columns(4)
        a.metric("Total Records", total_records)
        b.metric("Positive", positive_total)
        c.metric("Negative", negative_total)
        d.metric("Neutral", neutral_total)

        st.write("### Sentiment Distribution")
        render_pie_chart(positive_total, negative_total, neutral_total)

        st.write("### Processed Results")
        st.dataframe(df, use_container_width=True)

# ---------------- Tab 3 ----------------
with tab3:
    st.subheader("Search & Export")

    if df is None or df.empty:
        st.info("No processed data available yet. Upload and process a file first.")
    else:
        search_query = st.text_input("Search by sentence / keyword / repeated words")

        if search_query:
            analysis = analyze_search_text(search_query)

            st.write("### Search Word Analysis")

            col1, col2 = st.columns(2)

            with col1:
                st.write("**All Positive Words Found**")
                if analysis["all_positive_words"]:
                    st.write(", ".join(analysis["all_positive_words"]))
                else:
                    st.write("None")

                st.write("**Repeated Positive Words**")
                if analysis["repeated_positive_words"]:
                    st.write(analysis["repeated_positive_words"])
                else:
                    st.write("None")

            with col2:
                st.write("**All Negative Words Found**")
                if analysis["all_negative_words"]:
                    st.write(", ".join(analysis["all_negative_words"]))
                else:
                    st.write("None")

                st.write("**Repeated Negative Words**")
                if analysis["repeated_negative_words"]:
                    st.write(analysis["repeated_negative_words"])
                else:
                    st.write("None")

            st.write("### Search Sentiment Result")
            a, b, c, d = st.columns(4)
            a.metric("Positive Count", analysis["positive_count"])
            b.metric("Negative Count", analysis["negative_count"])
            c.metric("Final Score", analysis["final_score"])
            d.metric("Sentiment", analysis["final_sentiment"])

            search_words = (
                analysis["unique_positive_words"] +
                analysis["unique_negative_words"]
            )

            if search_words:
                pattern = "|".join(search_words)
                filtered = df[df["Text"].str.contains(pattern, case=False, na=False)]

                st.write("### Matching Records")
                if filtered.empty:
                    st.warning("No matching processed records found for the detected sentiment words.")
                else:
                    st.dataframe(filtered, use_container_width=True)
            else:
                filtered = df[df["Text"].str.contains(search_query, case=False, na=False)]

                st.write("### Matching Records")
                if filtered.empty:
                    st.warning("No results found for this search.")
                else:
                    st.dataframe(filtered, use_container_width=True)

        st.write("### Export Processed Data")
        csv_bytes = df.to_csv(index=False).encode("utf-8")
        st.download_button(
            "Download CSV",
            data=csv_bytes,
            file_name="processed_results.csv",
            mime="text/csv"
        )
# ---------------- Tab 4 ----------------
with tab4:
    st.subheader("Email Report")

    if df is None or df.empty:
        st.info("No processed data available yet. Upload and process a file first.")
    else:
        recipient = st.text_input("Recipient Email")
        sender = st.text_input("Sender Gmail")
        password = st.text_input("Gmail App Password", type="password")

        st.caption("For Gmail, use an App Password instead of your normal password.")

        if st.button("Send Email Report"):
            if not recipient or not sender or not password:
                st.error("Please fill all email fields.")
            else:
                try:
                    send_email_report(recipient, sender, password, df)
                    st.success("Email report sent successfully.")
                except Exception as e:
                    st.error(f"Failed to send email report: {e}")

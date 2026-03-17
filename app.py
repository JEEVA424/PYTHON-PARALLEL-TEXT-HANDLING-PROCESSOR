import streamlit as st
import pandas as pd
from processor import process_text
from database import create_table, get_all_results

create_table()

st.set_page_config(page_title="Parallel Text Processor", layout="wide")

st.title("Parallel Text Processing Dashboard")

uploaded_file = st.file_uploader(
    "Upload Text File",
    type=["txt"]
)

if uploaded_file:

    text = uploaded_file.read().decode("utf-8")

    st.subheader("File Preview")

    st.write(text[:500])

    if st.button("Start Processing"):

        progress = st.progress(0)

        for i in range(100):
            progress.progress(i+1)

        results = process_text(text)

        st.success("Processing Completed")

data = get_all_results()

if data:

    df = pd.DataFrame(data, columns=["Text","Sentiment Score"])

    st.subheader("Results Dashboard")

    st.dataframe(df)

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Text", len(df))
    col2.metric("Positive",(df["Sentiment Score"]>0).sum())
    col3.metric("Negative",(df["Sentiment Score"]<0).sum())

    keyword = st.text_input("Search")

    if keyword:

        filtered = df[df["Text"].str.contains(keyword, case=False)]

        st.dataframe(filtered)

    csv = df.to_csv(index=False)

    st.download_button(
        "Download CSV",
        csv,
        "results.csv",
        "text/csv"
    )
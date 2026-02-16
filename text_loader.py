import pandas as pd
from PyPDF2 import PdfReader
from docx import Document

def load_txt(file):
    return file.read().decode("utf-8")

def load_csv(file, column_name):
    df = pd.read_csv(file)
    if column_name not in df.columns:
        return ""
    return " ".join(df[column_name].astype(str))

def load_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

def load_docx(file):
    doc = Document(file)
    return " ".join([para.text for para in doc.paragraphs])

def break_text(text):
    chunks = text.split(".")
    return [chunk.strip() for chunk in chunks if chunk.strip()]

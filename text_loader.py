"""
TEXT LOADER MODULE
Loads text from TXT, PDF, and DOCX files.
Used by the Parallel Text Processor.
"""

import os

# Optional imports
try:
    from PyPDF2 import PdfReader
except ImportError:
    PdfReader = None

try:
    from docx import Document
except ImportError:
    Document = None


# --------------------------------------------------
# LOAD TXT FILE
# --------------------------------------------------

def load_txt(file_path):
    """
    Load plain text file
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()
        return text

    except FileNotFoundError:
        print("Error: TXT file not found.")
        return ""

    except Exception as e:
        print("TXT read error:", e)
        return ""


# --------------------------------------------------
# LOAD PDF FILE
# --------------------------------------------------

def load_pdf(file_path):
    """
    Load text from PDF file
    """
    if PdfReader is None:
        print("PyPDF2 not installed.")
        return ""

    try:
        reader = PdfReader(file_path)

        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""

        return text

    except Exception as e:
        print("PDF read error:", e)
        return ""


# --------------------------------------------------
# LOAD DOCX FILE
# --------------------------------------------------

def load_docx(file_path):
    """
    Load text from DOCX file
    """
    if Document is None:
        print("python-docx not installed.")
        return ""

    try:
        doc = Document(file_path)

        text = ""
        for para in doc.paragraphs:
            text += para.text + "\n"

        return text

    except Exception as e:
        print("DOCX read error:", e)
        return ""


# --------------------------------------------------
# AUTO FILE LOADER
# --------------------------------------------------

def load_file(file_path):
    """
    Automatically detect file type and load text
    """

    if not os.path.exists(file_path):
        print("File does not exist.")
        return ""

    extension = file_path.lower().split(".")[-1]

    if extension == "txt":
        return load_txt(file_path)

    elif extension == "pdf":
        return load_pdf(file_path)

    elif extension == "docx":
        return load_docx(file_path)

    else:
        print("Unsupported file format.")
        return ""
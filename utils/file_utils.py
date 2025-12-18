import os
from docx2pdf import convert

def ensure_temp_dir(path="temp"):
    os.makedirs(path, exist_ok=True)

def save_uploaded_file(uploaded_file, path):
    with open(path, "wb") as f:
        f.write(uploaded_file.read())

def word_to_pdf(word_path, pdf_path):
    convert(word_path, pdf_path)

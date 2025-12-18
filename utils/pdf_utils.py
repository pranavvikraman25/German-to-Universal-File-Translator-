import pdfplumber
from docx import Document
from utils.translator_utils import translate_text

def pdf_to_translated_word(pdf_path, word_path, target_lang):
    doc = Document()

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                translated = translate_text(text, target_lang)
                doc.add_paragraph(translated)

    doc.save(word_path)

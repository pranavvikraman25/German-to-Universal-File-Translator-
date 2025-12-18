import pdfplumber
from docx import Document
from services.translation_service import translate_block

def process_pdf(pdf_path, word_output_path, target_lang):
    doc = Document()

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                translated = translate_block(text, target_lang)
                doc.add_paragraph(translated)

    doc.save(word_output_path)

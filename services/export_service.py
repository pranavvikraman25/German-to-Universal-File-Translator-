from docx2pdf import convert

def export_pdf_from_word(word_path, pdf_path):
    convert(word_path, pdf_path)

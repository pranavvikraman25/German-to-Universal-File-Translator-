# 🌍 International Academic Document Translator

A student-focused document translation tool designed for
APS certification and German university admissions.

This project translates academic documents from German into
multiple target languages while preserving structure as much
as possible.

---

## 🚀 Features

- Upload **Word (.docx)** or **PDF (.pdf)** files
- Translate German documents into:
  - English
  - Chinese
  - Vietnamese
  - Japanese
- Export translated results as:
  - Word (.docx)
  - PDF (.pdf)
- Best-quality translation for Word documents
- Best-effort support for text-based PDFs
- Clean, visual, student-friendly UI

---

## 📂 Supported Formats

### ✅ Word (.docx) — Recommended
- Preserves paragraphs
- Preserves tables
- High-quality output
- APS-friendly

### ⚠️ PDF (.pdf)
- Text-based PDFs supported
- Layout may change
- Scanned PDFs not supported

---

## 🧠 Project Architecture
doc-translator/
│
├── app.py
├── requirements.txt
├── README.md
│
├── services/
│ ├── translation_service.py
│ ├── word_pipeline_service.py
│ ├── pdf_pipeline_service.py
│ └── export_service.py
│
├── utils/
│ ├── language_utils.py
│ ├── translator_utils.py
│ ├── word_utils.py
│ ├── pdf_utils.py
│ └── file_utils.py
│
└── temp/


---

## ▶️ How to Run

```bash
pip install -r requirements.txt
streamlit run app.py

⚠️ Important Notes

This project does NOT attempt to clone DeepL’s proprietary
PDF reconstruction engine.

For perfect layout preservation, always upload Word files.

PDF translation is provided as a convenience feature only.

👨‍🎓 Target Users

International students

APS applicants

German university applicants

Academic document reviewers

📌 Disclaimer

This tool is for educational and personal use.
Translation quality depends on the underlying translation engine.


---

## ✅ `temp/` folder (FILES YOU SHOULD CREATE)

Create an empty folder called `temp/`  
Inside it, **NO CODE FILES**, only placeholders.

### 📁 Structure


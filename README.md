# 🧠 AI DDR Generator (Detailed Diagnostic Report)

## 📌 Overview

This project is an AI-powered system that converts unstructured inspection and thermal reports into a structured, client-ready Detailed Diagnostic Report (DDR).

It demonstrates the ability to design real-world AI workflows involving document processing, reasoning, and structured output generation.

---

## 🚀 Features

- 📄 Extracts text and images from PDFs
- 🧠 Uses LLM (Google Gemini) for intelligent reasoning
- 🔗 Combines inspection + thermal insights
- ⚠️ Handles missing and conflicting data
- 🖼️ Attaches images to relevant observations
- 📑 Generates a professional PDF report

---

## 🏗️ Architecture
Input PDFs
↓
PDF Extraction (PyMuPDF)
↓
Data Processing
↓
LLM Reasoning (Gemini API)
↓
Post Processing (Image Mapping)
↓
PDF Generation (ReportLab)


---

## ⚙️ Tech Stack

- Python
- PyMuPDF (PDF parsing)
- Google Gemini API (LLM)
- ReportLab (PDF generation)
- dotenv (env management)

---

## 📂 Project Structure
ai-ddr-generator/
├── main.py
├── extractor.py
├── llm.py
├── utils.py
├── report_generator.py
├── requirements.txt
└── outputs/


---

## ▶️ How to Run

1. Clone the repo
2. Create virtual environment
3. Install dependencies: pip install -r requirements.txt
4. Add `.env` file: GOOGLE_API_KEY=your_api_key
5. Place input files:
- `inspection.pdf`
- `thermal.pdf`

6. Run: python main.py

---

## 📤 Output

- Generates: `outputs/DDR_Report.pdf`
- Includes structured sections and images

---

## ⚠️ Limitations

- Basic image-to-observation mapping
- Depends on LLM output quality
- Limited validation of engineering correctness

---

## 🚀 Future Improvements

- Semantic image matching
- Confidence scoring
- RAG-based retrieval system
- Web UI (Streamlit)
- Cloud deployment


## 👨‍💻 Author

Kapil
 

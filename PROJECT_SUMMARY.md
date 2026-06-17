# UrbanStride PDF Product Assistant - Project Summary

## Project Name
UrbanStride PDF Product Assistant

## Purpose
A PDF-based AI Q&A chatbot for a mock ecommerce footwear business. The assistant helps users ask questions about product catalog, shipping, returns, warranty, sizing, and shoe care using only the provided PDF documents.

## Client / Business
Mock client: UrbanStride Shoes  
Business type: Online footwear store  
Target users: customers, support staff, and sales assistants

## Tech Stack
- Python
- Streamlit
- PyMuPDF
- scikit-learn
- OpenAI API
- python-dotenv
- pytest

## Folder Structure
```text
urbanstride_pdf_assistant/
│
├── app.py
├── requirements.txt
├── pytest.ini
├── README.md
├── TEST_CHECKLIST.md
├── PORTFOLIO_CASE_STUDY.md
├── SCREENSHOTS_CHECKLIST.md
├── PROJECT_SUMMARY.md
│
├── data/
│   └── pdfs/
│       ├── UrbanStride_Product_Catalog_2026.pdf
│       ├── UrbanStride_Shipping_Returns_Warranty_2026.pdf
│       └── UrbanStride_Size_Care_Guide_2026.pdf
│
├── src/
│   ├── __init__.py
│   ├── ai_answer.py
│   ├── config.py
│   ├── fallback.py
│   ├── pdf_loader.py
│   ├── retriever.py
│   └── text_chunker.py
│
└── tests/
    ├── test_fallback.py
    ├── test_pdf_loader.py
    ├── test_retriever.py
    └── test_text_extraction.py

    ## GitHub Repository

Project link:

https://github.com/sobangrewal479/urbanstride-pdf-assistant
# UrbanStride PDF Product Assistant

## Project Name
UrbanStride PDF Product Assistant

## Purpose
UrbanStride PDF Product Assistant is a PDF-based AI Q&A chatbot for a mock ecommerce footwear business called UrbanStride Shoes.

The goal is to help customers and support staff ask questions about product catalog, shipping, returns, warranty, sizing, and shoe care using only the provided PDF documents.

## Project Type
PDF Q&A Chatbot  
AI document assistant  
RAG-style ecommerce support assistant  
Portfolio project

## Mock Client
UrbanStride Shoes  
Online footwear store  
United States shipping only for this mock dataset

## Tech Stack
- Python
- Streamlit
- PyMuPDF
- OpenAI API
- scikit-learn
- python-dotenv
- pytest

## Main Features
- Loads local PDF documents from the project folder
- Extracts readable text from PDFs
- Splits PDF text into searchable chunks
- Retrieves relevant PDF chunks for user questions
- Generates answers using OpenAI API when billing/credits are active
- Shows source document references
- Gives safe fallback responses when information is missing
- Handles live stock, order tracking, and medical questions safely
- Includes automated tests for core behavior

## PDF Documents Used
The project uses these 3 mock PDF files:

1. UrbanStride_Product_Catalog_2026.pdf
2. UrbanStride_Shipping_Returns_Warranty_2026.pdf
3. UrbanStride_Size_Care_Guide_2026.pdf

These files are stored in:

```text
data/pdfs/

## GitHub Repository

Project link:

https://github.com/sobangrewal479/urbanstride-pdf-assistant
# UrbanStride PDF Product Assistant - Portfolio Case Study

## Project Overview

UrbanStride PDF Product Assistant is a PDF-based AI Q&A chatbot built for a mock ecommerce footwear business called UrbanStride Shoes.

The assistant helps customers and support staff ask questions about product catalog, shipping, returns, warranty, sizing, and shoe care using the company’s PDF documents.

## Client Problem

UrbanStride Shoes had important customer information stored inside PDF documents.

Customers and support staff had to manually search documents to answer repeated questions such as:

- Is this shoe waterproof?
- What sizes are available?
- How long does shipping take?
- What is the return policy?
- How should I clean leather shoes?

This wasted support time and made it harder for customers to quickly find answers.

## Solution

I built a PDF Q&A assistant that:

- Loads the company’s PDF documents
- Extracts readable text
- Splits the text into searchable chunks
- Retrieves relevant PDF sections for each question
- Shows source document references
- Uses safe fallback responses when information is missing
- Connects to OpenAI API for AI-generated answers when API billing is active

## Key Features

- Local PDF document loading
- PDF text extraction
- RAG-style retrieval
- Source document reference
- Safe fallback handling
- Product, policy, sizing, warranty, and care support
- Streamlit app interface
- Automated tests with pytest

## Tech Stack

- Python
- Streamlit
- PyMuPDF
- scikit-learn
- OpenAI API
- python-dotenv
- pytest

## Testing Completed

Automated tests cover:

- PDF loading
- Text extraction
- Retrieval behavior
- Fallback behavior
- Empty question handling

Final test result:

```text
12 passed
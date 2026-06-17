from pathlib import Path
import fitz  # PyMuPDF


BASE_DIR = Path(__file__).resolve().parent.parent
PDF_DIR = BASE_DIR / "data" / "pdfs"


def get_pdf_files(pdf_dir: Path = PDF_DIR) -> list[Path]:
    """
    Find all PDF files inside the PDF folder.
    """
    if not pdf_dir.exists():
        raise FileNotFoundError(f"PDF folder not found: {pdf_dir}")

    pdf_files = sorted(pdf_dir.glob("*.pdf"))

    if not pdf_files:
        raise FileNotFoundError(f"No PDF files found in: {pdf_dir}")

    return pdf_files


def extract_text_from_pdf(pdf_path: Path) -> str:
    """
    Extract readable text from one PDF file.
    """
    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")

    if pdf_path.suffix.lower() != ".pdf":
        raise ValueError(f"File is not a PDF: {pdf_path}")

    text_parts = []

    with fitz.open(pdf_path) as pdf:
        for page in pdf:
            page_text = page.get_text()
            if page_text:
                text_parts.append(page_text)

    full_text = "\n".join(text_parts).strip()

    if not full_text:
        raise ValueError(f"No readable text found in PDF: {pdf_path.name}")

    return full_text


def load_all_pdfs(pdf_dir: Path = PDF_DIR) -> dict[str, str]:
    """
    Load all PDFs and return their extracted text.
    """
    pdf_texts = {}

    for pdf_file in get_pdf_files(pdf_dir):
        pdf_texts[pdf_file.name] = extract_text_from_pdf(pdf_file)

    return pdf_texts
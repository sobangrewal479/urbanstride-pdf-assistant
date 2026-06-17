from src.pdf_loader import get_pdf_files, load_all_pdfs


def test_pdf_files_exist():
    pdf_files = get_pdf_files()

    assert len(pdf_files) == 3

    pdf_names = [pdf.name for pdf in pdf_files]

    assert "UrbanStride_Product_Catalog_2026.pdf" in pdf_names
    assert "UrbanStride_Shipping_Returns_Warranty_2026.pdf" in pdf_names
    assert "UrbanStride_Size_Care_Guide_2026.pdf" in pdf_names


def test_all_pdfs_load_successfully():
    pdf_texts = load_all_pdfs()

    assert len(pdf_texts) == 3

    for document_name, text in pdf_texts.items():
        assert document_name.endswith(".pdf")
        assert len(text.strip()) > 100
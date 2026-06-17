from src.pdf_loader import load_all_pdfs


def test_product_catalog_text_extraction():
    pdf_texts = load_all_pdfs()

    catalog_text = pdf_texts["UrbanStride_Product_Catalog_2026.pdf"]

    assert "UrbanWalk Pro" in catalog_text
    assert "StreetFlex Runner" in catalog_text
    assert "MetroClassic Leather" in catalog_text


def test_shipping_policy_text_extraction():
    pdf_texts = load_all_pdfs()

    shipping_text = pdf_texts["UrbanStride_Shipping_Returns_Warranty_2026.pdf"]

    assert "Standard shipping usually takes 4 to 7 business days" in shipping_text
    assert "UrbanStride accepts returns within 30 days" in shipping_text
    assert "90-day limited warranty" in shipping_text


def test_size_care_text_extraction():
    pdf_texts = load_all_pdfs()

    care_text = pdf_texts["UrbanStride_Size_Care_Guide_2026.pdf"]

    assert "UrbanWalk Lite has a slightly narrow fit" in care_text
    assert "Do not put mesh or knit shoes in a washing machine" in care_text
    assert "Most UrbanStride shoes are not waterproof" in care_text
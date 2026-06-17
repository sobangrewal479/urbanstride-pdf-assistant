from src.fallback import get_fallback_response


def test_general_fallback_for_missing_product():
    answer = get_fallback_response("Do you sell kids shoes?")

    assert "could not find that information" in answer
    assert "support@urbanstride-demo.com" in answer


def test_stock_fallback_for_live_availability():
    answer = get_fallback_response("Is UrbanWalk Pro in black size 10 available right now?")

    assert "may not show live stock" in answer
    assert "support@urbanstride-demo.com" in answer


def test_order_status_fallback():
    answer = get_fallback_response("Where is my order #US9283?")

    assert "do not include live order status" in answer
    assert "tracking email" in answer


def test_medical_fallback():
    answer = get_fallback_response("I have heel pain. Which shoe will cure it?")

    assert "do not give medical advice" in answer
    assert "healthcare professional" in answer
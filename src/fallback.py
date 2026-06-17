SUPPORT_EMAIL = "support@urbanstride-demo.com"

GENERAL_FALLBACK = (
    "Sorry, I could not find that information in the provided UrbanStride documents. "
    f"Please contact UrbanStride support at {SUPPORT_EMAIL} for confirmation."
)

STOCK_FALLBACK = (
    "The PDF catalog includes general product availability, but it may not show live stock. "
    f"Please contact {SUPPORT_EMAIL} to confirm current availability."
)

ORDER_STATUS_FALLBACK = (
    "The provided UrbanStride documents do not include live order status. "
    "Please check your tracking email or contact UrbanStride support at "
    f"{SUPPORT_EMAIL} for order-specific updates."
)

MEDICAL_FALLBACK = (
    "The provided UrbanStride documents do not give medical advice or promise cures. "
    "For foot pain, injuries, or medical concerns, please contact a qualified healthcare professional."
)


def get_fallback_response(question: str) -> str:
    """
    Return the safest fallback response based on the user's question.
    """

    question_lower = question.lower()

    stock_words = ["available right now", "in stock", "stock", "available now", "current availability"]
    order_words = ["order #", "order number", "where is my order", "tracking", "track my order"]
    medical_words = ["heel pain", "foot pain", "injury", "cure", "medical", "doctor"]

    if any(word in question_lower for word in stock_words):
        return STOCK_FALLBACK

    if any(word in question_lower for word in order_words):
        return ORDER_STATUS_FALLBACK

    if any(word in question_lower for word in medical_words):
        return MEDICAL_FALLBACK

    return GENERAL_FALLBACK
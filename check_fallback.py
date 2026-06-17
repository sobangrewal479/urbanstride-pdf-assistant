from src.fallback import get_fallback_response


def main():
    test_questions = [
        "Do you sell kids shoes?",
        "Is UrbanWalk Pro in black size 10 available right now?",
        "Where is my order #US9283?",
        "I have heel pain. Which shoe will cure it?",
    ]

    print("Fallback test started")
    print("-" * 40)

    for question in test_questions:
        print(f"Question: {question}")
        print(f"Fallback: {get_fallback_response(question)}")
        print("-" * 40)

    print("Fallback test completed successfully")


if __name__ == "__main__":
    main()
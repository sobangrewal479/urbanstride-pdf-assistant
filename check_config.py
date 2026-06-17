from src.config import OPENAI_MODEL, has_valid_openai_key


def main():
    print("Config check started")
    print("-" * 40)
    print(f"OpenAI model: {OPENAI_MODEL}")
    print(f"Real API key found: {has_valid_openai_key()}")
    print("-" * 40)
    print("Config check completed successfully")


if __name__ == "__main__":
    main()
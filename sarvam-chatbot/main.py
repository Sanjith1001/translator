from src.chat import chat


def main() -> None:
    print("Indian Language Chatbot CLI")
    print("Type 'exit' to quit.")

    history = []
    while True:
        user_message = input("You: ").strip()
        if not user_message:
            continue
        if user_message.lower() in {"exit", "quit"}:
            print("Goodbye!")
            break

        reply, lang_code, history = chat(user_message, history=history)
        print(f"Detected: {lang_code}")
        print(f"Assistant: {reply}\n")


if __name__ == "__main__":
    main()


import os


def get_response(user_input):
    message = user_input.lower().strip()

    # Greetings
    if message in ["hi", "hello", "hey", "good morning",
                   "good afternoon", "good evening"]:
        return "Hello! Welcome to DecodeBot. How can I help you?"

    # Introduction
    elif message in ["what is your name", "who are you",
                     "introduce yourself"]:
        return "I am DecodeBot, a rule-based AI chatbot built using Python."

    # Small talk
    elif message in ["how are you", "how are you doing"]:
        return "I'm doing great! Thanks for asking. How are you?"

    elif message in ["i am fine", "i'm fine", "fine", "good"]:
        return "That's great to hear! What would you like to learn today?"

    # AI questions
    elif message in ["what is ai", "define ai",
                     "what is artificial intelligence"]:
        return (
            "Artificial Intelligence (AI) is a field of computer science "
            "that enables machines to perform tasks requiring human-like "
            "intelligence."
        )

    elif message in ["what is machine learning", "define machine learning"]:
        return (
            "Machine Learning is a branch of AI that enables computers "
            "to learn patterns from data and make predictions or decisions."
        )

    elif message in ["what is a chatbot", "what is chatbot",
                     "define chatbot"]:
        return (
            "A chatbot is a computer program designed to communicate "
            "with users through text or voice."
        )

    # Programming questions
    elif message in ["what is python", "define python"]:
        return (
            "Python is a high-level programming language known for its "
            "readable syntax and wide range of applications."
        )

    elif message in ["what is a loop", "define loop"]:
        return (
            "A loop repeats a block of code. Python provides for loops "
            "and while loops."
        )

    elif message in ["what is a function", "define function"]:
        return (
            "A function is a reusable block of code that performs a "
            "specific task."
        )

    # Project information
    elif message in ["what is your purpose", "why were you created"]:
        return (
            "I demonstrate rule-based chatbot development using Python, "
            "conditional statements, functions, and loops."
        )

    # Help
    elif message in ["help", "menu", "what can you do"]:
        return (
            "Here are my available topics and commands:\n"
            "1. Greetings and small talk\n"
            "2. Artificial Intelligence\n"
            "3. Machine Learning\n"
            "4. Chatbots and Python\n"
            "5. Loops and functions\n"
            "6. Type 'history' to view this session's conversation\n"
            "7. Type 'clear' to clear the terminal screen\n"
            "8. Type 'bye' to exit"
        )

    # Thanks
    elif message in ["thanks", "thank you"]:
        return "You're welcome! Happy to help."

    # Unknown input
    else:
        return (
            "Sorry, I don't understand that yet. "
            "Try rephrasing your question or type 'help'."
        )


def main():
    conversation_history = []

    print("=" * 50)
    print("             WELCOME TO DECODEBOT")
    print("              Rule-Based AI Chatbot")
    print("=" * 50)
    print("Type 'help' for available options.")
    print("Type 'history' to view this conversation.")
    print("Type 'bye' to exit.\n")

    while True:
        try:
            user_input = input("You: ").strip()

            if not user_input:
                print("Bot: Please enter a message.\n")
                continue

            message = user_input.lower()

            # Exit commands
            if message in ["bye", "goodbye", "exit", "quit"]:
                response = "Goodbye! Thank you for chatting with DecodeBot."
                print("Bot:", response)
                conversation_history.append(
                    ("You", user_input, "Bot", response)
                )
                break

            # Display conversation history
            elif message == "history":
                if not conversation_history:
                    print("Bot: No conversation history yet.\n")
                else:
                    print("\n--- Conversation History ---")
                    for user, question, bot, answer in conversation_history:
                        print(f"{user}: {question}")
                        print(f"{bot}: {answer}\n")
                continue

            # Clear the terminal screen
            elif message == "clear":
                os.system("cls" if os.name == "nt" else "clear")
                print("DecodeBot - Rule-Based AI Chatbot\n")
                continue

            # Generate a response
            response = get_response(user_input)
            print("Bot:", response, "\n")

            # Store the interaction in session history
            conversation_history.append(
                ("You", user_input, "Bot", response)
            )

        except (EOFError, KeyboardInterrupt):
            print("\nBot: Chat session ended. Goodbye!")
            break


if __name__ == "__main__":
    main()

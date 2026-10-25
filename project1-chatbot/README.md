# DecodeBot – Rule-Based AI Chatbot

## 1. Project Overview

DecodeBot is a rule-based chatbot developed using Python as part of the DecodeLabs Artificial Intelligence Internship, 2026.

The chatbot simulates basic human interaction by accepting text input from users and generating predefined responses using conditional statements. It continues the conversation until the user enters an exit command.

## 2. Project Objectives

- Understand the fundamentals of rule-based Artificial Intelligence.
- Implement decision-making using `if`, `elif`, and `else` statements.
- Handle greetings, common questions, and exit commands.
- Use a continuous loop to support repeated interactions.
- Handle unknown inputs with appropriate fallback responses.
- Develop practical Python programming skills.

## 3. Technologies Used

- **Programming Language:** Python
- **Code Editor:** Visual Studio Code
- **Version Control:** Git
- **Code Hosting:** GitHub

### Python Concepts

- Conditional statements
- `while` loop
- Functions
- String handling
- Lists
- User input and output

## 4. Features

- **Greeting Handling:** Responds to greetings such as `hi`, `hello`, and `hey`.
- **Chatbot Introduction:** Provides information about its name and purpose.
- **General Conversation:** Responds to predefined conversational questions.
- **AI Information:** Answers basic questions about Artificial Intelligence.
- **Python Information:** Provides a basic explanation of Python.
- **Chatbot Information:** Explains what a chatbot is.
- **Help Menu:** Lists supported questions and commands.
- **Case-Insensitive Input:** Recognizes supported phrases regardless of capitalization.
- **Unknown-Input Handling:** Provides a fallback response when the input does not match a predefined rule.
- **Exit Commands:** Ends the conversation when the user enters `bye`, `goodbye`, `exit`, or `quit`.

## 5. Project Structure

```text
DecodeLabs_AI_Chatbot/
├── chatbot.py
└── README.md
```

## 6. How It Works

1. The chatbot displays a welcome message.
2. The user enters a message through the terminal.
3. The program converts the input to lowercase and removes surrounding whitespace for response matching.
4. The `get_response()` function checks the message against predefined conditions.
5. The chatbot returns the corresponding response or a fallback message.
6. The `while` loop continues the conversation until an exit command is entered.

## 7. Installation and Execution

### Prerequisites

- Python 3 installed on your computer.
- Visual Studio Code or another Python-compatible editor.
- Git installed for version control.

### Steps to Run

1. Clone or download the project repository.
2. Open the project folder in Visual Studio Code.
3. Open a terminal in the project directory.
4. Execute the following command:

```bash
python chatbot.py
```

On Windows, you can also use:

```powershell
py chatbot.py
```

5. Enter a message when prompted.
6. Type `help` to see supported commands.
7. Type `bye`, `goodbye`, `exit`, or `quit` to end the conversation.

## 8. Sample Interaction

```text
WELCOME TO DECODEBOT
Rule-Based AI Chatbot

You: HELLO
Bot: Hello! Welcome to DecodeBot. How can I help you?

You: what is AI
Bot: Artificial Intelligence (AI) is a field of computer science
that enables machines to perform tasks requiring human-like intelligence.

You: help
Bot: Here is what you can ask me:
1. Say hello or hi
2. Ask how I am
3. Ask my name
4. Ask about Artificial Intelligence
5. Ask about chatbots or Python
6. Ask about my purpose
7. Type 'bye' to exit

You: bye
Bot: Goodbye! Thank you for chatting with DecodeBot.
```

*Note: The sample output is illustrative; line wrapping may differ in the terminal.*

## 9. Testing

The following test cases can be used to verify the chatbot.

| Test Case | Input | Expected Result |
|---|---|---|
| Greeting | `hello` | Displays a greeting |
| Capitalization | `HELLO` | Recognizes the greeting |
| Introduction | `who are you` | Introduces the chatbot |
| AI question | `what is AI` | Explains Artificial Intelligence |
| Python question | `what is python` | Explains Python |
| Help command | `help` | Displays supported questions |
| Unknown input | `tell me a joke` | Displays a fallback response |
| Empty input | Press Enter without typing | Requests a message |
| Exit command | `bye` | Displays goodbye and terminates |

## 10. Limitations

- Responses are predefined and depend on programmed conditions.
- The chatbot does not learn from previous conversations.
- It cannot reliably answer questions outside its supported rules.
- It does not use machine learning or a language model.

## 11. Future Enhancements

- Add more predefined questions and responses.
- Organize chatbot intents and responses into separate modules.
- Develop a graphical user interface.
- Add conversation history.
- Explore natural language processing techniques in a future version.

## 12. Conclusion

DecodeBot demonstrates the fundamentals of rule-based chatbot development using Python. The project applies conditional statements, functions, string handling, and loops to simulate a simple conversation. It provides practical experience with basic AI concepts, software testing, and GitHub-based version control.

## Internship Information

**Organization:** DecodeLabs  
**Program:** Artificial Intelligence Internship  
**Project:** Project 1 – Rule-Based AI Chatbot  
**Year:** 2026
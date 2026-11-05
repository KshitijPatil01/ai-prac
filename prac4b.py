#TC:(n*k)
import re
rules = [
    (r"\bhello\b|\bhi\b|\bhey\b", "Hello! How can I help you?"),
    (r"\bhow are you\b", "I am fine! How are you?"),
    (r"\byour name\b", "I am a simple chatbot."),
    (r"\bcollege\b", "College is a great place to learn."),
    (r"\bthank you\b|\bthanks\b", "You're welcome!")
]

print("Chatbot: Hello! Welcome to the chatbot.")
print("Type 'bye', 'goodbye' or 'exit' to end.")

while True:

    user = input("You: ").lower().strip()

    # Check exit condition
    if re.search(r"\bbye\b|\bgoodbye\b|\bexit\b", user):
        print("Chatbot: Goodbye! Have a nice day.")
        break
    found = False
    # Match user input with predefined rules
    for pattern, response in rules:
        if re.search(pattern, user):
            print("Chatbot:", response)
            found = True
            break

    if not found:
        print("Chatbot: Sorry, I didn't understand that.")

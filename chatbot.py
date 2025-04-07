import nltk
from nltk.chat.util import Chat, reflections

# Define predefined responses using pattern-response pairs
pairs = [
    (r"hi|hello|hey", ["Hello!", "Hey there!", "Hi! How can I assist you?"]),
    (r"how are you?", ["I'm just a bot, but I'm doing great!", "I'm fine, thanks for asking!"]),
    (r"what is your name?", ["I'm a chatbot!", "You can call me ChatBot."]),
    (r"who created you?", ["I was created by a programmer!", "I'm a result of some cool coding skills."]),
    (r"what can you do?", ["I can chat with you, answer simple questions, and keep you entertained!"]),
    (r"bye|goodbye", ["Goodbye!", "See you soon!", "Bye! Have a great day!"]),
    (r"(.*)", ["I'm not sure how to respond to that.", "Can you ask something else?", "Interesting! Tell me more."])
]

# Create a chatbot instance
chatbot = Chat(pairs, reflections)

# Start chatting with the user
def start_chat():
    print("Hello! I'm your chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ").lower()
        if user_input in ["bye", "exit", "quit"]:
            print("ChatBot: Goodbye! Have a great day!")
            break
        response = chatbot.respond(user_input)
        print("ChatBot:", response)

# Run the chatbot
if __name__ == "__main__":
    start_chat()



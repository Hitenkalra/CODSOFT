import re

def chatbot():
    print("Hi! I'm ChatBot. Type 'exit' to end the chat.")

    while True:
        user_input = input("You: ").lower().strip()

        # Exit condition
        if user_input in ['exit', 'quit', 'bye']:
            print("ChatBot: Goodbye! Have a great day.")
            break

        # Rule-based responsesh
        if re.search(r'hello|hi|hey', user_input):
            print("ChatBot: Hello there! How can I help you today?")
        elif re.search(r'how are you', user_input):
            print("ChatBot: I'm just a program, but I'm doing great! Thanks for asking.")
        elif re.search(r'what is your name', user_input):
            print("ChatBot: I am a simple rule-based chatbot.")
        elif re.search(r'your purpose|what do you do', user_input):
            print("ChatBot: I respond to your questions based on predefined rules!")
        elif re.search(r'thank you|thanks', user_input):
            print("ChatBot: You're welcome!")
        elif re.search(r'time', user_input):
            from datetime import datetime
            now = datetime.now()
            print(f"ChatBot: Current time is {now.strftime('%H:%M:%S')}")
        elif re.search(r'date', user_input):
            from datetime import datetime
            today = datetime.today()
            print(f"ChatBot: Today's date is {today.strftime('%Y-%m-%d')}")
        else:
            print("ChatBot: Sorry, I don't understand that. Can you rephrase?")

# Run the chatbot
if __name__ == "__main__":
    chatbot()

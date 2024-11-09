import datetime

# Define responses for keywords
responses = {
    "hello": "Hello! How can I help you today?",
    "hi": "Hi there! What’s on your mind?",
    "weather": "I'm not sure about the weather, but it’s always a good day to code!",
    "time": f"The current time is {datetime.datetime.now().strftime('%H:%M')}.",
    "day": f"Today is {datetime.datetime.now().strftime('%A')}.",
    "python": "Python is a versatile programming language, great for web development, data science, and more.",
    "bye": "Bye! Have a great day!",
}

def chatbot():
    print("Chatbot: Hello! I’m here to chat. Type 'bye' to exit.")
    
    while True:
        # Get user input
        user_input = input("You: ").strip().lower()
        
        # Check if the user wants to exit
        if user_input == "bye":
            print("Chatbot:", responses["bye"])
            break
        
        # Check for a matching keyword in the user's input
        response = None
        for keyword in responses:
            if keyword in user_input:
                response = responses[keyword]
                break
        
        # Print the response or a default message if no keyword is found
        if response:
            print("Chatbot:", response)
        else:
            print("Chatbot: I'm sorry, I don't understand. Can you try asking something else?")

if __name__ == "__main__":
    chatbot()

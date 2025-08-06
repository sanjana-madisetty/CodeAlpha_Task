def chatbot():
    print("hello! i am your chatbot. Type 'bye' to exit.")
    while True:
        user_input=input("you:").lower()
        if user_input=="hello":
            print("Bot:Hi!")
        elif user_input=="how are you":
            print("Bot: I'm fine,thanks!")
        elif user_input=="bye":
            print("Bot: goodbye!")
            break
        else:
            print("Bot: I don't understand that!")
chatbot()

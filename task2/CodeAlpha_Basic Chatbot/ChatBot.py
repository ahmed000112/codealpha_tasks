def chatbot():
    print("🤖 Chatbot: Hello! Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()
        
        if user_input in ["hello", "hi", "hey"]:
            print("Chatbot: Hi!")

        elif user_input in ["how are you", "how are you?"]:
            print("Chatbot: I'm fine, thanks!")

        elif user_input in ["what is your name", "who are you"]:
            print("Chatbot: I'm a simple chatbot.")

        elif user_input in ["good morning"]:
            print("Chatbot: Good morning!")

        elif user_input in ["good afternoon"]:
            print("Chatbot: Good afternoon!")

        elif user_input in ["good evening"]:
            print("Chatbot: Good evening!")

        elif user_input in ["what are you doing"]:
            print("Chatbot: Just chatting with you!")

        elif user_input in ["thank you", "thanks"]:
            print("Chatbot: You're welcome!")

        elif user_input in ["sorry"]:
            print("Chatbot: No problem!")

        elif user_input in ["help"]:
            print("Chatbot: I can respond to basic questions like greetings.")

        elif user_input in ["what is python"]:
            print("Chatbot: Python is a programming language.")

        elif user_input in ["what is ai"]:
            print("Chatbot: AI stands for Artificial Intelligence.")

        elif user_input in ["who made you"]:
            print("Chatbot: I was created by a programmer like you!")

        elif user_input in ["where are you from"]:
            print("Chatbot: I live inside your computer.")

        elif user_input in ["tell me a joke"]:
            print("Chatbot: Why did the computer get cold? Because it left its Windows open!")

        elif user_input in ["what time is it"]:
            print("Chatbot: I can't check time, but your system can!")

        elif user_input in ["what is your favorite color"]:
            print("Chatbot: I like blue!")

        elif user_input in ["do you like music"]:
            print("Chatbot: Yes, I enjoy digital music!")

        elif user_input in ["what is your hobby"]:
            print("Chatbot: Chatting with humans!")

        elif user_input in ["are you human"]:
            print("Chatbot: No, I'm a chatbot.")

        elif user_input in ["what is your purpose"]:
            print("Chatbot: To help and chat with you.")

        elif user_input in ["can you help me"]:
            print("Chatbot: Sure! Tell me your question.")

        elif user_input in ["what is your age"]:
            print("Chatbot: I don't have an age.")

        elif user_input in ["what is computer"]:
            print("Chatbot: A computer is an electronic machine.")

        elif user_input in ["do you sleep"]:
            print("Chatbot: No, I am always awake!")

        elif user_input in ["are you smart"]:
            print("Chatbot: I try my best!")

        elif user_input in ["what is internet"]:
            print("Chatbot: Internet is a global network.")

        elif user_input in ["who is your friend"]:
            print("Chatbot: You are my friend!")

        elif user_input in ["do you eat"]:
            print("Chatbot: No, I don't eat.")

        elif user_input in ["do you drink"]:
            print("Chatbot: No, I don't drink.")

        elif user_input in ["bye", "exit", "quit"]:
            print("Chatbot: Goodbye!")
            break

        else:
            print("Chatbot: Sorry, I don't understand that.")
chatbot()
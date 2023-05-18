#!usr/bin/env python3

# A simple chatbot using chatterbot and chatternot-corpus

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

def train_chatbot(chatbot):
    trainer = ChatterBotCorpusTrainer(chatbot)
    trainer.train("chatterbot.corpus.english.greetings", "chatterbot.corpus.english.conversations")

def get_chatbot_response(chatbot, user_input):
    return chatbot.get_response(user_input)

def chat():
    chatbot = ChatBot("My Chatbot")
    train_chatbot(chatbot)

    print("Chatbot: Hello! How can I assist you today?")

    while True:
        user_input = input("User: ")

        if user_input.lower() == "bye":
            print("Chatbot: Goodbye!")
            break

        response = get_chatbot_response(chatbot, user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    chat()
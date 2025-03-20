# Lógica principal do chatbot

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# Lógica principal do chatbot
from src.chatbot import chatbot

if __name__ == "__main__":
    chatbot = chatbot()
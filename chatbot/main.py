from fastapi import FastAPI
from chatbot.chat import ChatInteraction

app = FastAPI()
bot = ChatInteraction()

@app.post("/chat/{prompt}")
def chat(prompt: str):
    response = bot.chat_interface(prompt)
    return response

@app.get("/view_chat")
def view_chat():
    return bot.view_chat_history()

# To start server:
# fastapi dev main.py
# https://www.youtube.com/watch?v=vzC2alPiWz0
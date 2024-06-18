import io
import os
import telebot
from PIL import Image


class TelegramBot:
    def __init__(self):
        CHAT_ID = os.getenv("TELEGRAM_CHAT")
        TELEGRAM_KEY = os.getenv("TELEGRAM_KEY")
        if not CHAT_ID or not TELEGRAM_KEY:
            raise Exception("Bot could not be initialized")
        self.bot = telebot.TeleBot(TELEGRAM_KEY)
        self.chat_id = CHAT_ID

    def send_image(self, frame):
        img = Image.fromarray(frame)
        bio = io.BytesIO()
        bio.name = "bit_is_here.jpeg"
        img.save(bio, "JPEG")
        bio.seek(0)
        self.bot.send_photo(self.chat_id, bio)

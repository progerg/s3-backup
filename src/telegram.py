import requests
from config import TG_BOT_TOKEN, TG_CHAT_ID


class Telegram:
    @staticmethod
    def send_message(text: str):
        data = {
            "chat_id": TG_CHAT_ID,
            "text": text
        }
        requests.post(f"https://api.telegram.org/bot{TG_BOT_TOKEN}/sendMessage", json=data)

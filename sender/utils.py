import requests
from decouple import config

def usdispatch_send_telegram_message(message_text):
    chat_id = config('USDISPATCH_CHAT_ID')
    bot_token = config('USDISPATCH_BOT_TOKEN')
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {"chat_id": chat_id, "text": message_text}
    requests.post(url, json=payload)

# USfuelsystems
def usfuelsystems_send_telegram_message(message_text):
    chat_id = config('USFUELSYSTEMS_CHAT_ID')
    bot_token = config('USFUELSYSTEMS_BOT_TOKEN')
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {"chat_id": chat_id, "text": message_text}
    requests.post(url, json=payload)

import requests, json
from bot_mp.settings import TOKEN, sock


def build_keyboard():
    keyboard = [[item] for item in ['Liga', 'Desliga']]
    reply_markup = {"keyboard": keyboard}
    return json.dumps(reply_markup)


def send_message(text, chat_id):
    data = {'chat_id': chat_id, 'text': text, 'reply_markup': build_keyboard()}
    url = 'https://api.telegram.org/bot{}/sendMessage'.format(TOKEN)
    requests.post(url, data = data)


def send_message_esp(text):
    sock.sendto(text.encode('ascii'), ('10.224.24.40', 1060))


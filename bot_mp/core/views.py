from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from bot_mp.core.utils import send_message, send_message_esp


def home(request):
    return render(request, "index.html")


@csrf_exempt
def event(requests):
    json_list = json.loads(requests.body)
    first_name = json_list['message']['chat']['first_name']
    chat_id = json_list['message']['chat']['id']
    text_message = json_list['message']['text']
    print('{} disse: {}'.format(first_name, text_message))
    if not text_message in ('Liga', 'Desliga'):
        send_message('{}, use o teclado para acionar o dispositivo.'.format(first_name), chat_id)
    else:
        send_message_esp(text_message)
    return HttpResponse()

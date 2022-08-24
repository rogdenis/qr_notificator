import json
import requests
import time
import sys

BOT_TOKEN = '1618200578:AAGxrM7DkYfyNCin5OyULGIWZvBCJBEWObg'
CHANNEL = '-1001365917705'
HELP_REPLY = "Принцип прост - ты постишь свою фотку и где ты находишься. Мы показываем тебе тех, кто поблизости. Вы взаимно лайкаете друг-друга, а дальше всё зависит от тебя)"
CREATE_REPLY = "Чтобы создать объявление нам потребуется:\n твоё селфи(чтобы тебя сразу нашли) \nтвоё местоположение на данные момент\nимя\nпол\nкого ищем"
UPS = "Что-то пошло не так"

def send_tg_message(chat_id, text):
    r = requests.get('https://api.telegram.org/bot{}/sendMessage'.format(BOT_TOKEN), params=dict(
        chat_id=chat_id,
        text=text
    ))
    if r.status_code != 200:
        sys.stderr.write(text)
        sys.stderr.write(r.text)
        raise
    return "Done!"

def handler(event, context):
    try:
        userid = event["queryStringParameters"]["id"]
        send_tg_message(userid, "Стирка закончена!")
        return {
            'statusCode': 200,
            'body':{"result":"Successfully sent!","color":"#09a129"}
        }
    except:
        return {
            'statusCode': 200,
            'body':{"result":"Failed(","color":"#f21b3f"}
        }
from telegram.ext import Updater, InlineQueryHandler, CommandHelper
import requests
import re
import os

PORT = int(os.environ.get('PORT', 5000))
TOKEN = os.environ["TOKEN"]
API_ENDPOINT = ""

# function to obtain the URL of
def get_url():
    contents = requests.get(API_ENDPOINT).json()
    url = contents['message']
    return url

def get_lyric_url

def lyric(update, context):
    url = get_lyric_url()
    chat_id = update.message.chat.id
    context.bot.send_message(chat_id=chat_id,text=url)

import urllib.request
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from telegram.ext import Updater, InlineQueryHandler, CommandHandler, MessageHandler, Filters
import requests
import os
import re

PORT = int(os.environ.get('PORT', 5000))
TOKEN = os.environ["5052808423:AAGL9xY4r16WfPsAr111BJiQcUuOoymJ1lQ"]

def song(update, context):
    text = update.message.text
    def get_song_url():
        song_choice = text
        req = Request("https://glccsongbook.github.io/english.html")
        html_page = urlopen(req)

        soup = BeautifulSoup(html_page, "lxml")

        links = []
        for link in soup.findAll('a'):
            links.append(link.get('href'))

        song_choice = song_choice.replace(" ", "-").replace(",", "")
        pattern = re.compile(song_choice)
        str_match = [x for x in links if re.search(song_choice, x)]

        song_url = "https://glccsongbook.github.io" + ''.join(map(str, str_match)).replace('.', '', 1)

        return song_url

    def print_lyrics():
        song_url = get_song_url()
        soup = BeautifulSoup(urllib.request.urlopen(song_url), "lxml")
        result = soup.find_all("div", {"class": "bs-component"})
        lyrics = result[1].text

        return lyrics
    lyrics = print_lyrics()
    chat_id = update.message.chat.id
    update.message.reply_text(chat_id=chat_id, message=lyrics)
    return

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.text, song))

    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook('https://glcc-lyric-bot.herokuapp.com/' + TOKEN)
    updater.idle()

if __name__ == '__main__':
    main()
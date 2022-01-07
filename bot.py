import urllib.request

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re

# This uses bs4 to extract all the links in the english page
song_choice = "just"

req = Request("https://glccsongbook.github.io/english.html")
html_page = urlopen(req)

soup = BeautifulSoup(html_page, "lxml")

links = []
for link in soup.findAll('a'):
    links.append(link.get('href'))

song_choice = song_choice.replace(" ", "-").replace(",", "")
pattern = re.compile(song_choice)
str_match = [x for x in links if re.search(song_choice, x)]

song_url = "https://glccsongbook.github.io"+''.join(map(str, str_match)).replace('.', '', 1)

soup = BeautifulSoup(urllib.request.urlopen(song_url),"lxml")
result = soup.find_all("div", {"class":"bs-component"})

print(result[1].text)
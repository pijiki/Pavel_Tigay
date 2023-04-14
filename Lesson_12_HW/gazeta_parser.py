import requests
import unicodedata
import re
from bs4 import BeautifulSoup
import json


CATEGORY = 'news'
URL = 'https://www.gazeta.ru/' + CATEGORY
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
html = requests.get(URL, headers=HEADERS).text
soup = BeautifulSoup(html, 'html.parser')
articles = soup.find_all('div', class_='nblock')

json_data = []
for article in articles:
    title = article.find('div', class_='pobbzvtq b_ear-title').get_text(strip=True)
    publication_orig = article.find('time', class_='b_ear-time').get_text()
    publication = re.match(r'(\d+ \w+ \d+,|\w+,) \d\d:\d\d', publication_orig).group()
    image_link = article.find('b_ear-image mgffo')
    description = article.find('div', class_='nt').get_text()

    json_data.append({
        'title': unicodedata.normalize('NFKD', title),
        'context': unicodedata.normalize('NFKD', description),
        'image_link': image_link
    })

with open(f'gazeta_{CATEGORY}.json', mode='w', encoding='UTF-8') as file:
    json.dump(json_data, file, ensure_ascii=False, indent=4)



import requests
from bs4 import BeautifulSoup
import json


def get_content(url):
    response = requests.get(url, headers={
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36'})
    soup = BeautifulSoup(response.content, 'html.parser')
    news = soup.findAll('div', {'class', 'posts one-in-row'})

    news_dict = {}
    for index, value in enumerate(news):
        news_dict[index + 1] = {
            'image_url': value.find('div', {'posts__item'}).find('a', {'posts__item_img'}).find('img').get('src'),
            'title': value.find('div', {'class', 'posts__item_title'}).get_text(),
            'description': value.find('p').get_text(),
            'date': value.find('span', {'posts__item_date'}).get_text()
        }
    return news_dict[1]

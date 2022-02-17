import time
import json
import requests
from bs4 import BeautifulSoup

from config import USERNAME, PASSWORD, url_login, url, user_agent

session = requests.Session()

session.headers.update({'Referer': url_login})
session.headers.update(user_agent)
_xsrf = session.cookies.get('_xsrf', domain="monitor.st65.ru/")

post_request = session.post(url_login, {
    'name': USERNAME,
    'password': PASSWORD,
    'autologin': '1',
    'enter': 'Sign in'
})

result = []

def get_page():
    response = session.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    return soup

def get_addresses(page):
    quotes = page.find_all('span', class_='link-action')

    addresses = []
    for item in quotes:
        item_attr = item.get('data-menu-popup')
        if '"type":"host"' in str(item_attr):
            addresses.append(item.text)

    return addresses[:10]

while True:
    result = get_addresses(get_page())
    with open("info.json", 'w', encoding='utf-8') as write_info:
        json.dump(result, write_info, ensure_ascii=False, indent=4)
    time.sleep(1)
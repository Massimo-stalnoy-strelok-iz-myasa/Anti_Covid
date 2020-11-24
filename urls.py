import requests
from bs4 import BeautifulSoup as BS

URL = 'https://covid.osnova.news/self-isolation/'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
           'accept': '*/*'}

URL_1 = 'https://coronavirus-online.moscow/sluchai-koronavirusa-v-moskve/'
HEADERS_1 = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36 Edg/87.0.664.41',
           'accept': '*/*'}


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BS(html, 'html.parser')
    names = soup.find_all('div', class_='card-body p-2 pl-3 text-nowrap')
    for name in names:
        all_cities.append((' '.join(name.get_text().lower().split())).split()[0])
        all_index.append((' '.join(name.get_text().lower().split())).split()[1])

def get_content_1(html):
    soup = BS(html, 'html.parser')
    otvet = ""
    streets = soup.find_all('td', class_='column-1')
    houses = soup.find_all('td', class_='column-2')
    dates = soup.find_all('td', class_='column-3')
    for i in range(len(streets)):
        otvet = streets[i].get_text() + " " + houses[i].get_text() + " " + dates[i].get_text()
        all_streets.append(otvet)
        otvet = ""



all_streets = []
all_cities = []
all_index = []

html = get_html(URL)
html_1 = get_html(URL_1)
get_content(html.text)
get_content_1(html_1.text)

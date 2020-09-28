import lxml.html as html
import autopep8
import requests
import os
import datetime

# Constantes
XPATH_LINKS_TO_ARTICLE = '//h2/a/@href'
XPATH_TITLE = '//h2/a[@class="finanzasSect"]/text()' # Devuelve una lista
XPATH_SUMMARY = '//div[@class="lead"]/p/text()'
XPATH_BODY = '//div[@class="html-content"]/p[not(@class)]/text()'
HOME_URL = 'https://www.larepublica.co/'

def parse_home():
    try:
        response = requests.get(HOME_URL)
        if response.status_code == 200:
            home = response.content.decode('utf-8')
            parsed = html.fromstring(home)
            links_to_news = parsed.xpath(XPATH_LINKS_TO_ARTICLE)
            print(links_to_news)

        else:
            raise ValueError(f'Error: {response.status_code}.')

    except ValueError as ve:
        print(ve)

def main():
    parse_home()

if __name__ == '__main__':
   main()

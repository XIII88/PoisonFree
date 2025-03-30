import requests
from bs4 import BeautifulSoup
import os


def crawl(url, depth):
    if depth == 0:
        return
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        print("Crawling:", url)

        print("Page Title:", soup.title.text)
        headers = soup.find_all('h1')
        for header in headers:
            print("Header:", header.text.strip())

        links = soup.find_all('a')
        for link in links:
            next_url = link.get('href')
            if next_url.startswith('http'):
                crawl(next_url, depth - 1)
            elif next_url.startswith('/'):
                next_url = '/'.join(url.split('/')[:3]) + next_url
                crawl(next_url, depth - 1)
    except Exception as e:
        print("Error crawling:", url)
        print(e)


start_url = input("Введите URL для краулинга: ")

depth = int(input("Введите глубину краулинга: "))

crawl(start_url, depth)

input("Краулинг завершен. Нажмите Enter для перехода в меню")

os.system("python venom.py")

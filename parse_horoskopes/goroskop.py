import requests
import time
from bs4 import BeautifulSoup as bs

headers = {
    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}

# global zodiacs
zodiacs = (
'aries/', 'taurus/', 'gemini/', 'cancer/', 'leo/', 'virgo/', 'libra/', 'scorpio/', 'sagittarius/', 'capricorn/',
'aquarius/', 'pisces/')
BASE_URL = 'https://horoscopes.rambler.ru/'
TEST_URL = 'https://horoscopes.rambler.ru/capricorn/'


def parse(BASE_URL, headers):
    goroskops = []
    session = requests.Session()
    for zodiac in zodiacs:
        url = BASE_URL + zodiac
        request = session.get(url, headers=headers)
        if request.status_code == 200:
            soup = bs(request.content, 'html.parser')
            # print(soup)
            # title = soup.find('h1').text , attrs={'data-reactid':'122'} v0ls
            title1 = soup.find('div', attrs={'class': 'v0ls'})
            title = title1.find('h1').text
            # text = soup.find('span', attrs={'data-reactid':'134'}).text
            div = soup.find('div', attrs={'class': '_1dQ3'})  # _1dQ3
            text = div.find('span').text
            # print(div)
            goroskop = {
                'title': title,
                'text': text
            }
            # print(title + text)
            goroskops.append(goroskop)
        else:
            print("ERROR")

    return goroskops


def main():
    res = parse(BASE_URL, headers)
    return res


if __name__ == '__main__':
    time1 = time.time()
    print(main())
    time2 = time.time()
    print(time2 - time1)
    time.sleep(20)
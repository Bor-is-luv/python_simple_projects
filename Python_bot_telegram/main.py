from flask import Flask
from flask import request
from flask import jsonify
from flask_sslify import SSLify
import requests
import json
import random
import pyowm


app = Flask(__name__)
sslify = SSLify(app)
token = ''
token_VK = ''
URL = 'https://api.telegram.org/bot' + token + '/'
owm = pyowm.OWM('')
observation = owm.weather_at_place('Zelenograd,Russia')
w = observation.get_weather()

last_update_id = 0


def get_tempa(a):
    tempa = a.get_temperature('celsius')['temp']
    return tempa


def get_status(a):
    det_stat = a.get_detailed_status()
    return det_stat


def write_json(data, filename='answer.json'):
    with open(filename, 'a') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def write_txt(data, filename='answer1.txt'):
    with open(filename, 'a') as f:
        f.write(data)


def send_message(chat_id, text='Wait a second, please...'):
    url = URL + 'sendmessage?chat_id={}&text={}'.format(chat_id, text)
    requests.get(url)


def send_photo(chat_id, photo_url):
    url = URL + 'sendphoto?chat_id={}&photo={}'.format(chat_id, photo_url)
    requests.get(url)


def aneki_VK(chat_id):
    rand = random.randint(1, 5000)
    params = '&v=5.92&domain=jumoreski&offset={}&count=1'.format(rand)
    com_VK = 'https://api.vk.com/method/wall.get?access_token=' + token_VK + params
    r = requests.get(com_VK)
    likes = r.json()['response']['items'][0]['likes']['count']
    while likes < 30:
        rand = random.randint(1, 5000)
        params = '&v=5.92&domain=jumoreski&offset={}&count=1'.format(rand)
        com_VK = 'https://api.vk.com/method/wall.get?access_token=' + token_VK + params
        r = requests.get(com_VK)
        likes = r.json()['response']['items'][0]['likes']['count']

    anek_text = r.json()['response']['items'][0]['text']
    if 'attachments' in r.json()['response']['items'][0]:
        if r.json()['response']['items'][0]['attachments'][0]['type'] == 'photo':
            photo_at_place = True
            anek_photo = r.json()['response']['items'][0]['attachments'][0]['photo']['sizes'][4]['url']
        else:
            photo_at_place = False

    if photo_at_place:
        send_message(chat_id, anek_text)
        send_photo(chat_id, anek_photo)
    else:
        send_message(chat_id, anek_text)

    write_txt(anek_text)


def commands(message, chat_id, photo):
    if photo:
        send_message(chat_id, 'Фотки обрабатывать будем позже')

    if message == '/temp':
        whether = owm.weather_at_place('Zelenograd,Russia')
        a = whether.get_weather()
        send_message(chat_id, get_tempa(a))
    if message == '/cloud':
        whether = owm.weather_at_place('Zelenograd,Russia')
        a = whether.get_weather()
        send_message(chat_id, get_status(a))
    if message == 'raz':
        send_message(chat_id, 'dva')
    if message == '/anek':
        aneki_VK(chat_id)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        r = request.get_json()
        name = r['message']['from']['username']
        write_txt(name)
        # write_json('\n')
        chat_id = r['message']['chat']['id']
        if 'text' in r['message']:
            message = r['message']['text']
            write_txt(message)
        else:
            message = 'rtbgrtbewrfe'
        if 'photo' in r['message']:
            photo = True
        else:
            photo = False
        commands(message, chat_id, photo)

        return jsonify(r)
    return '<h1>Bot welcom you</h1>'


def main():
    pass


if __name__ == '__main__':
    app.run()

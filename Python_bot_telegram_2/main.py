# -*- coding: utf-8 -*-

import telebot
from telebot.types import Message
from flask import Flask
from flask import request
from flask import jsonify
from flask_sslify import SSLify
import requests
import json
import random
import pyowm
import time
from bs4 import BeautifulSoup as bs
from vedis import Vedis
from enum import Enum

Zodiacs = {
    'Овен': "aries/",
    'Телец': "taurus/",
    'Близнецы': "gemini/",
    'Рак': "cancer/",
    'Лев': 'leo/',
    'Дева': 'virgo/',
    'Весы': 'libra/',
    'Скорпион': 'scorpio/',
    'Стрелец': 'sagittarius/',
    'Козерог': 'capricorn/',
    'Водолей': 'aquarius/',
    'Рыбы': 'pisces/',
    'error': 'False',
}

db_file = "database.vdb"
token = '660308305:AAG-0FberRD73c55u6obRVr__fj7LTsjWJM'
bot = telebot.TeleBot(token, threaded=False)
app = Flask(__name__)
sslify = SSLify(app)
token = ''
token_VK = ''
URL = 'https://api.telegram.org/bot' + token + '/'
owm = pyowm.OWM('')
BASE_URL = 'https://horoscopes.rambler.ru/'
TEST_URL = 'https://horoscopes.rambler.ru/capricorn/'

headers = {
    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}
secret = ''
url = 'https://.pythonanywhere.com/' + secret

bot.remove_webhook()
bot.set_webhook(url=url)


@app.route('/' + secret, methods=['POST'])
def webhook():
    update = telebot.types.Update.de_json(request.stream.read().decode('utf-8'))
    bot.process_new_updates([update])
    return 'ok', 200


def get_current_state(user_id):
    with Vedis(db_file) as db:
        try:
            return db[user_id].decode()  # Если используете Vedis версии ниже, чем 0.7.1, то .decode() НЕ НУЖЕН
        except KeyError:  # Если такого ключа почему-то не оказалось
            return False  # значение по умолчанию - начало диалога


# Сохраняем текущее «состояние» пользователя в нашу базу
def set_state(user_id, value):
    with Vedis(db_file) as db:
        try:
            db[user_id] = value
            return True
        except:
            print('Что-то не так')
            return False


def write_txt(data, filename='answer1.txt'):
    with open(filename, 'a') as f:
        f.write(data)
        f.write('\n')


def send_goroskope(message, BASE_URL, headers):
    url_goroskop = BASE_URL + get_current_state(message.chat.id)
    session = requests.Session()
    request = session.get(url_goroskop, headers=headers)
    if request.status_code == 200:
        soup = bs(request.content, 'html.parser')
        div = soup.find('div', attrs={'class': '_1dQ3'})  # _1dQ3
        text = div.find('span').text
        bot.send_message(message.chat.id, text)
    else:
        bot.send_message(message.chat.id, "ERROR")


def chek_goroskope(message, BASE_URL, headers):  # , BASE_URL, headers
    if get_current_state(message.chat.id) != Zodiacs['error']:
        send_goroskope(message, BASE_URL, headers)
    else:
        bot.send_message(message.chat.id, 'Tell me your zodiac in Russian')


@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    itembtn1 = telebot.types.KeyboardButton('Вау')
    itembtn2 = telebot.types.KeyboardButton('Супер!')
    itembtn3 = telebot.types.KeyboardButton('Великолепно)))')
    markup.row(itembtn1)
    markup.row(itembtn2, itembtn3)
    bot.send_message(message.chat.id, 'Будем программировать ботов для telegram :-)))', reply_markup=markup)
    set_state(message.chat.id, Zodiacs['error'])


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id, 'I can say you weather at your place, your goroskop for today or talk jumoreska')


@bot.message_handler(commands=['anek'])
def send_anek(message):
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
        bot.send_message(message.chat.id, anek_text)
        bot.send_photo(message.chat.id, anek_photo)
    else:
        bot.send_message(message.chat.id, anek_text)

    write_txt(anek_text)


@bot.message_handler(commands=['temp'])
def send_temp(message):
    markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    itembtn1 = telebot.types.KeyboardButton('TempZelenograd')
    itembtn2 = telebot.types.KeyboardButton('TempBryansk')
    itembtn3 = telebot.types.KeyboardButton('TempSPB')
    markup.row(itembtn1)
    markup.row(itembtn2, itembtn3)
    bot.send_message(message.chat.id, "Choose your city:", reply_markup=markup)


@bot.message_handler(commands=['cloud'])
def send_cloud(message):
    markup = telebot.types.ReplyKeyboardMarkup()
    itembtn1 = telebot.types.KeyboardButton('CloudZelenograd')
    itembtn2 = telebot.types.KeyboardButton('CloudBryansk')
    itembtn3 = telebot.types.KeyboardButton('CloudSPB')
    markup.row(itembtn1)
    markup.row(itembtn2, itembtn3)
    bot.send_message(message.chat.id, "Choose your city:", reply_markup=markup)


@bot.message_handler(content_types=['photo'])
def when_get_photo(message):
    bot.send_message(message.chat.id, 'I hope it is boobs or vegana')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "CloudZelenograd" or message.text == "CloudBryansk":
        global town
        town = message.text[5:]
        write_txt(town)
        weather = owm.weather_at_place(town + ',Russia')
        weather1 = weather.get_weather()
        cloud = weather1.get_detailed_status()
        bot.send_message(message.chat.id, cloud, reply_markup=telebot.types.ReplyKeyboardRemove())
        # markup = types.ReplyKeyboardRemove()
    elif message.text == "TempZelenograd" or message.text == "TempBryansk":
        town = message.text[4:]
        write_txt(town)
        weather = owm.weather_at_place(town + ',Russia')
        weather1 = weather.get_weather()
        temp = weather1.get_temperature('celsius')['temp']
        bot.send_message(message.chat.id, temp, reply_markup=telebot.types.ReplyKeyboardRemove())
        # markup = types.ReplyKeyboardRemove()
    elif message.text == "goroskop":
        try:
            chek_goroskope(message, BASE_URL, headers)
        except:
            write_txt('чтото случилось')
    elif message.text in Zodiacs.keys() and get_current_state(message.chat.id) == Zodiacs['error']:
        set_state(message.chat.id, Zodiacs[message.text])
        bot.send_message(message.chat.id, "Запомнил!")
        send_goroskope(message, BASE_URL, headers)

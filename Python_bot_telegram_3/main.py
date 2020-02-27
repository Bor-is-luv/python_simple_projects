# -*- coding: utf-8 -*-

import telebot
from flask import Flask
from flask import request
from flask_sslify import SSLify
import datetime


token = '660308305:AAG-0FberRD73c55u6obRVr__fj7LTsjWJM'
bot = telebot.TeleBot(token, threaded=False)
app = Flask(__name__)
sslify = SSLify(app)
token = '660308305:AAG-0FberRD73c55u6obRVr__fj7LTsjWJM'
URL = 'https://api.telegram.org/bot' + token + '/'
secret = 'gu454nti45nt45bhi4h'
url = 'https://borislavv.pythonanywhere.com/' + secret
bot.remove_webhook()
bot.set_webhook(url=url)
@app.route('/' + secret, methods = ['POST'])
def webhook():
    update = telebot.types.Update.de_json(request.stream.read().decode('utf-8'))
    bot.process_new_updates([update])
    return 'ok', 200

#/home/Borislavv/venvv/lib/python3.7/site-packages/telebot/types.py

def read_data(chat_id):
    times_today = 0
    times_week = 0
    times_month = 0
    with open("bot/file.txt", "r") as f:
        times = [line.split() for line in f if int(line.split()[0]) == chat_id]
        all = len(times)
        times.reverse()
        now = datetime.datetime.now()
        for time in times:
            if now - datetime.timedelta(days=1) < datetime.datetime.strptime(time[1] +' '+ time[2], "%Y-%m-%d %H:%M:%S.%f"):
                times_today += 1
                times_week += 1
                times_month += 1
            elif now - datetime.timedelta(days=7) < datetime.datetime.strptime(time[1] +' '+ time[2], "%Y-%m-%d %H:%M:%S.%f"):
                times_week += 1
                times_month += 1
            elif now - datetime.timedelta(days=30) < datetime.datetime.strptime(time[1] +' '+ time[2], "%Y-%m-%d %H:%M:%S.%f"):
                times_month += 1

        return all, times_today, times_week, times_month


@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True)
    itembtn1 = telebot.types.KeyboardButton('+1')
    itembtn2 = telebot.types.KeyboardButton('info')
    markup.row(itembtn1, itembtn2)
    bot.send_message(message.chat.id, 'Если дрочила, жми на кнопку "+1", '
                                      'если хочешь узнать статистику, жми на "info"', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def write_data(message):
    if message.text == "+1":
        with open("bot/file.txt", "a") as f:
            f.write(f'{message.chat.id} {datetime.datetime.now()}\n')

        info = read_data(message.chat.id)
        bot.send_message(message.chat.id, f'Всего подрочено: {info[0]}\n'
                                          f'За сегодня: {info[1]}\n'
                                          f'За неделю: {info[2]}\n'
                                          f'За месяц: {info[3]}')
    elif message.text == "info":
        info = read_data(message.chat.id)
        bot.send_message(message.chat.id, f'Всего подрочено: {info[0]}\n'
                                          f'За сегодня: {info[1]}\n'
                                          f'За неделю: {info[2]}\n'
                                          f'За месяц: {info[3]}\n')

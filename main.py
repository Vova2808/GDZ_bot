import telebot
from telebot import types
# import subprocess
# import time
# import openai
import time
import schedule
import telebot
import random

from freeGPT import Client
from googletrans import Translator

from backround import keep_alive

import requests

import datetime
import os
import pytz

#######################################################################################
###############_ПРОВЕРЯЕТ_ЗАПУЩЕН_ЛИ_БОТ_ЧТО_БЫ_НЕ_БЫЛО_КОНФЛИКТОВ_С_API###############
#######################################################################################
# import logging
# import socket
# import sys
#
#
# lock_id = "MYPROCESS"
#
# __lock_socket = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
#
# try:
#     __lock_socket.bind('\0' + lock_id)
#     logging.debug("Acquired lock %r" % (lock_id,))
#
# except socket.error:
#     logging.info("FAILED to acquire lock %r" % (lock_id,))
#     sys.exit()
#######################################################################################
#######################################################################################
#######################################################################################

bot = telebot.TeleBot('5901990283:AAGvaI4GAlOzdLej5JSg_DLRmKi521AY2jE')

print("Bot Запущен")

emoge = ['👌', '👋', '👎', '🖖', '👍', '😃', '🤓', '🧐', '😎', '🙃', '🥳', '🤖', '👾']
random_emoge = random.choice(emoge)


@bot.message_handler(commands=['start'])
def start(message):
  random_emoge = random.choice(emoge)
  # bot.send_message(message.chat.id, '1. russian ', parse_mode='Markdown')
  text = '''<code>/russ</code> и плюс пробел и номер упражнения\n
Пример /russ 123 еслм химия то нужно\n написать номер парагрофа\n
Все эти команды можно скопировать просто нажатиям на них\n
Пиши один пробел между командой и номером упражнения\n
_____________________________________________
1. <code>/russ</code>
2. <code>/algebra</code>
3. <code>/geometria</code>
4. <code>/himia</code>
5. <code>/physic</code>
6. <code>/eanglish</code>
7. /teoria виликая теория по русскому
_____________________________________________

Расписание шкилы - /raspisanie
Погода - /weather
Сколько до лета - /summer
'''

  bot.send_message(message.chat.id, text, parse_mode='html')
  markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
  raspisan = types.KeyboardButton("Расписание")
  raspisan_call = types.KeyboardButton("Расписание звонков")
  teoria = types.KeyboardButton("Теория")
  predmet = types.KeyboardButton("Предметы")
  developer = types.KeyboardButton("Разработчик")
  tester = types.KeyboardButton("Тестеровщики")
  weather_types = types.KeyboardButton("Погода")
  summer = types.KeyboardButton("Сколько до лета")
  chat_gpt = types.KeyboardButton("ChatGPT")
  # markup.add(raspisan, raspisan_call, teoria, predmet, chat_gpt, weather_types, summer, developer, tester)
  markup.add(raspisan, raspisan_call, teoria, predmet, weather_types, summer, developer, tester)
  bot.send_message(message.chat.id, random_emoge, reply_markup=markup)


@bot.message_handler(commands=['help'])
def start(message):
  random_emoge = random.choice(emoge)
  # bot.send_message(message.chat.id, '1. russian ', parse_mode='Markdown')
  text = '''<code>/russ</code> и плюс пробел и номер упражнения\n
Пример /russ 123 еслм химия то нужно\n написать номер парагрофа\n
Все эти команды можно скопировать просто нажатиям на них\n
Пиши один пробел между командой и номером упражнения\n
_____________________________________________
1. <code>/russ</code>
2. <code>/algebra</code>
3. <code>/geometria</code>
4. <code>/himia</code>
5. <code>/physic</code>
6. <code>/eanglish</code>
7. /teoria виликая теория по русскому
_____________________________________________

Расписание шкилы - /raspisanie
Погода - /weather
Сколько до лета - /summer
  '''

  bot.send_message(message.chat.id, text, parse_mode='html')
  markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
  raspisan = types.KeyboardButton("Расписание")
  raspisan_call = types.KeyboardButton("Расписание звонков")
  teoria = types.KeyboardButton("Теория")
  predmet = types.KeyboardButton("Предметы")
  developer = types.KeyboardButton("Разработчик")
  tester = types.KeyboardButton("Тестеровщики")
  weather_types = types.KeyboardButton("Погода")
  summer = types.KeyboardButton("Сколько до лета")
  chat_gpt = types.KeyboardButton("ChatGPT")
  markup.add(raspisan, raspisan_call, teoria, predmet, chat_gpt, weather_types, summer, developer, tester)
  bot.send_message(message.chat.id, random_emoge, reply_markup=markup)


@bot.message_handler(commands=['weather'])
def weathers(message):
    city = "Санкт-Петербург"
    url = 'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347'
    weather_data = requests.get(url).json()
    temperature = round(weather_data['main']['temp'])
    temperature_feels = round(weather_data['main']['feels_like'])
    w_now = 'Сейчас в ' + city + ' ' + str(temperature) + ' °C'
    w_feels = 'Ощущается как ' + str(temperature_feels) + ' °C'
    bot.send_message(message.from_user.id, w_now)
    bot.send_message(message.from_user.id, w_feels)


@bot.message_handler(commands=['summer'])
def summer(message):
    today = datetime.datetime.now()
    summer_start = datetime.datetime(today.year, 6, 1)

    if today.month > 6 or (today.month == 6 and today.day >= 21):
        summer_start = summer_start.replace(year=today.year + 1)

    time_diff = summer_start - today
    days = time_diff.days

    if days < 0:
        bot.send_message(message.chat.id, "УРА ЛЕТО")

    else:
        time_diff = summer_start - today
        days = time_diff.days
        hours, remainder = divmod(time_diff.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        bot.send_message(message.chat.id, "До лета")
        bot.send_message(message.chat.id, f"{days} дней {hours-3} часов {minutes} минут {seconds} секунд")
        time.sleep(0.6)


@bot.message_handler(commands=['russ'])
def kill_process(message):
  try:
    user_msg = '{0}'.format(message.text)

    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

    print("Рсский ",
          user_msg.split(' ')[1],
          "время -- (",
          formatted_time,
          ")",
          f" вот ID - {message.from_user.username} ",
          file=open("log.txt", "a"))

    if int(user_msg.split(' ')[1]) <= 417:
      bot.send_message(message.chat.id, 'Вот cсылка 👇')
      bot.send_message(
          message.chat.id, 'https://reshak.ru/otvet/reshebniki.php?otvet=' +
          user_msg.split(' ')[1] + '&predmet=razumovskaya8')
      bot.send_message(message.chat.id, 'Вот фото 👇')
      bot.send_message(
          message.chat.id,
          'https://reshak.ru/reshebniki/russkijazik/8/razumovskaya/images1/' +
          user_msg.split(' ')[1] + '.png')
      bot.send_message(message.chat.id, '')

    else:
      bot.send_message(message.chat.id, 'Такого упражнения нету')

  except:
    # bot.send_message(message.chat.id,
                     # "Что то не так у тебя один пробел после /russ 123")

      print("Error ")


@bot.message_handler(commands=['eanglish'])
def eanglish(message):
  _teaxt = '''1. Пример:\n
| <code>/eanglish module1 a 1</code> |\n \n первое это модуль второе
это буква модуля третье это номер задания с буквой
если она там есть эту команду тоже можно скопировать'''
  bot.send_message(message.chat.id, _teaxt, parse_mode='html')

  try:
    user_msg = '{0}'.format(message.text)
    print("Английский ",
          user_msg.split(' ')[1],
          user_msg.split(' ')[2],
          user_msg.split(' ')[3])
    i = user_msg.split(' ')[1]

    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

    print("Английски ",
          user_msg.split(' ')[1],
          user_msg.split(' ')[2],
          user_msg.split(' ')[3],
          "время -- (",
          formatted_time,
          ")",
          f" вот ID - {message.from_user.username} ",
          file=open("log.txt", "a"))

    print(i[6])
    if int(i[6]) <= 8:
      bot.send_message(
          message.chat.id, 'Вот cсылка 👇'
      )  #https://reshak.ru/otvet/otvet_txt.php?otvet1=/spotlight8/images/module1/a/1
      bot.send_message(
          message.chat.id,
          'https://reshak.ru/otvet/otvet_txt.php?otvet1=/spotlight8/images/' +
          user_msg.split(' ')[1] + "/" + user_msg.split(' ')[2] + "/" +
          user_msg.split(' ')[3])
      bot.send_message(message.chat.id, '')

    else:
      bot.send_message(message.chat.id, 'Такого модуля нету')

  except:
    # bot.send_message(message.chat.id, "Что то не тае у тебя один пробел после /russ 123")
    print("Error")


@bot.message_handler(commands=['teoria'])
def kill_process(message):
  try:
    bot.send_message(message.chat.id, 'Вот виликая теория 👇')
    bot.send_photo(message.chat.id, 'https://i.imgur.com/6TBByEL.jpeg')
    bot.send_photo(message.chat.id, 'https://i.imgur.com/2GnuFKY.jpeg')
    bot.send_photo(message.chat.id, 'https://add.pics/images/2024/02/25/IMG_20240225_210508.jpeg')

  except:
    # bot.send_message(message.chat.id, "Что то не хочет робить")
    print("Error")


@bot.message_handler(commands=['algebra'])
def kill_process(message):
  try:
    user_msg = '{0}'.format(message.text)

    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

    print("Алгебра ",
          user_msg.split(' ')[1],
          "время -- (",
          formatted_time,
          ")",
          f" вот ID - {message.from_user.username} ",
          file=open("log.txt", "a"))

    if int(user_msg.split(' ')[1]) <= 917:
      bot.send_message(message.chat.id, 'Вот cсылка 👇')
      bot.send_message(
          message.chat.id, 'https://reshak.ru/otvet/reshebniki.php?otvet=' +
          user_msg.split(' ')[1] + '&predmet=kolyagin8')
      bot.send_message(message.chat.id, 'Вот фото 👇')
      bot.send_message(
          message.chat.id,
          'https://reshak.ru/reshebniki/algebra/8/kolyagin/images1/' +
          user_msg.split(' ')[1] + '.png')
      bot.send_message(message.chat.id, '')

    else:
      bot.send_message(message.chat.id, 'Такого номера нету')
  except:
    # bot.send_message(message.chat.id, "Что то не хочет робить у тебя один пробел после /algebra 123")
    print("Error")


@bot.message_handler(commands=['geometria'])
def kill_process(message):
  try:
    user_msg = '{0}'.format(message.text)

    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

    print("Алгебра ",
          user_msg.split(' ')[1],
          "время -- (",
          formatted_time,
          ")",
          f" вот ID - {message.from_user.username} ",
          file=open("log.txt", "a"))

    if int(user_msg.split(' ')[1]) <= 1413:
      bot.send_message(message.chat.id, 'Вот cсылка 👇')
      bot.send_message(
          message.chat.id,
          'https://pomogalka.me/7-klass/geometriya/atanasyan/nomer-' +
          user_msg.split(' ')[1] + '/')
      bot.send_message(message.chat.id, 'Вот фото 👇')
      bot.send_message(
          message.chat.id, 'https://pomogalka.me/img/7-9-klass-atanasyan/' +
          user_msg.split(' ')[1] + '.png')
      bot.send_message(message.chat.id, '')

    else:
      bot.send_message(message.chat.id, 'Такого номера нету')
  except:
    # bot.send_message(message.chat.id,
                     # "Что то не так у тебя один пробел после /geometria 123")
    print("Error")


@bot.message_handler(commands=['himia'])
def kill_process(message):
  try:
    user_msg = '{0}'.format(message.text)
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

    print("Химия ",
          user_msg.split(' ')[1],
          "время -- (",
          formatted_time,
          ")",
          f" вот ID - {message.from_user.username} ",
          file=open("log.txt", "a"))

    if int(user_msg.split(' ')[1]) <= 55:
      bot.send_message(
          message.chat.id, 'Вот cсылка 👇'
      )  #https://reshak.ru/reshebniki/ximiya/8/kuznecova/images1/6.png
      bot.send_message(
          message.chat.id, 'https://reshak.ru/otvet/reshebniki.php?otvet=' +
          user_msg.split(' ')[1] + '&predmet=kuznecova8')
      bot.send_message(message.chat.id, 'Вот фото 👇')
      bot.send_message(
          message.chat.id,
          'https://reshak.ru/reshebniki/ximiya/8/kuznecova/images1/' +
          user_msg.split(' ')[1] + '.png')
      bot.send_message(message.chat.id, '')

    else:
      bot.send_message(message.chat.id, 'Такого парагрофа нету')
  except:
    # bot.send_message(message.chat.id,
                     # "Что то не так у тебя один пробел после /himia 123")
    print("Error")


@bot.message_handler(commands=['physic'])
def physic(message):
  try:
    user_msg = '{0}'.format(message.text)
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

    print("Физика ",
          user_msg.split(' ')[1],
          "время -- (",
          formatted_time,
          ")",
          f" вот ID - {message.from_user.username} ",
          file=open("log.txt", "a"))

    if int(user_msg.split(' ')[1]) <= 55:
      bot.send_message(
          message.chat.id, 'Вот cсылка 👇'
      )  #https://reshak.ru/otvet/reshebniki.php?otvet=paragraph/33&predmet=perishkin_new8
      bot.send_message(
          message.chat.id,
          'https://reshak.ru/otvet/reshebniki.php?otvet=paragraph/' +
          user_msg.split(' ')[1] + '&predmet=perishkin_new8')
      bot.send_message(message.chat.id, 'Вот фото 👇')
      bot.send_message(
          message.chat.id,
          'https://reshak.ru/reshebniki/fizika/8/perishkin_new/images1/paragraph/'
          + user_msg.split(' ')[1] + '.png')
      bot.send_message(message.chat.id, '')

    else:
      bot.send_message(message.chat.id, 'Такого парагрофа нету')
  except:
    # bot.send_message(message.chat.id,
                     # "Что то не так у тебя один пробел после /himia 123")
      print("Error")


@bot.message_handler(commands=['raspisanie'])
def raspisanie(message):
  bot.send_message(message.chat.id, "Расписание 👇")
  bot.send_photo(message.chat.id, "https://i.imgur.com/G5gCOpp.jpeg")
  # current_time = datetime.datetime.now()
  # formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

  # day_of_week = datetime.datetime.today().weekday()
  moscow_timezone = pytz.timezone('Europe/Moscow')
  moscow_time = datetime.datetime.now(moscow_timezone)
  day_of_week = moscow_time.weekday()

  days_of_week = {
      0: "Понедельник",
      1: "Вторник",
      2: "Среда",
      3: "Четверг",
      4: "Пятница",
      5: "Суббота",
      6: "Воскресенье"
  }
  print(days_of_week[day_of_week])
  # bot.send_messge(message.chat.id, "Сегодня", days_of_week[day_of_week])

  if days_of_week[day_of_week] == "Понедельник":
    bot.send_message(message.chat.id, "Грёбанный ПОНЕДЕЛЬНИК")
    raspis = ('''1. <b>Разговор о не важном</b> - 8:00 - 9:15
2. <b>Физ-ра</b> - 9:25 - 10:10
3. <b>География</b> - 10:30 - 11:15
4. <b>Русский</b> - 11:30 - 12:15
5. <b><b><b>Лит-ра</b> - 12:35 - 13:20
6. <b><b>Химия</b> - 13:30 - 14:15
7. <b>Геометрия</b> - 14:20 - 15:05''')
    bot.send_message(message.chat.id, raspis, parse_mode='html')
    bot.send_message(message.chat.id, "😩")

  if days_of_week[day_of_week] == "Вторник":
    bot.send_message(message.chat.id, "Вторник какие 8 уроков")
    raspis = ('''1. <b>Физ-ра</b> - 8:00 - 9:15
2. <b>Инф 1гр. Ин.яз 2гр</b> - 9:25 - 10:10
3. <b>Алгебра</b> - 10:30 - 11:15
4. <b>История</b> - 11:30 - 12:15
5. <b>Русский</b> - 12:35 - 13:20
6. <b>Обществознание</b> - 13:30 - 14:15
7. <b>Биология</b> - 14:20 - 15:05
8. <b>Английский 1гр</b> - 15:10 - 15:55''')
    bot.send_message(message.chat.id, raspis, parse_mode='html')
    bot.send_message(message.chat.id, "🤯")

  if days_of_week[day_of_week] == "Среда":
    bot.send_message(message.chat.id, "Среда сколько можно")
    raspis = ('''1. <b>Физика</b> - 8:30 - 9:15
2. <b>Алгебра</b> - 9:25 - 10:10
3. <b>Инф 2гр. Английский 1гр.</b> - 10:30 - 11:15
4. <b>ОБЖ</b> - 11:30 - 12:15
5. <b>Геометрия</b> - 12:35 - 13:20
6. <b>Лит-ра - 13:30</b> - 14:15
7. <b>Английский 2гр</b> - 14:20 - 15:05''')
    bot.send_message(message.chat.id, raspis, parse_mode='html')
    bot.send_message(message.chat.id, "🤬")

  if days_of_week[day_of_week] == "Четверг":
    bot.send_message(message.chat.id, "Четверг :(")
    raspis = ('''1. <b>Английский</b> - 8:30 - 9:15
2. <b>Русский</b> - 9:25 - 10:10
3. <b>Геометрия</b> - 10:30 - 11:15
4. <b>История</b> - 11:30 - 12:15
5. <b>География</b> <b>- 12:35 - 13:20
6. <b>Химия</b> - 13:30 - 14:15
7. <b>Биология</b> - 14:20 - 15:05''')
    bot.send_message(message.chat.id, raspis, parse_mode='html')
    bot.send_message(message.chat.id, "🫠")

  if days_of_week[day_of_week] == "Пятница":
    bot.send_message(message.chat.id, "Ура Пятница последний день")
    raspis = ('''1. <b>Алгебра</b> - 8:30 - 9:15
2. <b>Физ-ра</b> - 9:25 - 10:10
3. <b>Физика</b> - 10:30 - 11:15
4. <b>ИЗО</b> - 11:30 - 12:15
5. <b>Технология</b> - 12:35 - 13:20
6. <b>Технология</b> - 13:30 - 14:15
7. <b>Английски</b> - 14:20 - 15:05''')
    bot.send_message(message.chat.id, raspis, parse_mode='html')
    bot.send_message(message.chat.id, "🥳")

  if days_of_week[day_of_week] == "Суббота":
    raspis = ("Сегодня Суббота в школу не надо")
    bot.send_message(message.chat.id, raspis)
    bot.send_message(message.chat.id, "😎")

  if days_of_week[day_of_week] == "Воскресенье":
    raspis = ("Сегодня Воскресенье так что в шкилу не надо чиииииил")
    bot.send_message(message.chat.id, raspis)
    bot.send_message(message.chat.id, "😎")

  current_time = datetime.datetime.now()
  formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

  print("Расписание время -- (",
        formatted_time,
        ")",
        f" вот ID - {message.from_user.username} ",
        file=open("log.txt", "a"))


##############################TEXT##############################################


@bot.message_handler(content_types=['text'])
def text(message):
  get_message_bot = message.text.strip().lower()

  if message.text == 'Русский Язык':
    bot.send_message(message.chat.id, "Ёбаный русский")

  if message.text == 'Расписание':
    bot.send_message(message.chat.id, "Расписание 👇")
    bot.send_photo(message.chat.id, "https://i.imgur.com/G5gCOpp.jpeg")
    # current_time = datetime.datetime.now()
    # formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

    # day_of_week = datetime.datetime.today().weekday()
    moscow_timezone = pytz.timezone('Europe/Moscow')
    moscow_time = datetime.datetime.now(moscow_timezone)
    day_of_week = moscow_time.weekday()

    days_of_week = {
        0: "Понедельник",
        1: "Вторник",
        2: "Среда",
        3: "Четверг",
        4: "Пятница",
        5: "Суббота",
        6: "Воскресенье"
    }

    # days_of_week[day_of_week] = "Во скресенье"

    # print(days_of_week[day_of_week])
    # bot.send_messge(message.chat.id, "Сегодня", days_of_week[day_of_week])

    if days_of_week[day_of_week] == "Понедельник":
      bot.send_message(message.chat.id, "Грёбанный ПОНЕДЕЛЬНИК")
      raspis = ('''1. <b>Разговор о НЕ важном</b> - 8:00 - 9:15
2. <b>Физ-ра</b> - 9:25 - 10:10
3. <b>География</b> - 10:30 - 11:15
4. <b>Русский</b> - 11:30 - 12:15
5. <b>Лит-ра</b> - 12:35 - 13:20
6. <b>Химия</b> - 13:30 - 14:15
7. <b>Геометрия</b> - 14:20 - 15:05''')
      bot.send_message(message.chat.id, raspis, parse_mode='html')
      bot.send_message(message.chat.id, "😩")

    if days_of_week[day_of_week] == "Вторник":
      bot.send_message(message.chat.id, "Вторник какие 8 уроков")
      raspis = ('''1. <b>Физ-ра</b> - 8:30 - 9:15
2. <b>Инф 1гр. Ин.яз 2гр</b> - 9:25 - 10:10
3. <b>Алгебра</b> - 10:30 - 11:15
4. <b>История</b> - 11:30 - 12:15
5. <b>Русский</b> - 12:35 - 13:20
6. <b>Обществознание</b> - 13:30 - 14:15
7. <b>Биология</b> - 14:20 - 15:05
8. <b>Английский 1гр</b> - 15:10 - 15:55''')
      bot.send_message(message.chat.id, raspis, parse_mode='html')
      bot.send_message(message.chat.id, "🤯")

    if days_of_week[day_of_week] == "Среда":
      bot.send_message(message.chat.id, "Среда сколько можно")
      raspis = ('''1. <b>Физика</b> - 8:30 - 9:15
2. <b>Алгебра</b> - 9:25 - 10:10
3. <b>Инф 2гр. Английский 1гр.</b> - 10:30 - 11:15
4. <b>ОБЖ</b> - 11:30 - 12:15
5. <b>Геометрия</b> - 12:35 - 13:20
6. <b>Лит-ра</b> - 13:30 - 14:15
7. <b>Английский 2гр</b> - 14:20 - 15:05''')
      bot.send_message(message.chat.id, raspis, parse_mode='html')
      bot.send_message(message.chat.id, "🤬")

    if days_of_week[day_of_week] == "Четверг":
      bot.send_message(message.chat.id, "Четверг :(")
      raspis = ('''1. <b>Английский</b> - 8:30 - 9:15
2. <b>Русский</b> - 9:25 - 10:10
3. <b>Геометрия</b> - 10:30 - 11:15
4. <b>История</b> - 11:30 - 12:15
5. <b>География</b> - 12:35 - 13:20
6. <b>Химия</b> - 13:30 - 14:15
7. <b>Биология</b> - 14:20 - 15:05''')
      bot.send_message(message.chat.id, raspis, parse_mode='html')
      bot.send_message(message.chat.id, "🫠")

    if days_of_week[day_of_week] == "Пятница":
      bot.send_message(message.chat.id, "Ура Пятница последний день")
      raspis = raspis = ('''1. <b>Алгебра</b> - 8:30 - 9:15
2. <b>Физ-ра - 9:25</b> - 10:10
3. <b>Физика - 10:30</b> - 11:15
4. <b>ИЗО - 11:30</b> - 12:15
5. <b>Технология</b> - 12:35 - 13:20
6. <b>Технология</b> - 13:30 - 14:15
7. <b>Английски</b> - 14:20 - 15:05''')
      bot.send_message(message.chat.id, raspis,  parse_mode='html')
      bot.send_message(message.chat.id, "🥳")

    if days_of_week[day_of_week] == "Суббота":
      raspis = ("Сегодня Суббота в школу не надо")
      bot.send_message(message.chat.id, raspis)
      bot.send_message(message.chat.id, "😎")

    if days_of_week[day_of_week] == "Воскресенье":
      raspis = ("Сегодня Воскресенье так что в шкилу не надо чиииииил")
      bot.send_message(message.chat.id, raspis)
      bot.send_message(message.chat.id, "😎")
    ##################################################################################

    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

    print("Расписание время -- (",
          formatted_time,
          ")",
          f" вот ID - {message.from_user.username} ",
          file=open("log.txt", "a"))


  if message.text == 'Лаки':
      bot.send_photo(message.chat.id, "https://i.imgur.com/5OotKDV.jpeg")

  if message.text == 'Тестеровщики':
      testr_spisk = '''1. @collector0133
2. @bobr15243
3. @oohhhhmygooodness'''
      bot.send_message(message.chat.id, "Вот она команда тестировщиков")
      bot.send_message(message.chat.id,testr_spisk)
      bot.send_message(message.chat.id, '😎')


  if message.text == 'Предметы':
    random_emoge = random.choice(emoge)
    text = '''<code>/russ</code> и плюс пробел и номер упражнения\n
Пример /russ 123 еслм химия то нужно\n написать номер парагрофа\n
Все эти команды можно скопировать просто нажатиям на них\n
_____________________________________________
1. <code>/russ</code>
2. <code>/algebra</code>
3. <code>/geometria</code>
4. <code>/himia</code>
5. <code>/physic</code>
6. <code>/eanglish</code>
7. /teoria виликая теория по русскому
_____________________________________________

Расписание шкилы - /raspisanie
Погода - /weather
Сколько до лета - /summer
'''
    bot.send_message(message.chat.id, text, parse_mode='html')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    raspisan = types.KeyboardButton("Расписание")
    raspisan_call = types.KeyboardButton("Расписание звонков")
    teoria = types.KeyboardButton("Теория")
    predmet = types.KeyboardButton("Предметы")
    developer = types.KeyboardButton("Разработчик")
    tester = types.KeyboardButton("Тестеровщики")
    weather_types = types.KeyboardButton("Погода")
    summer = types.KeyboardButton("Сколько до лета")
    # markup.add(raspisan, raspisan_call, teoria, predmet, weather_types, summer, developer, tester)
    markup.add(raspisan, raspisan_call, teoria, predmet, weather_types, summer, developer, tester)
    bot.send_message(message.chat.id, random_emoge, reply_markup=markup)


  if message.text == 'Погода':
      city = "Санкт-Петербург"
      url = 'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347'
      weather_data = requests.get(url).json()
      temperature = round(weather_data['main']['temp'])
      temperature_feels = round(weather_data['main']['feels_like'])
      w_now = 'Сейчас в ' + city + ' ' + str(temperature) + ' °C'
      w_feels = 'Ощущается как ' + str(temperature_feels) + ' °C'
      bot.send_message(message.from_user.id, w_now)
      bot.send_message(message.from_user.id, w_feels)


  if message.text == 'Сколько до лета':
    today = datetime.datetime.now()
    summer_start = datetime.datetime(today.year, 6, 1)

    if today.month > 6 or (today.month == 6 and today.day >= 21):
        summer_start = summer_start.replace(year=today.year + 1)

    time_diff = summer_start - today
    days = time_diff.days

    if days < 0:
        bot.send_message(message.chat.id, "УРА ЛЕТО")

    else:
        time_diff = summer_start - today
        days = time_diff.days
        hours, remainder = divmod(time_diff.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        bot.send_message(message.chat.id, "До лета")
        bot.send_message(message.chat.id, f"{days} дней {hours-3} часов {minutes} минут {seconds} секунд")
        time.sleep(0.6)


  if message.text == 'Теория':
    bot.send_message(message.chat.id, "Виликая теория 👇")
    bot.send_photo(message.chat.id, 'https://i.imgur.com/H4Cvv6U.jpeg')
    bot.send_photo(message.chat.id, 'https://i.imgur.com/zvXrxoj.jpeg')
    bot.send_photo(message.chat.id, 'https://add.pics/images/2024/02/25/IMG_20240225_210508.jpeg')

  if message.text == 'Расписание звонков':
    raspisanie_ = '''1) 8:30 - 9:15
2) 9:25 - 10:10
3) 10:30 - 11:15
4) 11:30 - 12:15
5) 12:35 - 13:20
6) 13:30 - 14:15
7) 14:20 - 15:05
8) 15:10 - 15:55'''
    bot.send_message(message.chat.id, raspisanie_)
    # bot.send_photo(message.chat.id,'')

  if message.text == 'Разработчик':
    text_developer = '''Я @Aboba868 ты можешь помочь\nмне накидав звёздочек на проект git hub пж\n '''
    bot.send_message(message.chat.id, text_developer)
    bot.send_message(message.chat.id, 'Вот накидай сюда звёздочек 👇')
    bot.send_message(message.chat.id, 'https://github.com/Vova2808/GDZ_bot')
    bot.send_message(message.chat.id, '😎')

  iphone_or_android = [
      'Iphone или Android', 'iphone или android', 'айфон или андроид',
      'Айфон или Андроид', 'Айфон или андроид', 'айфон или Андроид'
  ]

  iphone_govno = [
      'Iphone полное говно', 'Iphone вообще говно', 'Iphone шлак',
      'Конечно Android Iphone говно полное'
  ]
  random_phrase = random.choice(iphone_govno)

  if message.text in iphone_or_android:
    bot.send_message(message.chat.id, random_phrase)

  if message.text == 'ChatGPT':
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    raspisan_call = types.KeyboardButton("выход")
    markup.add(raspisan_call)
    bot.send_message(message.chat.id, "Пожалуйсто отправте сообщение:", reply_markup=markup)

    bot.register_next_step_handler(message, handle_user_message)


  # else:
  #     bot.send_message(message.chat.id, 'Чего напиши /help')


def handle_user_message(message):
    try:
        bot.send_chat_action(message.chat.id, 'typing')
        resp = Client.create_completion("gpt3", message.text)
        translator = Translator()
        translation = translator.translate(resp, src='en', dest='ru')

        bot.send_message(message.chat.id, translation.text)
    except Exception as e:
        print("Ошибка")

    if message.text == "выход":
        bot.send_message(message.chat.id, text, parse_mode='html')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        raspisan = types.KeyboardButton("Расписание")
        raspisan_call = types.KeyboardButton("Расписание звонков")
        teoria = types.KeyboardButton("Теория")
        predmet = types.KeyboardButton("Предметы")
        developer = types.KeyboardButton("Разработчик")
        tester = types.KeyboardButton("Тестеровщики")
        weather_types = types.KeyboardButton("Погода")
        summer = types.KeyboardButton("Сколько до лета")
        chat_gpt = types.KeyboardButton("ChatGPT")
        # markup.add(raspisan, raspisan_call, teoria, predmet, chat_gpt, weather_types, summer, developer, tester)
        markup.add(raspisan, raspisan_call, teoria, predmet, weather_types, summer, developer, tester)
        bot.send_message(message.chat.id, "Выход", reply_markup=markup)

    else:
        bot.register_next_step_handler(message, handle_user_message)


keep_alive()

bot.polling(none_stop=True)

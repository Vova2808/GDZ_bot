import telebot
from telebot import types
# import subprocess
# import time
# import openai
import time
import schedule
import telebot
import random

from backround import keep_alive

import datetime
import os
import pytz

bot = telebot.TeleBot('YOUR TOKEN')


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
Расписание шкилы
/raspisanie
'''

  bot.send_message(message.chat.id, text, parse_mode='html')
  markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
  raspisan = types.KeyboardButton("Расписание")
  raspisan_call = types.KeyboardButton("Расписание звонков")
  teoria = types.KeyboardButton("Теория")
  predmet = types.KeyboardButton("Предметы")
  developer = types.KeyboardButton("Разработчик")
  markup.add(raspisan, raspisan_call, teoria, predmet, developer)
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
Расписание шкилы
/raspisanie
  '''

  bot.send_message(message.chat.id, text, parse_mode='html')
  markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
  raspisan = types.KeyboardButton("Расписание")
  raspisan_call = types.KeyboardButton("Расписание звонков")
  teoria = types.KeyboardButton("Теория")
  predmet = types.KeyboardButton("Предметы")
  developer = types.KeyboardButton("Разработчик")
  markup.add(raspisan, raspisan_call, teoria, predmet, developer)
  bot.send_message(message.chat.id, random_emoge, reply_markup=markup)


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
    bot.send_photo(message.chat.id, 'https://i.imgur.com/mQEsPjg.jpeg')

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
    raspis = ('''1. Разговор о важном - 8:00 - 9:15\n
2. Физ-ра - 9:25 - 10:10\n
3. География - 10:30 - 11:15\n
4. Русский - 11:30 - 12:15\n
5. Лит-ра - 12:35 - 13:20\n
6. Химия - 13:30 - 14:15\n
7. Геометрия - 14:20 - 15:05''')
    bot.send_message(message.chat.id, raspis)
    bot.send_message(message.chat.id, "😩")

  if days_of_week[day_of_week] == "Вторник":
    bot.send_message(message.chat.id, "Вторник какие 8 уроков")
    raspis = ('''1. Физ-ра - 8:00 - 9:15\n
2. Инф 1гр. Ин.яз 2гр - 9:25 - 10:10\n
3. Алгебра - 10:30 - 11:15
4. История - 11:30 - 12:15\n
5. Русский - 12:35 - 13:20\n
6. Обществознание - 13:30 - 14:15\n
7. Биология - 14:20 - 15:05\n
8. Английский 1гр - 15:10 - 15:55''')
    bot.send_message(message.chat.id, "🤯")

  if days_of_week[day_of_week] == "Среда":
    bot.send_message(message.chat.id, "Среда сколько можно")
    raspis = ('''1. Физика - 8:00 - 9:15\n
2. Алгебра - 9:25 - 10:10\n
3. Инф 2гр. Английский 1гр. - 10:30 - 11:15\n
4. ОБЖ - 11:30 - 12:15\n
5. Геометрия - 12:35 - 13:20\n
6. Лит-ра - 13:30 - 14:15\n
7. Английский 2гр - 14:20 - 15:05''')
    bot.send_message(message.chat.id, raspis)
    bot.send_message(message.chat.id, "🤬")

  if days_of_week[day_of_week] == "Четверг":
    bot.send_message(message.chat.id, "Четверг :(")
    raspis = ('''1. Английский - 8:00 - 9:15\n
2. Русский - 9:25 - 10:10\n
3. Геометрия - 10:30 - 11:15\n
4. История - 11:30 - 12:15\n
5. География - 12:35 - 13:20\n
6. Химия - 13:30 - 14:15\n
7. Биология - 14:20 - 15:05''')
    bot.send_message(message.chat.id, raspis)
    bot.send_message(message.chat.id, "🫠")

  if days_of_week[day_of_week] == "Пятница":
    bot.send_message(message.chat.id, "Ура Пятница последний день")
    raspis = ('''1. Алгебра - 8:00 - 9:15\n
2. Физ-ра - 9:25 - 10:10\n
3. Физика - 10:30 - 11:15\n
4. ИЗО - 11:30 - 12:15\n
5. Технология - 12:35 - 13:20\n
6. Технология - 13:30 - 14:15\n
7. Английски - 14:20 - 15:05''')
    bot.send_message(message.chat.id, raspis)
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
    # print(days_of_week[day_of_week])
    # bot.send_messge(message.chat.id, "Сегодня", days_of_week[day_of_week])

    if days_of_week[day_of_week] == "Понедельник":
      bot.send_message(message.chat.id, "Грёбанный ПОНЕДЕЛЬНИК")
      raspis = ('''1. Разговор о важном - 8:00 - 9:15\n
2. Физ-ра - 9:25 - 10:10\n
3. География - 10:30 - 11:15\n
4. Русский - 11:30 - 12:15\n
5. Лит-ра - 12:35 - 13:20\n
6. Химия - 13:30 - 14:15\n
7. Геометрия - 14:20 - 15:05''')
      bot.send_message(message.chat.id, raspis)
      bot.send_message(message.chat.id, "😩")

    if days_of_week[day_of_week] == "Вторник":
      bot.send_message(message.chat.id, "Вторник какие 8 уроков")
      raspis = ('''1. Физ-ра - 8:00 - 9:15\n
2. Инф 1гр. Ин.яз 2гр - 9:25 - 10:10\n
3. Алгебра - 10:30 - 11:15
4. История - 11:30 - 12:15\n
5. Русский - 12:35 - 13:20\n
6. Обществознание - 13:30 - 14:15\n
7. Биология - 14:20 - 15:05\n
8. Английский 1гр - 15:10 - 15:55''')
      bot.send_message(message.chat.id, "🤯")

    if days_of_week[day_of_week] == "Среда":
      bot.send_message(message.chat.id, "Среда сколько можно")
      raspis = ('''1. Физика - 8:00 - 9:15\n
2. Алгебра - 9:25 - 10:10\n
3. Инф 2гр. Английский 1гр. - 10:30 - 11:15\n
4. ОБЖ - 11:30 - 12:15\n
5. Геометрия - 12:35 - 13:20\n
6. Лит-ра - 13:30 - 14:15\n
7. Английский 2гр - 14:20 - 15:05''')
      bot.send_message(message.chat.id, raspis)
      bot.send_message(message.chat.id, "🤬")

    if days_of_week[day_of_week] == "Четверг":
      bot.send_message(message.chat.id, "Четверг :(")
      raspis = ('''1. Английский - 8:00 - 9:15\n
2. Русский - 9:25 - 10:10\n
3. Геометрия - 10:30 - 11:15\n
4. История - 11:30 - 12:15\n
5. География - 12:35 - 13:20\n
6. Химия - 13:30 - 14:15\n
7. Биология - 14:20 - 15:05''')
      bot.send_message(message.chat.id, raspis)
      bot.send_message(message.chat.id, "🫠")

    if days_of_week[day_of_week] == "Пятница":
      bot.send_message(message.chat.id, "Ура Пятница последний день")
      raspis = raspis = ('''1. Алгебра - 8:00 - 9:15\n
2. Физ-ра - 9:25 - 10:10\n
3. Физика - 10:30 - 11:15\n
4. ИЗО - 11:30 - 12:15\n
5. Технология - 12:35 - 13:20\n
6. Технология - 13:30 - 14:15\n
7. Английски - 14:20 - 15:05''')
      bot.send_message(message.chat.id, raspis)
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
Расписание шкилы
/raspisanie
'''
    bot.send_message(message.chat.id, text, parse_mode='html')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    raspisan = types.KeyboardButton("Расписание")
    raspisan_call = types.KeyboardButton("Расписание звонков")
    teoria = types.KeyboardButton("Теория")
    predmet = types.KeyboardButton("Предметы")
    developer = types.KeyboardButton("Разработчик")
    markup.add(raspisan, raspisan_call, teoria, predmet, developer)
    bot.send_message(message.chat.id, random_emoge, reply_markup=markup)

  if message.text == 'Теория':
    bot.send_message(message.chat.id, "Виликая теория 👇")
    bot.send_photo(message.chat.id, 'https://i.imgur.com/6TBByEL.jpeg')
    bot.send_photo(message.chat.id, 'https://i.imgur.com/2GnuFKY.jpeg')
    bot.send_photo(message.chat.id, 'https://i.imgur.com/mQEsPjg.jpeg')

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

  # else:
  #     bot.send_message(message.chat.id, 'Чего напиши /help')


keep_alive()

bot.polling(none_stop=True)

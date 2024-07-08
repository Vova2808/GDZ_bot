import telebot
from telebot import types
# import subprocess
# import time
# import openai
import time
import schedule
import telebot
import random

import hashlib
import json

from backround import keep_alive
import requests

import datetime
from datetime import datetime
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
#     logging.info("FAILED####################################################################################### to acquire lock %r" % (lock_id,))
#     sys.exit()
#######################################################################################
#######################################################################################

bot = telebot.TeleBot('Token')

print("Bot Запущен")

emoge = ['👌', '👋', '👎', '🖖', '👍', '😃', '🤓', '🧐', '😎', '🙃', '🥳', '🤖', '👾']
random_emoge = random.choice(emoge)


if not os.path.exists('media'):
    os.makedirs('media')

users = set()  # define the users set
reactions = {}  # dictionary to store reactions
messages = {}  # dictionary to store messages IDs for each media
user_choice = {}  # dictionary to store user choices

STATE_FILE = 'state.json'


def save_state():
    state = {
        'users': list(users),
        'reactions': {k: {rk: list(rv) for rk, rv in v.items()} for k, v in reactions.items()},
        'messages': messages
    }
    with open(STATE_FILE, 'w') as f:
        json.dump(state, f)


def load_state():
    if os.path.exists(STATE_FILE) and os.path.getsize(STATE_FILE) > 0:
        with open(STATE_FILE, 'r') as f:
            state = json.load(f)
            global users, reactions, messages
            users = set(state['users'])
            reactions = {k: {rk: set(rv) for rk, rv in v.items()} for k, v in state['reactions'].items()}
            messages = state['messages']


# Load state on startup
load_state()



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
  mems = types.KeyboardButton("Mems")
  developer = types.KeyboardButton("Разработчик")
  tester = types.KeyboardButton("Тестеровщики")
  weather_types = types.KeyboardButton("Погода")
  summer = types.KeyboardButton("Сколько до лета")
  markup.add(raspisan, raspisan_call, teoria, predmet, mems, weather_types, summer, developer, tester)
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
  mems = types.KeyboardButton("Mems")
  developer = types.KeyboardButton("Разработчик")
  tester = types.KeyboardButton("Тестеровщики")
  weather_types = types.KeyboardButton("Погода")
  summer = types.KeyboardButton("Сколько до лета")
  markup.add(raspisan, raspisan_call, teoria, predmet, mems, weather_types, summer, developer, tester)
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
          user_msg.split(' ')[1] + '&predmet=razumovskaya9')
      bot.send_message(message.chat.id, 'Вот фото 👇')
      bot.send_message(
          message.chat.id,
          'https://reshak.ru/reshebniki/russkijazik/9/razumovskaya/images/' +
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
          'https://reshak.ru/otvet/otvet_txt.php?otvet1=/spotlight9/images/' +
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
          user_msg.split(' ')[1] + '&predmet=kolyagin9')
      bot.send_message(message.chat.id, 'Вот фото 👇')
      bot.send_message(
          message.chat.id,
          'https://reshak.ru/reshebniki/algebra/9/kolyagin/images1/' +
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
  _teaxt = '''1. Пример:\n
  | <code>/himia 1 2</code> |\n \n первое это параграф второе
  это номер вопроса эту команду тоже можно скопировать'''
  bot.send_message(message.chat.id, _teaxt, parse_mode='html')
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
      )  #https://reshak.ru/otvet/reshebniki.php?otvet=1/2&predmet=kuznecova9
      bot.send_message(
          message.chat.id, 'https://reshak.ru/otvet/reshebniki.php?otvet=' +
          user_msg.split(' ')[1] + "/" + user_msg.split(' ')[2] +'&predmet=kuznecova9')
      bot.send_message(message.chat.id, 'Вот фото 👇')
      bot.send_message(
          message.chat.id,
          'https://reshak.ru/reshebniki/ximiya/9/kuznecova/images1/' +
          user_msg.split(' ')[1] + "/" + user_msg.split(' ')[2] + '.png')
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


@bot.message_handler(content_types=['photo', 'video'])
def handle_media(message):
    try:
        if message.photo:
            file_id = message.photo[-1].file_id
            file_ext = 'jpg'
        elif message.video:
            file_id = message.video.file_id
            file_ext = 'mp4'
        else:
            return

        bot.delete_message(message.chat.id, message.message_id)
        file_info = bot.get_file(file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        # Save the file to a specific path
        file_path = f'media/{file_id}.{file_ext}'
        with open(file_path, 'wb') as f:
            f.write(downloaded_file)

        user_username = message.from_user.username
        user_id = message.from_user.id

        if user_choice.get(message.chat.id) == "Отправить анонимно":
            caption = "Отправил - Анонимус 🥸\n"
        else:
            caption = f"Отправил - @{user_username}\n" if user_username else f"[ID: {user_id}] 'Смотрите какой мем'\n"

        if message.caption:
            caption += f"Подпись: {message.caption}"

        # Generate a short unique ID for the file
        short_file_id = hashlib.md5(file_id.encode()).hexdigest()[:8]

        # Initialize reactions and messages for this specific short_file_id
        reactions[short_file_id] = {
            'like': set(),
            'dislike': set(),
            'kloun': set(),
            'haha': set(),
            'fack': set()
        }
        messages[short_file_id] = []

        # Create reaction buttons with correct short_file_id
        reaction_markup = types.InlineKeyboardMarkup()
        reaction_markup.add(
            types.InlineKeyboardButton(
                f'👍 {len(reactions[short_file_id]["like"])}',
                callback_data=f'like_{short_file_id}'),
            types.InlineKeyboardButton(
                f'👎 {len(reactions[short_file_id]["dislike"])}',
                callback_data=f'dislike_{short_file_id}'),
            types.InlineKeyboardButton(
                f'🤡 {len(reactions[short_file_id]["kloun"])}',
                callback_data=f'kloun_{short_file_id}'),
            types.InlineKeyboardButton(
                f'😂 {len(reactions[short_file_id]["haha"])}',
                callback_data=f'haha_{short_file_id}'),
            types.InlineKeyboardButton(
                f'🖕 {len(reactions[short_file_id]["fack"])}',
                callback_data=f'fack_{short_file_id}'))

        # Send the media to each user and store message IDs
        for user_id in users:
            try:
                with open(file_path, 'rb') as f:
                    if message.photo:
                        sent_message = bot.send_photo(
                            user_id,
                            f,
                            caption=caption,
                            reply_markup=reaction_markup)
                    elif message.video:
                        sent_message = bot.send_video(
                            user_id,
                            f,
                            caption=caption,
                            reply_markup=reaction_markup)
                    messages[short_file_id].append(sent_message.message_id)
            except Exception as e:
                print(f"Could not send message to user {user_id}: {e}")

        # Remove the file after sending
        os.remove(file_path)

        # Save state after handling media
        save_state()

    except Exception as e:
        bot.send_message(message.chat.id, f"Произошла ошибка: {str(e)}")


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    try:
        action, short_file_id = call.data.split('_')
        user_id = call.from_user.id

        # Проверяем наличие short_file_id в reactions
        if short_file_id not in reactions:
            raise ValueError(
                f"Short file ID '{short_file_id}' not found in reactions.")

        # Обновляем реакции в зависимости от действия (like, dislike, kloun, haha, fack)
        if action == 'like':
            if user_id in reactions[short_file_id]['like']:
                reactions[short_file_id]['like'].remove(user_id)
            else:
                reactions[short_file_id]['like'].add(user_id)
                reactions[short_file_id]['dislike'].discard(user_id)
                reactions[short_file_id]['kloun'].discard(user_id)
                reactions[short_file_id]['haha'].discard(user_id)
                reactions[short_file_id]['fack'].discard(user_id)
        elif action == 'dislike':
            if user_id in reactions[short_file_id]['dislike']:
                reactions[short_file_id]['dislike'].remove(user_id)
            else:
                reactions[short_file_id]['dislike'].add(user_id)
                reactions[short_file_id]['like'].discard(user_id)
                reactions[short_file_id]['kloun'].discard(user_id)
                reactions[short_file_id]['haha'].discard(user_id)
                reactions[short_file_id]['fack'].discard(user_id)
        elif action == 'kloun':
            if user_id in reactions[short_file_id]['kloun']:
                reactions[short_file_id]['kloun'].remove(user_id)
            else:
                reactions[short_file_id]['kloun'].add(user_id)
                reactions[short_file_id]['like'].discard(user_id)
                reactions[short_file_id]['dislike'].discard(user_id)
                reactions[short_file_id]['haha'].discard(user_id)
                reactions[short_file_id]['fack'].discard(user_id)
        elif action == 'haha':
            if user_id in reactions[short_file_id]['haha']:
                reactions[short_file_id]['haha'].remove(user_id)
            else:
                reactions[short_file_id]['haha'].add(user_id)
                reactions[short_file_id]['like'].discard(user_id)
                reactions[short_file_id]['dislike'].discard(user_id)
                reactions[short_file_id]['kloun'].discard(user_id)
                reactions[short_file_id]['fack'].discard(user_id)
        elif action == 'fack':
            if user_id in reactions[short_file_id]['fack']:
                reactions[short_file_id]['fack'].remove(user_id)
            else:
                reactions[short_file_id]['fack'].add(user_id)
                reactions[short_file_id]['like'].discard(user_id)
                reactions[short_file_id]['dislike'].discard(user_id)
                reactions[short_file_id]['kloun'].discard(user_id)
                reactions[short_file_id]['haha'].discard(user_id)

        # Обновляем клавиатуру с новыми значениями реакций
        like_count = len(reactions[short_file_id]['like'])
        dislike_count = len(reactions[short_file_id]['dislike'])
        kloun_count = len(reactions[short_file_id]['kloun'])
        haha_count = len(reactions[short_file_id]['haha'])
        fack_count = len(reactions[short_file_id]['fack'])

        new_markup = types.InlineKeyboardMarkup()
        new_markup.add(
            types.InlineKeyboardButton(f'👍 {like_count}',
                                       callback_data=f'like_{short_file_id}'),
            types.InlineKeyboardButton(
                f'👎 {dislike_count}',
                callback_data=f'dislike_{short_file_id}'),
            types.InlineKeyboardButton(f'🤡 {kloun_count}',
                                       callback_data=f'kloun_{short_file_id}'),
            types.InlineKeyboardButton(f'😂 {haha_count}',
                                       callback_data=f'haha_{short_file_id}'),
            types.InlineKeyboardButton(f'🖕 {fack_count}',
                                       callback_data=f'fack_{short_file_id}'))

        # Обновляем сообщения для каждого пользователя
        for user_id in users:
            for message_id in messages[short_file_id]:
                try:
                    bot.edit_message_reply_markup(chat_id=user_id,
                                                  message_id=message_id,
                                                  reply_markup=new_markup)
                except Exception as e:
                    print(f"Could not update message for user {user_id}: {e}")

        bot.answer_callback_query(call.id, f"Вы выбрали: {action}")

        # Save state after updating reactions
        save_state()

    except Exception as e:
        bot.send_message(call.message.chat.id, f"Произошла ошибка: {str(e)}")



@bot.message_handler(commands=['raspisanie'])
def raspisanie(message):
    bot.send_message(message.chat.id, "Расписание 👇")
    bot.send_photo(message.chat.id, "https://i.postimg.cc/VLzCLgPr/IMG-20240410-215628.jpg")
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
        raspis = ('''1. <b>Разговор о НЕ важном</b> - 8:00 - 9:15
2. <b>Физ-ра</b> - 9:35 - 10:20
3. <b>География</b> - 10:40 - 11:25
4. <b>Русский</b> - 11:40 - 12:25
5. <b>Лит-ра</b> - 12:45 - 13:30
6. <b>Химия</b> - 13:40 - 14:25
7. <b>Геометрия</b> - 14:30 - 15:15''')
        bot.send_message(message.chat.id, raspis, parse_mode='html')
        bot.send_message(message.chat.id, "😩")

    if days_of_week[day_of_week] == "Вторник":
      bot.send_message(message.chat.id, "Вторник какие 8 уроков")
      raspis = ('''1. <b>Физ-ра</b> - 8:30 - 9:15
2. <b>Русский</b> - 9:35 - 10:20
3. <b>Алгебра</b> - 10:40 - 11:25
4. <b>История</b> - 11:40 - 12:25
5. <b>Лит-ра</b> - 12:45 - 13:30
6. <b>Обществознание</b> - 13:40 - 14:25
7. <b>Биология</b> - 14:30 - 15:15
8. <b>Английский 1гр</b> - 15:20 - 16:05''')
      bot.send_message(message.chat.id, raspis, parse_mode='html')
      bot.send_message(message.chat.id, "🤯")

    if days_of_week[day_of_week] == "Среда":
      bot.send_message(message.chat.id, "Среда сколько можно")
      raspis = ('''1. <b>Физика</b> - 8:30 - 9:15
2. <b>Алгебра</b> - 9:35 - 10:20
3. <b>Инф 2гр. Английский 1гр.</b> - 10:40 - 11:25
4. <b>ОБЖ</b> - 11:40 - 12:25
5. <b>Геометрия</b> - 12:45 - 13:30
6. <b>Русский</b> - 13:40 - 14:25
7. <b>Английский 2гр</b> - 14:30 - 16:05''')
      bot.send_message(message.chat.id, raspis, parse_mode='html')
      bot.send_message(message.chat.id, "🤬")

    if days_of_week[day_of_week] == "Четверг":
      bot.send_message(message.chat.id, "Четверг :(")
      raspis = ('''1. <b>Английский 1гр.</b> - 8:30 - 9:15
2. <b>Русский, Английский 2гр.</b> - 9:35 - 10:20
3. <b>Геометрия</b> - 10:40 - 11:25
4. <b>История</b> - 11:40 - 12:25
5. <b>География</b> - 12:45 - 13:30
6. <b>Химия</b> - 13:40 - 14:25
7. <b>Биология</b> - 14:30 - 16:05''')
      bot.send_message(message.chat.id, raspis, parse_mode='html')
      bot.send_message(message.chat.id, "🫠")

    if days_of_week[day_of_week] == "Пятница":
      bot.send_message(message.chat.id, "Ура Пятница последний день")
      raspis = raspis = ('''1. <b>Алгебра</b> - 8:30 - 9:15
2. <b>Физ-ра - 9:35</b> - 10:20
3. <b>Физика - 10:40</b> - 11:35
4. <b>ИЗО - 11:40</b> - 12:25
5. <b>Технология</b> - 12:45 - 13:30
6. <b>Технология</b> - 13:40 - 14:25
7. <b>Английски 2гр.</b> - 14:30 - 16:05''')
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
        bot.send_photo(message.chat.id, "https://i.postimg.cc/VLzCLgPr/IMG-20240410-215628.jpg")
        # current_time = datetime.datetime.now()
        # formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

        # day_of_week = datetime.datetime.today().weekday()
        moscow_timezone = pytz.timezone('Europe/Moscow')
        moscow_time = datetime.now(moscow_timezone)
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
    2. <b>Физ-ра</b> - 9:35 - 10:20
    3. <b>География</b> - 10:40 - 11:25
    4. <b>Русский</b> - 11:40 - 12:25
    5. <b>Лит-ра</b> - 12:45 - 13:30
    6. <b>Химия</b> - 13:40 - 14:25
    7. <b>Геометрия</b> - 14:30 - 15:15''')
            bot.send_message(message.chat.id, raspis, parse_mode='html')
            bot.send_message(message.chat.id, "😩")

        if days_of_week[day_of_week] == "Вторник":
            bot.send_message(message.chat.id, "Вторник какие 8 уроков")
            raspis = ('''1. <b>Физ-ра</b> - 8:30 - 9:15
    2. <b>Русский</b> - 9:35 - 10:20
    3. <b>Алгебра</b> - 10:40 - 11:25
    4. <b>История</b> - 11:40 - 12:25
    5. <b>Лит-ра</b> - 12:45 - 13:30
    6. <b>Обществознание</b> - 13:40 - 14:25
    7. <b>Биология</b> - 14:30 - 15:15
    8. <b>Английский 1гр</b> - 15:20 - 16:05''')
            bot.send_message(message.chat.id, raspis, parse_mode='html')
            bot.send_message(message.chat.id, "🤯")

        if days_of_week[day_of_week] == "Среда":
            bot.send_message(message.chat.id, "Среда сколько можно")
            raspis = ('''1. <b>Физика</b> - 8:30 - 9:15
    2. <b>Алгебра</b> - 9:35 - 10:20
    3. <b>Инф 2гр. Английский 1гр.</b> - 10:40 - 11:25
    4. <b>ОБЖ</b> - 11:40 - 12:25
    5. <b>Геометрия</b> - 12:45 - 13:30
    6. <b>Русский</b> - 13:40 - 14:25
    7. <b>Английский 2гр</b> - 14:30 - 16:05''')
            bot.send_message(message.chat.id, raspis, parse_mode='html')
            bot.send_message(message.chat.id, "🤬")

        if days_of_week[day_of_week] == "Четверг":
            bot.send_message(message.chat.id, "Четверг :(")
            raspis = ('''1. <b>Английский 1гр.</b> - 8:30 - 9:15
    2. <b>Русский, Английский 2гр.</b> - 9:35 - 10:20
    3. <b>Геометрия</b> - 10:40 - 11:25
    4. <b>История</b> - 11:40 - 12:25
    5. <b>География</b> - 12:45 - 13:30
    6. <b>Химия</b> - 13:40 - 14:25
    7. <b>Биология</b> - 14:30 - 16:05''')
            bot.send_message(message.chat.id, raspis, parse_mode='html')
            bot.send_message(message.chat.id, "🫠")

        if days_of_week[day_of_week] == "Пятница":
            bot.send_message(message.chat.id, "Ура Пятница последний день")
            raspis = raspis = ('''1. <b>Алгебра</b> - 8:30 - 9:15
    2. <b>Физ-ра - 9:35</b> - 10:20
    3. <b>Физика - 10:40</b> - 11:35
    4. <b>ИЗО - 11:40</b> - 12:25
    5. <b>Технология</b> - 12:45 - 13:30
    6. <b>Технология</b> - 13:40 - 14:25
    7. <b>Английски 2гр.</b> - 14:30 - 16:05''')
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
        ##################################################################################

        current_time = datetime.now()
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

        print(f"Расписание время Вот ID - {message.from_user.username} ",
              f"время -- ({formatted_time})\n",
              file=open("log_mem.txt", "a"))



    if message.text == 'Лаки':
        bot.send_photo(message.chat.id, "https://i.imgur.com/5OotKDV.jpeg")


    get_message_bot = message.text.strip().lower()

    if message.text == "Mems":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        send_mem = types.KeyboardButton("Отправить мем")
        send_anonymous = types.KeyboardButton("Отправить анонимно")
        markup.add(send_mem, send_anonymous)
        bot.send_message(message.chat.id,
                         'Выберите, как вы хотите отправить мем:',
                         reply_markup=markup)



    elif message.text in ["Отправить мем", "Отправить анонимно"]:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        raspisan = types.KeyboardButton("Расписание")
        raspisan_call = types.KeyboardButton("Расписание звонков")
        teoria = types.KeyboardButton("Теория")
        predmet = types.KeyboardButton("Предметы")
        mems = types.KeyboardButton("Mems")
        developer = types.KeyboardButton("Разработчик")
        tester = types.KeyboardButton("Тестеровщики")
        weather_types = types.KeyboardButton("Погода")
        summer = types.KeyboardButton("Сколько до лета")
        markup.add(raspisan, raspisan_call, teoria, predmet, mems, weather_types, summer, developer, tester)

        user_choice[message.chat.id] = message.text
        bot.send_message(message.chat.id, 'Отправьте фото или видео', reply_markup=markup)

        current_time = datetime.now()
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
        print(f"вот ID - {message.from_user.username} ",
              f"время -- ({formatted_time})\n",
              file=open("log_mem.txt", "a"))

        if message.chat.id not in users:
            users.add(message.chat.id)
        save_state()

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
        mems = types.KeyboardButton("Mems")
        developer = types.KeyboardButton("Разработчик")
        tester = types.KeyboardButton("Тестеровщики")
        weather_types = types.KeyboardButton("Погода")
        summer = types.KeyboardButton("Сколько до лета")
        markup.add(raspisan, raspisan_call, teoria, predmet, mems, weather_types, summer, developer, tester)
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
        url = "https://www.calc.ru/dney-do-leta.html"
        response = requests.get(url)
        response.encoding = response.apparent_encoding  # Правильная обработка кодировки
        soup = BeautifulSoup(response.text, 'html.parser')
        countdown_div = soup.find('div', id='count')

        if countdown_div:
            countdown_text = countdown_div.get_text(strip=True)
            bot.send_message(message.chat.id,f"До лета 2025 года осталось\n <b>{countdown_text}</b>", parse_mode='html')

        else:
            bot.send_message(message.chat.id,"Не удалось найти элемент с нужными данными.")

    if message.text == 'Теория':
        bot.send_message(message.chat.id, "Виликая теория 👇")
        bot.send_photo(message.chat.id, 'https://i.imgur.com/H4Cvv6U.jpeg')
        bot.send_photo(message.chat.id, 'https://i.imgur.com/zvXrxoj.jpeg')
        bot.send_photo(message.chat.id, 'https://add.pics/images/2024/02/25/IMG_20240225_210508.jpeg')

    if message.text == 'Расписание звонков':
        raspisanie_ = '''1) 8:30 - 9:15
2) 9:35 - 10:20
3) 10:40 - 11:25
4) 11:40 - 12:25
5) 12:45 - 13:30
6) 13:40 - 14:25
7) 14:30 - 15:15
8) 15:20 - 16:05'''
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


  # else:
  #     bot.send_message(message.chat.id, 'Чего напиши /help')



keep_alive()

bot.infinity_polling()

bot.polling(none_stop=True)

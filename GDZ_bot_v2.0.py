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
from datetime import datetime, timedelta
import os
import pytz





bot = telebot.TeleBot('7669086286:AAGTBW0iEW_w76o9jtUnk-U9OpNEiETAB0M')

# Путь к файлу с балансами
BALANCE_FILE = 'user_balances.json'
initial_balance = 100


bot_data = {}
user_status = {}
user_data = {}
message_data = {}


reactions = {}
messages = {}
users = set()
user_choice = {}

# Инициализация бота

def set_bot_commands():
    commands = [
        telebot.types.BotCommand(command="/start", description="Запустить бота"),
        telebot.types.BotCommand(command="/help", description="Получить помощь")
    ]
    bot.set_my_commands(commands)


set_bot_commands()


# Загружаем баланс пользователей из файла
def load_balances():
    if os.path.exists(BALANCE_FILE):
        with open(BALANCE_FILE, 'r') as f:
            return json.load(f)
    else:
        return {}


# Сохраняем баланс пользователей в файл
def save_balances():
    with open(BALANCE_FILE, 'w') as f:
        json.dump(user_balances, f)


# Загружаем данные балансов
print(f"Загружаем данные из {BALANCE_FILE}...")
user_balances = load_balances()


@bot.message_handler(commands=['start', 'help'])
def start(message):
    user_id = str(message.from_user.id)

    # Инициализация баланса, если пользователя ещё нет
    if user_id not in user_balances:
        user_balances[user_id] = initial_balance
        print(f"Новый пользователь: {user_id}. Установлен начальный баланс: {initial_balance} 🍆")
        save_balances()  # Сохраняем данные сразу при создании нового пользователя

    # Создание клавиатуры
    markup_start = types.InlineKeyboardMarkup(row_width=1)
    predmet = types.InlineKeyboardButton("📚 Предметы", callback_data='predmet')
    raspisan = types.InlineKeyboardButton('🗓 Расписание (На сегодня)', callback_data='raspisan')
    raspisan_all = types.InlineKeyboardButton('🗓 Расписание (На всю неделю)', callback_data='raspisan_all')
    # dz = types.InlineKeyboardButton("🏫 Д/З", callback_data='dz')
    raspisan_call = types.InlineKeyboardButton('⏰ Расписание звонков', callback_data='raspisan_call')
    # teoria = types.InlineKeyboardButton('📝 Теория', callback_data='teoria')
    top = types.InlineKeyboardButton('🔝 Топ по баклажанам', callback_data='top')
    baklagan = types.InlineKeyboardButton('🍆 Баклажан', callback_data='baklagan')
    # mems = types.InlineKeyboardButton('😂 Мемы (Пиздец смешно)', callback_data='mems')

    # Добавление кнопок на клавиатуру
    markup_start.add(predmet, raspisan, raspisan_all, raspisan_call, top, baklagan)

    # Открываем файл фотографии перед отправкой

    text_start = f'''🏛 Главное меню ⌵\n
<b>╭ Username:</b> <code>{message.from_user.username}</code>
<b>├ User ID:</b> <code>{message.from_user.id}</code>
<b>╰ Balance:</b> <code>{user_balances[user_id]} 🍆</code>\n
'''
    photo_start = open('start.jpg', 'rb')
    msg_start = bot.send_photo(message.chat.id, photo_start, caption=text_start, parse_mode='HTML', reply_markup=markup_start)

    bot_data[message.chat.id] = {
        'message_id': msg_start.message_id,
        'photo': photo_start
    }

# Обработчик для любых нажатий на кнопки
user_click_data = {}


@bot.callback_query_handler(func=lambda call: call.data == 'mems')
def mems_menu(call):
    # Проверяем, содержит ли сообщение текст
    if call.message.text:
        # Если текст есть, редактируем его
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        send_mem = types.KeyboardButton("Отправить мем")
        send_anonymous = types.KeyboardButton("Отправить анонимно")
        markup.add(send_mem, send_anonymous)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Отправьте фото или видео с подписью, если хотите",
                              reply_markup=markup)
    else:
        # Если текста нет, отправляем новое сообщение с клавиатурой
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        send_mem = types.KeyboardButton("Отправить мем")
        send_anonymous = types.KeyboardButton("Отправить анонимно")
        markup.add(send_mem, send_anonymous)
        bot.send_message(call.message.chat.id,
                         "Отправьте фото или видео с подписью, если хотите",
                         reply_markup=markup)


# Обработчик нажатий на кнопки
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    user_id = str(call.from_user.id)
    current_time = datetime.now()

    # Проверяем, есть ли информация о пользователе
    if user_id not in user_click_data:
        user_click_data[user_id] = {'last_click': current_time - timedelta(seconds=1)}

    # Ограничение по времени (например, не чаще, чем каждые 1 секунды)
    if (current_time - user_click_data[user_id]['last_click']).total_seconds() < 1:
        bot.answer_callback_query(call.id, "Подождите 1 секунды перед следующим начислением.")
        return

    if call.message.caption:
        # Случайное начисление от 5 до 15 баклажанов
        earned_baklagans = random.randint(5, 15)
        user_balances[user_id] += earned_baklagans
        user_click_data[user_id]['last_click'] = current_time

        print(f"Пользователь {user_id} получил {earned_baklagans} баклажанов. Новый баланс: {user_balances[user_id]} 🍆")

        # Сохраняем баланс
        save_balances()

        # Отправляем сообщение пользователю о начислении
        bot.answer_callback_query(call.id, f"Вам начислено {earned_baklagans} 🍆 баклажанов!")

        # Обновляем сообщение с новым балансом
        text_start = f'''🏛 Главное меню ⌵\n
<b>╭ Username:</b> <code>{call.from_user.username}</code>
<b>├ User ID:</b> <code>{call.from_user.id}</code>
<b>╰ Balance:</b> <code>{user_balances[user_id]} 🍆</code>\n
'''
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                 caption=text_start, parse_mode='HTML', reply_markup=call.message.reply_markup)

    else:
        # Логика для случая, когда подписи нет
        print("Подписи в сообщении нет, невозможно редактировать")

    # Обработка нажатий на другие кнопки
    if call.data == 'back_to_menu':
        bot.answer_callback_query(call.id, "🏛 Главное меню")
        text_start = f'''🏛 Главное меню ⌵\n
<b>╭ Username:</b> <code>{call.message.from_user.username}</code>
<b>├ User ID:</b> <code>{call.message.from_user.id}</code>
<b>╰ Balance:</b> <code>{user_balances[user_id]} 🍆</code>\n
'''

        markup_menu = types.InlineKeyboardMarkup(row_width=1)
        predmet = types.InlineKeyboardButton("📚 Предметы", callback_data='predmet')
        raspisan = types.InlineKeyboardButton('🗓 Расписание (На сегодня)', callback_data='raspisan')
        raspisan_all = types.InlineKeyboardButton('🗓 Расписание (На всю неделю)', callback_data='raspisan_all')
        # dz = types.InlineKeyboardButton("🏫 Д/З", callback_data='dz')
        raspisan_call = types.InlineKeyboardButton('⏰ Расписание звонков', callback_data='raspisan_call')
        # teoria = types.InlineKeyboardButton('📝 Теория', callback_data='teoria')
        top = types.InlineKeyboardButton('🔝 Топ по баклажанам', callback_data='top')
        baklagan = types.InlineKeyboardButton('🍆 Баклажан', callback_data='baklagan')
        # mems = types.InlineKeyboardButton('😂 Мемы (Пиздец смешно)', callback_data='mems')

        # Добавление кнопок на клавиатуру
        markup_menu.add(predmet, raspisan, raspisan_all, raspisan_call, top, baklagan)

        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                 caption=text_start, parse_mode='HTML', reply_markup=markup_menu)


    if call.data == 'predmet':
        bot.answer_callback_query(call.id, "📚 Предметы")
        markup_predmet = types.InlineKeyboardMarkup()
        algebra = types.InlineKeyboardButton("➕➖Алгебра✖️➗", callback_data='algebra')
        geometria = types.InlineKeyboardButton("📐Геометрия", callback_data='geometria')
        russ = types.InlineKeyboardButton("🇷🇺 Русский", callback_data='russ')
        english = types.InlineKeyboardButton("🇺🇸 Английский", callback_data='english')
        phisic = types.InlineKeyboardButton("⚛️Физика🍎", callback_data='phisic')
        # himia = types.InlineKeyboardButton("👩‍🔬Химия", callback_data='himia')
        back = types.InlineKeyboardButton("🔙 Назад", callback_data='back_to_menu')

        markup_predmet.add(algebra, geometria)
        markup_predmet.add(russ, english)
        markup_predmet.add(phisic)
        markup_predmet.add(back)


        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                 caption="Выберите предмет:", reply_markup=markup_predmet)

    if call.data == 'raspisan':
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
        # print(days_of_week[day_of_week])

        if days_of_week[day_of_week] == "Понедельник":
            raspis = ('''Понедельник:
            
1. <b>Разговор о важном</b> - 8:30 - 9:15
2. <b>👩‍🔬Химия</b> - 9:35 - 10:20
3. <b>📐Геометрия</b> - 10:40 - 11:25
4. <b>📜 История</b> - 11:40 - 12:25
5. <b>🇺🇸 Английский</b> - 12:45 - 13:30
6. <b>Физик</b> - 13:40 - 14:25
7. <b>📖 Лит-ра</b> - 14:30 - 15:15

Вторник:
            
1. <b>⚽️Физ-ра</b> - 8:30 - 9:15
2. <b>📖 Лит-ра</b> - 9:35 - 10:20
3. <b>🗺 География</b> - 10:40 - 11:25
4. <b>🧍 Обществознание</b> - 11:40 - 12:25
5. <b>➕➖Алгебра✖️➗</b> - 12:45 - 13:30
6. <b>🇷🇺 Русский</b> - 13:40 - 14:25
7. <b>⚛️Физика🍎</b> - 14:30 - 15:15''')
            bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                     caption=raspis, parse_mode='HTML', reply_markup=call.message.reply_markup)


        if days_of_week[day_of_week] == "Вторник":
            raspis = ('''Вторник:
            
1. <b>⚽️Физ-ра</b> - 8:30 - 9:15
2. <b>📖 Лит-ра</b> - 9:35 - 10:20
3. <b>🗺 География</b> - 10:40 - 11:25
4. <b>🧍 Обществознание</b> - 11:40 - 12:25
5. <b>➕➖Алгебра✖️➗</b> - 12:45 - 13:30
6. <b>🇷🇺 Русский</b> - 13:40 - 14:25
7. <b>⚛️Физика🍎</b> - 14:30 - 15:15

Среда:
            
1. <b>➕➖Алгебра✖️➗</b> - 8:30 - 9:15
2. <b>📐Геометрия</b> - 9:35 - 10:20
3. <b>🇺🇸 Английский</b> - 10:40 - 11:25
4. <b>🇷🇺 Русский</b> - 11:40 - 12:25
4. <b>🇷🇺 Русский</b> - 11:40 - 12:25
5. <b>💻 Информатика</b> - 12:45 - 13:30
6. <b>💻 Труд</b> - 13:40 - 14:25
7. <b>🧬 Биология</b> - 14:30 - 16:05''')
            bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                     caption=raspis, parse_mode='HTML', reply_markup=call.message.reply_markup)

        if days_of_week[day_of_week] == "Среда":
            raspis = ('''Среда:
            
1. <b>➕➖Алгебра✖️➗</b> - 8:30 - 9:15
2. <b>📐Геометрия</b> - 9:35 - 10:20
3. <b>🇺🇸 Английский</b> - 10:40 - 11:25
4. <b>🇷🇺 Русский</b> - 11:40 - 12:25
4. <b>🇷🇺 Русский</b> - 11:40 - 12:25
5. <b>💻 Информатика</b> - 12:45 - 13:30
6. <b>💻 Труд</b> - 13:40 - 14:25
7. <b>🧬 Биология</b> - 14:30 - 16:05

Четверг:
            
1. <b>Профориентация</b> - 8:30 - 9:15
2. <b>⚽️Физ-ра</b> - 9:35 - 10:20
3. <b>📜 История</b> - 10:40 - 11:25
4. <b>🇷🇺 Русский</b> - 11:40 - 12:25
5. <b>👩‍🔬Химия</b> - 12:45 - 13:30
6. <b>➕➖Алгебра✖️➗</b> - 13:40 - 14:25
7. <b>📖 Лит-ра</b> - 14:30 - 15:15
8. <b>ОБЗР</b> - 15:20 - 16:05 ''')
            bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                     caption=raspis, parse_mode='HTML', reply_markup=call.message.reply_markup)

        if days_of_week[day_of_week] == "Четверг":
            raspis = ('''Четверг:
            
1. <b>Профориентация</b> - 8:30 - 9:15
2. <b>⚽️Физ-ра</b> - 9:35 - 10:20
3. <b>📜 История</b> - 10:40 - 11:25
4. <b>🇷🇺 Русский</b> - 11:40 - 12:25
5. <b>👩‍🔬Химия</b> - 12:45 - 13:30
6. <b>➕➖Алгебра✖️➗</b> - 13:40 - 14:25
7. <b>📖 Лит-ра</b> - 14:30 - 15:15
8. <b>ОБЗР</b> - 15:20 - 16:05 

Пятница:
            
1. <b>🧬 Биология</b> - 8:30 - 9:15
2. <b>🇺🇸 Английский - 9:35</b> - 10:20
3. <b>📜 История - 10:40</b> - 11:35
4. <b>⚛️Физика🍎 - 11:40</b> - 12:25
5. <b>🗺 География</b> - 12:45 - 13:30
6. <b>Вероятность и стат.</b> - 13:40 - 14:25''')
            bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                     caption=raspis, parse_mode='HTML', reply_markup=call.message.reply_markup)

        if days_of_week[day_of_week] == "Пятница":
            raspis = ('''Пятница:
            
1. <b>🧬 Биология</b> - 8:30 - 9:15
2. <b>🇺🇸 Английский - 9:35</b> - 10:20
3. <b>📜 История - 10:40</b> - 11:35
4. <b>⚛️Физика🍎 - 11:40</b> - 12:25
5. <b>🗺 География</b> - 12:45 - 13:30
6. <b>Вероятность и стат.</b> - 13:40 - 14:25''')
            bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                     caption=raspis, parse_mode='HTML', reply_markup=call.message.reply_markup)

        if days_of_week[day_of_week] == "Суббота":
            raspis = '''😎 Сегодня Суббота в школу не надо
            
<b>Понедельник:</b>         
1. <b>Разговор о важном</b> - 8:30 - 9:15
2. <b>👩‍🔬Химия</b> - 9:35 - 10:20
3. <b>📐Геометрия</b> - 10:40 - 11:25
4. <b>📜История</b> - 11:40 - 12:25
5. <b>🇺🇸 Английский</b> - 12:45 - 13:30
6. <b>⚛️Физика🍎</b> - 13:40 - 14:25
7. <b>📖 Лит-ра</b> - 14:30 - 15:15'''
            bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                     caption=raspis, parse_mode='HTML', reply_markup=call.message.reply_markup)

        if days_of_week[day_of_week] == "Воскресенье":
            raspis = '''😎Сегодня Воскресенье так что в шкилу не надо
            
<b>Понедельник:</b>          
1. <b>Разговор о важном</b> - 8:30 - 9:15
2. <b>👩‍🔬Химия</b> - 9:35 - 10:20
3. <b>📐Геометрия</b> - 10:40 - 11:25
4. <b>📜История</b> - 11:40 - 12:25
5. <b>🇺🇸 Английский язык</b> - 12:45 - 13:30
6. <b>⚛️Физика🍎</b> - 13:40 - 14:25
7. <b>📖 Лит-ра</b> - 14:30 - 15:15'''
            bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                     caption=raspis, parse_mode='HTML', reply_markup=call.message.reply_markup)

    if call.data == 'raspisan_all':
        raspis = '''---------------------------------------
<b>Понедельник:</b>         
1. <b>Разговор о важном</b> - 8:30 - 9:15
2. <b>👩‍🔬Химия</b> - 9:35 - 10:20
3. <b>📐Геометрия</b> - 10:40 - 11:25
4. <b>📜История</b> - 11:40 - 12:25
5. <b>🇺🇸 Английский язык</b> - 12:45 - 13:30
6. <b>⚛️Физика🍎</b> - 13:40 - 14:25
7. <b>📖 Лит-ра</b> - 14:30 - 15:15
---------------------------------------
<b>Вторник:</b>
1. <b>⚽️Физ-ра</b> - 8:30 - 9:15
2. <b>📖 Лит-ра</b> - 9:35 - 10:20
3. <b>🗺 География</b> - 10:40 - 11:25
4. <b>🧍 Обществознание</b> - 11:40 - 12:25
5. <b>➕➖Алгебра✖️➗</b> - 12:45 - 13:30
6. <b>🇷🇺 Русский</b> - 13:40 - 14:25
7. <b>⚛️Физика🍎</b> - 14:30 - 15:15
---------------------------------------
<b>Среда:</b>
1. <b>➕➖Алгебра✖️➗</b> - 8:30 - 9:15
2. <b>📐Геометрия</b> - 9:35 - 10:20
3. <b>🇺🇸 Английский</b> - 10:40 - 11:25
4. <b>🇷🇺 Русский</b> - 11:40 - 12:25
5. <b>💻 Информатика</b> - 12:45 - 13:30
6. <b>💻 Труд</b> - 13:40 - 14:25
7. <b>🧬 Биология</b> - 14:30 - 16:05
---------------------------------------
<b>Четверг:</b>
1. <b>Профориентация</b> - 8:30 - 9:15
2. <b>⚽️Физ-ра</b> - 9:35 - 10:20
3. <b>📜История</b> - 10:40 - 11:25
4. <b>🇷🇺 Русский</b> - 11:40 - 12:25
5. <b>👩‍🔬Химия</b> - 12:45 - 13:30
6. <b>➕➖Алгебра✖️➗</b> - 13:40 - 14:25
7. <b>📖 Лит-ра</b> - 14:30 - 15:15
8. <b>ОБЗР</b> - 15:20 - 16:05
---------------------------------------
<b>Пятница:</b>
1. <b>🧬 Биология</b> - 8:30 - 9:15
2. <b>🇺🇸 Английский - 9:35</b> - 10:20
3. <b>📜 История - 10:40</b> - 11:35
4. <b>⚛️Физика🍎 - 11:40</b> - 12:25
5. <b>🗺 География</b> - 12:45 - 13:30
6. <b>Вероятность и стат.</b> - 13:40 - 14:25
---------------------------------------'''

        markup_predmet = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton("🔙 Назад", callback_data='back_to_menu_')
        markup_predmet.add(back)

        bot.send_message(call.message.chat.id, raspis, parse_mode='HTML', reply_markup=markup_predmet)


    if call.data == 'back_to_menu_':
        bot.answer_callback_query(call.id, "🏛 Главное меню")
        markup_start = types.InlineKeyboardMarkup(row_width=1)
        predmet = types.InlineKeyboardButton("📚 Предметы", callback_data='predmet')
        raspisan = types.InlineKeyboardButton('🗓 Расписание (На сегодня)', callback_data='raspisan')
        raspisan_all = types.InlineKeyboardButton('🗓 Расписание (На всю неделю)', callback_data='raspisan_all')
        # dz = types.InlineKeyboardButton("🏫 Д/З", callback_data='dz')
        raspisan_call = types.InlineKeyboardButton('⏰ Расписание звонков', callback_data='raspisan_call')
        # teoria = types.InlineKeyboardButton('📝 Теория', callback_data='teoria')
        top = types.InlineKeyboardButton('🔝 Топ по баклажанам', callback_data='top')
        baklagan = types.InlineKeyboardButton('🍆 Баклажан', callback_data='baklagan')
        # mems = types.InlineKeyboardButton('😂 Мемы (Пиздец смешно)', callback_data='mems')

        # Добавление кнопок на клавиатуру
        markup_start.add(predmet, raspisan, raspisan_all, raspisan_call, top, baklagan)

        # Открываем файл фотографии перед отправкой

        text_back_menu = f'''🏛 Главное меню ⌵\n
<b>╭ Username:</b> <code>{call.message.from_user.username}</code>
<b>├ User ID:</b> <code>{call.message.from_user.id}</code>
<b>╰ Balance:</b> <code>{user_balances[user_id]} 🍆</code>\n
        '''
        photo_start = open('start.jpg', 'rb')
        msg_start = bot.send_photo(call.message.chat.id, photo_start, caption=text_back_menu, parse_mode='HTML',
                                   reply_markup=markup_start)

        bot_data[call.message.chat.id] = {
            'message_id': msg_start.message_id,
            'photo': photo_start
        }

        # Открываем файл фотографии перед отправкой

#         text_start = f'''🏛 Главное меню ⌵\n
# <b>╭ Username:</b> <code>{call.message.from_user.username}</code>
# <b>├ User ID:</b> <code>{call.message.from_user.id}</code>
# <b>╰ Balance:</b> <code>{user_balances[user_id]} 🍆</code>\n
#         '''
#         photo_start = open('start.jpg', 'rb')
#
#         time.sleep(2)
#
#         msg_start = bot.send_photo(call.message.chat.id, photo_start, caption=text_start, parse_mode='HTML',
#                                    reply_markup=markup_start)
#
#         bot_data[call.message.chat.id] = {
#             'message_id': msg_start.message_id,
#             'photo': photo_start
#         }

    if call.data == 'raspisan_call':
        raspisan_call = '''<b>Расписанаие звонков</b>
        
1) 8:30 - 9:15
2) 9:35 - 10:20
3) 10:40 - 11:25
4) 11:40 - 12:25
5) 12:45 - 13:30
6) 13:40 - 14:25
7) 14:30 - 15:15
8) 15:20 - 16:05'''
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                 caption=raspisan_call, parse_mode='HTML', reply_markup=call.message.reply_markup)

    if call.data == 'teoria':
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                 caption="У меня её нету", parse_mode='HTML', reply_markup=call.message.reply_markup)

    if call.data == 'baklagan':
        text = f'''Профиль 👔\n
<b>╭ Username:</b> <code>{call.from_user.username}</code>
<b>├ User ID:</b> <code>{call.from_user.id}</code>
<b>╰ Balance:</b> <code>{user_balances[user_id]} 🍆</code>\n
'''

        bot.answer_callback_query(call.id, "Профиль 🍆")
        markup_predmet = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton("🔙 Назад", callback_data='back_to_menu')
        markup_predmet.add(back)

        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                 caption=text, parse_mode='HTML', reply_markup=markup_predmet)

    if call.data == 'top':
        # Сортируем пользователей по балансу в порядке убывания
        sorted_balances = sorted(user_balances.items(), key=lambda x: x[1], reverse=True)

        # Ограничим топ 10 пользователями (или больше/меньше, как нужно)
        top_users = sorted_balances[:30]

        # Формируем текст для вывода топа
        text = '⭐️ ТОП пользователей ⭐️\n\n'
        for i, (user_id, balance) in enumerate(top_users, start=1):
            # Получаем username пользователя или заменяем на его user_id, если username нет
            username = bot.get_chat(user_id).username or f'User {user_id}'
            text += f"<b>{i}. @{username}</b>\n"
            text += f"<b>├ User ID:</b> <code>{user_id}</code>\n"
            text += f"<b>╰ Balance:</b> <code>{balance} 🍆</code>\n\n"

        bot.answer_callback_query(call.id, "⭐️ ТОП пользователей ⭐️")
        markup_predmet = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton("🔙 Назад", callback_data='back_to_menu')
        markup_predmet.add(back)

        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                 caption=text, parse_mode='HTML', reply_markup=markup_predmet)

    ###############################ПРЕДМЕТЫ###############################

    # algebra = types.InlineKeyboardButton("➕➖Алгебра✖️➗", callback_data='algebra')
    # geometria = types.InlineKeyboardButton("📐Геометрия", callback_data='geometria')
    # russ = types.InlineKeyboardButton("🇷🇺 Русский", callback_data='russ')
    # english = types.InlineKeyboardButton("🇺🇸 Английский", callback_data='english')
    # phisic = types.InlineKeyboardButton("⚛️Физика🍎", callback_data='phisic')
    # himia = types.InlineKeyboardButton("👩‍🔬Химия", callback_data='himia')


    if call.data == "algebra":
        bot.answer_callback_query(call.id, "➕➖Алгебра✖️➗")

        text = f'''➕➖Алгебра✖️➗
        
<b>Введи номер упранения: </b>\n'''

        markup_predmet = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton("🔙 Назад", callback_data='predmet')
        markup_predmet.add(back)

        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                 caption=text, parse_mode='HTML', reply_markup=markup_predmet)

        bot.register_next_step_handler(call.message, get_exercise_number_algbra)

    if call.data == 'geometria':
        bot.answer_callback_query(call.id,"📐Геометрия")

        text = f'''📐Геометрия

<b>Введи номер упранения: </b>\n'''

        markup_predmet = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton("🔙 Назад", callback_data='predmet')
        markup_predmet.add(back)

        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                 caption=text, parse_mode='HTML', reply_markup=markup_predmet)

        bot.register_next_step_handler(call.message, get_exercise_number_geometria)

    if call.data == 'russ':
        bot.answer_callback_query(call.id, "🇷🇺 Русский")

        text = f'''🇷🇺 Русский

<b>Введи номер упранения: </b>\n'''

        markup_predmet = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton("🔙 Назад", callback_data='predmet')
        markup_predmet.add(back)

        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                 caption=text, parse_mode='HTML', reply_markup=markup_predmet)

        bot.register_next_step_handler(call.message, get_exercise_number_russ)


    if call.data == 'english':
        bot.answer_callback_query(call.id, '🇺🇸 Английский')

        text = f'''🇺🇸 Английский

<b>Введи номер страницы: </b>\n'''

        markup_predmet = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton("🔙 Назад", callback_data='predmet')
        markup_predmet.add(back)

        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                 caption=text, parse_mode='HTML', reply_markup=markup_predmet)

        bot.register_next_step_handler(call.message, get_exercise_number_english)

    if call.data == 'phisic':
        bot.answer_callback_query(call.id, '⚛️Физика🍎')

        text = f'''⚛️Физика🍎

<b>Выбери упражнения или вопросы: </b>\n'''

        markup_predmet = types.InlineKeyboardMarkup()
        upr = types.InlineKeyboardButton("⚛️ Упражнение", callback_data='upr')
        questshens = types.InlineKeyboardButton("🍎 Вопросы", callback_data='questshens')
        back = types.InlineKeyboardButton("🔙 Назад", callback_data='predmet')
        markup_predmet.add(upr, questshens)
        markup_predmet.add(back)

        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                 caption=text, parse_mode='HTML', reply_markup=markup_predmet)

    if call.data == 'upr':
        text = f'''⚛️Физика🍎 --> №Упражнение

<b>Введи номер упранения: </b>\n'''

        markup_predmet = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton("🔙 Назад", callback_data='phisic')
        markup_predmet.add(back)

        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                 caption=text, parse_mode='HTML', reply_markup=markup_predmet)

        bot.register_next_step_handler(call.message, get_exercise_number_phisic_upr)


    if call.data == 'questshens':
        text = f'''⚛️Физика🍎 --> Вопросы?

<b>Введи номер §Параграфа: </b>\n'''

        markup_predmet = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton("🔙 Назад", callback_data='phisic')
        markup_predmet.add(back)

        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                 caption=text, parse_mode='HTML', reply_markup=markup_predmet)

        bot.register_next_step_handler(call.message, get_exercise_number_phisic_questshens)


    if call.data == 'himia':
        bot.answer_callback_query(call.id, '👩‍🔬Химия')
#
#         text = f'''👩‍🔬Химия
#
# <b>Введи номер упранения: </b>\n'''

        text =  f'''👩‍🔬Химия

<b>Я ещё не сделал</b>\n'''
        markup_predmet = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton("🔙 Назад", callback_data='predmet')
        markup_predmet.add(back)

        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                 caption=text, parse_mode='HTML', reply_markup=markup_predmet)

        # bot.register_next_step_handler(call.message, get_exercise_number_himia)

    ###############################МЕМЫ###############################

    # if call.data == 'mems':
    #     time.sleep(1)
    #     bot.answer_callback_query(call.id, 'Мемы 😂 (ПИИИЗДЕЦ СЕМЕШНО 🗿)')

    if call.data == 'dz':
        bot.answer_callback_query(call.id, '🏫 Д/З')

        text = f'''🏫 Д/З

<b>Я ещё не сделал</b>\n'''
        markup_predmet = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton("🔙 Назад", callback_data='back_to_menu')
        markup_predmet.add(back)

        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                 caption=text, parse_mode='HTML', reply_markup=markup_predmet)


def get_exercise_number_algbra(message):
    exercise_number = message.text.strip()  # Получаем номер упражнения
    if exercise_number.isdigit():  # Проверяем, что введено число
        # Удаляем сообщение пользователя
        bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)

        # Формируем ссылку с номером упражнения
        link = f"https://reshak.ru/otvet/reshebniki.php?otvet={exercise_number}&predmet=kolyagin9"

        markup_predmet = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton("🔙 Назад", callback_data='back_to_menu_')
        markup_predmet.add(back)

        # Отправляем сообщение с ссылкой
        bot.send_message(message.chat.id, f"Твоя ссылка на упражнение:\n {link}", reply_markup=markup_predmet)

    else:
        # Сообщение об ошибке
        markup_predmet = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton("🔙 Назад", callback_data='back_to_menu_')
        markup_predmet.add(back)

        bot.send_message(message.chat.id, "Пожалуйста, введи корректный номер упражнения.", reply_markup=markup_predmet)
        bot.register_next_step_handler(message, get_exercise_number_algbra)  # Повторный запрос номера


def get_exercise_number_geometria(message):
    exercise_number = message.text.strip()  # Получаем номер упражнения
    if exercise_number.isdigit():  # Проверяем, что введено число
        # Удаляем сообщение пользователя
        bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)

        # Формируем ссылку с номером упражнения
        link = f"https://pomogalka.me/7-klass/geometriya/atanasyan/nomer-{exercise_number}/"

        markup_predmet = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton("🔙 Назад", callback_data='back_to_menu_')
        markup_predmet.add(back)

        # Отправляем сообщение с ссылкой
        bot.send_message(message.chat.id, f"Твоя ссылка на упражнение:\n {link}", reply_markup=markup_predmet)

    else:
        # Сообщение об ошибке
        markup_predmet = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton("🔙 Назад", callback_data='back_to_menu_')
        markup_predmet.add(back)

        bot.send_message(message.chat.id, "Пожалуйста, введи корректный номер упражнения.", reply_markup=markup_predmet)
        bot.register_next_step_handler(message, get_exercise_number_algbra)  # Повторный запрос номера


def get_exercise_number_russ(message):
    exercise_number = message.text.strip()  # Получаем номер упражнения
    if exercise_number.isdigit():  # Проверяем, что введено число
        # Удаляем сообщение пользователя
        bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)

        # Формируем ссылку с номером упражнения
        link = f"https://pomogalka.me/9-klass/russkij-yazyk/razumovskaja/uprazhnenie-{exercise_number}/"

        markup_predmet = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton("🔙 Назад", callback_data='back_to_menu_')
        markup_predmet.add(back)

        # Отправляем сообщение с ссылкой
        bot.send_message(message.chat.id, f"Твоя ссылка на упражнение:\n {link}", reply_markup=markup_predmet)

    else:
        # Сообщение об ошибке
        markup_predmet = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton("🔙 Назад", callback_data='back_to_menu_')
        markup_predmet.add(back)

        bot.send_message(message.chat.id, "Пожалуйста, введи корректный номер упражнения.", reply_markup=markup_predmet)
        bot.register_next_step_handler(message, get_exercise_number_algbra)  # Повторный запрос номера


def get_exercise_number_english(message):
    exercise_number = message.text.strip()  # Получаем номер упражнения
    if exercise_number.isdigit():  # Проверяем, что введено число
        # Удаляем сообщение пользователя
        bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)

        # Формируем ссылку с номером упражнения
        link = f"https://pomogalka.me/9-klass/anglijskij-yazyk/spotlight/2023-stranica-{exercise_number}/"

        markup_predmet = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton("🔙 Назад", callback_data='back_to_menu_')
        markup_predmet.add(back)

        # Отправляем сообщение с ссылкой
        bot.send_message(message.chat.id, f"Твоя ссылка по английскому:\n {link}", reply_markup=markup_predmet)

    else:
        # Сообщение об ошибке
        markup_predmet = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton("🔙 Назад", callback_data='back_to_menu_')
        markup_predmet.add(back)

        bot.send_message(message.chat.id, "Пожалуйста, введи корректный номер упражнения.", reply_markup=markup_predmet)
        bot.register_next_step_handler(message, get_exercise_number_algbra)  # Повторный запрос номера


def get_exercise_number_phisic_upr(message):
    exercise_number = message.text.strip()  # Получаем номер упражнения
    if exercise_number.isdigit():  # Проверяем, что введено число
        # Удаляем сообщение пользователя
        bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)

        # Формируем ссылку с номером упражнения
        link = f"https://reshak.ru/otvet/reshebniki.php?otvet=new/Upr/{exercise_number}&predmet=per9"

        markup_predmet = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton("🔙 Назад", callback_data='back_to_menu_')
        markup_predmet.add(back)

        # Отправляем сообщение с ссылкой
        bot.send_message(message.chat.id, f"Твоя ссылка на упражнение:\n {link}", reply_markup=markup_predmet)

    else:
        # Сообщение об ошибке
        markup_predmet = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton("🔙 Назад", callback_data='back_to_menu_')
        markup_predmet.add(back)

        bot.send_message(message.chat.id, "Пожалуйста, введи корректный номер упражнения.", reply_markup=markup_predmet)
        bot.register_next_step_handler(message, get_exercise_number_phisic_upr)  # Повторный запрос номера


def get_exercise_number_phisic_questshens(message):
    exercise_number = message.text.strip()  # Получаем номер упражнения
    if exercise_number.isdigit():  # Проверяем, что введено число
        # Удаляем сообщение пользователя
        bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)

        # Формируем ссылку с номером упражнения
        link = f"https://reshak.ru/otvet/reshebniki.php?otvet=new/paragraph/{exercise_number}&predmet=per9"

        markup_predmet = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton("🔙 Назад", callback_data='back_to_menu_')
        markup_predmet.add(back)

        # Отправляем сообщение с ссылкой
        bot.send_message(message.chat.id, f"Твоя ссылка на вопросы:\n {link}", reply_markup=markup_predmet)

    else:
        # Сообщение об ошибке
        markup_predmet = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton("🔙 Назад", callback_data='back_to_menu_')
        markup_predmet.add(back)

        bot.send_message(message.chat.id, "Пожалуйста, введи корректный номер упражнения.", reply_markup=markup_predmet)
        bot.register_next_step_handler(message, get_exercise_number_phisic_questshens)  # Повторный запрос номера


def get_exercise_number_himia(message):
    exercise_number = message.text.strip()  # Получаем номер упражнения
    if exercise_number.isdigit():  # Проверяем, что введено число
        # Удаляем сообщение пользователя
        bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)

        # Формируем ссылку с номером упражнения
        link = f"https://reshak.ru/otvet/reshebniki.php?otvet={exercise_number}&predmet=kolyagin9"

        markup_predmet = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton("🔙 Назад", callback_data='back_to_menu_')
        markup_predmet.add(back)

        # Отправляем сообщение с ссылкой
        bot.send_message(message.chat.id, f"Твоя ссылка на упражнение:\n {link}", reply_markup=markup_predmet)

    else:
        # Сообщение об ошибке
        markup_predmet = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton("🔙 Назад", callback_data='back_to_menu_')
        markup_predmet.add(back)

        bot.send_message(message.chat.id, "Пожалуйста, введи корректный номер упражнения.", reply_markup=markup_predmet)
        bot.register_next_step_handler(message, get_exercise_number_algbra)  # Повторный запрос номера

bot.polling(none_stop=True)

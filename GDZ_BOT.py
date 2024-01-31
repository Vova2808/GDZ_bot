import telebot
from telebot import types
# import subprocess
# import time
# import openai
import time
import schedule
import telebot
import random

bot = telebot.TeleBot('5901990283:AAGvaI4GAlOzdLej5JSg_DLRmKi521AY2jE')
# 6619437777:AAGAmak2lcgXlaJc1KniqJrpT2sjlSwXpIg
# 5901990283:AAGvaI4GAlOzdLej5JSg_DLRmKi521AY2jE

print("Bot Запущен")

emoge = ['👌','👋','👎','🖖','👍','😃','🤓','🧐','😎','🙃','🥳','🤖','👾']
random_emoge = random.choice(emoge)



# @bot.message_handler(commands=['start'])
#
# def start_message(message):
#
#     markdown_text = "Hello, <mark>world!</mark>"
#
#     bot.send_message(message.chat.id, markdown_text, parse_mode='Markdown')


@bot.message_handler(commands=['start'])
def start(message):
    random_emoge = random.choice(emoge)
    # bot.send_message(message.chat.id, '1. russian ', parse_mode='Markdown')
    text = '''<code>/russ</code> и плюс пробел и номер упражнения\n
Пример /russ 123 еслм химия то нужно\n написать номер парагрофа\n
_____________________________________________
1. <code>/russ </code>
2. <code>/algebra</code>
3. <code>/geometria</code>
4. <code>/himia </code>
5. <code>/physic </code>
6. /teoria виликая теория по русскому
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
_____________________________________________
1. <code>/russ </code>
2. <code>/algebra</code>
3. <code>/geometria</code>
4. <code>/himia </code>
5. <code>/physic </code>
6. /teoria виликая теория по русскому
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
        print("Рсский ",user_msg.split(' ')[1])

        if int(user_msg.split(' ')[1]) <= 417:
            bot.send_message(message.chat.id, 'Вот cсылка 👇')
            bot.send_message(message.chat.id, 'https://reshak.ru/otvet/reshebniki.php?otvet=' + user_msg.split(' ')[1] + '&predmet=razumovskaya8')
            bot.send_message(message.chat.id, 'Вот фото 👇')
            bot.send_message(message.chat.id, 'https://reshak.ru/reshebniki/russkijazik/8/razumovskaya/images1/' + user_msg.split(' ')[1] + '.png')
            bot.send_message(message.chat.id, '')

        else:
            bot.send_message(message.chat.id, 'Такого упражнения нету')

    except:
        # bot.send_message(message.chat.id, "Что то не хочет робить у тебя один пробел после /russ 123")
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
        print("Алгебра ", user_msg.split(' ')[1])

        if int(user_msg.split(' ')[1]) <= 917:
            bot.send_message(message.chat.id, 'Вот cсылка 👇')
            bot.send_message(message.chat.id, 'https://reshak.ru/otvet/reshebniki.php?otvet=' + user_msg.split(' ')[1] + '&predmet=kolyagin8')
            bot.send_message(message.chat.id, 'Вот фото 👇')
            bot.send_message(message.chat.id, 'https://reshak.ru/reshebniki/algebra/8/kolyagin/images1/' + user_msg.split(' ')[1] + '.png')
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
        print("Геометрия ", user_msg.split(' ')[1])

        if int(user_msg.split(' ')[1]) <= 1413:
            bot.send_message(message.chat.id, 'Вот cсылка 👇')
            bot.send_message(message.chat.id, 'https://pomogalka.me/7-klass/geometriya/atanasyan/nomer-' + user_msg.split(' ')[1] + '/')
            bot.send_message(message.chat.id, 'Вот фото 👇')
            bot.send_message(message.chat.id, 'https://pomogalka.me/img/7-9-klass-atanasyan/' + user_msg.split(' ')[1] + '.png')
            bot.send_message(message.chat.id, '')

        else:
            bot.send_message(message.chat.id, 'Такого номера нету')
    except:
        # bot.send_message(message.chat.id, "Что то не хочет робить у тебя один пробел после /geometria 123")
        print("Error")


@bot.message_handler(commands=['himia'])
def kill_process(message):
    try:
        user_msg = '{0}'.format(message.text)
        print("Геометрия ", user_msg.split(' ')[1])

        if int(user_msg.split(' ')[1]) <= 55:
            bot.send_message(message.chat.id, 'Вот cсылка 👇')#https://reshak.ru/reshebniki/ximiya/8/kuznecova/images1/6.png
            bot.send_message(message.chat.id, 'https://reshak.ru/otvet/reshebniki.php?otvet=' + user_msg.split(' ')[1] + '&predmet=kuznecova8')
            bot.send_message(message.chat.id, 'Вот фото 👇')
            bot.send_message(message.chat.id, 'https://reshak.ru/reshebniki/ximiya/8/kuznecova/images1/' + user_msg.split(' ')[1] + '.png')
            bot.send_message(message.chat.id, '')

        else:
            bot.send_message(message.chat.id, 'Такого парагрофа нету')
    except:
        # bot.send_message(message.chat.id, "Что то не хочет робить у тебя один пробел после /himia 123")
        print("Error")


@bot.message_handler(commands=['physic'])
def physic(message):
    try:
        user_msg = '{0}'.format(message.text)
        print("Геометрия ", user_msg.split(' ')[1])

        if int(user_msg.split(' ')[1]) <= 55:
            bot.send_message(message.chat.id, 'Вот cсылка 👇')#https://reshak.ru/otvet/reshebniki.php?otvet=paragraph/33&predmet=perishkin_new8
            bot.send_message(message.chat.id, 'https://reshak.ru/otvet/reshebniki.php?otvet=paragraph/' + user_msg.split(' ')[1] + '&predmet=perishkin_new8')
            bot.send_message(message.chat.id, 'Вот фото 👇')
            bot.send_message(message.chat.id, 'https://reshak.ru/reshebniki/fizika/8/perishkin_new/images1/paragraph/' + user_msg.split(' ')[1] + '.png')
            bot.send_message(message.chat.id, '')

        else:
            bot.send_message(message.chat.id, 'Такого парагрофа нету')
    except:
        # bot.send_message(message.chat.id, "Что то не хочет робить у тебя один пробел после /himia 123")
        print("Error")


@bot.message_handler(commands=['raspisanie'])
def raspisanie(message):
    try:
        bot.send_message(message.chat.id, 'Вот фото 👇')
        bot.send_photo(message.chat.id, "https://i.imgur.com/G5gCOpp.jpeg")

    except:
        bot.send_message(message.chat.id, "Что то не хочет робить")
        # print("Error")

@bot.message_handler(content_types=['text'])
def text(message):
    get_message_bot = message.text.strip().lower()

    if message.text == 'Русский Язык':
        bot.send_message(message.chat.id, "Ёбаный русский")


    if message.text == 'Расписание':
        bot.send_message(message.chat.id, "Расписание 👇")
        bot.send_photo(message.chat.id,"https://i.imgur.com/G5gCOpp.jpeg")


    if message.text == 'Предметы':
        random_emoge = random.choice(emoge)
        text = '''<code>/russ</code> и плюс пробел и номер упражнения\n
Пример /russ 123 еслм химия то нужно\n написать номер парагрофа\n
_____________________________________________
1. <code>/russ </code>
2. <code>/algebra</code>
3. <code>/geometria</code>
4. <code>/himia </code>
5. <code>/physic </code>
6. /teoria виликая теория по русскому
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


    iphone_or_android = ['Iphone или Android', 'iphone или android', 'айфон или андроид', 'Айфон или Андроид',
                         'Айфон или андроид', 'айфон или Андроид']

    iphone_govno = ['Iphone полное говно', 'Iphone вообще говно', 'Iphone шлак', 'Конечно Android Iphone говно полное']
    random_phrase = random.choice(iphone_govno)


    if message.text in iphone_or_android:
        bot.send_message(message.chat.id, random_phrase)


    # else:
    #     bot.send_message(message.chat.id, 'Чего напиши /help')

bot.polling(none_stop=True)

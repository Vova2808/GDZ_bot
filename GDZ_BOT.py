import telebot
from telebot import types
import subprocess
import time

bot = telebot.TeleBot('5901990283:AAGvaI4GAlOzdLej5JSg_DLRmKi521AY2jE')

print("Bot Запущен")


@bot.message_handler(commands=['start'])
def start(message):
    # bot.send_message(message.chat.id, '1. russian ', parse_mode='Markdown')
    text = '''<code>/russ</code> и плюс пробел и номер упражнения
_____________________________________________
1. <code>/russ </code>
2. <code>/algebra</code>
3. <code>/geometria</code>
4. <code>/litra</code>
5. /teoria виликая теория по русскому
_____________________________________________
'''
    bot.send_message(message.chat.id,text,parse_mode='html')


@bot.message_handler(commands=['russ'])
def kill_process(message):
    try:
        user_msg = '{0}'.format(message.text)
        a = f"https://reshak.ru/otvet/reshebniki.php?otvet={message.text}&predmet=razumovskaya8"
        e = f"https://reshak.ru/reshebniki/russkijazik/8/razumovskaya/images1/{message.text}.png"
        bot.send_message(message.chat.id, 'Вот cсылка 👇')
        bot.send_message(message.chat.id, 'https://reshak.ru/otvet/reshebniki.php?otvet=' + user_msg.split(' ')[1] + '&predmet=razumovskaya8')
        bot.send_message(message.chat.id, 'Вот фото 👇')
        bot.send_message(message.chat.id, 'https://reshak.ru/reshebniki/russkijazik/8/razumovskaya/images1/' + user_msg.split(' ')[1] + '.png')
        bot.send_message(message.chat.id, '')

    except:
        bot.send_message(message.chat.id, "Что то не хочет робить")
        # print("Error")


@bot.message_handler(commands=['teoria'])
def kill_process(message):
    try:
        bot.send_message(message.chat.id, 'Вот фото 👇')
        bot.send_photo(message.chat.id, "https://sun9-76.userapi.com/impg/c858128/v858128004/177d9a/QW_hlfek85U.jpg?size=1280x720&quality=96&sign=3dde694f7f045bdbe7a8e81a1b8a5b63&c_uniq_tag=P7Hb1N1-dCn0IJKbETX_E6pJcoBaJNeGFSr9VZdQ_FA&type=album")

    except:
        bot.send_message(message.chat.id, "Что то не хочет робить")
        # print("Error")


@bot.message_handler(commands=['algebra'])
def kill_process(message):
    try:
        user_msg = '{0}'.format(message.text)
        a = f"https://reshak.ru/otvet/reshebniki.php?otvet={message.text}&predmet=razumovskaya8"
        e = f"https://reshak.ru/reshebniki/russkijazik/8/razumovskaya/images1/{message.text}.png"
        bot.send_message(message.chat.id, 'Вот cсылка 👇')
        bot.send_message(message.chat.id, 'https://reshak.ru/otvet/reshebniki.php?otvet=' + user_msg.split(' ')[1] + '&predmet=razumovskaya8')
        bot.send_message(message.chat.id, 'Вот фото 👇')
        bot.send_message(message.chat.id, 'https://reshak.ru/reshebniki/russkijazik/8/razumovskaya/images1/' + user_msg.split(' ')[1] + '.png')
        bot.send_message(message.chat.id, '')

    except:
        bot.send_message(message.chat.id, "Что то не хочет робить")
        # print("Error")


@bot.message_handler(commands=['litra'])
def kill_process(message):
    try:
        user_msg = '{0}'.format(message.text)
        a = f"https://reshak.ru/otvet/reshebniki.php?otvet={message.text}&predmet=razumovskaya8"
        e = f"https://reshak.ru/reshebniki/russkijazik/8/razumovskaya/images1/{message.text}.png"
        bot.send_message(message.chat.id, 'Вот cсылка 👇')
        bot.send_message(message.chat.id, 'https://reshak.ru/otvet/reshebniki.php?otvet=' + user_msg.split(' ')[1] + '&predmet=razumovskaya8')
        bot.send_message(message.chat.id, 'Вот фото 👇')
        bot.send_message(message.chat.id, 'https://reshak.ru/reshebniki/russkijazik/8/razumovskaya/images1/' + user_msg.split(' ')[1] + '.png')
        bot.send_message(message.chat.id, '')

    except:
        bot.send_message(message.chat.id, "Что то не хочет робить")
        # print("Error")


@bot.message_handler(content_types=['geometria'])
def text(message):
    if message.text == 'Русский Язык':
        bot.send_message(message.chat.id, "Ёбаный русский")
    else:
        bot.send_message(message.chat.id, 'Напиши /help')

bot.polling(none_stop=True)
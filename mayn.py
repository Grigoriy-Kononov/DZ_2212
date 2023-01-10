import telebot
import random
from config import TOKEN
from coding import *


bot = telebot.TeleBot(TOKEN)

def comrpes(message):
    str = rle_code(message.text)
    bot.send_message(message.chat.id, str)
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEG73Vjo1mRgC9-dIS5kUjjdMG09qeodAACXwEAAhAabSLLoLkqsC4-oywE')
    bot.send_message(message.chat.id, 'для повторного сжатия снова нажмите на кнопку "Кодировать текст"')

def decomrpes(message):
    str = rle_decode(message.text)
    bot.send_message(message.chat.id, str)
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEG73Vjo1mRgC9-dIS5kUjjdMG09qeodAACXwEAAhAabSLLoLkqsC4-oywE')
    bot.send_message(message.chat.id, 'для повторного сжатия снова нажмите на кнопку "Декодировать текст"')

"""Команда СТАРТ"""

@bot.message_handler(commands=['start'])
def welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

    item1 = telebot.types.KeyboardButton('Рандомное число')
    item2 = telebot.types.KeyboardButton('Кинуть кость')
    item3 = telebot.types.KeyboardButton('Кодировать текст')
    item4 = telebot.types.KeyboardButton('Декодировать текст')
    item5 = telebot.types.KeyboardButton('Знак зодиака')
    item6 = telebot.types.KeyboardButton('Угадайка')

    markup.add(item1, item2, item3, item4, item5, item6)

    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEHMj5jvYowLwQ49UFWhN5opwSvJtdWHwACPgcAAkb7rASvXDpewRmI9i0E')
    bot.send_message(message.chat.id, 'Добро пожаловать! Выберите нужный вам пункт меню: ', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Привет':
        bot.send_message(message.chat.id, 'Привет, как дела?')
    elif message.text == 'Рандомное число':
        bot.send_message(message.chat.id, str(random.randint(1, 10)))
    elif message.text == 'Кинуть кость':
        bot.send_message(message.chat.id, f'Вам выпало {(str(random.randint(1, 6)))}')
    elif message.text == "Кодировать текст":
        mesg = bot.send_message(message.chat.id, 'Введите строку которую хотите кодировать')
        bot.register_next_step_handler(mesg, comrpes)
    elif message.text == 'Декодировать текст':
        mesg = bot.send_message(message.chat.id, 'Введите строку которую хотите декодировать')
        bot.register_next_step_handler(mesg, decomrpes)
    elif message.text == 'Знак зодиака':
        markup = telebot.types.InlineKeyboardMarkup(row_width=2)
        item_1 = telebot.types.InlineKeyboardButton('Овен', callback_data='Овен')
        item_2 = telebot.types.InlineKeyboardButton('Телец', callback_data='Телец')
        item_3 = telebot.types.InlineKeyboardButton('Близнецы', callback_data='Близнецы')
        item_4 = telebot.types.InlineKeyboardButton('Рак', callback_data='Рак')
        item_5 = telebot.types.InlineKeyboardButton('Лев', callback_data='Лев')
        item_6 = telebot.types.InlineKeyboardButton('Дева', callback_data='Дева')
        item_7 = telebot.types.InlineKeyboardButton('Весы', callback_data='Весы')
        item_8 = telebot.types.InlineKeyboardButton('Скорпион', callback_data='Скорпион')
        item_9 = telebot.types.InlineKeyboardButton('Стрелец', callback_data='Стрелец')
        item_10 = telebot.types.InlineKeyboardButton('Козерог', callback_data='Козерог')
        item_11 = telebot.types.InlineKeyboardButton('Водолей', callback_data='Водолей')
        item_12 = telebot.types.InlineKeyboardButton('Рыбы', callback_data='Рыбы')
        markup.add(item_1, item_2, item_3, item_4, item_5, item_6, item_7, item_8, item_9, item_10, item_11, item_12)
        bot.send_message(message.chat.id, 'Отлично, нажимай.', reply_markup=markup)
    elif message.text == 'Угадайка':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEHMmhjvY6RsMlSBCibLHWY67iUsw7J8gACUgcAAkb7rASWmLFio0Tomy0E')
        msg = bot.send_message(message.chat.id, 'я загадал число от 1 до 5, попробуй угадай')
        bot.register_next_step_handler(msg, num_rnd)
    else:
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEHMk9jvYrrZfLQyFSmWdeMhsXYYwq42wACmBoAAozRMUnu9m9YtsiLGC0E')
        bot.send_message(message.chat.id, 'Данный функционал находится в разработке.')

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    dict_znak = znak_har()
    if call.data == 'Овен':
        bot.send_message(call.message.chat.id, dict_znak["Овен"])
    elif call.data == 'Телец':
        bot.send_message(call.message.chat.id, dict_znak["Телец"])
    elif call.data == 'Близнецы':
        bot.send_message(call.message.chat.id, dict_znak["Близнецы"])
    elif call.data == 'Рак':
        bot.send_message(call.message.chat.id, dict_znak["Рак"])
    elif call.data == 'Лев':
        bot.send_message(call.message.chat.id, dict_znak["Лев"])
    elif call.data == 'Дева':
        bot.send_message(call.message.chat.id, dict_znak["Дева"])
    elif call.data == 'Весы':
        bot.send_message(call.message.chat.id, dict_znak["Весы"])
    elif call.data == 'Скорпион':
        bot.send_message(call.message.chat.id, dict_znak["Скорпион"])
    elif call.data == 'Стрелец':
        bot.send_message(call.message.chat.id, dict_znak["Стрелец"])
    elif call.data == 'Козерог':
        bot.send_message(call.message.chat.id, dict_znak["Козерог"])
    elif call.data == 'Водолей':
        bot.send_message(call.message.chat.id, dict_znak["Водолей"])
    elif call.data == 'Рыбы':
        bot.send_message(call.message.chat.id, dict_znak["Рыбы"])

def num_rnd(message):
    x = random.randint(0, 5)
    print(x)
    if message.text == str(x):
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEHMmpjvY6vNCjHjE1-y4NxxxKBX2QjFgACNgcAAkb7rAQKl_Oq3VFfNi0E')
        bot.send_message(message.chat.id, f'угадал моё число {x}, молодец.')
    else:
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEHMk9jvYrrZfLQyFSmWdeMhsXYYwq42wACmBoAAozRMUnu9m9YtsiLGC0E')
        bot.send_message(message.chat.id, 'Не угадал')

bot.polling(none_stop=True)
import telebot
import keyboard
import requests

bot = telebot.TeleBot('7526150677:AAHh7H12GFRwJr5ml7YU_duIxmG5Y7E13Bc')
url = 'https://cbu.uz/ru/arkhiv-kursov-valyut/json/'
USD = requests.get(url).json()[0]['Rate']
EUR = requests.get(url).json()[1]['Rate']
RUB = requests.get(url).json()[2]['Rate']


@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    print(message)
    bot.send_message(user_id, f'Привет, @{message.from_user.username}!', reply_markup=keyboard.menu())

@bot.message_handler(content_types=['text'])
def text(message):
    user_id = message.from_user.id
    if message.text.title() == '$':
        bot.send_message(user_id, 'Введите сумму в UZS', reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, usd)
    elif message.text.title() == '€':
        bot.send_message(user_id, 'Введите сумму в UZS', reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, eur)
    elif message.text.title() == '₽':
        bot.send_message(user_id, 'Введите сумму в UZS', reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, rub)
    else:
        bot.send_message(user_id, 'Что-то пошло не так. Нажмите /start')

def usd(message):
    user_id = message.from_user.id
    if message.text.isnumeric():
        bot.send_message(user_id, f'{int(message.text)/float(USD)}')
    else:
        bot.send_message(user_id, 'Пишите только цифры!')
        bot.register_next_step_handler(message, usd)

def eur(message):
    user_id = message.from_user.id
    if message.text.isnumeric():
        bot.send_message(user_id, f'{int(message.text)/float(EUR)}')
    else:
        bot.send_message(user_id, 'Пишите только цифры!')
        bot.register_next_step_handler(message, eur)

def rub(message):
    user_id = message.from_user.id
    if message.text.isnumeric():
        bot.send_message(user_id, f'{int(message.text)/float(RUB)}')
    else:
        bot.send_message(user_id, 'Пишите только цифры!')
        bot.register_next_step_handler(message, rub)


bot.polling()
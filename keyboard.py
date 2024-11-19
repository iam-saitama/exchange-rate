from telebot import types

def menu():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    usd = types.KeyboardButton('$')
    eur = types.KeyboardButton('€')
    kb.add(usd, eur)

    return kb
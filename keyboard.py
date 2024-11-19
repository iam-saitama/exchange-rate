from telebot import types

def menu():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    usd = types.KeyboardButton('$')
    eur = types.KeyboardButton('€')
    rub = types.KeyboardButton('₽')
    kb.add(usd, eur, rub)

    return kb
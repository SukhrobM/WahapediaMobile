from telebot import types


def faction_choice():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    imperium = types.KeyboardButton('Imperium')
    chaos = types.KeyboardButton('Chaos')
    xenos = types.KeyboardButton('Xenos')
    unaligned = types.KeyboardButton('Unaligned')
    kb.add(imperium, chaos, xenos, unaligned)
    return kb

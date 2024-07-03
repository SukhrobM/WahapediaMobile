from telebot import types


def chaos_choise():
    traitors = types.ReplyKeyboardMarkup(resize_keyboard=True)
    demons = types.KeyboardButton('Chaos Daemons')
    cool_robots = types.KeyboardButton('Chaos Knights')
    cool_marines = types.KeyboardButton('Chaos Space Marines')
    chads = types.KeyboardButton('Death Guard')
    nerds = types.KeyboardButton('Thousand Sons')
    jogs = types.KeyboardButton('World Eaters')
    traitors.add(demons, cool_robots, cool_marines, chads, nerds, jogs)
    return traitors

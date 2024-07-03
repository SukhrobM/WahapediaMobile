from telebot import types


def imperium_choice():
    filty_loyalist = types.ReplyKeyboardMarkup(resize_keyboard=True)
    hot_nuns = types.KeyboardButton('Adepta Sororitas')
    golden_boys = types.KeyboardButton('Adeptus Custodes')
    gear_heads = types.KeyboardButton('Adeptus Mechanicus')
    walking_buildings = types.KeyboardButton('Adeptus Titanicus')
    cannon_fodder = types.KeyboardButton('Astra Militarum')
    fan_club = types.KeyboardButton('Grey Knights')
    lame_robots = types.KeyboardButton('Imperial Knights')
    posterboys = types.KeyboardButton('Space Marines')
    filty_loyalist.add(hot_nuns, golden_boys, gear_heads, walking_buildings, cannon_fodder,
                       fan_club, lame_robots, posterboys)
    return filty_loyalist
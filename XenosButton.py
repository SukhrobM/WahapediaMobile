from telebot import types


def xeno_choise():
    xenos_scumm = types.ReplyKeyboardMarkup(resize_keyboard=True)
    elfs = types.KeyboardButton('Aeldari')
    fking_elfs = types.KeyboardButton('Drukhari')
    citizen = types.KeyboardButton('Genestealer Cults')
    dwarfs = types.KeyboardButton('Leagues of Votann')
    can_heads = types.KeyboardButton('Necrons')
    gitz = types.KeyboardButton('Orks')
    commies = types.KeyboardButton("T'au Empire")
    omnom = types.KeyboardButton('Tyranids')
    xenos_scumm.add(elfs, fking_elfs, citizen, dwarfs, can_heads, gitz, commies, omnom)
    return xenos_scumm

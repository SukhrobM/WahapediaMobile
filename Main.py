import requests

import telebot

import FactionButton

import ImperiumButton

import ChaosButton

import XenosButton

bot = telebot.TeleBot('6789758225:AAE8bomEaEVUwXG_1PIIxaex5Qnkk8UGEss')


@bot.message_handler(commands=['start'])
def title_message(message):
    user_id = message.from_user.id
    bot.send_message(user_id, 'Choose your faction',
                     reply_markup=FactionButton.faction_choice())


@bot.message_handler(content_types=['text'])
def faction(message):
    chat_id = message.chat.id
    if message.text == 'Imperium':
        bot.send_message(chat_id, 'Choose your army', reply_markup=ImperiumButton.imperium_choice())
    elif message.text == 'Chaos':
        bot.send_message(chat_id, 'Choose your army', reply_markup=ChaosButton.chaos_choise())
        bot.register_next_step_handler(message, death_guard)
    elif message.text == 'Xenos':
        bot.send_message(chat_id, 'Choose your army', reply_markup=XenosButton.xeno_choise())
    elif message.text == 'Unaligned':
        bot.send_message(chat_id, 'Choose units')


def death_guard(message):
    chat_id = message.chat.id
    dg_page = requests.get('https://wahapedia.ru/wh40k10ed/factions/death-guard')
    if message.text == 'Death Guard':
        bot.send_message(chat_id, dg_page.text)


bot.polling(non_stop=True)

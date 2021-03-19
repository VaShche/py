"""
for TG bot
"""
import telebot
import os
from calc_test import script_executer
from threading import Thread

import settings
import asr_ya
token = settings.token
script = settings.script

bot = telebot.TeleBot(settings.token)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, '''Я умею считать выражения без скобок с операциями: + - * / ^
Просто напишите мне например:
5 + 6.4 / 2
Если я не пойму, я промолчу :)''')


@bot.message_handler(content_types=['text'])
def get_text_msg(msg):
    print(msg.from_user.username)
    bot.send_chat_action(msg.from_user.id, 'typing')

    res = ''.join(script_executer([msg.text])[0])
    print(res)
    if 'Result: ' in res:
        #bot.send_message(msg.from_user.id, '@{0}\n{1}\n{2}'.format(msg.from_user.username, msg.text, res))
        bot.reply_to(msg, res)
    else:
        pass


@bot.message_handler(content_types=['voice'])
def get_voice_message(msg):
    print(msg.from_user.username)
    bot.send_chat_action(msg.from_user.id, 'typing')

    f_info = bot.get_file(msg.voice.file_id)
    content = bot.download_file(f_info.file_path)

    try:
        asr_res = asr_ya.getAsrRes(content)
        print('Voice: {}'.format(asr_res))
        asr_res = asr_ya.asrPostProc(asr_res)
        print('PostP: {}'.format(asr_res))
        res = ''.join(script_executer([asr_res])[0])
        if 'Result: ' not in res:
            res = '🙀'
        bot.reply_to(msg, '{0}\n{1}'.format(asr_res, res))
    except:
        bot.reply_to(msg, '😿')

while True:
    try:
        bot.polling(none_stop=True)
    finally:
        print('zzz')

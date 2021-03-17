"""
for TG bot
"""
import settings
import telebot
from calc_test import script_executer
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
    if True:
        #print(msg)
        print(msg.from_user.username)
        bot.send_chat_action(msg.from_user.id, 'typing')
        res = ''.join(script_executer([msg.text])[0])
        print(res)
        if 'Result: ' in res:
            #bot.send_message(msg.from_user.id, '@{0}\n{1}\n{2}'.format(msg.from_user.username, msg.text, res))
            bot.reply_to(msg, res)
        else:
            pass

bot.polling(none_stop=True)

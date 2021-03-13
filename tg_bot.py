"""
for TG bot
"""
import settings
import telebot
from calc_test import script_executer
token = settings.token
script = settings.script

bot = telebot.TeleBot(settings.token)

@bot.message_handler(content_types=['text'])
def get_text_msg(msg):
    if True:
        print(msg.text)
        res = ''.join(script_executer([msg.text])[0])
        bot.send_message(msg.from_user.id, res)

bot.polling(none_stop=True)

import telebot

TOKEN = ''
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['hello'])
def say_hello(message):
    bot.send_message(message.chat.id, text='Привет, хорошего дня')

@bot.message_handler(content_types=['text'])
def handle_message(message):
    bot.send_message(message.chat.id, text='Hello')
    bot.send_message(message.chat.id, text='Я 123')
    bot.send_message(message.chat.id, text='Я могу отправлять приветы')
    bot.send_message(message.chat.id, text='Мои команды: /hello, /start')
    txt = message.text
    #if txt.isdigit():
    #    bot.send_message(message.chat.id, text='Вы отправили число')
    #else:
    #    bot.send_message(message.chat.id, text='Вы отправили что то другое')

print('OK')
bot.polling(
    none_stop=True,
    interval=1
)
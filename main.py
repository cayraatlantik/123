import telebot

TOKEN = '7153742355:AAF_BCTGywwK3DMYkUditKA1actDYxRhHX0'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def say_hello(message):
    txt = (
    'Привет, я бот калькулятор.' 
    'Могу решить любое выражение.'
    'Отправь его мне и я найду ответ'
    )
    bot.send_message(message.chat.id, txt)


@bot.message_handler(content_types=['text'])
def handle_message(message):
    try:
        res = eval(message.text)
        bot.send_message(message.chat.id, text=f'Результат:{res}')
    except Exception as ex:
        bot.send_message(message.chat.id,f'Ошибка:{ex}')



print('OK')
bot.polling(
    none_stop=True,
    interval=1
)
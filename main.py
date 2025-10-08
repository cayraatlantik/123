import telebot
import random

TOKEN = ''
bot = telebot.TeleBot(TOKEN)
users_info = {}

class MyException(Exception):
    pass

@bot.message_handler(commands=['start'])

def say_hello(message):

    txt = (

    "Привет! Я загадал число от 1 до 100. "

    "Сможешь угадать максимум за 7 попыток? "

    "Для того, чтобы начать, отправь мне слово 'начать'"

)
    bot.send_message(message.chat.id, txt)


@bot.message_handler(content_types=['text'])
def handle_message(message):
    user_id = message.chat.id
    txt = message.text.strip().lower()
    if txt == 'начать':
        n = random.randint(1, 100)
        users_info[user_id] = {
            'number': n,
            'tries':0
        }
        bot.send_message(message.chat.id, text='Я загадал число, можешь начинать!')
    else:
        try:
            n = int(txt)
            if user_id not in users_info:
                raise MyException('Вы еще не начали игру')
            if not 1 <= n <= 100:
                raise MyException('Введите число из диапозона от 1 до 100')
            users_info[user_id]['tries'] +=1
            x = users_info[user_id]['number']
            if n == x:
                k = users_info(user_id)['tries']
                bot.send_message(user_id,text=f'Вы угадали!! кол-во попыток {k}')
                del users_info[user_id]
            elif n > x:
                bot.send_message(user_id, f'Загаданное число меньше')
            else:
                bot.send_message(user_id, f'Загаданное число больше')
        except ValueError:
            bot.send_message(message.chat.id, text='Из всех слов я понимаю только начать')
        except  MyException as me:
            bot.send_message(user_id, me)
#def say_hello(message):
    #bot.send_message(message.chat.id, text='Привет, хорошего дня')

#@bot.message_handler(content_types=['text'])
#def handle_message(message):
    #bot.send_message(message.chat.id, text='Hello')
    #bot.send_message(message.chat.id, text='Я 123')
    #bot.send_message(message.chat.id, text='Я могу отправлять приветы')
    #bot.send_message(message.chat.id, text='Мои команды: /hello, /start')
    #txt = message.text
    #if txt.isdigit():
    #    bot.send_message(message.chat.id, text='Вы отправили число')
    #else:
    #    bot.send_message(message.chat.id, text='Вы отправили что то другое')

print('OK')
bot.polling(
    none_stop=True,
    interval=1
)

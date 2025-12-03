import telebot
from for_db import *

TOKEN = ''
bot = telebot.TeleBot(TOKEN)

# #button_3 = telebot.types.KeyboardButton('Подсчет общего расхода по категориям')
#keyboard.add(button_3)

@bot.message_handler(commands=['start'])
def say_hello(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    button_1 = telebot.types.InlineKeyboardButton(
        'Добавить расход', callback_data='dobavit'
    )
    button_2 = telebot.types.InlineKeyboardButton(
        'Просмотр всех раcходов', callback_data='prosmotr'
    )
    keyboard.add(button_1)
    keyboard.add(button_2)
    bot.send_message(message.chat.id, 'Привет! Я бот, который поможет тебе с подсчетами расходов\n' \
    'Я помогу тебе с общим расходом по категориям и просмотром всех расходов за определенный период', 
    reply_markup=keyboard)

@bot.callback_query_handler(func=lambda callback: True)
def handle_callback(callback):
     if callback.data == 'dobavit':
          
          

print('OK')

bot.polling(
    none_stop=True,
    interval=1
)


DDDBBBB


import sqlite3


def create():
    connection = sqlite3.connect("expenses.db")
    cursor_object = connection.execute("""
        CREATE TABLE IF NOT EXISTS katalog(
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        amount FLOAT ,
        category TEXT,
        date TEXT
                )
        """
        )
    connection.close()

def insert(data):
    connection = sqlite3.connect("expenses.db")
    cursor_object = connection.execute(
    """
        INSERT INTO katalog(
        )

        """)
    
    connection.close()



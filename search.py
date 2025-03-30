import os
from colorama import init, Fore
import time
import socket
import requests
import pystyle
from terminaltables import SingleTable
from pystyle import Colors, Box, Write, Center, Colorate

banner = """

                                                       

            ██╗░░░██╗███████╗███╗░░██╗░█████╗░███╗░░░███╗             базы кидать в папку Base
            ██║░░░██║██╔════╝████╗░██║██╔══██╗████╗░████║
            ╚██╗░██╔╝█████╗░░██╔██╗██║██║░░██║██╔████╔██║             By Poison 
            ░╚████╔╝░██╔══╝░░██║╚████║██║░░██║██║╚██╔╝██║
            ░░╚██╔╝░░███████╗██║░╚███║╚█████╔╝██║░╚═╝░██║
            ░░░╚═╝░░░╚══════╝╚═╝░░╚══╝░╚════╝░╚═╝░░░░░╚═╝
            
                        Найдется всё!

"""
Write.Print(Center.XCenter(banner), Colors.white,interval=0.001)



init(autoreset=True)
if not os.path.exists('base'):
    print(Fore.RED + "Директория 'base' не существует. Пожалуйста, создайте её и добавьте файлы для поиска.")
else:
    count = len(os.listdir('base'))
    print(Fore.WHITE + f"Обнаружено {count} баз.\n")
    data = input(Fore.WHITE + 'Введите данные для поиска: ')
    print(Fore.WHITE + '\nПроизводится поиск...\n')

    result = ''
    for label in os.listdir('base'):
        file_path = os.path.join('base', label)
        try:
            with open(file_path, 'r', encoding='UTF-8') as f:
                for line in f:
                    if data in line:
                        result += f"[{label}] - {line}".replace('.', '').replace('[', '').replace(']', '').replace('"',
                                                                                                                   '').replace(
                            'NULL', '')
                        break
        except Exception as e:
            print(Fore.RED + f"Ошибка при чтении файла {label}: {e}")


    print(Fore.WHITE +'Поиск завершён!')
    if result:
        print(Fore.WHITE + '\nРезультаты поиска:\n')
        print(result)
    else:
        print(Fore.WHITE + "Совпадений не найдено.")

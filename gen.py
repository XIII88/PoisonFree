import os
import subprocess
import sys
import random
import pystyle
from pystyle import *

def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')
        sys.stdout.write("\x1b[8;40;140t")

def generate_random_numbers(start, end, count):
    result = [random.randint(start, end) for _ in range(count)]
    return result


pystyle.Write.Print(pystyle.Center.XCenter('''

       ██╗░░░██╗███████╗███╗░░██╗░█████╗░███╗░░░███╗
       ██║░░░██║██╔════╝████╗░██║██╔══██╗████╗░████║
       ╚██╗░██╔╝█████╗░░██╔██╗██║██║░░██║██╔████╔██║
       ░╚████╔╝░██╔══╝░░██║╚████║██║░░██║██║╚██╔╝██║
       ░░╚██╔╝░░███████╗██║░╚███║╚█████╔╝██║░╚═╝░██║
       ░░░╚═╝░░░╚══════╝╚═╝░░╚══╝░╚════╝░╚═╝░░░░░╚═╝
                            
'''), pystyle.Colors.red_to_white, interval = 0.0005)

start_number = int(pystyle.Write.Input(f'\n                    Введите начальное число >> ', color=pystyle.Colors.red_to_white))

end_number = int(pystyle.Write.Input(f'                    Введите конечное число >> ', color=pystyle.Colors.red_to_white))

while start_number > end_number:
    pystyle.Write.Print(f'                    Ошибка: Начальное число больше конечного. Пожалуйста, повторите ввод.', pystyle.Colors.red_to_white, interval = 0.0005)
    start_number = int(pystyle.Write.Input(f'                    Введите начальное число >> ', color=pystyle.Colors.red_to_white))
    end_number = int(pystyle.Write.Input(f'                    Введите конечное число >> ', color=pystyle.Colors.red_to_white))


result_count = int(pystyle.Write.Input(f'                    Введите количество результатов >> ', color=pystyle.Colors.red_to_white))

random_numbers = generate_random_numbers(start_number, end_number, result_count)

pystyle.Write.Print(f"                   Случайные числа от {start_number} до {end_number}\n                   {random_numbers}", pystyle.Colors.red_to_white, interval = 0.0005)
pystyle.Write.Input(f'\n                   Нажмите Enter, чтобы вернуться в меню', color=pystyle.Colors.red_to_white)
clear()
subprocess.run(['python', os.path.join(os.path.dirname(__file__), 'venom.py')])

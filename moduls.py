import os
import subprocess
import sys

def install_requirements():
    """Устанавливает все необходимые модули."""
    required_modules = [
        "colorama",
        "requests",
        "bs4",      
        "phonenumbers", 
        "whois",    
        "pyfiglet",  
        "faker",   
        "pystyle",
        "time",
        "subprocess",
        "os",
        "sys",
        "pytube",
        "random",
    ]

    print("[~] Установка необходимых модулей...")
    for module in required_modules:
        try:
            __import__(module)
            print(f"[+] Модуль {module} уже установлен.")
        except ImportError:
            print(f"[~] Установка модуля {module}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", module])
            print(f"[+] Модуль {module} успешно установлен.")
            input()

install_requirements()
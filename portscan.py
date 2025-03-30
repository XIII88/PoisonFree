import socket
from concurrent.futures import ThreadPoolExecutor, as_completed
import colorama

open_ports = []
failed_ports = []

# Инициализируем colorama для поддержки цветного вывода в консоль
colorama.init()

# Задаем цвета для вывода
COLOR_CODE = {
    "GREEN": colorama.Fore.GREEN,
    "RED": colorama.Fore.RED,
    "BLUE": colorama.Fore.BLUE,
    "RESET": colorama.Fore.RESET
}


def port_scan(ip_address, port_range):
    class PortScanner:
        def __init__(self, ip, port_range):
            self.ip = ip
            self.port_range = port_range

        def scan(self):
            with ThreadPoolExecutor(max_workers=50) as executor:
                futures = {executor.submit(self.scan_port, port): port for port in range(1, self.port_range + 1)}
                for future in as_completed(futures):
                    result = future.result()
                    if result is not None:
                        open_ports.append(result)

        def scan_port(self, port):
            try:
                with socket.socket() as sock:
                    sock.settimeout(0.5)
                    sock.connect((self.ip, port))
                    return port
            except (socket.timeout, ConnectionRefusedError, socket.error):
                failed_ports.append(port)
                return None

    scanner = PortScanner(ip_address, port_range)
    scanner.scan()

    print("Открытые порты:")
    for port in open_ports:
        print(f'{COLOR_CODE["GREEN"]}Порт {port} открыт{COLOR_CODE["RESET"]}')

    print(f'{COLOR_CODE["RED"]}Неудачные порты:{COLOR_CODE["RESET"]}')
    for port in failed_ports:
        print(f"Порт {port} закрыт")

    input(f'{COLOR_CODE["GREEN"]}Нажмите Enter для продолжения...{COLOR_CODE["RESET"]}')
    import main


if __name__ == "__main__":
    ip_address = input(f'{COLOR_CODE["GREEN"]}Введите IP-адрес для сканирования: {COLOR_CODE["RESET"]}')
    port_range = int(input(f'{COLOR_CODE["GREEN"]}Введите диапазон портов для сканирования: {COLOR_CODE["RESET"]}'))

    port_scan(ip_address, port_range)

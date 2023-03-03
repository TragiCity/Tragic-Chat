import socket
import time
import os.path
import os
import colorama
from colorama import Fore
from loguru import logger
import configparser
from cryptography.fernet import Fernet

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def banner():
        print(Fore.LIGHTMAGENTA_EX + r"""
 _________  ________  ________  ________  ___  ________          ________  ___  ___  ________  _________   
|\___   ___\\   __  \|\   __  \|\   ____\|\  \|\   ____\        |\   ____\|\  \|\  \|\   __  \|\___   ___\ 
\|___ \  \_\ \  \|\  \ \  \|\  \ \  \___|\ \  \ \  \___|        \ \  \___|\ \  \\\  \ \  \|\  \|___ \  \_| 
     \ \  \ \ \   _  _\ \   __  \ \  \  __\ \  \ \  \            \ \  \    \ \   __  \ \   __  \   \ \  \  
      \ \  \ \ \  \\  \\ \  \ \  \ \  \|\  \ \  \ \  \____        \ \  \____\ \  \ \  \ \  \ \  \   \ \  \ 
       \ \__\ \ \__\\ _\\ \__\ \__\ \_______\ \__\ \___ ____\      \ \_______\ \__\ \__\ \__\ \__\   \ \__\
        \|__|  \|__|\|__|\|__|\|__|\|_______|\|__|\|_______|        \|_______|\|__|\|__|\|__|\|__|    \|__|   
    """)
        print(Fore.LIGHTMAGENTA_EX + "[GITHUB]" + Fore.LIGHTBLACK_EX + " https://github.com/TragiCity")
        print(Fore.LIGHTMAGENTA_EX + "[DISCORD]" + Fore.LIGHTBLACK_EX + " 𝐓𝐫𝐚𝐠𝐢𝐜 𝐂𝐢𝐭𝐲#0001")
        
def return_data():
    return input(Fore.LIGHTBLACK_EX + '[' + Fore.LIGHTMAGENTA_EX + 'Tragic' + Fore.LIGHTBLUE_EX + 'Chat' + Fore.LIGHTBLACK_EX + ']' + " >>> ")
    
def choice_create(title: str, choice_list):
    print(Fore.LIGHTBLACK_EX + '[' + Fore.LIGHTMAGENTA_EX + 'Tragic' + Fore.LIGHTBLUE_EX + 'Chat' + Fore.LIGHTBLACK_EX + ']' + ' {0}'.format(title))
    for choice in choice_list:
        print(Fore.LIGHTMAGENTA_EX + '[{0}] - '.format(choice_list.index(str(choice))) + Fore.LIGHTBLACK_EX + str(choice))

def generate_key():
    key = Fernet.generate_key()
    with open('crypto.key', 'wb') as key_file:
        key_file.write(key)

def load_key():
    return open('crypto.key', 'rb').read()

def config_create():
    clear()
    banner()
    logger.info('Создание конфигурации')
    logger.info('Настройка раздела CLIENT..')
    logger.info('Введите IP сервера для подключения (default: 127.0.0.1) :')
    client_server_ip = return_data()
    if len(client_server_ip) == 0:
        client_server_ip = '127.0.0.1'

    logger.info('Введите PORT сервера для подключения (default: 8080) :')
    client_server_port = return_data()
    if len(str(client_server_port)) == 0:
        client_server_port = 8080

    logger.info('Введите размер буфера для сообщений между CLIENT-SERVER (default: 16000) :')
    client_buffer_size = return_data()
    if len(str(client_buffer_size)) == 0:
        client_buffer_size = 16000

    clear()
    banner()

    logger.info('Настройка раздела SERVER..')
    logger.info('Введите IP сервера (default: 127.0.0.1) :')
    server_ip = return_data()
    if len(server_ip) == 0:
        server_ip = '127.0.0.1'

    logger.info('Введите PORT сервера (default: 8080) :')
    server_port = return_data()
    if len(str(server_port)) == 0:
        server_port = 8080

    logger.info('Введите время ожидания подключения клиента к серверу (default: 100) :')
    server_timeout = return_data()
    if len(str(server_timeout)) == 0:
        server_timeout = 100

    logger.info('Введите размер буфера для сообщений между SERVER-CLIENT (default: 16000) :')
    server_buffer_size = return_data()
    if len(str(server_buffer_size)) == 0:
        server_buffer_size = 16000
    
    logger.info('Настройка файла CRYPTO..')
    choice_create('Инициализация ключа', ['Создать', 'У меня есть файл'])
    crypto_key = return_data()
    if int(crypto_key) == 0:
        generate_key()
    elif int(crypto_key) == 1:
        pass

    clear()
    banner()
    logger.info('Создание конфигурации...')
    config = configparser.ConfigParser()
    config['CLIENT'] = {'ip': client_server_ip, 'port': client_server_port, 'buffer_size': client_buffer_size}
    config['SERVER'] = {'ip': server_ip, 'port': server_port, 'timeout': server_timeout, 'buffer_size': server_buffer_size}
    with open('config.ini', 'w') as configfile:
        config.write(configfile)
    logger.info('Конфигурация создана, перезапуск...')
    time.sleep(3)
    inizialize()


def inizialize():
    colorama.init()
    
    clear()
    banner()
    if not os.path.exists('config.ini'):
        logger.error('Не удалось загрузить файл - config.ini')
        time.sleep(3)
        config_create()
    else:
        config = configparser.ConfigParser()
        config.read('config.ini')

        logger.info('Загружен - config.ini')

    if not os.path.exists('crypto.key'):
        logger.error('Не удалось загрузить файл - crypto.key')
        time.sleep(3)
        config_create()
    else:
        logger.info('Загружен - crypto.key')


    choice_create("Выберите вариант запуска: ",['Клиент (cryptography)', 'Сервер (cryptography)', 'Клиент (без cryptography)', 'Сервер (без cryptography)', 'Выход'])

    while True:
        response = int(return_data())
        if response == 0:
            client(config)
            break
        elif response == 1:
            server(config)
            break
        elif response == 2:
            client_nocrypt(config)
        elif response == 3:
            server_nocrypt(config)
        elif response == 4:
            logger.info('Хорошего дня :3')
            exit()

def server(config):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (config['SERVER']['ip'], int(config['SERVER']['port']))

    logger.info('Запуск сервера. | IP: {0} | PORT: {1}'.format(config['SERVER']['ip'], config['SERVER']['port']))
    sock.bind(server_address)
    logger.info('Количество соединений: ')
    connect = int(return_data())

    sock.listen(connect)

    clear()
    banner()

    logger.info('Запуск сервера. | IP: {0} | PORT: {1}'.format(config['SERVER']['ip'], config['SERVER']['port']))
    logger.info('Количество соединений задано: {0}'. format(str(connect)))

    while True:
        logger.info('Режим ожидания соединения')
        sock.settimeout(int(config['SERVER']['timeout']))
        try:
            connection, client_address = sock.accept()
            logger.warning('Подключен: {0}'.format(client_address))
            while True:
                data = connection.recv(int(config['SERVER']['buffer_size']))
                mess = data.decode()
                cryptkey = Fernet(load_key())
                decryptmessage = cryptkey.decrypt(mess)
                print(Fore.BLUE +  f'CLIENT' + Fore.LIGHTBLACK_EX + ' > ' + decryptmessage.decode('utf-8').replace("b", "").replace("'", ""))
                if data:
                    mess = str(return_data())
                    mess = bytes(mess, encoding='utf8')
                    cryptkey = Fernet(load_key())
                    cryptmessage = cryptkey.encrypt(mess)
                    connection.sendall(cryptmessage)
                else:
                    break

        finally:
            connection.close()

def client(config):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = (config['CLIENT']['ip'], int(config['CLIENT']['port']))
    sock.connect(server_address)
    logger.warning('Подключено | IP: {0} | PORT: {1}'.format(config['CLIENT']['ip'], config['CLIENT']['port']))

    while True:
        mess = str(return_data())
        mess = bytes(mess, encoding='utf8')
        cryptkey = Fernet(load_key())
        cryptmessage = cryptkey.encrypt(mess)
        sock.sendall(cryptmessage)
        
        amount_received = 0
        amount_expected = len(cryptmessage)
        while amount_received < amount_expected:
            data = sock.recv(int(config['CLIENT']['buffer_size']))
            amount_received += len(data)
            mess = data.decode()
            cryptkey = Fernet(load_key())
            decryptmessage = cryptkey.decrypt(mess)
            print(Fore.BLUE + f"SERVER" + Fore.LIGHTBLACK_EX + " > " + decryptmessage.decode('utf-8').replace("b", "").replace("'", ""))
            break


def server_nocrypt(config):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (config['SERVER']['ip'], int(config['SERVER']['port']))

    logger.info('Запуск сервера. | IP: {0} | PORT: {1} | без cryptography'.format(config['SERVER']['ip'], config['SERVER']['port']))
    sock.bind(server_address)
    logger.info('Количество соединений: ')
    connect = int(return_data())

    sock.listen(connect)

    clear()
    banner()

    logger.info('Запуск сервера. | IP: {0} | PORT: {1}'.format(config['SERVER']['ip'], config['SERVER']['port']))
    logger.info('Количество соединений задано: {0}'. format(str(connect)))

    while True:
        logger.info('Режим ожидания соединения')
        sock.settimeout(int(config['SERVER']['timeout']))
        try:
            connection, client_address = sock.accept()
            logger.warning('Подключен: {0}'.format(client_address))
            while True:
                data = connection.recv(int(config['SERVER']['buffer_size']))
                mess = data.decode()
                print(Fore.BLUE +  f'CLIENT' + Fore.LIGHTBLACK_EX + ' > ' + mess)
                if data:
                    mess = str(return_data())
                    connection.sendall(mess.encode('utf8'))
                else:
                    break

        finally:
            connection.close()

def client_nocrypt(config):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = (config['CLIENT']['ip'], int(config['CLIENT']['port']))
    sock.connect(server_address)
    logger.warning('Подключено | IP: {0} | PORT: {1} | Без cryptography'.format(config['CLIENT']['ip'], config['CLIENT']['port']))

    while True:
        mess = str(return_data())
        sock.sendall(mess.encode('utf8'))
        
        amount_received = 0
        amount_expected = len(mess)
        while amount_received < amount_expected:
            data = sock.recv(int(config['CLIENT']['buffer_size']))
            amount_received += len(data)
            mess = data.decode('utf8')
            print(Fore.BLUE + f"SERVER" + Fore.LIGHTBLACK_EX + " > " + mess)
            break

if __name__ == '__main__':
    inizialize()
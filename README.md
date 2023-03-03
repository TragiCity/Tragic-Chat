# Tragic-Chat
Python чат с использованием криптографии в качестве защиты.

![изображение](https://user-images.githubusercontent.com/126518312/222764228-de4d664b-b699-49e2-a0ae-2970258e2cb7.png)
> Локальный тест передачи сообщений с использованием cryptography

# Особенности
- Поддержка режимов с cryptography и без
- Локальное и глобальное соединение
- Для общения с человеком на расстоянии с использовании cryptography вы должны иметь одинкаовый файл crypto.key

# Стандартные настройки config.ini
```ini
[CLIENT]
ip = 127.0.0.1
port = 8080
buffer_size = 16000

[SERVER]
ip = 127.0.0.1
port = 8080
timeout = 100
buffer_size = 16000
```

# Установка для Windows
- Запустить файл Tragic City.exe

# Установка для Linux
```sh

git clone https://github.com/TragiCity/Tragic-Chat
cd Tragic-Chat
python3.10 Tragic Chat.py
```

# Сборка файла с использованием pyinstaller
```sh
git clone https://github.com/TragiCity/Tragic-Chat
cd Tragic-Chat
pyinstaller --onefile --console --icon=icon.ico "Tragic Chat.py"
```

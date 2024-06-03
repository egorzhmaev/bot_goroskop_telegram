# Телеграм-бот

## Описание

Бот-гороскоп. Показывает актуальный гороскоп на сегодня.

Принцип работы бота:
- Бот обращается к сервису Гороскоп mail.ru , парсит страницу по указанному знаку зодиака и возвращает гороскоп.

#### Технологии

- Python 3.9
- aiogram
- asynco
- BeautifulSoup

#### Запуск проекта

- Склонируйте репозиторий:  
``` git clone <название репозитория> ``` 
- Заполнить переменную main.py   
``` BOT_TOKEN = токен_Вашего_Telegtam_бота ```  
- Установите и активируйте виртуальное окружение:  
``` python -m venv venv ```  
``` source venv/Scripts/activate ``` 
- Установите зависимости из файла requirements.txt:   
``` pip install -r requirements.txt ```


![pic](https://github.com/egorzhmaev/bot_goroskop_telegram/blob/master/photo_2024-03-03_15-20-09.jpg)

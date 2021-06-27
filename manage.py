#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import locale
import os
import sqlite3
import sys
from datetime import datetime

import telebot

locale.setlocale(
    category=locale.LC_ALL,
    locale="Uz"
)


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'atsite.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

TOKEN = '1795627820:AAGqhDfebUuQUhUpJxrvmruutkW1cRBN0PI'
CHAT_ID = '-568473273'

bot = telebot.TeleBot(TOKEN, parse_mode='html')


def read_sqlite_table():
    try:
        sqlite_connection = sqlite3.connect('db.sqlite3')
        cursor = sqlite_connection.cursor()
        sqlite_select_query = """SELECT * from atapp_news"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        title = records[len(records) - 1][1]
        content = records[len(records) - 1][2]
        created_at = datetime.strptime(records[len(records) - 1][3], '%Y-%m-%d %H:%M:%S.%f').strftime(
            f'%d.%m.%Y | %A | %H:%M')
        # src = f"D:/Personal/Programm/Python/diplom.v3/atsite/media/{records[len(records) - 1][6]}".replace('/', '\\')
        # photo = open(src, 'rb')
        bot.send_message(CHAT_ID, '<b>{title}</b>.\n\n'
                                  f'{content}\n\n'
                                  f'{os.path.abspath("db.sqlite3")}')
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


def watch_file_update(path):
    timestamp = os.stat(path).st_mtime
    print(timestamp)
    while 1:
        if timestamp != os.stat(path).st_mtime:
            timestamp = os.stat(path).st_mtime
            print('Файл изменён!')

            return read_sqlite_table()


while 1:
    watch_file_update(os.path.abspath('db.sqlite3'))

import threading
from mails_search import gmail_parse
from config import Keys
from telegram import Bot
from time import sleep
from telegram.utils.request import Request
from telegram.ext import Updater


CHAT_ID = Keys.CHAT_ID_LOAD  # chat_id для line 17
TOKEN = Keys.TOKEN_LOAD  # Токен для бота
URL = Keys.URL_LOAD  # Проксирующий URL


# функция, опрашивающая функцию real_gmail
def gmail_checking():
    while True:
        mails = gmail_parse()
        if mails:
            for mail in mails:
                Bot.send_message(chat_id=CHAT_ID, text="Вам пришло новое сообщение!")
        sleep(0.1)


t = threading.Thread(target=gmail_checking, args=())  # Запуск функции в отдельном потоке
t.start()


# Скелет бота
def main():
    req = Request(
        connect_timeout=0.5,
    )

    bot = Bot(
        request=req,
        token=TOKEN,
        base_url=URL,
    )

    updater = Updater(
        bot=bot,
        use_context=True,
    )

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
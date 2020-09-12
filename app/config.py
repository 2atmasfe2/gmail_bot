import os
from dotenv import load_dotenv

load_dotenv()


class Keys:
    EMAIL_LOGIN = os.getenv("LOGIN")
    EMAIL_PASSWORD = os.getenv("PASSWORD")
    EMAIL_SERVER = os.getenv("SERVER")
    CHAT_ID_LOAD = os.getenv("CHAT_ID")
    TOKEN_LOAD = os.getenv("TOKEN")
    URL_LOAD = os.getenv("URL")
    HOST = os.getenv("HOST")
    PORT = os.getenv("PORT")

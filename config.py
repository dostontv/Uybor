import os

from dotenv import load_dotenv

load_dotenv('.env')

class DB:
    NAME = os.getenv('PS_NAME')
    USER = os.getenv('PS_USER')
    PASSWORD = os.getenv('PS_PASSWORD')
    HOST = os.getenv('PS_HOST')
    PORT = int(os.getenv('PS_PORT'))

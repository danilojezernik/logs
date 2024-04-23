import os

from dotenv import load_dotenv

load_dotenv()
PORT = int(os.getenv('PORT'))
DOMAIN = str(os.getenv('DOMAIN'))
DB_PROCES = str(os.getenv('DB_PROCES'))
DB_CONNECTION_LOGGING = str(os.getenv('DB_CONNECTION_LOGGING'))

DB_USER = str(os.getenv('DB_USER'))
SECRET_KEY = str(os.getenv('SECRET_KEY'))
ALGORITHM = str(os.getenv('ALGORITHM'))

print('lalalalala')

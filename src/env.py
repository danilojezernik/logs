import os

from dotenv import load_dotenv

load_dotenv()
PORT = int(os.getenv('PORT'))
DOMAIN = str(os.getenv('DOMAIN'))
DB_PROCES = str(os.getenv('DB_PROCES'))
DB_PROCESS = str(os.getenv('DB_PROCESS'))
DB_CONNECTION_LOGGING = str(os.getenv('DB_CONNECTION_LOGGING'))
DB_CONNECTION_LOGGING_PDJ = str(os.getenv('DB_CONNECTION_LOGGING_PDJ'))

DB_USER = str(os.getenv('DB_USER'))
SECRET_KEY = str(os.getenv('SECRET_KEY'))
ALGORITHM = str(os.getenv('ALGORITHM'))

print('lalalalala')

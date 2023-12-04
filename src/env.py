import os

from dotenv import load_dotenv

load_dotenv()
PORT = int(os.getenv('PORT'))
DOMAIN = str(os.getenv('DOMAIN'))
DB_PROCES_PRIVATE_HSA_LOGGING = str(os.getenv('DB_PROCES_PRIVATE_HSA_LOGGING'))
DB_PROCES_PUBLIC_HSA_LOGGING = str(os.getenv('DB_PROCES_PUBLIC_HSA_LOGGING'))
DB_CONNECTION_LOGGING = str(os.getenv('DB_CONNECTION_LOGGING'))

DB_USER = str(os.getenv('DB_USER'))
SECRET_KEY = str(os.getenv('SECRET_KEY'))
ALGORITHM = str(os.getenv('ALGORITHM'))

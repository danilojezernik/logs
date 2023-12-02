import os

from dotenv import load_dotenv

load_dotenv()
PORT = int(os.getenv('PORT'))
DOMAIN = str(os.getenv('DOMAIN'))
DB_PROCES_LOGGING = str(os.getenv('DB_PROCES_LOGGING'))
DB_CONNECTION_LOGGING = str(os.getenv('DB_CONNECTION_LOGGING'))
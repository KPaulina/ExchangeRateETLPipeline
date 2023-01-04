import os
import dotenv
from datetime import datetime


dotenv.load_dotenv()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))[:-3]
DATA_DIR = os.path.join(BASE_DIR, 'data')

DATE = str(datetime.now())[:10]


DB_NAME = os.environ.get('POSTGRES_DB')
DB_USER = os.environ.get('POSTGRES_USER')
DB_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
DB_HOST = os.environ.get('POSTGRES_HOST')
DB_PORT = os.environ.get('POSTGRES_PORT')

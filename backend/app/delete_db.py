import os
from dotenv import load_dotenv
from .utils import delete_db

load_dotenv()
db_path = str(os.getenv('DATABASE_NAME'))

delete_db(db_path)
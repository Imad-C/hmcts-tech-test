import os
from dotenv import load_dotenv

load_dotenv()
db_path = str(os.getenv('DATABASE_NAME'))

if os.path.exists(db_path):
    os.remove(db_path)
    print(f"{db_path} has been deleted.")
else:
    print(f"{db_path} does not exist.")
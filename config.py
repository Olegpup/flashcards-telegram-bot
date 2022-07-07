import os
from dotenv import load_dotenv

load_dotenv(os.getcwd() + "/.env")
BOT_TOKEN = str(os.getenv("BOT_TOKEN"))
CONNECT_STR_MONGO = str(os.getenv("CONNECT_STR_MONGO"))

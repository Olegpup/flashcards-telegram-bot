import os
from dotenv import load_dotenv

load_dotenv(".env")
BOT_TOKEN = str(os.getenv("BOT_TOKEN"))
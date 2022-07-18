import os
from dotenv import load_dotenv


load_dotenv(os.getcwd() + "/.env")


BOT_TOKEN = str(os.getenv("BOT_TOKEN"))
CONNECT_STR_MONGO = str(os.getenv("CONNECT_STR_MONGO"))

ADMINS = list(map(lambda x: int(x.strip()), os.getenv("ADMINS").split(",")))

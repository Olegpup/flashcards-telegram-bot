from aiogram import executor
from loader import dp
from handlers import *
from logging import basicConfig, INFO

basicConfig(level=INFO)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

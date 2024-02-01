from loader import dp
from aiogram import executor
import handlers, utils, keyboards, states, data
from utils.db_data import create_table


async def on_startup(dp):
    create_table()


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)

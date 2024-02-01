from aiogram import executor

from loader import dp
import handlers, utils, keyboards, states, data
from utils.db_data import create_table
from utils.misc.notify_admins import on_startup_notify
from utils.misc.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    create_table()
    await set_default_commands(dispatcher)
    await on_startup_notify(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
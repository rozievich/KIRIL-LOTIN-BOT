import logging
from aiogram import Bot

from data.config import ADMINS
from utils.db_data import Base, engine


async def on_startup_notify(bot: Bot):
    Base.metadata.create_all(engine)
    for admin in ADMINS:
        try:
            await bot.send_message(admin, "Bot ishga tushdi ♻")
        except Exception as err:
            logging.exception(err)

from aiogram import Dispatcher, Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from data.config import TOKEN

bot = Bot(TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot=bot, storage=MemoryStorage())

from aiogram.types import BotCommand


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            BotCommand(command='start', description="Ishga Tushirish ♻"), 
            BotCommand(command='info', description="Sizning ma'lumotlaringiz 🗂")
        ]
    )
from aiogram import types
from utils.db_data import get_user, register
from keyboards.reply_btn import main_btn


async def start_handler(msg: types.Message):
    if not get_user(str(msg.from_user.id)):
        register(str(msg.from_user.id), msg.from_user.username)
    await msg.answer(text=f'Assalomu alaykum {msg.from_user.first_name}\n<b>Kirill-Lotin</b> - botiga xush kelibsiz 😊\nBu bot orqali siz Kirillcha matnlarni Lotinga aksincha Lotincha matnlarni Kirilga o\'girish imkoniga ega bo\'lasiz 🗂\nShunchaki matn kiriting va natijani oling ♻️\n\nTalab va takliflar uchun: @rozievich', reply_markup=main_btn())


async def user_info_handler(msg: types.Message):
    await msg.answer(text=f"<b>Sizning Ma'lumotlaringiz 🗂</b>\n<b>ID:</b> {msg.from_user.id}\n<b>Ism:</b> {msg.from_user.first_name}\n<b>Username:</b> {msg.from_user.username}")


async def help_handler(msg: types.Message):
    await msg.answer("Yordam bo'limi")

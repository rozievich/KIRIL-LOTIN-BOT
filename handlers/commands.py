from aiogram import types

from utils.db_data import session, User

async def start_handler(msg: types.Message):
    user = session.query(User).filter(User.user_id == str(msg.from_user.id)).first()
    if not user:
        session.add(User(user_id=str(msg.from_user.id)))
        session.commit()
    await msg.answer(text=f'Assalomu alaykum {msg.from_user.first_name}\n<b>Kirill-Lotin</b> - botiga xush kelibsiz 😊\nBu bot orqali siz Kirillcha matnlarni Lotinga aksincha Lotincha matnlarni Kirilga o\'girish imkoniga ega bo\'lasiz 🗂\nShunchaki matn kiriting va natijani oling ♻️\n\nTalab va takliflar uchun: @rozievich')


async def user_info_handler(msg: types.Message):
    await msg.answer(text=f"<b>Sizning Ma'lumotlaringiz 🗂</b>\n<b>ID:</b> {msg.from_user.id}\n<b>Ism:</b> {msg.from_user.first_name}\n<b>Username:</b> {msg.from_user.username}")


async def help_handler(msg: types.Message):
    await msg.answer("Yordam bo'limi")

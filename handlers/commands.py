from aiogram import types, Bot
from utils.db_data import session, User


async def start_handler(msg: types.Message, bot: Bot):
    user = session.query(User).filter(User.user_id == str(msg.from_user.id)).first()
    if not user:
        session.add(User(user_id=str(msg.from_user.id)))
        session.commit()
    await bot.set_my_commands([types.BotCommand(command='start', description="Ishga Tushirish ♻"), types.BotCommand(command='help', description="Yordam olish 🛠"), types.BotCommand(command='info', description="Sizning ma'lumotlaringiz 🗂")])
    await msg.answer(text=f"Assalomu alaykum {msg.from_user.first_name}\n<b>KIRIL-LOTIN - Matn O'giruvchi Botga Xush Kelibsiz! 😊</b>\n\nBu bot yordamida siz o'z matnlaringizni istalgancha Kirill yoki Lotin yozuviga aylantira olasiz!\nFaqatgina matningizni kiriting va hoziroq o'girib olish imkoniyatiga ega bo'ling! 🗂\n\n<b>♻️ Bot imkoniyatlari:</b>\n— Kirill yozuvidagi matnlarni Lotinga o‘girish\n— Lotin yozuvidagi matnlarni Kirillga o‘girish\n\n<b>Taklif va fikrlaringiz uchun: @rozievich</b>")


async def help_handler(msg: types.Message):
    await msg.answer("<b>Botdan foydalanish bo‘yicha qo‘llanma 📝</b>\n\n— Kirill yoki Lotin yozuvida matn kiriting.\n— Bot matningizni avtomatik ravishda boshqa yozuvga o‘girib beradi.\n— Yana boshqa matnlar uchun qayta matn kiriting va zavq bilan foydalaning!\n\nSizning qulayligingiz uchun mo‘ljallangan bu bot har qanday vazifani oson va tez bajaradi!\n\n<b>📋 Sizning ma'lumotlaringiz /info:</b>\nBiz sizga Telegram ID, Username, Ism va Familiya taqdim etamiz ✍️\n\n<b>Fikr va takliflar uchun murojaat: @rozievich</b>")


async def user_info_handler(msg: types.Message):
    await msg.answer(text=f"🗂 Sizning ma'lumotingiz:\n\n<b>ID:</b> {msg.from_user.id}\n<b>Ism:</b> {msg.from_user.full_name}\n<b>Username:</b> {'@' + msg.from_user.username if msg.from_user.username else '❌'}\n\n💬 @kirlat_bot - Biz bilan hammasi oson!")

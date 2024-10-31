from aiogram import types, Bot
from aiogram.fsm.context import FSMContext

from keyboards.reply_btn import main_admin_btn, settings_admin_btn, exit_btn
from states.state import AdsState
from data.config import ADMINS
from utils.db_data import session, User
from utils.send_ads import send_adversment


async def admin_panel_handler(msg: types.Message):
    if msg.from_user.id in ADMINS:
        await msg.answer(text=f"Assalomu alaykum {msg.from_user.full_name} 🙃\nSizni boshqaruv panelida ko'rganimdan xursandman 🥳\n\n🤖 Qani tog'a endi nima qilamiz?", reply_markup=main_admin_btn)
    else:
        await msg.answer(text=f"Kechirasiz, {msg.from_user.full_name}\nSiz admin emasga o'xshaysiz 🙄", reply_markup=types.ReplyKeyboardRemove())


async def user_statistic_handler(msg: types.Message):
    if msg.from_user.id in ADMINS:

        await msg.answer(text=f"Admin uchun userlar hisoboti bo'ladi", reply_markup=main_admin_btn)
    else:
        await msg.answer(text=f"Kechirasiz, {msg.from_user.full_name}\nSiz admin emasga o'xshaysiz 🙄", reply_markup=types.ReplyKeyboardRemove())


async def ads_main_handler(msg: types.Message, state: FSMContext):
    if msg.from_user.id in ADMINS:
        await state.set_state(AdsState.ads)
        await msg.answer(text=f"Foydalanuvchilarga yuborish kerak bo'lgan xabarni yuboring ✍️", reply_markup=exit_btn)
    else:
        await msg.answer(text=f"Kechirasiz, {msg.from_user.full_name}\nSiz admin emasga o'xshaysiz 🙄", reply_markup=types.ReplyKeyboardRemove())

async def ads_send_handler(msg: types.Message, bot: Bot, state: FSMContext):
    if msg.text == "❌":
        await msg.answer(text="Foydalanuvchilarga xabar yuborish bekor qilindi 🔙", reply_markup=main_admin_btn)
        await state.clear()
    else:
        try:
            blocked_users = 0
            users = session.query(User).all()
            for user in users:
                blocked_users += await send_adversment(msg=msg, user_id=user.user_id)
            else:
                for admin in ADMINS:
                    await bot.send_message(chat_id=admin, text=f"<b>Botni bloklagan foydalanuvchilar soni:</b>  {blocked_users}")
        except Exception as e:
            await bot.send_message(chat_id=admin, text=f"{e}")


async def setting_btn_handler(msg: types.Message):
    if msg.from_user.id in ADMINS:
        await msg.answer(text="Sozlamalar Paneliga xush kelibsiz ✍️", reply_markup=settings_admin_btn)
    else:
        await msg.answer(text=f"Kechirasiz, {msg.from_user.full_name}\nSiz admin emasga o'xshaysiz 🙄", reply_markup=types.ReplyKeyboardRemove())


async def setting_channel_add_handler(msg: types.Message, state: FSMContext):
    if msg.from_user.id in ADMINS:
        await msg.answer(text=f" ✍️", reply_markup=exit_btn)
    else:
        await msg.answer(text=f"Kechirasiz, {msg.from_user.full_name}\nSiz admin emasga o'xshaysiz 🙄", reply_markup=types.ReplyKeyboardRemove())

from aiogram import types
from aiogram.fsm.context import FSMContext

from keyboards.reply_btn import main_admin_btn, settings_admin_btn, exit_btn
from states.state import AdsState
from data.config import ADMINS


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




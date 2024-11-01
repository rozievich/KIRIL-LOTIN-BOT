from aiogram import types, Bot
from aiogram.fsm.context import FSMContext

from keyboards.reply_btn import main_admin_btn, settings_admin_btn, exit_btn
from states.state import AdsState, ChannelAddState, ChannelDeleteState
from data.config import ADMINS
from utils.db_data import session, User, Channel
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
                    await bot.send_message(chat_id=admin, text=f"<b>Botni bloklagan foydalanuvchilar soni:</b>  {blocked_users}", reply_markup=main_admin_btn)
            await state.clear()
        except Exception as e:
            await bot.send_message(chat_id=admin, text=f"{e}")
            await state.clear()


async def setting_btn_handler(msg: types.Message):
    if msg.from_user.id in ADMINS:
        await msg.answer(text="Sozlamalar Paneliga xush kelibsiz ✍️", reply_markup=settings_admin_btn)
    else:
        await msg.answer(text=f"Kechirasiz, {msg.from_user.full_name}\nSiz admin emasga o'xshaysiz 🙄", reply_markup=types.ReplyKeyboardRemove())


async def setting_channel_add_handler(msg: types.Message, state: FSMContext):
    if msg.from_user.id in ADMINS:
        await state.set_state(ChannelAddState.url)
        await msg.answer(text=f"Qo'shish kerak bo'lgan kanal URL manzilini kiriting ✍️", reply_markup=exit_btn)
    else:
        await msg.answer(text=f"Kechirasiz, {msg.from_user.full_name}\nSiz admin emasga o'xshaysiz 🙄", reply_markup=types.ReplyKeyboardRemove())

async def channel_add_handler(msg: types.Message, state: FSMContext):
    if msg.text == "❌":
        await msg.answer(text="Kanal ulash bekor qilindi ⛓️‍💥", reply_markup=main_admin_btn)
        await state.clear()
    else:
        await state.update_data(channel_url=msg.text)
        await msg.answer("Qo'shish kerak bo'lgan kanal ID raqamini kiriting ⛓️", reply_markup=exit_btn)
        await state.set_state(ChannelAddState.channel_id)

async def channel_add_id_handler(msg: types.Message, state: FSMContext):
    if msg.text == "❌":
        await msg.answer(text="Kanal ulash bekor qilindi ⛓️‍💥", reply_markup=main_admin_btn)
        await state.clear()
    else:
        try:
            channel_info = await state.get_data()
            session.add(Channel(channel_url=channel_info['channel_url'], channel_id=str(msg.text)))
            session.commit()
            await msg.answer("Kanal muvaffaqiyatli ulandi 🌐", reply_markup=main_admin_btn)
        except:
            await msg.answer("Kanal ulashda muammo yuzaga keldi 🔕", reply_markup=main_admin_btn)
        await state.clear()


async def channel_delete_handler(msg: types.Message, state: FSMContext):
    if msg.from_user.id in ADMINS:
        await state.set_state(ChannelDeleteState.channel_id)
        await msg.answer(text=f"O'chirish kerak bo'lgan kanal ID raqamini kiriting ✍️", reply_markup=exit_btn)
    else:
        await msg.answer(text=f"Kechirasiz, {msg.from_user.full_name}\nSiz admin emasga o'xshaysiz 🙄", reply_markup=types.ReplyKeyboardRemove())

async def channel_delete_id_handler(msg: types.Message, state: FSMContext):
    if msg.text == "❌":
        await msg.answer(text="Kanal ulash bekor qilindi ⛓️‍💥", reply_markup=main_admin_btn)
        await state.clear()
    else:
        try:
            user_info = session.query(Channel).filter_by(channel_id=str(msg.text)).first()
            if user_info:
                session.delete(user_info)
                session.commit()
                await msg.answer(f"{msg.text} - ID raqamli kanal muvaffaqiyatli o'chirildi ✅", reply_markup=setting_btn_handler)
            else:
                await msg.answer("Bu ID raqam bilan hech qanday kanal topilmadi ⛓️", reply_markup=setting_btn_handler)
            await state.clear()
        except:
            await msg.answer("Kanal o'chirishda qandaydir muammo yuzaga keldi 🤔", reply_markup=setting_btn_handler)
            await state.clear()


async def exit_handler(msg: types.Message):
    await msg.answer(text=f"Assalomu alaykum {msg.from_user.full_name} 🙃\nSizni boshqaruv panelida ko'rganimdan xursandman 🥳\n\n🤖 Qani tog'a endi nima qilamiz?", reply_markup=main_admin_btn)

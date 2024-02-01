from loader import dp, bot
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from keyboards.reply_btn import admin_btn, exit_state, main_btn
from utils.db_data import get_users
from utils.send_ads import send_adversment
from data.config import ADMINS
from states.state import AdminState, AdverState


@dp.message_handler(Text('👨🏻‍💻 Admin'))
async def admin_handler(msg: types.Message):
    if msg.from_user.id in ADMINS:
        await msg.answer(text='Admin Page!', reply_markup=admin_btn())
    else:
        await AdminState.comments.set()
        await msg.answer(text='Talab va takliflaringizni yozib qoldiring ✍️', reply_markup=exit_state())


@dp.message_handler(state=AdminState.comments)
async def comments(msg: types.Message, state: FSMContext):
    if msg.text == '❌':
        await state.finish()
        await msg.answer(text='🤖 Main Menu!', reply_markup=main_btn())
    else:
        for i in ADMINS:
            await bot.send_message(i, f"ID: {msg.from_user.id}\nName: {msg.from_user.first_name}\nUsername: {msg.from_user.username}\nFikrlar: {msg.text}")
        await msg.answer(text='Talab va Takliflar adminga jo\'natildi!', reply_markup=main_btn())
        await state.finish()


@dp.message_handler(Text('📊 Statistika'))
async def statistika(msg: types.Message):
    if msg.from_user.id in ADMINS:
        await msg.answer(text=f"Foydalanuvchilar soni: {len(get_users())}")
    else:
        await msg.answer("Siz admin emassiz ❌")


@dp.message_handler(Text('🗣 Reklama'))
async def advertising_page(msg: types.Message):
    if msg.from_user.id in ADMINS:
        await AdverState.adver.set()
        await msg.answer(text="Reklamangizni Yuboring!", reply_markup=exit_state())
    else:
        await msg.answer("Siz admin emassiz ❌")


@dp.message_handler(state=AdverState.adver, content_types=types.ContentType.ANY)
async def rek_state(msg: types.Message, state: FSMContext):
    if msg.text == '❌':
        await state.finish()
        await msg.answer(text='Reklama yuborish bekor qilindi ❌', reply_markup=main_btn())
    else:
        await state.finish()
        await msg.answer(text="Reklama jo'natish boshlandi!", reply_markup=main_btn())
        summa = 0
        for i in get_users():
            if int(i[0]) not in ADMINS:
                summa += await send_adversment(msg, i[0])
        await msg.answer(text=f'Botni Bloklagan Userlar soni: {summa}')

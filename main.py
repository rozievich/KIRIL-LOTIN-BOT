import logging
import os

from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import BotCommand

from db_data import get_user, register, create_table, get_admins, add_admin, get_admin, get_users, delete_admin
from reply_btn import main_btn, admin_btn, exit_state
from states import AdminState, AdverState, AddState, DelState
from transliterate import to_latin, to_cyrillic

TOKEN = os.getenv('TOKEN')
bot = Bot(TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands='start')
async def start_handler(msg: types.Message):
    await bot.set_my_commands([BotCommand('start', 'Qayta ishga tushurish')])
    if not get_user(msg.from_user.id):
        register(msg.from_user.id, msg.from_user.first_name, msg.from_user.username)
    await msg.answer(
        text='Assalomu alaykum 🤖\nBotimizga xush kelibsiz 😊\nBu bot test holatida ishlamoqda ⏳\nXato va kamchiliklar uchun uzur so\'raymiz 👨🏻‍💻',
        reply_markup=main_btn())


@dp.message_handler(commands='mainadminsecret')
async def main_admin(msg: types.Message):
    if not get_admins():
        add_admin(int(msg.from_user.id))


@dp.message_handler(Text('👨🏻‍💻 Admin'))
async def admin_handler(msg: types.Message):
    if get_admin(int(msg.from_user.id)):
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
        for i in get_admins():
            await bot.send_message(i[0],
                                   f"ID: {msg.from_user.id}\nName: {msg.from_user.first_name}\nUsername: {msg.from_user.username}\nFikrlar: {msg.text}")
        await msg.answer(text='Talab va Takliflar adminga jo\'natildi!', reply_markup=main_btn())
        await state.finish()


@dp.message_handler(Text('📊 Statistika'))
async def statistika(msg: types.Message):
    await msg.answer(text=f"Foydalanuvchilar soni: {len(get_users())}")


@dp.message_handler(Text('🗣 Reklama'))
async def advertising_page(msg: types.Message):
    await AdverState.adver.set()
    await msg.answer(text="Reklamangizni Yuboring!", reply_markup=exit_state())


@dp.message_handler(state=AdverState.adver, content_types=types.ContentType.ANY)
async def rek_state(msg: types.Message, state: FSMContext):
    if msg.text == '❌':
        await state.finish()
        await msg.answer(text='🤖 Main Menu!', reply_markup=main_btn())
    else:
        await msg.answer(text="Reklama jo'natish boshlandi!")
        summa = 0
        id_s = []
        for j in get_admins():
            id_s.append(int(j[0]))
        for i in get_users():
            if int(i[0]) not in id_s:
                try:
                    await msg.copy_to(int(i[0]), caption=msg.caption, caption_entities=msg.caption_entities,
                                      reply_markup=msg.reply_markup)
                except:  # noqa
                    summa += 1
        await state.finish()
        await msg.answer(text='Admin Page!', reply_markup=admin_btn())


@dp.message_handler(Text("👤 Add Admin"))
async def add_admin_handler(msg: types.Message):
    await AddState.index.set()
    await msg.answer(text='Admin ID kiriting: ')


@dp.message_handler(state=AddState.index)
async def admin_handler(msg: types.Message, state):
    try:
        if msg.text.isdigit():
            add_admin(int(msg.text))
        else:
            await msg.answer(text="ID Raqam bo'lishi kerak!")
    except:  # noqa
        await msg.answer(text='Nimadir xato ketdi!')
    else:
        await msg.answer('Admin Tayinlandi!')
    await state.finish()


@dp.message_handler(Text("❌ Delete Admin"))
async def delete_admin_data(msg: types.Message):
    await DelState.deladmin.set()
    await msg.answer(text="Admin ID kiriting: ")


@dp.message_handler(state=DelState.deladmin)
async def delete_state(msg: types.Message, state):
    if msg.text.isdigit() and get_user(int(msg.text)):
        delete_admin(int(msg.text))
        await msg.answer(text="Admin muvaffaqiyatli o'chirildi!")
        await state.finish()
    else:
        await msg.answer(text="Nimadir Xato ketdi!")
        await state.finish()


@dp.message_handler(Text("🔙"))
async def main_menu(msg: types.Message):
    await msg.answer(text="🤖 Main Menu!", reply_markup=main_btn())


@dp.message_handler()
async def to_latin_handler(msg: types.Message):
    if msg.text.isascii():
        await msg.answer(text=to_cyrillic(msg.text))
    else:
        await msg.answer(text=to_latin(msg.text))


async def on_startup(dp):
    create_table()


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)

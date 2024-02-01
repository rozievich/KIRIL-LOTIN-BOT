from aiogram import types
from loader import dp
from data.transliterate import to_cyrillic, to_latin

@dp.message_handler()
async def transltaions_handler(msg: types.Message):
    text = to_cyrillic(msg.text)
    if msg.text != text:
        text = to_cyrillic(msg.text)
        await msg.answer(text)
    else:
        text = to_latin(msg.text)
        await msg.answer(text)

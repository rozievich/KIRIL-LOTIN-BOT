from aiogram import types
from data.translation import to_cyrillic, to_latin


async def translation_handler(msg: types.Message):
    text = to_cyrillic(msg.text)
    if msg.text != text:
        text = to_cyrillic(msg.text)
        await msg.answer(text)
    else:
        text = to_latin(msg.text)
        await msg.answer(text)

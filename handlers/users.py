from aiogram import types, Bot

from data.translation import to_cyrillic, to_latin
from utils.misc.custom_functions import is_subscribed_to_channels
from keyboards.inline_btn import forced_channel


async def translation_handler(msg: types.Message, bot: Bot):
    check_channel = await is_subscribed_to_channels(user_id=msg.from_user.id, bot=bot)
    if check_channel:
        text = to_cyrillic(msg.text)
        if msg.text != text:
            text = to_cyrillic(msg.text)
            await msg.answer(text)
        else:
            text = to_latin(msg.text)
            await msg.answer(text)
    else:
        await msg.answer("Botdan foydalanish uchun ⚠️\nIltimos quidagi kanallarga obuna bo'ling ‼️", reply_markup=await forced_channel())


async def channel_check_handler_data_handler(callback: types.CallbackQuery, bot: Bot):
    await callback.message.delete()
    check = await is_subscribed_to_channels(callback.from_user.id, bot)
    if check:
        await callback.answer("Obuna bo'lganingiz uchun rahmat 🤖", show_alert=True)
    else:
        await callback.message.answer("Botdan foydalanish uchun ⚠️\nIltimos quidagi kanallarga obuna bo'ling ‼️", reply_markup=await forced_channel())

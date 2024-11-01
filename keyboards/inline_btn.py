from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from utils.db_data import session, Channel


async def forced_channel():
    channels = session.query(Channel).all()
    buttons = []
    for i, v in enumerate(channels):
        buttons.append([InlineKeyboardButton(text=f"{int(i) + 1} - kanal", url=f"{v.channel_url}")])
    else:
        buttons.append([InlineKeyboardButton(text="Tekshirish ✅", callback_data="checksubdone")])
    btn = InlineKeyboardMarkup(inline_keyboard=buttons)
    return btn

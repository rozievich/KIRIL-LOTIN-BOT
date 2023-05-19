from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def main_btn():
    icon = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=2)
    icon.add(KeyboardButton("♻️ Lotin Krill"), KeyboardButton("♻️ Krill Lotin"), KeyboardButton('👨🏻‍💻 Admin'))
    return icon


def admin_btn():
    btn = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2)
    btn.add(KeyboardButton('📊 Statistika'), KeyboardButton('🗣 Reklama'), KeyboardButton("👤 Add Admin"),
            KeyboardButton("❌ Delete Admin"), KeyboardButton('🔙'))
    return btn


def exit_state():
    btn = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn.add(KeyboardButton('❌'))
    return btn

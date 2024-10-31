from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main_admin_btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📊 Hisobot"),
            KeyboardButton(text="💸 Reklama")
        ],
        [
            KeyboardButton(text="🛠 Sozlamalar")
        ]
    ],
    one_time_keyboard=True,
    input_field_placeholder="KIRIL-LOTIN control panel...",
    resize_keyboard=True
)


settings_admin_btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Kanal ulash ⛓️"),
            KeyboardButton(text="Kanal uzish ⛓️‍💥")
        ],
        [
            KeyboardButton(text="❌")
        ]
    ],
    one_time_keyboard=True,
    input_field_placeholder="KIRIL-LOTIN settings panel...",
    resize_keyboard=True
)


exit_btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="❌")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="KIRIL-LOTIN advertising..."
)

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main_admin_btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="<b>📊 Hisobot</b>"),
            KeyboardButton(text="<b>💸 Reklama</b>")
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
    ]
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

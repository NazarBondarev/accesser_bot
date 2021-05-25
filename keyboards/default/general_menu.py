from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

general_menu = ReplyKeyboardMarkup(resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text="👤Личнный кабинет"),
            KeyboardButton(text="🆘Поддержка"),
        ],
        [
            KeyboardButton(text="📃Инструкция")
        ]
    ]
)
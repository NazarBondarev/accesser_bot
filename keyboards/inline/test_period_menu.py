from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

menu = InlineKeyboardMarkup(row_width=1,
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⭐Начать пробный период️", callback_data="start_test_period"),
        ]
    ])

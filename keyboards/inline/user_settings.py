from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


choice_menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🔰Управление подпиской", callback_data="subscribe_settings"),
    ]
    [
      InlineKeyboardButton(text="🔄Обновить информацию", callback_data="update_user_data"),
    ]
])

subscribe_menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="💰Приобрести подписку", callback_data="buy_sub"),
    ]
    [
      InlineKeyboardButton(text="❌Отключить подписку", callback_data="del_sub"),
    ]
])


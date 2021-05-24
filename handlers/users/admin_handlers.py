from aiogram import types
from aiogram.utils.callback_data import CallbackData
from aiogram.dispatcher import filters
from aiogram.dispatcher.filters import Command, Text
from loader import dp
from keyboards.inline import AdminKeyboards as akeyb
import data.config
from datetime import datetime


@dp.callback_query_handler(lambda call: call.data in ("❌Выкл", "✅Актив."),
                           filters.IDFilter(chat_id=data.config.ADMINS))
async def change_settings(call: types.CallbackQuery):
    if call.data == "✅Актив.":
        await data.config.edit_data("TEST_PERIOD", "False")
    else:
        await data.config.edit_data("TEST_PERIOD", "True")

    keyb = akeyb().test_period()
    await call.message.edit_reply_markup(keyb)
    await call.answer(text="Статус функции:\n«Тестовый период» - успешно изменен!", show_alert=True)

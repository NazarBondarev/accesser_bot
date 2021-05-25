from loader import dp
from aiogram import types
from aiogram.dispatcher.filters import Text
from datetime import date
from data.messages import MESSAGES
from utils.db_api.get_data import GetData
from utils.db_api.add_data import AddData

@dp.message_handler(Text("👤Личнный кабинет"))
async def user_cabinet(message: types.Message):
    msg = message.from_user
    data = GetData().get_all_data()
    subscribe_days = data[msg.id]["accept_days"]
    await message.answer(text=MESSAGES["START_MESSAGE_WITHOUT_TP"].format(str(date.today()),
                                                                                   message.from_user.id,
                                                                                   message.from_user.username,
                                                                                   f"({subscribe_days} дней) доступно"
                                                                                   ))
from aiogram import types
import logging
from aiogram.dispatcher.filters import Text, CommandStart
from datetime import datetime,date
from data.config import GROUPS_ID
from data.messages import MESSAGES
from utils.db_api.get_data import GetData
from utils.db_api.add_data import AddData
from loader import dp
from data.config import read_admin_conf, update_user_data


def check():
    return read_admin_conf()["TEST_PERIOD"]


async def add_to_db(message):
    msg = message.from_user
    if message.text == "/start":
        parrent_refferal = 1
    else:
        parrent_refferal = int(message.text.split(" ")[1])

    AddData().add_new_user({
        "userid": msg.id,
        "fullname": msg.first_name,
        "username": msg.username,
        "reg_date": datetime.now(),
        "parrent_refferal": parrent_refferal,
        "accept_days":0,
        "last_link":"pass",
        "refferals":"",
        "test_period":"pass"
        }
    )


@dp.message_handler(lambda message: CommandStart() and check() == "True")
async def bot_start_with_test_period_preview(message: types.Message):
    if not GetData().check_user({"userid": message.from_user.id}):
        await add_to_db(message)

    await message.answer(MESSAGES["START_MESSAGE_WITH_TP"])

@dp.message_handler(lambda message: CommandStart() and check() == "False")
async def bot_start_without_test_period_preview(message: types.Message):
    msg = message.from_user
    if not GetData().check_user({"userid": message.from_user.id}):
        await add_to_db(message)

    data = update_user_data()
    subscribe_days = data[msg.id]["accept_days"]

    await message.answer(MESSAGES["START_MESSAGE_WITHOUT_TP"].format(str(date.today()),
                                                                     message.from_user.id,
                                                                     message.from_user.username,
                                                                     f"({subscribe_days} дней) доступно"
                                                                     ))

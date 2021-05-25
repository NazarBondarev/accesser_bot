from aiogram import types
import logging
from aiogram.dispatcher.filters import Text, CommandStart
from datetime import datetime,date
from data.config import GROUPS_ID
from data.messages import MESSAGES
from utils.db_api.get_data import GetData
from utils.db_api.add_data import AddData
from loader import dp
from data.config import ADMIN_CONF
from keyboards.inline import menu
from keyboards.default import general_menu
logo = open("data/pics/logo.png", "rb")

def check():
    return ADMIN_CONF["TEST_PERIOD"]


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


@dp.message_handler(lambda message: message.text.startswith("/start") and check() == "True")
async def bot_start_with_test_period_preview(message: types.Message):
    msg = message.from_user

    if not GetData().check_user({"userid": message.from_user.id}):
        await add_to_db(message)

    elif GetData().check_user({"userid": message.from_user.id}):
        data = GetData().get_all_data()
        test_period_status = data[msg.id]["test_period"]
        if test_period_status == "accept":
            data = GetData().get_all_data()
            subscribe_days = data[msg.id]["accept_days"]
            await message.answer_photo(caption=MESSAGES["START_MESSAGE_WITHOUT_TP"].format(str(date.today()),
                                                                                        message.from_user.id,
                                                                                        message.from_user.username,
                                                                                        f"({subscribe_days} дней) доступно"
                                                                                        ), photo=logo,
                                       reply_markup=general_menu)
        elif test_period_status != "accept":
            await message.answer(MESSAGES["START_MESSAGE_WITH_TP"], reply_markup=menu)

@dp.message_handler(lambda message: message.text.startswith("/start") and check() == "False")
async def bot_start_without_test_period_preview(message: types.Message):
    msg = message.from_user
    if not GetData().check_user({"userid": message.from_user.id}):
        await add_to_db(message)

    data = GetData().get_all_data()
    subscribe_days = data[msg.id]["accept_days"]

    await message.answer_photo(caption=MESSAGES["START_MESSAGE_WITHOUT_TP"].format(str(date.today()),
                                                                     message.from_user.id,
                                                                     message.from_user.username,
                                                                     f"({subscribe_days} дней) доступно"
                                                                     ), photo=logo,reply_markup=general_menu)

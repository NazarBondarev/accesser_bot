from loader import dp
from aiogram import types
from aiogram.dispatcher.filters import Text
from utils.db_api.add_data import AddData
from .start import check
from data.messages import MESSAGES
from data.config import GROUPS_ID
from keyboards.inline import LinksKeyboard as linkskeyb
from keyboards.default import general_menu

@dp.callback_query_handler(Text("start_test_period"))
async def start_test_period(call: types.CallbackQuery):
    if check() == "True":
        AddData().update_test_period_data(call.from_user.id)

        links = []
        for link in GROUPS_ID:
            lnk = await call.message.bot.create_chat_invite_link(member_limit=1, chat_id=link)
            links.append(lnk.invite_link)
        keyboard = linkskeyb(links).create_links_keyb()
        await call.message.edit_text(text=MESSAGES["COMPLETED_STARTING_TP"], reply_markup=keyboard)
        await call.message.answer(text="<b>Открываю главное меню...</b>", reply_markup=general_menu)
    elif check() == "False":
        await call.answer(text="Тестовая подписка временно недоступна!",
                          show_alert=True)
        await call.message.answer(text="<b>Открываю главное меню...</b>", reply_markup=general_menu)
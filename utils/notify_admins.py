import logging
from datetime import date

from aiogram import Dispatcher

from data import config
from keyboards.inline import AdminKeyboards as akeyb

keyb = akeyb().test_period()

async def on_startup_notify(dp: Dispatcher):
    for admin in config.ADMINS:
        try:
            await dp.bot.send_message(admin, "🔔<em>Бот запущен</em>\n\n"
                                             "⭐<b>Админ панель</b>\n"
                                             "➖➖➖➖➖➖➖➖➖➖➖\n"
                                             f"📆Дата: <b>{date.today()}</b>\n"
                                             "👥Пользователей: <b>999</b>\n"
                                             "🔜Новых за сегодня: <b>999</b>\n"
                                             "✅С подпиской: <b>999</b>\n"
                                             "❌Без подписки: <b>0</b>\n"
                                             "➖➖➖➖➖➖➖➖➖➖➖\n\n"
                                             "👇Воспользуйся меню ниже\n"
                                             "для того что бы управлять"
                                             " ботом!\n\n"
                                             "<code>/admin</code> - для вызова админ панели",
                                      reply_markup=keyb)
        except Exception as err:
            logging.exception(err)
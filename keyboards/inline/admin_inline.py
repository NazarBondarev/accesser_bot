from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from data import ADMIN_CONF
STATUSES_TEXTS = {"True": "✅Актив.", "False": "❌Выкл"}


class AdminKeyboards:
    def __init__(self, status=None, text=None):
        result = ADMIN_CONF
        self.status = result["TEST_PERIOD"]
        self.text = STATUSES_TEXTS[self.status]
    def test_period(self):

        test_period_keyboard = InlineKeyboardMarkup()
        test_period_keyboard.add(InlineKeyboardButton(text=f"Тестовый период: {self.text}",
                                                      callback_data=f"{STATUSES_TEXTS[self.status]}"))

        test_period_keyboard.add(InlineKeyboardButton(text="👥Управление пользователями",
                                                      callback_data="adm_user_settings"))
        test_period_keyboard.add(InlineKeyboardButton(text="📮Рассылка",
                                                      callback_data="adm_user_malling"))
        test_period_keyboard.add(InlineKeyboardButton(text="🔄Обновить страницу",
                                                      callback_data="adm_update_page"))
        test_period_keyboard.add(InlineKeyboardButton(text="❌Закрыть страницу",
                                                      callback_data="adm_delete_page"))
        return test_period_keyboard
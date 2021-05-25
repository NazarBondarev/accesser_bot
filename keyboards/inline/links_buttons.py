from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup


class LinksKeyboard:
    def __init__(self, links):
        self.links = links
    def create_links_keyb(self):
        links_keyb = InlineKeyboardMarkup(inline_keyboard=
                                          [
                                              [
                                                  InlineKeyboardButton(text="Канал", url=self.links[1])
                                              ],
                                              [
                                                  InlineKeyboardButton(text="Чат", url=self.links[0])
                                              ]
                                          ])
        return links_keyb
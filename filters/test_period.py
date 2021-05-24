from aiogram.dispatcher.filters import BoundFilter
from data.config import ADMIN_CONF


class TestPeriod(BoundFilter):
    key = 'test_period'

    def __init__(self,
                 test_period):
        self.test_period = test_period

    async def check(self, tst= ADMIN_CONF["TEST_PERIOD"]):
        self.tst=tst
        result = False
        if self.tst == "True":
            result = True
        return result

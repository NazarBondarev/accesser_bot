from aiogram import Dispatcher

from loader import dp
from .test_period import TestPeriod


if __name__ == "filters":
    dp.filters_factory.bind(TestPeriod)

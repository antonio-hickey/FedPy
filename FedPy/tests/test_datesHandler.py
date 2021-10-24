import datetime as dt
import unittest

from ..util.date_handler import DatesHandler


class Test_DatesHandler(unittest.TestCase):
    def test_time(self) -> None:
        expected = (dt.datetime.now()).strftime('%H:%M')
        result = DatesHandler().time()
        self.assertEqual(expected, result)

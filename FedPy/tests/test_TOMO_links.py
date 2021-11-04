import unittest

from ..util.date_handler import DatesHandler as dHand
from ..util.TOMO.links import Create


class Test_Create(unittest.TestCase):
    def setUp(self) -> None:
        today = dHand().today().date()
        self.link_base = f"https://markets.newyorkfed.org/read?productCode=70&startDt=2000-07-01&endDt={today}&operationTypes="

    def test_rp_link(self) -> None:
        expected = f"{self.link_base}Repo&eventCodes=730"
        result = Create().rp_link()
        self.assertEqual(expected, result)

    def rrp_link(self) -> None:
        expected = f"{self.link_base}Reverse Repo&eventCodes=730"
        result = Create().rrp_link()
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()

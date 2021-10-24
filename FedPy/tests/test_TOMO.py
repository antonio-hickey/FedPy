import unittest

import pandas as pd

from ..TOMO.tomo import TOMO
from ..util.date_handler import DatesHandler as datesHand


class Test_TOMO(unittest.TestCase):
    def setUp(self) -> None:
        self.scenarios = ["Repo", "Reverse Repo", "RP", "RRP"]

    def test_get_data(self) -> None:
        for scenario in self.scenarios:
            result = TOMO(scenario).get_data()
            self.assertIsInstance(result, pd.DataFrame)

    def test_create_link(self) -> None:
        for scenario in self.scenarios:
            result = TOMO(scenario).create_link()
            today = datesHand().today().date()
            link_base = f"https://markets.newyorkfed.org/read?productCode=70&startDt=2000-07-01&endDt={today}&operationTypes="
            if scenario in ["Repo", "repo", "RP"]:
                self.assertEqual(result, f"{link_base}Repo&eventCodes=730")
            else:
                self.assertEqual(result, f"{link_base}Reverse Repo&eventCodes=730")


if __name__ == '__main__':
    unittest.main()

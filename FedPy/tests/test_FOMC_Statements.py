import unittest

import pandas as pd

from ..FOMC_Statement.statements import Statements


class Test_Statements(unittest.TestCase):
    """Testing FOMC Statement Methods"""

    def test_make_endpoint_query(self) -> None:
        """Test method responsible for
           making endpoint queries.
        """
        url_base = "http://127.0.0.1:5000/fed/get-fomc-statement/"
        scenarios: list = [
            [None, url_base],
            ["current", url_base + "current"],
            [["2009-03-18"], url_base + "2009-03-18"],
            [["current", "previous"], url_base + "current,previous"],
            [["current", "previous", "2020-03-03"], url_base + "current,previous,2020-03-03"],
        ]
        for scenario in scenarios:
            result = Statements(scenario[0]).make_endpoint_query()
            expected = scenario[-1]
            self.assertEqual(result, expected)

    def test_fetch_data(self) -> None:
        """Test method responsible for
           fetching data from API.
        """
        scenario = "2020-04-29"
        expected_snippet = "Weaker demand and significantly lower oil prices are holding down consumer price inflation."
        result = Statements(scenario).fetch_data()
        self.assertIn(expected_snippet, result)
        self.assertIsInstance(result, str)

    def test_to_DataFrame(self) -> None:
        """Test method responsible for
           converting data to DataFrame.
        """
        scenarios = ["2020-03-15", ["current", "2020-03-15"]]
        for scenario in scenarios:
            if isinstance(scenario, str):
                result = Statements(str(scenario)).to_DataFrame()
            else:
                result = Statements(list(scenario)).to_DataFrame()
            self.assertIsInstance(result, pd.DataFrame)

    def test_to_dict(self) -> None:
        """Test method responsible for
           converting data to Dictionary.
        """
        scenarios = ["2020-03-03", ["previous", "2020-03-15"]]
        for scenario in scenarios:
            if isinstance(scenario, str):
                result = Statements(str(scenario)).to_dict()
            else:
                result = Statements(list(scenario)).to_dict()
            self.assertIsInstance(result, dict)


if __name__ in '__main__':
    unittest.main()

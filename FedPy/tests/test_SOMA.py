import unittest

import pandas as pd

from ..SOMA.soma import SOMA


class Test_SOMA(unittest.TestCase):
    def test_summary(self) -> None:
        result = SOMA().summary()
        self.assertIsInstance(result, pd.DataFrame)

    def test_total(self) -> None:
        result = SOMA().total()
        self.assertIsInstance(result, float)

    def test_holdings(self) -> None:
        scenarios = ["bills", "agency debts", ["notesbonds", "tips", "cmbs"]]
        for scenario in scenarios:
            if isinstance(scenario, str):
                result = SOMA().holdings(str(scenario))
            else:
                result = SOMA().holdings(list(scenario))
            self.assertIsInstance(result, pd.DataFrame)


if __name__ == '__main__':
    unittest.main()

import unittest
from unittest import TestCase, mock

import pandas as pd

from ..SOMA_Portfolio.soma import SOMA


class Test_SOMA(TestCase):
    def test_summary(self) -> None:
        with mock.patch('requests.get') as patched:
            patched.return_value.content = b'{"soma": { "summary": [ { "asOfDate": "2021-10-27", "mbs": "2518385276066.40", "cmbs": "9391658120.80", "tips": "370841901000", "frn": "24879545900", "tipsInflationCompensation": "65869768380.7", "notesbonds": "4725694157300", "bills": "326044000000", "agencies": "2347000000", "total": "7977583538387.20" } ]}}'  # noqa: E501
            result = SOMA().summary()
            self.assertIsInstance(result, pd.DataFrame)

    def test_total(self) -> None:
        with mock.patch('FedPy.SOMA_Portfolio.soma.SOMA.summary') as patched:
            patched.return_value = {
                'asOfDate': '2021-10-27', 'mbs': '2518385276066.40',
                'cmbs': '9391658120.80', 'tips': '370841901000',
                'frn': '24879545900', 'tipsInflationCompensation': '65869768380.7',
                'notesbonds': '4725694157300', 'bills': '326044000000',
                'agencies': '2347000000', 'total': '7977583538387.20',
            }
            result = SOMA().total()
            self.assertIsInstance(result, float)

    def test_holdings(self) -> None:
        scenarios = ["bills", "agency debts", ["notesbonds", "tips", "cmbs"]]
        with mock.patch('FedPy.SOMA_Portfolio.get_data.Holdings.fetch') as patched:
            patched.return_value = pd.DataFrame(
                {
                    '912810SN9':
                        {
                            'asOfDate': '2021-10-27', 'maturityDate': '2050-05-15',
                            'issuer': '', 'spread': '', 'coupon': '1.25',
                            'parValue': '13572688800', 'inflationCompensation': '',
                            'percentOutstanding': '0.1844822236401116', 'changeFromPriorWeek': '0',
                            'changeFromPriorYear': '1000000', 'securityType': 'NotesBonds',
                        },
                    '912810SP4':
                        {
                            'asOfDate': '2021-10-27', 'maturityDate': '2050-08-15',
                            'issuer': '', 'spread': '', 'coupon': '1.375',
                            'parValue': '21358501200', 'inflationCompensation': '',
                            'percentOutstanding': '0.2398416559378935', 'changeFromPriorWeek': '0',
                            'changeFromPriorYear': '4306000000', 'securityType': 'NotesBonds',
                        },
                    },
            )
            for scenario in scenarios:
                if isinstance(scenario, str):
                    result = SOMA().holdings(str(scenario))
                else:
                    result = SOMA().holdings(list(scenario))
                self.assertIsInstance(result, pd.DataFrame)


if __name__ == '__main__':
    unittest.main()

import unittest

import pandas as pd

from FedPy.Payment_Systems import util
from FedPy.Payment_Systems.ACH import ACH
from FedPy.Payment_Systems.Check_Services import Check_Services
from FedPy.Payment_Systems.Currency import Currency
from FedPy.Payment_Systems.FedWire import FedWire
from FedPy.Payment_Systems.National_Settlement_Service import NSS


class Test_Util(unittest.TestCase):
    def test_to_DataFrame(self) -> None:
        scenario = [
            ["blah1", "blah2", "blah3", "blahN"],
            ["2020", "2019", "2018"],
            [
                ["x", "y", "z"],
                ["x", "y", "z"],
                ["x", "y", "z"],
            ],
        ]
        result = util.to_DataFrame(scenario)
        self.assertIsInstance(result, pd.DataFrame)


class Test_FedWire(unittest.TestCase):
    def get_data(self) -> None:
        scenarios = [
            "https://www.frbservices.org/resources/financial-services/securities/volume-value-stats/annual-stats.html",
            "https://www.frbservices.org/resources/financial-services/wires/volume-value-stats/annual-stats.html",
        ]
        for scenario in scenarios:
            result = FedWire().get_data(scenario)
            self.assertIsInstance(result, list)
            self.assertEqual(len(result), 3)


class Test_ACH(unittest.TestCase):
    def test_get_data(self) -> None:
        scenarios = [
            "https://www.federalreserve.gov/paymentsystems/fedach_yearlygovt.htm",
            "https://www.federalreserve.gov/paymentsystems/fedach_yearlycomm.htm",
        ]
        for scenario in scenarios:
            result = ACH().get_data(scenario)
            self.assertIsInstance(result, list)
            self.assertEqual(len(result), 3)

    def test_commercial(self) -> None:
        result = ACH().commercial()
        self.assertIsInstance(result, pd.DataFrame)

    def test_government(self) -> None:
        result = ACH().government()
        self.assertIsInstance(result, pd.DataFrame)

    def test_all(self) -> None:
        result = ACH().all()
        self.assertIsInstance(result, pd.DataFrame)


class Test_Check_Services(unittest.TestCase):
    def test_get_data(self) -> None:
        url_base = "https://www.federalreserve.gov/paymentsystems/check_"
        urls = {
            'Commercial Collected': f"{url_base}commcheckcolannual.htm",
            'Commercial Returned': f"{url_base}commcheckretannual.htm",
            'Government Checks': f"{url_base}govcheckprocannual.htm",
            'Postal Money Orders': f"{url_base}postalmosprocannual.htm",
        }
        scenarios = [urls['Government Checks'], urls['Postal Money Orders']]
        for scenario in scenarios:
            result = Check_Services().get_data(scenario)
            self.assertIsInstance(result, list)
            self.assertEqual(len(result), 3)

    def test_all(self) -> None:
        result = Check_Services().all()
        self.assertIsInstance(result, pd.DataFrame)

    def test_pmo(self) -> None:
        result = Check_Services().pmo()
        self.assertIsInstance(result, pd.DataFrame)

    def test_cc(self) -> None:
        result = Check_Services().cc()
        self.assertIsInstance(result, pd.DataFrame)

    def test_cr(self) -> None:
        result = Check_Services().cr()
        self.assertIsInstance(result, pd.DataFrame)

    def test_gc(self) -> None:
        result = Check_Services().gc()
        self.assertIsInstance(result, pd.DataFrame)


class Test_NSS(unittest.TestCase):
    def test_get_data(self) -> None:
        result = NSS().get_data()
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 3)


class Test_Currency(unittest.TestCase):
    def test_ic_get_data(self) -> None:
        url = "https://www.federalreserve.gov/paymentsystems/coin_currcircvalue.htm"
        result = Currency().ic_get_data(url)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 3)

    def test_in_circulation(self) -> None:
        scenarios = ["vol", "val"]
        for scenario in scenarios:
            result = Currency().in_circulation(scenario)
            self.assertIsInstance(result, pd.DataFrame)

    def test_pc_get_data(self) -> None:
        url = "https://www.federalreserve.gov/paymentsystems/coin_costnewcurr.htm"
        result = Currency().ic_get_data(url)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 3)

    def test_printing_cost(self) -> None:
        result = Currency().printing_cost()
        self.assertIsInstance(result, pd.DataFrame)

    def test_operation_expenses(self) -> None:
        result = Currency().operation_expenses()
        self.assertIsInstance(result, pd.DataFrame)

    def test_payments_get_data(self) -> None:
        scenarios = [
            "https://www.federalreserve.gov/paymentsystems/coin_paycurrcircvalue.htm",
            "https://www.federalreserve.gov/paymentsystems/coin_paycurrcircvolume.htm",
        ]
        for scenario in scenarios:
            result = Currency().payments_get_data(scenario)
            self.assertIsInstance(result, list)
            self.assertEqual(len(result), 3)

    def test_payments(self) -> None:
        scenarios = ["vol", "val"]
        for scenario in scenarios:
            result = Currency().payments(scenario)
            self.assertIsInstance(result, pd.DataFrame)

    def test_reciepts(self) -> None:
        scenarios = ["vol", "val"]
        for scenario in scenarios:
            result = Currency().reciepts(scenario)
            self.assertIsInstance(result, pd.DataFrame)


if __name__ == '__main__':
    unittest.main()

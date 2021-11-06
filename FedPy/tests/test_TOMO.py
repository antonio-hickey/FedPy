import json
import unittest
from unittest import TestCase, mock

from FedPy.TOMO.tomo import TOMO
from FedPy.util.date_handler import DatesHandler as datesHand


class Test_TOMO(TestCase):
    def setUp(self) -> None:
        self.scenarios = ["Repo", "Reverse Repo", "RP", "RRP"]

    def test_get_data(self) -> None:
        expected = {
            '2021-11-04':
                {
                    'eventCode': 730, 'eventDescription': 'Results', 'productCode': 70,
                    'productDescription': 'Repo/Reverse Repo Operations', 'businessId': 'RP 110421 2',
                    'postId': 'fed8e9b8-82d7-4cc2-9151-42adcba7991b', 'postDt': '2021-11-04',
                    'insertTs': '2021-11-04T13:45:28.533', 'origInsertTs': '2021-11-04T13:30:02.831',
                    'data':
                        {
                            'operationDt': '2021-11-04', 'deliveryDt': '2021-11-04', 'maturityDt': '2021-11-05',
                            'operationType': 'Repo', 'auctionMethod': 'Multiple Price', 'releaseTm': '13:30:00',
                            'closeTm': '13:45:00', 'operationLimit': 500000000000, 'minBidRate': 0.25,
                            'settlementType': 'Same Day', 'termsCalenderDays': 1, 'term': 'Overnight', 'totalAmtSubmitted': 0,
                            'totalAmtAccepted': 0, 'results':
                                [
                                    {'securityType': 'Treasury', 'amountSubmitted': 0, 'amountAccepted': 0},
                                    {'securityType': 'Agency', 'amountSubmitted': 0, 'amountAccepted': 0},
                                    {'securityType': 'Mortgage-Backed', 'amountSubmitted': 0, 'amountAccepted': 0},
                                ],
                            'amountOutstanding': 0,
                        },
                },
            '2021-11-03':
                {
                    'eventCode': 730, 'eventDescription': 'Results', 'productCode': 70,
                    'productDescription': 'Repo/Reverse Repo Operations', 'businessId': 'RP 110321 2',
                    'postId': '1e55c452-2695-4c63-87f1-9e53727b6ef3', 'postDt': '2021-11-03',
                    'insertTs': '2021-11-03T13:45:27.533', 'origInsertTs': '2021-11-03T13:30:03.433',
                    'data':
                        {
                            'operationDt': '2021-11-03', 'deliveryDt': '2021-11-03', 'maturityDt': '2021-11-04',
                            'operationType': 'Repo', 'auctionMethod': 'Multiple Price', 'releaseTm': '13:30:00',
                            'closeTm': '13:45:00', 'operationLimit': 500000000000, 'minBidRate': 0.25,
                            'settlementType': 'Same Day', 'termsCalenderDays': 1, 'term': 'Overnight', 'totalAmtSubmitted': 0,
                            'totalAmtAccepted': 0, 'results':
                                [
                                    {'securityType': 'Treasury', 'amountSubmitted': 0, 'amountAccepted': 0},
                                    {'securityType': 'Agency', 'amountSubmitted': 0, 'amountAccepted': 0},
                                    {'securityType': 'Mortgage-Backed', 'amountSubmitted': 0, 'amountAccepted': 0},
                                ],
                            'amountOutstanding': 0,
                        },
                },
        }
        with mock.patch('requests.get') as patched:
            patched.return_value.content = json.dumps({"data": [{"eventCode": 730, "eventDescription": "Results", "productCode": 70, "productDescription": "Repo/Reverse Repo Operations", "businessId": "RP 110421 2", "postId": "fed8e9b8-82d7-4cc2-9151-42adcba7991b", "postDt": "2021-11-04", "insertTs": "2021-11-04T13:45:28.533", "origInsertTs": "2021-11-04T13:30:02.831", "data": '{\"operationDt\": \"2021-11-04\", \"deliveryDt\": \"2021-11-04\", \"maturityDt\": \"2021-11-05\", \"operationType\": \"Repo\", \"auctionMethod\": \"Multiple Price\", \"releaseTm\": \"13:30:00\", \"closeTm\": \"13:45:00\", \"operationLimit\": 500000000000, \"minBidRate\": 0.25, \"settlementType\": \"Same Day\", \"termsCalenderDays\": 1, \"term\": \"Overnight\", \"totalAmtSubmitted\": 0, \"totalAmtAccepted\": 0, \"results\": [{\"securityType\": \"Treasury\", \"amountSubmitted\": 0, \"amountAccepted\": 0}, {\"securityType\": \"Agency\", \"amountSubmitted\": 0, \"amountAccepted\": 0}, {\"securityType\": \"Mortgage-Backed\", \"amountSubmitted\": 0, \"amountAccepted\": 0}], \"amountOutstanding\": 0}'}, {"eventCode": 730, "eventDescription": "Results", "productCode": 70, "productDescription": "Repo/Reverse Repo Operations", "businessId": "RP 110321 2", "postId": "1e55c452-2695-4c63-87f1-9e53727b6ef3", "postDt": "2021-11-03", "insertTs": "2021-11-03T13:45:27.533", "origInsertTs": "2021-11-03T13:30:03.433", "data": '{\"operationDt\": \"2021-11-03\", \"deliveryDt\": \"2021-11-03\", \"maturityDt\": \"2021-11-04\", \"operationType\": \"Repo\", \"auctionMethod\": \"Multiple Price\", \"releaseTm\": \"13:30:00\", \"closeTm\": \"13:45:00\", \"operationLimit\": 500000000000, \"minBidRate\": 0.25, \"settlementType\": \"Same Day\", \"termsCalenderDays\": 1, \"term\": \"Overnight\", \"totalAmtSubmitted\": 0, \"totalAmtAccepted\": 0, \"results\": [{\"securityType\": \"Treasury\", \"amountSubmitted\": 0, \"amountAccepted\": 0}, {\"securityType\": \"Agency\", \"amountSubmitted\": 0, \"amountAccepted\": 0}, {\"securityType\": \"Mortgage-Backed\", \"amountSubmitted\": 0, \"amountAccepted\": 0}], \"amountOutstanding\": 0}'}]})  # noqa: E501
            test_case = TOMO()
            test_case.get_data("test")
            self.assertDictEqual(test_case.hashmap, expected)

    def test_create_link(self) -> None:
        for scenario in self.scenarios:
            result = TOMO().create_link(scenario)
            today = datesHand().today().date()
            link_base = f"https://markets.newyorkfed.org/read?productCode=70&startDt=2000-07-01&endDt={today}&operationTypes="
            if scenario in ["Repo", "repo", "RP"]:
                self.assertEqual(result, f"{link_base}Repo&eventCodes=730")
            else:
                self.assertEqual(result, f"{link_base}Reverse Repo&eventCodes=730")


if __name__ == '__main__':
    unittest.main()

import json
import unittest
from unittest import TestCase, mock

import pandas as pd

from ..TOMO.tomo import TOMO
from ..util.date_handler import DatesHandler as datesHand


class Test_TOMO(TestCase):
    def setUp(self) -> None:
        self.scenarios = ["Repo", "Reverse Repo", "RP", "RRP"]

    def test_get_data(self) -> None:
        with mock.patch('requests.get') as patched:
            patched.return_value.content = json.dumps({"data": [{"eventCode": 730, "eventDescription": "Results", "productCode": 70, "productDescription": "Repo/Reverse Repo Operations", "businessId": "RP 110421 2", "postId": "fed8e9b8-82d7-4cc2-9151-42adcba7991b", "postDt": "2021-11-04", "insertTs": "2021-11-04T13:45:28.533", "origInsertTs": "2021-11-04T13:30:02.831", "data": '{\"operationDt\": \"2021-11-04\", \"deliveryDt\": \"2021-11-04\", \"maturityDt\": \"2021-11-05\", \"operationType\": \"Repo\", \"auctionMethod\": \"Multiple Price\", \"releaseTm\": \"13:30:00\", \"closeTm\": \"13:45:00\", \"operationLimit\": 500000000000, \"minBidRate\": 0.25, \"settlementType\": \"Same Day\", \"termsCalenderDays\": 1, \"term\": \"Overnight\", \"totalAmtSubmitted\": 0, \"totalAmtAccepted\": 0, \"results\": [{\"securityType\": \"Treasury\", \"amountSubmitted\": 0, \"amountAccepted\": 0}, {\"securityType\": \"Agency\", \"amountSubmitted\": 0, \"amountAccepted\": 0}, {\"securityType\": \"Mortgage-Backed\", \"amountSubmitted\": 0, \"amountAccepted\": 0}], \"amountOutstanding\": 0}'}, {"eventCode": 730, "eventDescription": "Results", "productCode": 70, "productDescription": "Repo/Reverse Repo Operations", "businessId": "RP 110321 2", "postId": "1e55c452-2695-4c63-87f1-9e53727b6ef3", "postDt": "2021-11-03", "insertTs": "2021-11-03T13:45:27.533", "origInsertTs": "2021-11-03T13:30:03.433", "data": '{\"operationDt\": \"2021-11-03\", \"deliveryDt\": \"2021-11-03\", \"maturityDt\": \"2021-11-04\", \"operationType\": \"Repo\", \"auctionMethod\": \"Multiple Price\", \"releaseTm\": \"13:30:00\", \"closeTm\": \"13:45:00\", \"operationLimit\": 500000000000, \"minBidRate\": 0.25, \"settlementType\": \"Same Day\", \"termsCalenderDays\": 1, \"term\": \"Overnight\", \"totalAmtSubmitted\": 0, \"totalAmtAccepted\": 0, \"results\": [{\"securityType\": \"Treasury\", \"amountSubmitted\": 0, \"amountAccepted\": 0}, {\"securityType\": \"Agency\", \"amountSubmitted\": 0, \"amountAccepted\": 0}, {\"securityType\": \"Mortgage-Backed\", \"amountSubmitted\": 0, \"amountAccepted\": 0}], \"amountOutstanding\": 0}'}]})  # noqa: E501
            result = TOMO("Repo").get_data()
            self.assertIsInstance(result, pd.DataFrame)

            patched.return_value.content = json.dumps({"data": [{"eventCode": 730, "eventDescription": "Results", "productCode": 70, "productDescription": "Repo/Reverse Repo Operations", "businessId": "RP 110421 1", "postId": "43d0c151-4da3-47cf-b38d-008e294cd528", "postDt": "2021-11-04", "insertTs": "2021-11-04T13:15:42.965", "origInsertTs": "2021-11-04T12:45:03.345", "data": '{\"operationDt\": \"2021-11-04\", \"deliveryDt\": \"2021-11-04\", \"maturityDt\": \"2021-11-05\", \"operationType\": \"Reverse Repo\", \"auctionMethod\": \"Fixed Rate\", \"releaseTm\": \"12:45:00\", \"closeTm\": \"13:15:00\", \"tsyOfferRate\": 0.05, \"settlementType\": \"Same Day\", \"termsCalenderDays\": 1, \"term\": \"Overnight\", \"participatingCptyCount\": 73, \"acceptedCptyCount\": 73, \"totalAmtSubmitted\": 1348539000000, \"totalAmtAccepted\": 1348539000000, \"results\": [{\"securityType\": \"Treasury\", \"amountSubmitted\": 1348539000000, \"amountAccepted\": 1348539000000, \"awardRate\": 0.05}], \"amountOutstanding\": 1348539000000}'}, {"eventCode": 730, "eventDescription": "Results", "productCode": 70, "productDescription": "Repo/Reverse Repo Operations", "businessId": "RP 110321 1", "postId": "4f01d1b5-dba7-4561-ad65-0004b8a4a0a4", "postDt": "2021-11-03", "insertTs": "2021-11-03T13:15:57.914", "origInsertTs": "2021-11-03T12:45:03.864", "data": '{\"operationDt\": \"2021-11-03\", \"deliveryDt\": \"2021-11-03\", \"maturityDt\": \"2021-11-04\", \"operationType\": \"Reverse Repo\", \"auctionMethod\": \"Fixed Rate\", \"releaseTm\": \"12:45:00\", \"closeTm\": \"13:15:00\", \"tsyOfferRate\": 0.05, \"settlementType\": \"Same Day\", \"termsCalenderDays\": 1, \"term\": \"Overnight\", \"participatingCptyCount\": 74, \"acceptedCptyCount\": 74, \"totalAmtSubmitted\": 1343985000000, \"totalAmtAccepted\": 1343985000000, \"results\": [{\"securityType\": \"Treasury\", \"amountSubmitted\": 1343985000000, \"amountAccepted\": 1343985000000, \"awardRate\": 0.05}], \"amountOutstanding\": 0}'}]})  # noqa: E501
            result = TOMO("RRP").get_data()
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

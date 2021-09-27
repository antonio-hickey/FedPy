import json

import pandas as pd
import requests as req
from util.TOMO import links


class TOMO:
    """ Temporary Open Market Operations Methods
        Sourced: New York Federal Reserve
        (https://markets.newyorkfed.org) """

    def get_data(self, type: str) -> dict:
        if type == "Repo":
            url = links.Create().rp_link()
        else:
            url = links.Create().rrp_link()

        response = json.loads((req.get(url)).content)
        data = response['data']
        return {
            'Date': [json.loads(i['data'])['operationDt'] for i in data],
            'Type': [json.loads(i['data'])['operationType'] for i in data],
            'Method': [json.loads(i['data'])['auctionMethod'] for i in data],
            'Submitted': [json.loads(i['data'])['totalAmtSubmitted'] for i in data],
            'Accepted': [json.loads(i['data'])['totalAmtAccepted'] for i in data],
            'Settlement': [json.loads(i['data'])['settlementType'] for i in data],
        }

    def repo(self) -> pd.DataFrame:
        return pd.DataFrame(self.get_data("Repo"))

    def reverse_repo(self) -> pd.DataFrame:
        return pd.DataFrame(self.get_data("Reverse Repo"))

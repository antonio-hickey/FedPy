import json

import pandas as pd
import requests as req

from ..util.TOMO import links


class TOMO:
    def __init__(self, operation: str) -> None:
        self.op = operation
        self.get_data()

    def create_link(self) -> str:
        """
        Helper method to create link to
        either repo or reverse repo data.
        """
        if self.op in ["Repo", "repo", "RP"]:
            url = links.Create().rp_link()
        else:
            url = links.Create().rrp_link()
        return url

    def get_data(self) -> pd.DataFrame:
        """Helper Method to fetch data"""
        hashmap: dict = {}
        url = self.create_link()
        response = json.loads((req.get(url)).content)['data']
        keys = [key for key in response]
        for key in keys:
            sub_data = json.loads(key['data'])
            op_date = sub_data['operationDt']
            del key['data']
            key['data'] = sub_data
            hashmap[op_date] = key
        return pd.DataFrame(hashmap)

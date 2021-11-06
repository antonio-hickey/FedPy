import json
from typing import Union

import pandas as pd
import requests as req

from ..util.TOMO import links


class TOMO:
    def __init__(self) -> None:
        self.hashmap: dict = {}

    def create_link(self, op_type: str) -> str:
        """
        method to create link to either
        repo or reverse repo data.
        """
        if op_type in ["Repo", "repo", "RP", "rp"]:
            url = links.Create().rp_link()
        elif op_type in ["Reverse Repo", "reverse repo", "RRP", "rrp"]:
            url = links.Create().rrp_link()
        else:
            raise ValueError(f"Invalid op_type: {op_type}, please use 'rp' or 'rrp'.")
        return url

    def get_data(self, url: str) -> None:
        """Helper Method to fetch data"""
        response = json.loads((req.get(url)).content)['data']
        keys = [key for key in response]
        for key in keys:
            sub_data = json.loads(key['data'])
            op_date = sub_data['operationDt']
            del key['data']
            key['data'] = sub_data
            self.hashmap[op_date] = key

    def repo(self, asDict: bool = False) -> Union[pd.DataFrame, dict]:
        """
        Method to return repo operation data as DataFrame.

        asDict: If true returns data as dict, Defaults to False.
        """
        url = self.create_link("rp")
        self.get_data(url)
        if asDict:
            return self.hashmap
        return pd.DataFrame(self.hashmap)

    def reverse_repo(self, asDict: bool = False) -> Union[pd.DataFrame, dict]:
        """
        Method to return reverse repo operation data as DataFrame.

        asDict: If true returns data as dict, Defaults to False.
        """
        url = self.create_link("rrp")
        self.get_data(url)
        if asDict:
            return self.hashmap
        return pd.DataFrame(self.hashmap)

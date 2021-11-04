import json
from typing import Union

import pandas as pd
import requests as req


class Statements:
    """Methods for FOMC Statements"""

    def __init__(self, dates: Union[str, list, None] = None) -> None:
        self.url_base = "http://18.220.119.101:8080/fed/get-fomc-statement/"
        self.dates = dates

    def make_endpoint_query(self) -> str:
        """Method to create query for endpoint"""
        if self.dates and isinstance(self.dates, list):
            return self.url_base + ",".join(date for date in self.dates)
        elif self.dates:
            date = str(self.dates)
            return self.url_base + date
        else:
            return self.url_base

    def fetch_data(self) -> str:
        """Method to fetch data"""
        query = self.make_endpoint_query()
        response = (req.get(query).content).decode()
        return response

    def to_DataFrame(self) -> pd.DataFrame:
        response = json.loads(self.fetch_data())
        columns = ["date", "statement"]
        df = pd.concat([pd.DataFrame([[key, response[key]]], columns=columns) for key in response], ignore_index=True)
        return df

    def to_dict(self) -> dict:
        return json.loads(self.fetch_data())

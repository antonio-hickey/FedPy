import json

import pandas as pd
import requests as req


class Holdings:
    """SOMA portfolio holding details"""
    def __init__(self, url: str) -> None:
        self.hashmap: dict = {}
        self.response = json.loads(req.get(url).content)
        self.data = self.response["soma"]["holdings"]
        self.to_dict()

    def to_dict(self) -> None:
        for row in self.data:
            key = row['cusip']
            del row['cusip']
            self.hashmap[key] = row

    def fetch(self) -> pd.DataFrame:
        """Method to output a DataFrame."""
        return pd.DataFrame(self.hashmap)

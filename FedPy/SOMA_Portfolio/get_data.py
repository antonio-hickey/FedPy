import json
import pandas as pd


async def create_holdings(url: str, session):
    """Top level f(x) for creating Holdings Instance."""
    holdings = Holdings()
    await holdings._init(url, session)

    return holdings


class Holdings:
    """SOMA portfolio holding details"""
    def __init__(self) -> None:
        self.hashmap: dict = {}

    async def _init(self, url: str, session):
        _response = await session.get(url)
        response = _response.decode()
        self.data = json.loads(response)["soma"]["holdings"]
        self.to_dict()

    def to_dict(self) -> None:
        for row in self.data:
            key = row['cusip']
            del row['cusip']
            self.hashmap[key] = row

    def fetch(self) -> pd.DataFrame:
        """Method to output a DataFrame."""
        return pd.DataFrame(self.hashmap)


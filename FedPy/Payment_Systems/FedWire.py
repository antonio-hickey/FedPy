import pandas as pd
import requests as req
from bs4 import BeautifulSoup as bs


class FedWire:
    """Class of methods to fetch data for FedWire."""
    def __init__(self) -> None:
        self.url_base = "https://www.frbservices.org/resources/financial-services/"

    def to_DataFrame(self, data: list) -> pd.DataFrame:
        """Helper method to convert data to DataFrame."""
        for idx in enumerate(data[1]):
            data[2][idx[0]].insert(0, idx[1])
        return pd.DataFrame(columns=data[0], data=data[2])

    def funds(self) -> None:
        """Get DataFrame for FedWire funds data."""
        url = f"{self.url_base}wires/volume-value-stats/annual-stats.html"
        data = self.get_data(url)
        self.to_DataFrame(data)

    def securities(self) -> None:
        """Get DataFrame for FedWire securities data"""
        url = f"{self.url_base}securities/volume-value-stats/annual-stats.html"
        data = self.get_data(url)
        self.to_DataFrame(data)

    def get_data(self, url: str) -> list:
        """Helper method to fetch data from frbservices."""
        response = bs(req.get(url).content, "lxml").find("div", {"id": "content"})
        columns = [(i.text).replace('\n', ' ').replace('\r', '').replace('               ', '')
                   for i in response.findAll("th", {"scope": "col"})]
        years = [i.text for i in response.findAll("th", {"scope": "row"})]
        data = [i.text for i in response.findAll("td")]

        if 'securities' in url:
            rows = [data[i:i+8] for i in range(0, len(data), 8)]
        else:
            rows = [data[i:i+7] for i in range(0, len(data), 7)]
        return [columns, years, rows]

import pandas as pd
import requests as req
from bs4 import BeautifulSoup as bs

from FedPy.Payment_Systems import util


class FedWire:
    """Class of methods to fetch data for FedWire."""
    def __init__(self) -> None:
        self.url_base = "https://www.frbservices.org/resources/financial-services/"

    def funds(self) -> pd.DataFrame:
        """Get DataFrame for FedWire funds data."""
        url = f"{self.url_base}wires/volume-value-stats/annual-stats.html"
        data = self.get_data(url)
        return util.to_DataFrame(data)

    def securities(self) -> pd.DataFrame:
        """Get DataFrame for FedWire securities data."""
        url = f"{self.url_base}securities/volume-value-stats/annual-stats.html"
        data = self.get_data(url)
        return util.to_DataFrame(data)

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

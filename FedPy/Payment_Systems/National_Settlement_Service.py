import pandas as pd
import requests as req
from bs4 import BeautifulSoup as bs

from FedPy.Payment_Systems import util


class NSS:
    """Outputs a DataFrame of National Settlement Service data."""
    def __init__(self) -> None:
        self.url_base = 'https://www.frbservices.org/resources/financial-services/national-settlement-service/'
        self.url = f'{self.url_base}volume-value-stats/annual-stats.html'

    def get_data(self) -> list:
        """Helper method to fetch data."""
        response = bs(req.get(self.url).content, "lxml").find("div", {"id": "content"})
        columns = [(i.text).replace('\t', '').replace('\r\n', '').replace('  ', '').replace('1', '').replace('2', '')
                   .replace('(', ' (') for i in response.findAll("th", {"scope": "col"})]
        years = [i.text for i in response.findAll("th", {"scope": "row"})]
        data = [i.text for i in response.findAll("td")]
        rows = [data[i:i+8] for i in range(0, len(data), 8)]
        return [columns, years, rows]

    def fetch(self) -> pd.DataFrame:
        """Return DataFrame of National Settlement Service data."""
        return util.to_DataFrame(self.get_data())

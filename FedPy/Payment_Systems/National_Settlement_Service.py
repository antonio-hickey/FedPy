import pandas as pd
import requests as req
from bs4 import BeautifulSoup as bs


class NSS:
    def __init__(self) -> None:
        self.url_base = 'https://www.frbservices.org/resources/financial-services/national-settlement-service/'
        self.url = f'{self.url_base}volume-value-stats/annual-stats.html'
        self.to_DataFrame()

    def get_data(self) -> list:
        response = bs(req.get(self.url).content, "lxml").find("div", {"id": "content"})
        columns = [(i.text).replace('\t', '').replace('\r\n', '').replace('  ', '').replace('1', '').replace('2', '')
                   .replace('(', ' (') for i in response.findAll("th", {"scope": "col"})]
        years = [i.text for i in response.findAll("th", {"scope": "row"})]
        data = [i.text for i in response.findAll("td")]
        rows = [data[i:i+8] for i in range(0, len(data), 8)]
        return [columns, years, rows]

    def to_DataFrame(self) -> pd.DataFrame:
        data = self.get_data()
        for idx in enumerate(data[1]):
            data[2][idx[0]].insert(0, idx[1])
        return pd.DataFrame(columns=data[0], data=data[2])

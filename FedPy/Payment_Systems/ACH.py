import pandas as pd
import requests as req
from bs4 import BeautifulSoup as bs


class ACH:
    def __init__(self) -> None:
        self.comm_url = "https://www.federalreserve.gov/paymentsystems/fedach_yearlycomm.htm"
        self.govt_url = "https://www.federalreserve.gov/paymentsystems/fedach_yearlygovt.htm"

    def get_data(self, url: str = "") -> list:
        if url == "":
            url = self.comm_url
        response = bs(req.get(url).content, "lxml").find("div", {"class": "container container__main"})
        columns = [(i.text).replace('\n', ' ').replace('\t', '') for i in response.findAll("th")]
        years = [i.text for i in response.findAll("td", {"class": "left"})]
        data = [i.text.replace(',', '') for i in response.findAll("td", {"class": "left2"})]
        rows = [data[i:i+7] for i in range(0, len(data), 7)]
        return [columns, years, rows]

    def get_all_format(self, url: str) -> list:
        response = bs(req.get(url).content, "lxml").find("div", {"class": "container container__main"})
        columns = [(i.text).replace('\n', ' ').replace('\t', '') for i in response.findAll("th")]
        years = [i.text for i in response.findAll("td", {"class": "left"})]
        data = [float(i.text.replace(',', '').replace('n.a.', '0')) for i in response.findAll("td", {"class": "left2"})]
        rows = [data[i:i+7] for i in range(0, len(data), 7)]
        return [columns, years, rows]

    def to_DataFrame(self, data: list) -> pd.DataFrame:
        for idx in enumerate(data[1]):
            data[2][idx[0]].insert(0, idx[1])
        return pd.DataFrame(columns=data[0], data=data[2])

    def commercial(self) -> pd.DataFrame:
        url = self.comm_url
        data = self.get_data(url)
        return self.to_DataFrame(data)

    def government(self) -> pd.DataFrame:
        url = self.govt_url
        data = self.get_data(url)
        return self.to_DataFrame(data)

    def all(self) -> pd.DataFrame:
        comm = self.to_DataFrame(self.get_all_format(self.comm_url))
        govt = self.to_DataFrame(self.get_all_format(self.govt_url))

        df = pd.DataFrame()
        df[comm.columns[0]] = comm[comm.columns[0]]
        df[comm.columns[1]] = comm[comm.columns[1]] + govt[govt.columns[1]]
        df[comm.columns[3]] = comm[comm.columns[3]] + govt[govt.columns[3]]
        df[comm.columns[5]] = comm[comm.columns[5]] + govt[govt.columns[5]]
        df[comm.columns[6]] = comm[comm.columns[6]] + govt[govt.columns[6]]
        df[comm.columns[7]] = comm[comm.columns[7]] + govt[govt.columns[7]]
        return df

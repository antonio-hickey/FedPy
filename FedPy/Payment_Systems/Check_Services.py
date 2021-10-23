import pandas as pd
import requests as req
from bs4 import BeautifulSoup as bs


class Check_Services:
    """Class of methods to fetch data for check services"""
    def __init__(self) -> None:
        url_base = "https://www.federalreserve.gov/paymentsystems/check_"
        self.urls = {
            'Commercial Collected': f"{url_base}commcheckcolannual.htm",
            'Commercial Returned': f"{url_base}commcheckretannual.htm",
            'Government Checks': f"{url_base}govcheckprocannual.htm",
            'Postal Money Orders': f"{url_base}postalmosprocannual.htm",
        }

    def get_data(self, url: str) -> list:
        """Helper Method to get data for a specific url"""
        if "commcheckret" in url:
            response = bs(req.get(url).content, "lxml").find("table", {"class": "pubtables"})
        else:
            response = bs(req.get(url).content, "lxml").find("div", {"class": "data-table"})
        columns = [(i.text).replace('\n', ' ').replace('\t', '') for i in response.findAll("th", {"scope": "col"})]
        years = [i.text for i in response.findAll("td", {"class": "left"})]
        data = [float(i.text.replace(',', '').replace('n.a.', 'NaN')) for i in response.findAll("td", {"class": "left2"})]
        rows = [data[i:i+7] for i in range(0, len(data), 7)]
        return [columns, years, rows]

    def to_DataFrame(self, data: list) -> pd.DataFrame:
        """Helper method to convert data to DataFrame."""
        for idx in enumerate(data[1]):
            data[2][idx[0]].insert(0, idx[1])
        return pd.DataFrame(columns=data[0], data=data[2])

    def all(self) -> pd.DataFrame:
        """
        Get Volume and Value data
        for all Check Services.
        """
        df = self.cr()
        df[df.columns[3]].iloc[-1] = 0
        df[df.columns[3]].iloc[-2] = 0
        df[df.columns[1]] = df[df.columns[1]] + (self.cc()[df.columns[1]] + self.gc()[df.columns[1]] + self.pmo()[df.columns[1]])
        df[df.columns[3]] = df[df.columns[3]] + (self.cc()[df.columns[3]] + self.gc()[df.columns[3]] + self.pmo()[df.columns[3]])
        return(df[[df.columns[1], df.columns[3]]])

    def cc(self) -> pd.DataFrame:
        """Get data for Commercial Checks Collected."""
        data = self.get_data(self.urls['Commercial Collected'])
        return self.to_DataFrame(data)

    def cr(self) -> pd.DataFrame:
        """Get data for Commercial Checks Returned."""
        data = self.get_data(self.urls['Commercial Returned'])
        return self.to_DataFrame(data)

    def gc(self) -> pd.DataFrame:
        """Get data for Goverment Checks Processed."""
        data = self.get_data(self.urls['Government Checks'])
        return self.to_DataFrame(data)

    def pmo(self) -> pd.DataFrame:
        """Get data for Postal Money Orders Processed."""
        data = self.get_data(self.urls['Postal Money Orders'])
        return self.to_DataFrame(data)

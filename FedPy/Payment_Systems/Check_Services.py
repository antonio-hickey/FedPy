import pandas as pd
import requests as req
from bs4 import BeautifulSoup as bs

from FedPy.Payment_Systems import util


class Check_Services:
    def __init__(self) -> None:
        url_base = "https://www.federalreserve.gov/paymentsystems/check_"
        self.urls = {
            'Commercial Collected': f"{url_base}commcheckcolannual.htm",
            'Commercial Returned': f"{url_base}commcheckretannual.htm",
            'Government Checks': f"{url_base}govcheckprocannual.htm",
            'Postal Money Orders': f"{url_base}postalmosprocannual.htm",
        }

    def get_data(self, url: str) -> list:
        """Helper Method to get data for a specific url."""
        if "commcheckret" in url:
            response = bs(req.get(url).content, "lxml").find("table", {"class": "pubtables"})
        else:
            response = bs(req.get(url).content, "lxml").find("div", {"class": "data-table"})
        columns = [(i.text).replace('\n', ' ').replace('\t', '') for i in response.findAll("th", {"scope": "col"})]
        years = [i.text for i in response.findAll("td", {"class": "left"})]
        data = [float(i.text.replace(',', '').replace('n.a.', 'NaN')) for i in response.findAll("td", {"class": "left2"})]
        rows = [data[i:i+7] for i in range(0, len(data), 7)]
        return [columns, years, rows]

    def all(self) -> pd.DataFrame:
        """Get Volume and Value data for all Check Services."""
        cr, cc, gc, pmo = self.cr(), self.cc(), self.gc(), self.pmo()

        df = cr.copy()
        df.drop(df.columns[[2, 4, 5, 6, 7]], axis=1, inplace=True)
        n = df.index.size
        df.loc[(n-1), df.columns[2]] = 0
        df.loc[(n-2), df.columns[2]] = 0
        df[df.columns[1]] = df[df.columns[1]] + (cc[cc.columns[1]] + gc[gc.columns[1]] + pmo[pmo.columns[1]])
        df[df.columns[2]] = df[df.columns[2]] + (cc[cc.columns[3]] + gc[gc.columns[3]] + pmo[pmo.columns[3]])
        return(df)

    def cc(self) -> pd.DataFrame:
        """Get data for Commercial Checks Collected."""
        data = self.get_data(self.urls['Commercial Collected'])
        return util.to_DataFrame(data)

    def cr(self) -> pd.DataFrame:
        """Get data for Commercial Checks Returned."""
        data = self.get_data(self.urls['Commercial Returned'])
        return util.to_DataFrame(data)

    def gc(self) -> pd.DataFrame:
        """Get data for Goverment Checks Processed."""
        data = self.get_data(self.urls['Government Checks'])
        return util.to_DataFrame(data)

    def pmo(self) -> pd.DataFrame:
        """Get data for Postal Money Orders Processed."""
        data = self.get_data(self.urls['Postal Money Orders'])
        return util.to_DataFrame(data)

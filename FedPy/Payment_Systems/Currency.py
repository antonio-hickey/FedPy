import pandas as pd
import requests as req
from bs4 import BeautifulSoup as bs

from FedPy.Payment_Systems import util


class Currency:
    def ic_get_data(self, url: str) -> list:
        """
        Helper method to get data for
        currency in circulation.
        """
        response = bs(req.get(url).content, "lxml").find("div", {"class": "data-table"})
        columns = [(i.text).replace('\n', ' ').replace('\t', '') for i in response.findAll("th", {"scope": "col"})]
        years = [i.text for i in response.findAll("td", {"class": "left"})]
        if "value" in url:
            data = [i.text.replace(',', '').replace('.', '') + "000000000" for i in response.findAll("td", {"class": "left2"})]
        else:
            data = [i.text.replace(',', '') for i in response.findAll("td", {"class": "left2"})]
        rows = [data[i:i+9] for i in range(0, len(data), 9)]
        return [columns, years, rows]

    def in_circulation(self, _type: str = "value") -> pd.DataFrame:
        """
        Outputs a DataFrame of either value or
        volume of currency in circulation.
        """
        if _type in ["value", "Value", "val", "Val"]:
            url = "https://www.federalreserve.gov/paymentsystems/coin_currcircvalue.htm"
        elif _type in ["volume", "Volume", "vol", "Vol"]:
            url = "https://www.federalreserve.gov/paymentsystems/coin_currcircvolume.htm"
        else:
            raise ValueError(f"Invalid pass of type: {_type}, Please choose value or volume.")
        data = self.ic_get_data(url)
        return util.to_DataFrame(data)

    def pc_get_data(self, url: str) -> list:
        """
        Helper method to get data for
        the cost to print new currency.
        """
        response = bs(req.get(url).content, "lxml").find("div", {"class": "data-table"})
        columns = [(i.text).replace('\n', ' ').replace('\t', '') for i in response.findAll("th", {"scope": "col"})]
        years = [i.text for i in response.findAll("td", {"class": "left"})]
        data = [int(i.text.replace(',', '').replace('$', '') + "000000") for i in response.findAll("td", {"class": "left2"})]
        rows = [data[i:i+1] for i in range(0, len(data), 1)]
        return [columns, years, rows]

    def printing_cost(self) -> pd.DataFrame:
        """
        Outputs a DataFrame of cost
        to print new currency.
        """
        url = "https://www.federalreserve.gov/paymentsystems/coin_costnewcurr.htm"
        data = self.pc_get_data(url)
        return util.to_DataFrame(data)

    def operation_expenses(self) -> pd.DataFrame:
        """
        Outputs a DataFrame of cash operation
        expenses, including (processing, paying,
        recieving, verification, destruction,
        transportation, and non-standerd packaging).
        """
        url = "https://www.federalreserve.gov/paymentsystems/coin_expcashops.htm"
        data = self.pc_get_data(url)
        return util.to_DataFrame(data)

    def payments_get_data(self, url: str) -> pd.DataFrame:
        """Helper method to get data for payments."""
        response = bs(req.get(url).content, "lxml").find("div", {"class": "data-table"})
        columns = [(i.text).replace('\n', ' ').replace('\t', '') for i in response.findAll("th", {"scope": "col"})]
        years = [i.text for i in response.findAll("td", {"class": "left"})]
        if "value" in url:
            data = [i.text.replace(',', '').replace('.', '') + "000000000" for i in response.findAll("td", {"class": "left2"})]
        else:
            data = [i.text.replace(',', '') for i in response.findAll("td", {"class": "left2"})]
        rows = [data[i:i+8] for i in range(0, len(data), 8)]
        return [columns, years, rows]

    def payments(self, _type: str = "val") -> pd.DataFrame:
        """
        Outputs a DataFrame of payments of
        currency for either value or volume.
        """
        if _type in ["value", "Value", "val", "Val"]:
            url = "https://www.federalreserve.gov/paymentsystems/coin_paycurrcircvalue.htm"
        elif _type in ["volume", "Volume", "vol", "Vol"]:
            url = "https://www.federalreserve.gov/paymentsystems/coin_paycurrcircvolume.htm"
        else:
            raise ValueError(f"Invalid pass of type: {_type}, Please choose value or volume.")
        data = self.payments_get_data(url)
        return util.to_DataFrame(data)

    def reciepts(self, _type: str = "val") -> pd.DataFrame:
        """
        Outputs a DataFrame of reciepts of currency
        from circulation for either value or volume.
        """
        if _type in ["value", "Value", "val", "Val"]:
            url = "https://www.federalreserve.gov/paymentsystems/coin_reccurrcircvalue.htm"
        elif _type in ["volume", "Volume", "vol", "Vol"]:
            url = "https://www.federalreserve.gov/paymentsystems/coin_reccurrcircvolume.htm"
        else:
            raise ValueError(f"Invalid pass of type: {_type}, Please choose value or volume.")
        data = self.payments_get_data(url)
        return util.to_DataFrame(data)

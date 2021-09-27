import pandas as pd
import requests as req
from bs4 import BeautifulSoup as bs
from scripts.SOMA import get_data
from util.SOMA import links


class SOMA:
    """ System Open Market Operations Portfolio Methods
        Sourced: New York Federal Reserve (https://markets.newyorkfed.org) """
    def __init__(self) -> None:
        self.summary_url = links.Create().summary()
        self.summary_response = req.get(self.summary_url)
        self.summary_parsed = bs(self.summary_response.content, "lxml")
        self.summary_data = self.summary_parsed.find("summary")

    def summary(self) -> dict:
        """ Output's a dictionary summary
            of the current SOMA portfolio. """
        return {
            "Date": self.summary_data.find("asofdate").text,
            "Total": self.summary_data.find("total").text,
            "Bills": self.summary_data.find("bills").text,
            "Notes & Bonds": self.summary_data.find("notesbonds").text,
            "TIPS": self.summary_data.find("tips").text,
            "FRN": self.summary_data.find("frn").text,
            "CMBS": self.summary_data.find("cmbs").text,
            "MBS": self.summary_data.find("mbs").text,
            "Agencies": self.summary_data.find("agencies").text,
        }

    def hist(self) -> pd.DataFrame:
        """ Output's a dictionary summary
            of the historic SOMA portfolio. """
        return pd.read_csv(links.SOMA_HIST)

    def total(self) -> float:
        """ Output's a float of the Total
            current SOMA portfolio. """
        return float(self.summary_data.find("total").text)

    def bills(self) -> pd.DataFrame:
        """ Outputs a DataFrame of current
            SOMA portfolio bills holdings. """
        url = links.Create().current_holdings("bills")
        return get_data.Holdings(url).bills_data()

    def notes_bonds(self) -> pd.DataFrame:
        """ Outputs a DataFrame of current
            SOMA notes & bonds holdings. """
        url = links.Create().current_holdings("notesbonds")
        return get_data.Holdings(url).notesbonds_data()

    def tips(self) -> pd.DataFrame:
        """ Outputs a DataFrame of current
            SOMA portfolio TIPS holdings. """
        url = links.Create().current_holdings("tips")
        return get_data.Holdings(url).tips_data()

    def cmbs(self) -> pd.DataFrame:
        """ Outputs a DataFrame of current
            SOMA portfolio CMBS holdings. """
        url = links.Create().current_holdings("cmbs")
        return get_data.Holdings(url).cmbs_data()

    def frn(self) -> pd.DataFrame:
        """ Outputs a DataFrame of current
            SOMA portfolio FRN holdings. """
        url = links.Create().current_holdings("frn")
        return get_data.Holdings(url).frn_data()

    def agency_debts(self) -> pd.DataFrame:
        """ Outputs a DataFrame of current SOMA
            portfolio Agency Debt holdings. """
        url = links.Create().current_holdings("agency debts")
        return get_data.Holdings(url).agencydebts_data()

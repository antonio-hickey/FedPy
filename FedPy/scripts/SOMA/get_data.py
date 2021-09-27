import pandas as pd
import requests as req
from bs4 import BeautifulSoup as bs


class Holdings:
    """ Fetching Holdings Data """

    def __init__(self, url: str) -> None:
        """ Reusable variables """
        self.response = req.get(url)
        self.parsed = bs(self.response.content, "lxml")
        self.data = self.parsed.findAll("holding")
        self.hashmap = {'Date': [i.find("asofdate").text for i in self.data]}
        self.hashmap['CUSIP'] = [i.find("cusip").text for i in self.data]
        self.hashmap['Type'] = [i.find("securitytype").text for i in self.data]
        try:
            """ Reusable variables for select functions """
            self.hashmap['Par Value'] = [i.find("parvalue").text for i in self.data]
            self.hashmap['Maturity'] = [i.find("maturitydate").text for i in self.data]
            self.hashmap['Change From Week Ago'] = [i.find("changefrompriorweek").text for i in self.data]
            self.hashmap['Precent Out'] = [i.find("percentoutstanding").text for i in self.data]
        except AttributeError:
            """ Pass if function cant use x variable """
            pass

    def cmbs_data(self) -> pd.DataFrame:
        self.hashmap['Face Value'] = [i.find("currentfacevalue").text for i in self.data]
        self.hashmap['Description'] = [i.find("securitydescription").text for i in self.data]
        return pd.DataFrame(self.hashmap)

    def bills_data(self) -> pd.DataFrame:
        return pd.DataFrame(self.hashmap)

    def notesbonds_data(self) -> pd.DataFrame:
        self.hashmap['Coupon'] = [i.find("coupon").text for i in self.data]
        return pd.DataFrame(self.hashmap)

    def tips_data(self) -> pd.DataFrame:
        self.hashmap['Coupon'] = [i.find("coupon").text for i in self.data]
        self.hashmap['Inflation Comp'] = [i.find("inflationcompensation").text for i in self.data]
        return pd.DataFrame(self.hashmap)

    def frn_data(self) -> pd.DataFrame:
        self.hashmap['Spread'] = [i.find("spread").text for i in self.data]
        return pd.DataFrame(self.hashmap)

    def agencydebts_data(self) -> pd.DataFrame:
        self.hashmap['Coupon'] = [i.find("coupon").text for i in self.data]
        self.hashmap['Issuer'] = [i.find("issuer").text for i in self.data]
        return pd.DataFrame(self.hashmap)

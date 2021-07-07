from bs4 import BeautifulSoup as bs
import requests as req
import pandas as pd

class Transcripts:

    """
        Returns a Pandas DataFrame of historic FOMC statements    
    """
    def hist_fomc_statements():

        # Create pandas DataFrame of the dataset
        URL = "https://raw.githubusercontent.com/antonio-hickey/FedPy/main/FedPy/data/fomc_statement_historic.csv"
        df = pd.read_csv(URL)

        return df
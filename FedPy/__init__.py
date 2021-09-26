from typing import Optional
from .SOMA.soma import SOMA
from .TOMO.tomo import TOMO
from .FRED.fred import Fred
from .FOMC_Statement.statements import Transcripts
import pandas as pd

"""
    System Open Market Operations:

        - Commands:
            - "soma_hist()" = Returns Pandas DataFrame of
                              historical SOMA portfolio Summary.

            - "soma()" = Returns pandas DataFrame of
                        current SOMA portfolio Summary.

            - "soma_total()" = Returns a float of the total
                               current SOMA portfolio.

            - "soma_bills()" = Returns a Pandas DataFrame of
                               current bills in SOMA portfolio.

            - "soma_notesbonds()" = Returns a Pandas DataFrame of
                                    current Notes & Bonds in SOMA portfolio.

            - "soma_tips()" = Returns a Pandas DataFrame of 
                              current TIPS in SOMA portfolio.
            
            - "soma_frn()" = Returns a Pandas DataFrame of
                              current FRNs in SOMA portfolio.

            - "soma_agencies()" = Returns a Pandas DataFrame of
                                  current Agency Debts in SOMA portfolio.

            - "soma_cmbs()" = Returns a Pandas DataFrame of
                              current CMBS in SOMA portfolio.
"""

def soma_hist() -> pd.DataFrame:
    return SOMA.Hist()

def soma() -> pd.DataFrame:
    return SOMA.Summary()

def soma_total() -> float:
    return SOMA.Total()

def soma_bills() -> pd.DataFrame:
    return SOMA.Bills()

def soma_notesbonds() -> pd.DataFrame:
    return SOMA.NotesBonds()

def soma_tips() -> pd.DataFrame:
    return SOMA.TIPS()

def soma_frn() -> pd.DataFrame:
    return SOMA.FRNs()

def soma_agencies() -> pd.DataFrame:
    return SOMA.AgencyDebts()

def soma_cmbs() -> pd.DataFrame:
    return SOMA.CMBS()

"""
    Temporary Open Market Operations:
        
        - Commands:
            - "recent_rp()" = Returns a dictionary of data
                              on recent Repo Operations.

            - "recent_rrp()" = Returns a dictionary of data
                                on recent Reverse Repo Operations.
"""

def tomo_rp() -> dict:
    return TOMO.recent_rp()

def tomo_rrp() -> dict:
     return TOMO.recent_rrp()


"""
    Federal Reserve Economic Data:

        - Commands:
            - "fred(key, series_id, *start, *end)" = Returns a pandas DataFrame of any
                                                     FRED dataset, but requires the inputs
                                                     data series id, and your free api key.
"""

def fred(key: str, series_id: str, start: Optional[str]=None,
         end: Optional[str]=None) -> pd.DataFrame:
        fred = Fred(api_key=key)
        data = fred.get_series(series_id)

        return data

"""
    FOMC Statements:

        - Commands:
            - "fomc_statements()" = Returns a pandas DataFrame of historic
                                    FOMC statements going back to 2006 to today.
"""

def fomc_statements() -> pd.DataFrame:
    return Transcripts.hist_fomc_statements()

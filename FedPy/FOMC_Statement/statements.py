import pandas as pd


class Transcripts:
    """ Methods for FOMC Transcripts """

    def __init__(self) -> None:
        self.url = "https://raw.githubusercontent.com/antonio-hickey/FedPy/main/FedPy/data/fomc_statement_historic.csv"

    def historic(self) -> pd.DataFrame:
        """ Returns a Pandas DataFrame
            of historic FOMC statements. """
        return pd.read_csv(self.url)

    def latest(self) -> pd.Series:
        """ Returns a Pandas DataFrame of
            the most recent FOMC statement. """
        return pd.read_csv(self.url).iloc[0]

    def previous(self) -> pd.Series:
        """ Returns a Pandas DataFrame of the
            most previous FOMC statement. """

        return pd.read_csv(self.url).iloc[1]

# TODO: Add a compare func for latest and previous

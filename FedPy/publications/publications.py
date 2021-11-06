from typing import Union

import pandas as pd

from FedPy.publications.fomc_statements import fomc_statement


class Publications:
    def __init__(self) -> None:
        self.meta = "blank for now, but need in future"

    def fomc_statement(
        self,
        dates: Union[str, list, None] = None,
        asDict: bool = False,
    ) -> Union[pd.DataFrame, dict]:
        """
        Get FOMC statements for given date or dates

        `dates`: YYYY-MM-DD, or 'current', or 'previous'
        `asDict`: True or False, will return as dictionary if True.
        """
        return fomc_statement(dates, asDict)

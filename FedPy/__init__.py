from typing import Optional

import pandas as pd

from FedPy.Payment_Systems.ACH import ACH  # noqa
from FedPy.Payment_Systems.Check_Services import Check_Services  # noqa
from FedPy.Payment_Systems.Currency import Currency  # noqa
from FedPy.Payment_Systems.FedWire import FedWire  # noqa
from FedPy.Payment_Systems.National_Settlement_Service import NSS  # noqa

from .FOMC_Statement.statements import Statements  # noqa
from .FRED.fred import Fred
from .SOMA_Portfolio.soma import SOMA  # noqa
from .TOMO.tomo import TOMO  # noqa


def FRED(key: str, series_id: str, start: Optional[str] = None,
         end: Optional[str] = None) -> pd.Series:
    fred = Fred(api_key=key)
    return fred.get_series(series_id, start=start, end=end)

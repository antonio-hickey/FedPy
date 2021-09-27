from typing import Optional

import pandas as pd

from .FOMC_Statement.statements import Transcripts  # noqa
from .FRED.fred import Fred
from .SOMA.soma import SOMA  # noqa
from .TOMO.tomo import TOMO  # noqa


def FRED(key: str, series_id: str, start: Optional[str] = None,
         end: Optional[str] = None) -> pd.Series:
    fred = Fred(api_key=key)
    return fred.get_series(series_id, start=start, end=end)

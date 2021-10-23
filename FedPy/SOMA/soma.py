import json
from typing import Union

import pandas as pd
import requests as req

from ..util.SOMA import links
from . import get_data


class SOMA:
    def summary(self) -> pd.DataFrame:
        """
        Method to output a summary of the
        current SOMA portfolio as a dict.
        """
        url = links.Create().summary()
        hashmap = json.loads(req.get(url).content)['soma']['summary']
        return pd.DataFrame(hashmap)

    def total(self) -> float:
        """
        Method to output a float of
        the total current SOMA portfolio.
        """
        return float(self.summary()['total'])

    def holdings(self, security_type: Union[str, list[str]]) -> pd.DataFrame:
        """
        Method to output a DataFrame of specific
        securties held in the SOMA portfolio.
        """
        url = links.Create().holdings(security_type)
        return get_data.Holdings(url).fetch()

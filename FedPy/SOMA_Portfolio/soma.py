import json
from typing import Union

import pandas as pd

from ..util.SOMA import links
from ..web_client import ClientSession

from .get_data import create_holdings


class SOMA:
    def __init__(self, session):
        self.session = session

    async def summary(self) -> pd.DataFrame:
        """
        Method to output a summary of the
        current SOMA portfolio as a dict.
        """
        url = links.Create().summary()
        hashmap = json.loads(await self.session.get(url).content)['soma']['summary']
        async with ClientSession() as session:
            hashmap = json.loads(await session.fetch(url))
        return pd.DataFrame(hashmap)

    def total(self) -> float:
        """
        Method to output a float of
        the total current SOMA portfolio.
        """
        return float(self.summary()['total'])

    async def holdings(self, security_type: Union[str, list[str]]) -> pd.DataFrame:
        """
        Method to output a DataFrame of specific
        securties held in the SOMA portfolio.
        """
        session = await self.session.__aenter__()
        url = links.Create().holdings(security_type)
        holdings = await create_holdings(url, session)
        return holdings.fetch()

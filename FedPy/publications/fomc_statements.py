import json
from typing import Union

import pandas as pd
import requests as req


def fomc_statement(
    dates: Union[str, list[str], None] = None,
    asDict: bool = False,
) -> Union[pd.DataFrame, dict]:
    """
    Get FOMC statements for given date or dates.

    `dates`: YYYY-MM-DD, or 'current', or 'previous'.
    `asDict`: True or False, will return as dictionary if True.
    """
    url = make_endpoint_query(dates)
    if asDict:
        return to_dict(url)
    return to_DataFrame(url)


def make_endpoint_query(dates: Union[str, list[str], None] = None) -> str:
    """Method to create query for endpoint."""
    url_base = "http://18.220.119.101:8080/fed/get-fomc-statement/"
    if dates and isinstance(dates, list):
        return url_base + ",".join(date for date in dates)
    elif dates:
        date = str(dates)
        return url_base + date
    else:
        return url_base


def fetch_data(url: str) -> str:
    """Method to fetch data."""
    response = (req.get(url).content).decode()
    return response


def to_DataFrame(url: str) -> pd.DataFrame:
    """Method to convert and return as DataFrame."""
    response = json.loads(fetch_data(url))
    columns = ["date", "statement"]
    df = pd.concat([pd.DataFrame([[key, response[key]]], columns=columns) for key in response], ignore_index=True)
    return df


def to_dict(url: str) -> dict:
    """Method to convert and return as dictionary."""
    return json.loads(fetch_data(url))

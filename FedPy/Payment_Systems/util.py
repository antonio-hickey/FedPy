import pandas as pd


def to_DataFrame(data: list) -> pd.DataFrame:
    """Helper method to convert data to DataFrame."""
    for idx in enumerate(data[1]):
        data[2][idx[0]].insert(0, idx[1])
    return pd.DataFrame(columns=data[0], data=data[2])

import pandas as pd


def deduplicate_categories(data: pd.DataFrame, column_name: str) -> pd.Series:

    duplicated = data[column_name].str.split(";").apply(lambda x: len(x) != len(set(x)))
    return data[~duplicated]

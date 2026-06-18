import pandas as pd


def deduplicate_categories(data: pd.DataFrame, column_name: str) -> pd.Series:

    duplicated = data[column_name].str.split(";").apply(lambda x: len(x) != len(set(x)))
    return data[~duplicated]


def freq_of_freqs(data: pd.Series) -> pd.DataFrame:
    count = data.value_counts().reset_index(name="count")
    return count.value_counts().reset_index(name="frequency")


def calculate_stadistics(column: pd.Series) -> dict:
    return {
        "count": column.count(),
        "mean": column.mean(),
        "mode": column.mode()[0],
        "median": column.median(),
        "max": column.max(),
        "min": column.min(),
    }

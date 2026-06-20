import pandas as pd


def deduplicate_categories(data: pd.DataFrame, column_name: str) -> pd.Series:

    duplicated = data[column_name].str.split(";").apply(lambda x: len(x) != len(set(x)))
    return data[~duplicated]


def freq_of_freqs(data: pd.Series[list[str]]) -> pd.DataFrame:
    freq_of_freqs = data.value_counts().reset_index(name="count")
    freq_of_freqs["frequency"] = freq_of_freqs["count"].map(
        freq_of_freqs["count"].value_counts()
    )
    return freq_of_freqs


def calculate_stadistics(column: pd.Series) -> dict:
    return {
        "count": column.size,
        "mean": column.mean().round(0),
        "mode": column.mode()[0],
        "median": column.median(),
        "max": column.max(),
        "min": column.min(),
    }

import numpy as np
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


def group_and_sum(
    data: pd.DataFrame, groups: pd.Series, group_by: str, sum_by: str
) -> list:
    grouped = data.groupby(group_by)[sum_by]
    result = []
    for group in groups:
        group_count = grouped.apply(lambda x: x.str.contains(group).sum())
        result.append(
            {
                "index": group_count.index,
                "value": group_count.values,
                "label": group,
            }
        )
    return result


def tfidf_weight_binary(df, cols):
    X = df[cols].values.astype(float)
    n_docs = X.shape[0]
    df_freq = X.sum(axis=0)
    idf = np.log(n_docs / (df_freq + 1)) + 1
    return (X * idf).astype("float32")

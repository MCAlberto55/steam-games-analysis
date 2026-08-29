import numpy as np
import pandas as pd
from scipy.spatial.distance import pdist, squareform


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


def tfidf_weight_binary(data: pd.DataFrame):
    rows = data.shape[0]
    frequencies = data.sum(axis=0)
    idf = np.log(rows / (frequencies + 1)) + 1
    return (data * idf).astype("float32")


# Need to evaluate silhouette score using the same dissimilarity measure KPrototypes uses internally.
def kprototypes_dissimilarity(X_num, X_cat, gamma):
    """X_num: Numerical columns. X_cat: Categorical columns. gamma: Trained model gamma."""
    dist = squareform(pdist(X_num, metric="sqeuclidean"))

    n_cat = X_cat.shape[0]
    cat_dist = np.zeros((n_cat, n_cat))
    for col in range(X_cat.shape[1]):
        col_vals = X_cat[:, col].reshape(-1, 1)
        cat_dist += (col_vals != col_vals.T).astype(float)

    return dist + gamma * cat_dist

import numpy as np
import pandas as pd


def print_stadistics(column: pd.Series, title: str) -> str:
    data = column.value_counts()
    mean, mode, median, max_date, min_date = (
        data.mean(),
        data.mode()[0],
        data.median(),
        data.max(),
        data.min(),
    )

    output = f"""
    {title}
    ================================================
    Count:                {data.count()}
    Above-average values: {data[data > mean].count()}
    Mean:                 {mean:.0f}
    Mode:                 {mode}
    Median:               {median:.0f}
    Max:                  {max_date}
    Min:                  {min_date}
    """
    return output

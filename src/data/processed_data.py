import pandas as pd
from src.utils.config import VALIDATED_DATA_PATH


def get_validated_data():
    Validated_data = pd.read_parquet(VALIDATED_DATA_PATH)
    return Validated_data

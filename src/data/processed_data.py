import pandas as pd
from src.utils.config import VALIDATED_DATA_PATH
from src.utils.config import FEATURE_ENGINEERED_DATA_PATH


def get_validated_data():
    Validated_data = pd.read_parquet(VALIDATED_DATA_PATH)
    return Validated_data


def get_featured_data():
    Featured_data = pd.read_parquet(FEATURE_ENGINEERED_DATA_PATH, index_col=0)
    return Featured_data

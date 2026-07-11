import pandas as pd
from src.utils.config import VALIDATED_DATA_PATH
from src.utils.config import FEATURE_ENGINEERED_DATA_PATH


def get_validated_data():
    Validated_data = pd.read_parquet(VALIDATED_DATA_PATH)
    return Validated_data


def get_feature_engineered_data():
    Feature_engineered_data = pd.read_parquet(FEATURE_ENGINEERED_DATA_PATH)
    return Feature_engineered_data

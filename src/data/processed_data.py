import pandas as pd
from src.utils.config import VALIDATED_DATA_PATH
from src.utils.config import FE_OHE_DATA_PATH
from src.utils.config import FE_WEIGHTED_DATA_FILE_NAME


def get_validated_data():
    Validated_data = pd.read_parquet(VALIDATED_DATA_PATH)
    return Validated_data


def get_fe_ohe_data():
    Feature_engineered_data = pd.read_parquet(FE_OHE_DATA_PATH)
    return Feature_engineered_data


def get_fe_weighted_data():
    Feature_engineered_data = pd.read_parquet(FE_WEIGHTED_DATA_FILE_NAME)
    return Feature_engineered_data

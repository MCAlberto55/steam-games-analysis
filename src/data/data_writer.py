import json
import pandas as pd
from src.utils.config import (
    FE_OHE_DATA_PATH,
    FE_OUTPUT_PARAMS_PATH,
    FE_WEIGHTED_DATA_PATH,
    OHE_DATAFRAME_LABELS,
    OHE_TEST_LABELS_PATH,
    TRAINING_OUTPUT_PARAMS_PATH,
    TRAINING_SET_PATH,
    VALIDATION_SET_PATH,
    WEIGHTED_DATAFRAME_LABELS,
    WEIGHTED_TEST_LABELS_PATH,
)


# Dataframes
def export_fe_weighted_data(data: pd.DataFrame):
    data.to_parquet(FE_WEIGHTED_DATA_PATH, index=True)


def export_fe_ohe_data(data: pd.DataFrame):
    data.to_parquet(FE_OHE_DATA_PATH, index=True, engine="pyarrow")


def export_Xtrain_data(data: pd.DataFrame):
    data.to_parquet(TRAINING_SET_PATH, index=True)


def export_Xtest_data(data: pd.DataFrame):
    data.to_parquet(VALIDATION_SET_PATH, index=True)


def export_ohe_Ytrain(data: pd.DataFrame):
    data.to_parquet(OHE_DATAFRAME_LABELS, index=True)


def export_weighted_Ytrain(data: pd.DataFrame):
    data.to_parquet(WEIGHTED_DATAFRAME_LABELS, index=True)


def export_ohe_Ytest(data: pd.DataFrame):
    data.to_parquet(OHE_TEST_LABELS_PATH, index=True)


def export_weighted_Ytest(data: pd.DataFrame):
    data.to_parquet(WEIGHTED_TEST_LABELS_PATH, index=True)


# Params
def export_fe_params(params: dict):
    with open(FE_OUTPUT_PARAMS_PATH, "w", encoding="utf-8") as f:
        json.dump(params, f, ensure_ascii=False, indent=4)


def export_training_params(params: dict):
    with open(TRAINING_OUTPUT_PARAMS_PATH, "w", encoding="utf-8") as f:
        json.dump(params, f, ensure_ascii=False, indent=4)

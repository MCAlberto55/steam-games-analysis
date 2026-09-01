import json
import pandas as pd
from src.utils.config import (
    EDA_OUTPUT_PARAMS_PATH,
    FE_OHE_DATA_PATH,
    FE_OUTPUT_PARAMS_PATH,
    FE_WEIGHTED_DATA_PATH,
    OHE_DATAFRAME_LABELS,
    OHE_TEST_LABELS_PATH,
    TRAINING_OUTPUT_PARAMS_PATH,
    TRAINING_SET_PATH,
    VALIDATED_DATA_PATH,
    VALIDATION_SET_PATH,
    WEIGHTED_DATAFRAME_LABELS,
    WEIGHTED_TEST_LABELS_PATH,
)


# Processed Datasets
def get_validated_data():
    Validated_data = pd.read_parquet(VALIDATED_DATA_PATH)
    return Validated_data


def get_fe_ohe_data():
    ohe_fe_engineered_data = pd.read_parquet(FE_OHE_DATA_PATH)
    return ohe_fe_engineered_data


def get_fe_weighted_data():
    weighted_fe_engineered_data = pd.read_parquet(FE_WEIGHTED_DATA_PATH)
    return weighted_fe_engineered_data


# Params
def load_eda_params():
    with open(EDA_OUTPUT_PARAMS_PATH, "r", encoding="utf-8") as f:
        eda_params = json.load(f)
    return eda_params


def load_fe_params():
    with open(FE_OUTPUT_PARAMS_PATH, "r") as f:
        fe_params = json.load(f)
    return fe_params


def load_training_params():
    with open(TRAINING_OUTPUT_PARAMS_PATH, "r") as f:
        training_params = json.load(f)
    return training_params


# Validation data
def get_Xtrain_data():
    X_train = pd.read_parquet(TRAINING_SET_PATH)
    return X_train


def get_Xtest_data():
    X_test = pd.read_parquet(VALIDATION_SET_PATH)
    return X_test


def get_ohe_Ytrain():
    Y_train = pd.read_parquet(OHE_DATAFRAME_LABELS)
    return Y_train.values.ravel()


def get_weighted_Ytrain():
    Y_train = pd.read_parquet(WEIGHTED_DATAFRAME_LABELS)
    return Y_train.values.ravel()


def get_ohe_Ytest():
    Y_test = pd.read_parquet(OHE_TEST_LABELS_PATH)
    return Y_test.values.ravel()


def get_weighted_Ytest():
    Y_test = pd.read_parquet(WEIGHTED_TEST_LABELS_PATH)
    return Y_test.values.ravel()

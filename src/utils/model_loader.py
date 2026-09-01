import joblib

from src.utils.config import (
    FE_OUTPUT_SCALER_PATH,
)


def load_fe_scaler():
    return joblib.load(FE_OUTPUT_SCALER_PATH)

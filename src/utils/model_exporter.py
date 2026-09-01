import joblib
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from kmodes.kprototypes import KPrototypes
from src.utils.config import (
    FE_OUTPUT_SCALER_PATH,
    OHE_MODEL_PATH,
    WEIGHTED_MODEL_PATH,
    SUPERVISED_OHE_MODEL_PATH,
    SUPERVISED_WEIGHTED_MODEL_PATH,
)


# Models
def export_fe_scaler(scaler: StandardScaler):
    joblib.dump(scaler, FE_OUTPUT_SCALER_PATH)


def export_weighted_kmeams(kmeans: KMeans):
    joblib.dump(kmeans, WEIGHTED_MODEL_PATH)


def export_ohe_kprototypes(kproto: KPrototypes):
    joblib.dump(kproto, OHE_MODEL_PATH)


def export_ohe_supervised(model: RandomForestClassifier):
    joblib.dump(model, SUPERVISED_OHE_MODEL_PATH)


def export_weighted_supervised(model: RandomForestClassifier):
    joblib.dump(model, SUPERVISED_WEIGHTED_MODEL_PATH)

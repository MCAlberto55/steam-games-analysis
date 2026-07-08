import kagglehub
import pandas as pd
import os
from src.utils.config import RAW_DATA_PATH


def download_data():

    path = kagglehub.dataset_download(RAW_DATA_PATH)

    file_path = os.path.join(path, "a_steam_data_2021_2025.csv")

    steam_data = pd.read_csv(file_path)
    return steam_data

import kagglehub
import pandas as pd
import os

path = kagglehub.dataset_download("jypenpen54534/steam-games-dataset-2021-2025-65k")

file_path = os.path.join(path, "a_steam_data_2021_2025.csv")

steam_data = pd.read_csv(file_path)
print(steam_data.head())

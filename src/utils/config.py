from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent

# Main Routes
SRC_PATH = ROOT / "src"
DATA_PATH = ROOT / "data"
OUTPUT_PATH = ROOT / "outputs"

# File Names
VALIDATED_DATA_FILE_NAME = "validated_steam_games.parquet"
FEATURE_ENGINEERED_DATA_FILE_NAME = "feature_engineered_steam_games.parquet"
EDA_OUTPUT_FILE_NAME = "eda_outputs.json"

# Data Routes
RAW_DATA_PATH = "jypenpen54534/steam-games-dataset-2021-2025-65k"
VALIDATED_DATA_PATH = DATA_PATH / VALIDATED_DATA_FILE_NAME
FEATURE_ENGINEERED_DATA_PATH = DATA_PATH / FEATURE_ENGINEERED_DATA_FILE_NAME
EDA_OUTPUT_PARAMS_PATH = OUTPUT_PATH / "params" / EDA_OUTPUT_FILE_NAME

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent

# Main Routes
SRC_PATH = ROOT / "src"
DATA_PATH = ROOT / "data"
OUTPUT_PATH = ROOT / "outputs"

# File Names
VALIDATED_DATA_FILE_NAME = "validated_steam_games.parquet"

# Data Routes
RAW_DATA_PATH = "jypenpen54534/steam-games-dataset-2021-2025-65k"
VALIDATED_DATA_PATH = DATA_PATH / VALIDATED_DATA_FILE_NAME

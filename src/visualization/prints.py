import pandas as pd


def print_analysis_results(title: str, results: dict) -> None:
    output = f"================== {title} ==================\n"
    for key, value in results.items():
        output += f"{key}: {value}\n"
    print(output)

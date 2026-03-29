import pandas as pd
from extract.csv_extractor import extract_csv
from transform.cleaner import clean_data
from load.csv_loader import load_csv

def run_pipeline():
    # Extract
    df = extract_csv("data/raw/sample.csv")

    # Transform
    df_clean = clean_data(df)

    # Load
    load_csv(df_clean, "data/processed/output.csv")

if __name__ == "__main__":
    run_pipeline()
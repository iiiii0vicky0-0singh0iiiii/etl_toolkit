import pandas as pd
from extract.csv_extractor import extract_csv
from transform.cleaner import clean_data
from load.csv_loader import load_csv
from plugins.plugin_loader import apply_plugins
from config import CONFIG
from logger import log


def run_pipeline():
    try:
        log("Starting ETL pipeline")

        # Extract
        log("Extracting data...")
        df = extract_csv(CONFIG["data_source"])

        # Transform
        log("Cleaning data...")
        df_clean = clean_data(df)

        # Plugins (dynamic transformations)
        if CONFIG.get("plugins"):
            log(f"Applying plugins: {CONFIG['plugins']}")
            df_clean = apply_plugins(df_clean, CONFIG["plugins"])

        # Load
        log("Loading data...")
        load_csv(df_clean, CONFIG["output_path"])

        log("ETL pipeline completed successfully")

    except Exception as e:
        log(f"Pipeline failed: {e}")
        print(f"Error: {e}")


if __name__ == "__main__":
    run_pipeline()
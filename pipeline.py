from extract.csv_extractor import extract_csv
from transform.clean import clean_data
from load.db_loader import load_to_db
from plugins.plugin_loader import apply_plugins
from config import CONFIG

def run_pipeline():
    print("Starting ETL pipeline...")

    # Extract
    df = extract_csv(CONFIG["data_source"])

    # Transform
    df = clean_data(df)

    # Plugins
    df = apply_plugins(df, CONFIG["plugins"])

    # Load
    load_to_db(df, CONFIG["db_url"], CONFIG["table_name"])

    print("Pipeline completed!")
from sqlalchemy import create_engine

def load_to_db(df, db_url, table_name):
    try:
        engine = create_engine(db_url)
        df.to_sql(table_name, engine, if_exists='replace', index=False)
        print(f"Loaded data into {table_name}")
    except Exception as e:
        print(f"DB Load Error: {e}")
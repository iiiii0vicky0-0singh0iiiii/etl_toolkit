def transform(df):
    # Example custom logic
    df["bonus"] = df.get("salary", 0) * 0.10
    return df
def transform(df):
    df["salary"] = df["salary"] * 2
    return df
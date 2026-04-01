def transform(df):
    df["new_col"] = df["salary"] * 2
    return df
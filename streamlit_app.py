
import streamlit as st
import pandas as pd
import numpy as np
import csv

st.set_page_config(page_title="Universal ETL + ML Prep", layout="wide")
st.title(" Universal ETL + ML Data Prep")


# 1) Upload + AUTO DELIMITER DETECTION

file = st.file_uploader("Upload ANY CSV", type=["csv"])

if not file:
    st.info("Upload a CSV to begin.")
    st.stop()

# Detect delimiter automatically
try:
    sample = file.read(1024).decode("utf-8")
    file.seek(0)
    dialect = csv.Sniffer().sniff(sample)
    delimiter = dialect.delimiter
    df = pd.read_csv(file, delimiter=delimiter)
except:
    file.seek(0)
    df = pd.read_csv(file)

st.subheader("📄 Raw Data")
st.dataframe(df.head())



#  Missing Values BEFORE Cleaning

st.subheader("🔍 Missing Values (Before Cleaning)")

missing = df.isnull().sum()
missing_percent = (missing / len(df)) * 100

missing_df = pd.DataFrame({
    "Missing Count": missing,
    "Missing %": missing_percent
}).sort_values(by="Missing %", ascending=False)

st.dataframe(missing_df)

st.metric("Total Missing Values (Before)", int(missing.sum()))
st.bar_chart(missing)



#  Cleaning Function

def clean(df):
    df = df.copy()

    # Normalize column names
    df.columns = (
        df.columns.str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    # Drop duplicates
    df = df.drop_duplicates()

    # Strip whitespace
    for col in df.select_dtypes(include="object"):
        df[col] = df[col].astype(str).str.strip()

    # Handle missing values
    for col in df.columns:
        if pd.api.types.is_numeric_dtype(df[col]):
            df[col] = df[col].fillna(df[col].median())
        else:
            df[col] = df[col].fillna("Unknown")

    # Outlier clipping
    for col in df.select_dtypes(include=np.number):
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)
        iqr = q3 - q1
        df[col] = df[col].clip(q1 - 1.5 * iqr, q3 + 1.5 * iqr)

    return df


df_clean = clean(df)

st.subheader("🧹 Cleaned Data")
st.dataframe(df_clean.head())



#  Missing Values AFTER Cleaning

st.subheader("✅ Missing Values (After Cleaning)")

missing_after = df_clean.isnull().sum()
missing_after_percent = (missing_after / len(df_clean)) * 100

missing_after_df = pd.DataFrame({
    "Missing Count": missing_after,
    "Missing %": missing_after_percent
}).sort_values(by="Missing %", ascending=False)

st.dataframe(missing_after_df)

st.metric("Total Missing Values (After)", int(missing_after.sum()))
st.bar_chart(missing_after)



#  Feature Engineering

def feature_engineer(df):
    df = df.copy()

    num_cols = df.select_dtypes(include=np.number).columns
    cat_cols = df.select_dtypes(exclude=np.number).columns

    for col in num_cols:
        df[f"{col}_squared"] = df[col] ** 2
        df[f"{col}_log"] = df[col].apply(lambda x: np.log1p(x) if x >= 0 else 0)

    for col in cat_cols:
        freq = df[col].value_counts(normalize=True)
        df[f"{col}_freq"] = df[col].map(freq)

    return df


df_feat = feature_engineer(df_clean)

st.subheader("🧠 Feature Engineered Data")
st.dataframe(df_feat.head())



#  Auto Visualizations

st.subheader("📊 Auto Visualizations")

num_cols = df_clean.select_dtypes(include=np.number).columns
cat_cols = df_clean.select_dtypes(exclude=np.number).columns

if len(num_cols) > 0:
    st.write("### Numeric Distributions")
    for col in num_cols[:4]:
        st.write(col)
        st.bar_chart(df_clean[col])

if len(num_cols) > 1:
    st.write("### Correlation Matrix")
    corr = df_clean[num_cols].corr()
    st.dataframe(corr)

    st.write("### Correlation (Visual)")
    st.bar_chart(corr.abs())

if len(cat_cols) > 0:
    st.write("### Categorical Counts")
    for col in cat_cols[:3]:
        st.write(col)
        st.bar_chart(df_clean[col].value_counts())


#  ML Preview

st.subheader("🤖 ML Preview")

if len(num_cols) >= 1:
    target = st.selectbox("Select target column", num_cols)

    if target:
        X = df_feat.drop(columns=[target])
        y = df_feat[target]

        st.write("Feature Shape:", X.shape)
        st.write("Target Shape:", y.shape)



#  Download

csv_file = df_feat.to_csv(index=False).encode("utf-8")

st.download_button(
    "⬇ Download Processed CSV",
    data=csv_file,
    file_name="processed_data.csv",
    mime="text/csv",
)

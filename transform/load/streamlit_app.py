import streamlit as st
import pandas as pd

st.title("ETL Toolkit UI")

uploaded_file = st.file_uploader("Upload CSV")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Raw Data", df.head())

    if st.checkbox("Remove Duplicates"):
        df = df.drop_duplicates()

    if st.checkbox("Fill Missing Values"):
        df = df.fillna(method='ffill')

    st.write("Processed Data", df.head())

    if st.button("Download"):
        df.to_csv("output.csv", index=False)
        st.success("Saved as output.csv")
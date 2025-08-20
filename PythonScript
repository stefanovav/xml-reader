import streamlit as st
import pandas as pd



uploaded_file = st.file_uploader("Upload your file")
if uploaded_file:
    df = pd.read_xml(uploaded_file, parser = "lxml")
    df_cleaned = df.dropna().drop_duplicates()
    st.write(df_cleaned)
    df_cleaned.to_csv("cleaned.csv", index = False)

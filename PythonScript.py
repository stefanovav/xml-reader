import streamlit as st
import pandas as pd
import xml.etree.ElementTree as ET

uploaded_file = st.file_uploader("Upload your XML file")

if uploaded_file is not None:
    # Parse XML manually
    tree = ET.parse(uploaded_file)
    root = tree.getroot()

    items = [item.text.strip() for item in root.findall(".//Item") if item.text]

    # Split into supports and reactions
    half = len(items) // 2
    supports = pd.Series(items[:half])
    reactions = pd.Series(items[half:])

    result = pd.DataFrame({
        "Support": supports,
        "Reaction (x, y, z)": reactions
    })

    st.write(result)
    result.to_csv("Reactions.csv", index=False)
    st.success("Reaction data saved to Reactions.csv ✅")

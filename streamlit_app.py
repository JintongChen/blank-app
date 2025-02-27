import streamlit as st
import pandas as pd
st.title("this is atlascopco!!!")
def load_data(file_path):
    df = pd.read_csv(file_path)
    return df
file_Path = r"C:\Users\a00219912\Downloads\SPPALL\Quickly_get_faccts_sale.csv"
st.write("data from enovia zone")
data = load_data(file_Path)
st.dataframe(data)
if st.button("show summary"):
    st.write("summary statistics")
    st.write(data.describe())

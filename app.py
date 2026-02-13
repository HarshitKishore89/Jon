
import streamlit as st
import pandas as pd

st.title("Trader Sentiment Dashboard")

data = pd.read_csv("historical_data.csv")

st.write("Dataset Overview")
st.write(data.head())

st.write("PnL Distribution")
st.bar_chart(data.select_dtypes(include="number").iloc[:,0])

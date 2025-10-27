import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/processed_data.csv')
st.title("Operational Risk Forecasting Dashboard")

st.line_chart(df[['Operational_Losses']])
st.write("Dataset Snapshot")
st.dataframe(df.head())

# Highlight Risk Alerts
threshold = df['Operational_Losses'].mean() + 1.5*df['Operational_Losses'].std()
high_risk = df[df['Operational_Losses'] > threshold]
st.write("High Risk Events")
st.dataframe(high_risk)

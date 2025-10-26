
import streamlit as st
import pandas as pd

st.title('Heart Risk Predictor App')

st.write('This app builds a machine learning model')

with st.expander('Data'):
  st.write('**Raw data**')
  df = pd.read_csv('https://raw.githubusercontent.com/Mamai-hash/MP_Machinelearning/refs/heads/master/heart_risk_data_CLEANED.xls')
  df

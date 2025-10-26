
import streamlit as st
import pandas as pd

st.title('Heart Risk Predictor App')

st.info('This app builds a machine learning model!')

with st.expander('Data'):
  st.write('**Raw data**')
  df = pd.read_csv('https://raw.githubusercontent.com/Mamai-hash/MP_Machinelearning/refs/heads/master/heart_risk_data_CLEANED.xls')
  df

st.write('**X**')
X = df.drop('TenYearCHD',axis = 1 )
X

st.write('**Y**')
Y = df.TenYearCHD
Y

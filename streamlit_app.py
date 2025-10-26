
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
with st.expander ('Data visualization'):
   #CREATE the Plotly Figure (Only once!)
    fig = px.histogram(
        df,
        x='age',
        nbins=10,
        title='Distribution of Patient Age',
        # This is a good, distinct color for the heart app
        color_discrete_sequence=['#ff4b4b'] ) 
    fig.update_layout(
        xaxis_title="Age (Years)",  <-- Indent these lines by 4 spaces (or one tab)
        yaxis_title="Count of Patients"
       )
    st.plotly_chart(fig, use_container_width=True)

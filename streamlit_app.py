
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
   st.scatter_chart(date = df, x = 'age', y = 'sysBP', color = 'TenYearCHD')

with st.expander ('Data visualization'):
  fig_scatter = px.scatter(
        df,
        x='age',
        y='sysBP',
        color='TenYearCHD', # Plotly correctly uses the 'color' parameter for grouping
        title='Age vs. Systolic BP: CHD Risk Breakdown',
        labels={'sysBP': 'Systolic Blood Pressure (mmHg)'},
        # Map colors for clarity: Blue for No CHD, Red for CHD
        color_discrete_map={0: 'blue', 1: 'red'},
    )
st.write("Scatter Plot: Blue points = No CHD (0), Red points = Has CHD (1)")
st.plotly_chart(fig_scatter, use_container_width=True)

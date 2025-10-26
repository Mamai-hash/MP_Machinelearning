
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
   fig_hist = px.histogram(
        df,
        x='age',
        nbins=10,
        title='Distribution of Patient Age',
        color_discrete_sequence=['#ff4b4b'] 
    )
    fig_hist.update_layout(
        xaxis_title="Age (Years)",
        yaxis_title="Count of Patients"
    )
    st.plotly_chart(fig_hist, use_container_width=True)  
    fig_scatter = px.scatter(
        df,
        x='age',
        y='sysBP',
        color='TenYearCHD', # This works with Plotly
        title='Age vs. Systolic BP: CHD Risk Breakdown',
        labels={'sysBP': 'Systolic Blood Pressure (mmHg)'},
        color_discrete_map={0: 'blue', 1: 'red'}, 
    ) 
    st.plotly_chart(fig_scatter, use_container_width=True)
    st.write("Scatter Plot: Blue points = No CHD (0), Red points = Has CHD (1)")
    )

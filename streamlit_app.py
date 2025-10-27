import streamlit as st
import pandas as pd
import plotly.express as px # Added the necessary import for px

@st.cache_data
def load_data():
    """Loads and returns the cleaned heart risk data."""
    df = pd.read_csv('https://raw.githubusercontent.com/Mamai-hash/MP_Machinelearning/refs/heads/master/heart_risk_data_CLEANED.xls')
    return df

# --- App Layout ---
st.title('Heart Risk Predictor App')
st.info('This app builds a machine learning model!')

df = load_data()

with st.expander('Data'):
    st.write('**Raw data**')
    st.dataframe(df)

    st.write('**X (Features)**')
    X = df.drop('TenYearCHD', axis=1)
    st.dataframe(X)

    st.write('**Y (Target Variable)**')
    Y = df.TenYearCHD
    st.dataframe(Y)

# --- Data Visualization (Aesthetics) ---
with st.expander('Data visualization'):

    # 1. Age Distribution Histogram
    fig_hist = px.histogram(
        df,
        x='age',
        nbins=10,
        title='Distribution of Patient Age',
        color_discrete_sequence=['#FF6347'] # Tomato/Orange-Red (Less aggressive than pure red)
    )
    fig_hist.update_traces(marker=dict(line=dict(width=1, color='DarkSlateGrey')))

    fig_hist.update_layout(
        xaxis_title="Age (Years)",
        yaxis_title="Count of Patients",
        # Customizing the background to make it look cleaner
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
    )
    st.plotly_chart(fig_hist, use_container_width=True)

    # 2. Age vs. Systolic BP Scatter Plot
    fig_scatter = px.scatter(
        df,
        x='age',
        y='sysBP',
        color='TenYearCHD', # This tells Plotly to color by this categorical column
        title='Age vs. Systolic BP: CHD Risk Breakdown',
        labels={'sysBP': 'Systolic Blood Pressure (mmHg)'},
        # Defined clear, distinct colors: Green for No Risk (0), Red for Risk (1)
        color_discrete_map={0: 'green', 1: 'red'},
        opacity=0.6,
    )
    fig_scatter.update_layout(
        xaxis_title="Age (Years)",
        yaxis_title="Systolic Blood Pressure (mmHg)",
        # Customizing the background
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
    )
    st.plotly_chart(fig_scatter, use_container_width=True)
    st.write("Scatter Plot Legend: <span style='color:green;'>Green points = No CHD (0)</span>, <span style='color:red;'>Red points = Has CHD (1)</span>", unsafe_allow_html=True)

# Data preparations
with st.sidebar:
    st.header('input features') 
    sex = st.selectbox ('sex',('male', 'female'))
    prevalentstroke = st.selectbox('prevalentstroke', ('No (0)', 'Yes (1)'))
    age = st.slider('age (years)', min_value=32, max_value=70, value=49.6)
    heartRate = st.slider('Heart Rate (beats)', min_value=40, max_value=120, value=75)
    sysBP = st.slider('sysBP (mmHg)', min_value=83.5, max_value=295, value=132.35)
    totChol = st.slider('totChol (mg/dL)', min_value=107, max_value=696, value=236.7)
    
    
    

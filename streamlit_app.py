import streamlit as st
import pandas as pd
import plotly.express as px # Added the necessary import for px

st.title('Heart Risk Predictor App')

st.info('This app builds a machine learning model!')

# Initialize a default state for the application
if 'app_state' not in st.session_state:
    st.session_state.app_state = 'data_loading'

@st.cache_data
def load_data():
    """Loads and caches the dataset."""
    try:
        df = pd.read_csv('https://raw.githubusercontent.com/Mamai-hash/MP_Machinelearning/refs/heads/master/heart_risk_data_CLEANED.xls')
        return df
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return pd.DataFrame()

df = load_data()

if df.empty:
    st.stop()

with st.expander('Data Exploration'):
    st.subheader('Raw Data')
    st.dataframe(df.head())

    st.subheader('Feature Data (X)')
    X = df.drop('TenYearCHD', axis=1)
    st.dataframe(X.head())

    st.subheader('Target Variable (Y)')
    Y = df.TenYearCHD
    st.dataframe(Y.head())

# Corrected Data visualization block
with st.expander('Data visualization'):
    # Histogram of Age
    fig_hist = px.histogram(
        df,
        x='age',
        nbins=10,
        title='Distribution of Patient Age',
        color_discrete_sequence=['#ff4b4b']
    )
    # The indentation for update_layout is now correctly aligned with the code block
    fig_hist.update_layout(
        xaxis_title="Age (Years)",
        yaxis_title="Count of Patients",
        font=dict(family="Inter", size=14)
    )
    st.plotly_chart(fig_hist, use_container_width=True)

    # Scatter Plot: Age vs. Systolic BP
    fig_scatter = px.scatter(
        df,
        x='age',
        y='sysBP',
        color='TenYearCHD',  # Color by the target variable
        title='Age vs. Systolic BP: CHD Risk Breakdown',
        labels={'sysBP': 'Systolic Blood Pressure (mmHg)'},
        color_discrete_map={0: 'blue', 1: 'red'},
    )
    fig_scatter.update_layout(
        font=dict(family="Inter", size=14)
    )

    st.plotly_chart(fig_scatter, use_container_width=True)
    st.write("Scatter Plot: Blue points = No CHD (0), Red points = Has CHD (1)")

st.sidebar.markdown("## ML Model Settings")
st.sidebar.markdown("More features to be added here soon!")

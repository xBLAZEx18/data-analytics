import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

pd.options.plotting.backend = 'plotly'


@st.cache_data
def load_dataset():
    return pd.read_csv('dataset/canada_clean.csv')

st.title('Canada Immigration Analysis')

with st.spinner('Loading data...'):
    df = load_dataset()
    
with st.expander('Show Dataset'):
    st.dataframe(df)

countrylist = df ['country']
selected_country = st.selectbox('Select A Country',countrylist)
min_yr , max_yr = st.slider('select years',min_value=1980,max_value=2013,value=(1980,2013))
st.header(f'country:{selected_country}')
df = df.set_index('country')
country = df.loc[selected_country,str(min_yr):str(max_yr)]
fig = country.plot()
st.plotly_chart(fig)
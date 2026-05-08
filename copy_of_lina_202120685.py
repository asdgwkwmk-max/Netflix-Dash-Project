import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Netflix Content Analysis - Phase 1")

# تحميل البيانات
try:
    df = pd.read_csv('netflix_titles.csv')
    
    # رسمة بيانية بسيطة واحترافية
    fig = px.pie(df, names='type', title='Distribution of Movies vs TV Shows')
    st.plotly_chart(fig)
    
    st.write("Data Summary:", df.head())
except:
    st.error("Please ensure 'netflix_titles.csv' is uploaded to GitHub.")

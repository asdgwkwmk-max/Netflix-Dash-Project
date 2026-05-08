import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

# 1. تحميل البيانات (تأكدي أن ملف netflix_titles.csv مرفوع بجانب الكود في GitHub)
try:
    df = pd.read_csv('netflix_titles.csv')
except:
    # هذا السطر للاحتياط إذا كان اسم الملف مختلف
    df = pd.DataFrame({'Type': ['Movie', 'TV Show'], 'Count': [1, 1]})

# 2. تجهيز التطبيق
app = dash.Dash(__name__)
server = app.server

# 3. تصميم الواجهة (بسيطة جداً لضمان التشغيل)
app.layout = html.Div([
    html.H1("Netflix Content Analysis (Phase 1)"),
    
    html.Div([
        dcc.Graph(
            id='graph1',
            figure=px.pie(df, names='type', title='Distribution of Content Types')
        )
    ])
])

# 4. سطر التشغيل النهائي لـ Streamlit
if __name__ == '__main__':
    app.run_server(debug=True)

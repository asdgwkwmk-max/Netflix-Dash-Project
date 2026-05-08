import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

# إنشاء التطبيق
app = dash.Dash(__name__)
server = app.server

# تحميل البيانات (تأكدي أن الملف netflix_titles.csv موجود معك في GitHub)
try:
    df = pd.read_csv('netflix_titles.csv')
    fig = px.pie(df, names='type', title='Netflix Content Distribution')
except:
    fig = px.scatter(title="Error loading data - check file name")

# واجهة التطبيق
app.layout = html.Div([
    html.H1("Netflix Project - Phase 1"),
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run_server(debug=True)

import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output
import os

# 1. تحميل البيانات بطريقة متوافقة مع السيرفر
file_path = 'netflix_titles.csv'
if os.path.exists(file_path):
    df = pd.read_csv(file_path)
else:
    # هذا السطر احتياطي إذا كان اسم الملف مختلف
    df = pd.DataFrame(columns=['type', 'release_year', 'title', 'rating'])

# 2. تنظيف البيانات بشكل سريع
df['type'] = df['type'].fillna('Movie')
df['release_year'] = df['release_year'].fillna(2000)

# 3. إعداد تطبيق Dash
app = Dash(__name__)
server = app.server # ضروري جداً للاستضافة

# 4. تصميم واجهة الموقع (Layout)
app.layout = html.Div([
    html.H1("Netflix Content Analysis Dashboard", style={'textAlign': 'center', 'color': '#b20710', 'fontFamily': 'Arial'}),
    html.P("Prepared by: Lina - Student ID: 202120685", style={'textAlign': 'center'}),
    
    html.Div([
        html.Label("Select Content Type:", style={'fontWeight': 'bold'}),
        dcc.Dropdown(
            id='type-selection',
            options=[{'label': i, 'value': i} for i in df['type'].unique()],
            value='Movie',
            style={'width': '50%'}
        ),
    ], style={'padding': '20px', 'backgroundColor': '#f9f9f9', 'borderRadius': '10px', 'margin': '10px'}),

    html.Div([
        dcc.Graph(id='main-visualization'),
    ], style={'padding': '20px'})
])

# 5. تفعيل التفاعل (Callbacks)
@app.callback(
    Output('main-visualization', 'figure'),
    Input('type-selection', 'value')
)
def update_content_graph(selected_type):
    filtered_df = df[df['type'] == selected_type]
    fig = px.histogram(
        filtered_df, 
        x="release_year",
        title=f"Trend of {selected_type}s Over Years",
        color_discrete_sequence=['#b20710'],
        template='plotly_white'
    )
    fig.update_layout(title_x=0.5)
    return fig

# 6. تشغيل السيرفر
if __name__ == '__main__':
    app.run_server(debug=False)

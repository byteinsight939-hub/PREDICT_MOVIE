import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

# Load data
df = pd.read_csv("IMDb Movies India.csv", encoding='latin1')

# Print column names to debug
print(df.columns)

# Clean data if needed
df.columns = df.columns.str.strip()  # Remove leading/trailing spaces
df.dropna(subset=['Genre', 'Year', 'Rating'], inplace=True)  # Update column name

# Create Dash app
app = Dash(__name__)

# App layout
app.layout = html.Div([
    html.H1("🎬 IMDb India Movies Dashboard", style={'textAlign': 'center'}),

    html.Div([
        html.Label("🎭 Select Genre(s):"),
        dcc.Dropdown(
            id='genre_filter',
            options=[{'label': g, 'value': g} for g in sorted(df['Genre'].dropna().unique())],
            multi=True,
            value=['Drama']  # default
        ),
    ], style={'width': '40%', 'margin': 'auto'}),

    dcc.Graph(id='rating_chart')
])

# Callback to update graph
@app.callback(
    Output('rating_chart', 'figure'),
    Input('genre_filter', 'value')
)
def update_chart(selected_genres):
    if not selected_genres:
        return px.histogram(title="Please select a genre")

    filtered_df = df[df['Genre'].isin(selected_genres)]
    fig = px.histogram(
        filtered_df,
        x='Year',
        color='Genre',
        nbins=30,
        title="Number of Movies per Year (by Genre)",
        labels={'Year': 'Release Year'},
    )
    return fig

# Run app
if __name__ == '__main__':
    app.run(debug=True)
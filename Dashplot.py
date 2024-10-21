from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

# Load the dataset
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')

# Link the external CSS stylesheet
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# Initialize the Dash app with external stylesheets
app = Dash(__name__, external_stylesheets=external_stylesheets)

# Define the layout with columns
app.layout = html.Div([
    html.H1('Title of Dash App', style={'textAlign': 'Center', 'color': 'blue'}),

    # Define a row with two columns
    html.Div([
        
        # First column
        html.Div([
            html.H3('Country Selector'),
            dcc.Dropdown(
                options=[{'label': i, 'value': i} for i in df.country.unique()],
                value='Canada',
                id='dropdown-selection'
            ),
        ], style={'width': '30%', 'display': 'inline-block', 'verticalAlign': 'top'}),

        # Second column
        html.Div([
            dcc.Graph(id='graph-content'),
        ], style={'width': '65%', 'display': 'inline-block', 'verticalAlign': 'top'}),
        
    ], style={'display': 'flex', 'justifyContent': 'space-between'}),

   
])

# Callback to update the graph based on dropdown selection
@app.callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value):
    dff = df[df.country == value]
    return px.line(dff, x='year', y='pop', title=f'Population Over Time for {value}')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)

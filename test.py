from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

# Load the dataset
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')

# Get unique years for the slider
years = df['year'][1:7].unique()

# Link the external CSS stylesheet
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# Initialize the Dash app with external stylesheets
app = Dash(__name__, external_stylesheets=external_stylesheets)

# Define the layout
app.layout = html.Div([

    html.H1(children='Title of Dash App', style={'textAlign': 'center', 'color': 'blue'}),
        html.Div([
            html.H2('Country Selector'),
            dcc.Dropdown(
                options=[{'label': i, 'value': i} for i in df.continent.unique()],
                value=['Asia'],
                id='dropdown-selection',
                multi=True
            )]),
        html.Div([
            html.H2('Year Slider'),
            dcc.Slider(
                min=years.min(),
                max=years.max(),
                value=years.min(),
                step=None,
                marks={str(year): str(year) for year in years},
                id='slider-selection'
            )]),
        html.Div(
            dcc.Graph(id='graph-content')),
        html.Div(dcc.Graph(id='graph-content2'))
])

# Combined callback to update the graph based on dropdown and slider selection
@app.callback(
    Output('graph-content', 'figure'),
    Output('graph-content2', 'figure'),
    [Input('dropdown-selection', 'value'),
     Input('slider-selection', 'value')]
)
def update_graph(selected_continent, selected_year):
    if selected_continent is None:
        dff = df[df.year == selected_year]
        fig = px.scatter(dff, x='gdpPercap', y='lifeExp', 
                     title=f'Life Expectancy vs GDP Per Capita for {selected_continent} in {selected_year}',
                     labels={'gdpPercap': 'GDP Per Capita', 'lifeExp': 'Life Expectancy'})
        fig2 = px.scatter(dff, x='year', y='pop', title=f'Population Over Time for {selected_year}')
        
    else :

    # Filter the data for the selected country and year
        dff = df[(df.continent.isin(selected_continent)) & (df.year == selected_year)]
        
        # Plot the life expectancy vs. GDP per capita for the selected country and year
        fig = px.scatter(dff, x='gdpPercap', y='lifeExp', 
                        title=f'Life Expectancy vs GDP Per Capita for {selected_continent} in {selected_year}',
                        labels={'gdpPercap': 'GDP Per Capita', 'lifeExp': 'Life Expectancy'})
        fig2 = px.scatter(dff, x='gdpPercap', y='pop', title=f'Population Over Time for {selected_year}')
    
    return fig, fig2

    
    


# Run the app
if __name__ == '__main__':
    app.run(debug=True)

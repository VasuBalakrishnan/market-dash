import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
application = app.server

app.layout = html.Div([
    html.H1("Market Dashboards"),

    html.H2("Powered by Dash and hosted in Azure"),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SFO'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])

if __name__ == "__main__":
    application.run(debug=True, host="0.0.0.0")
# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc

import dash_html_components as html
import cf_deployment_tracker
import os

cf_deployment_tracker.track()

app = dash.Dash(__name__)
server=app.server
port = int(os.getenv('PORT', 8080))



app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])
	
if __name__ == '__main__':
    app.run_server(host='127.0.0.1', port=port, debug=True)
# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import plotly.figure_factory as FF

import scipy.io

matdata = scipy.io.loadmat('torus_data.mat')
x,y,z =  matdata['xyz']
simplices = matdata['simplices']

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Torus'),

    html.Div(children='''
        Particle dynamics on the Torus
    '''),

    dcc.Graph(
        id='example-graph',

# plotly express style
		figure = FF.create_trisurf(x=x, y=y, z=z,simplices=simplices, title="Torus", aspectratio=dict(x=1, y=1, z=0.3))
	)

])

if __name__ == '__main__':
    app.run_server(debug=True)
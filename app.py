


import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

import json
import datetime
import pandas as pd
from analytics.stdLookup import stdLookup as slu



external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


app.layout = html.Div([
    html.Br(),
    html.H3('BJJ App Console'),
    html.Br(),
    html.Div([
        dcc.Input(id='stdName', type='text', value='username'),
        html.Button(id='btn_stdSub', n_clicks=0, children='Submit')
    ]),
    html.Br(),
    html.Div(id='stdRep')
])

@app.callback(Output('stdRep', 'children'),
              [Input('btn_stdSub', 'n_clicks')],
              [State('stdName', 'value')])
def stdReporting(n_clicks, stdName):
    if n_clicks != None:
        tbldf = slu(username=stdName)
        tbldf = tbldf.set_index('userId')
        #need to sort on date for the table
        df = slu(username=stdName)
        totalClasses = df['date'].count()
        today = datetime.date.today()
        sevenDays = today - datetime.timedelta(days=7)
        thirtyDays = today - datetime.timedelta(days=30)
        sixtyDays = today - datetime.timedelta(days=60)
        nintyDays = today - datetime.timedelta(days=90)
        ytd = today - datetime.timedelta(days=365)
        df = df.set_index('date')
        df = df.sort_index()
        lastSevenDays = df.loc[sevenDays:today].count()['class']
        lastThirtyDays = df.loc[thirtyDays:today].count()['class']
        lastSixtyDays = df.loc[sixtyDays:today].count()['class']
        lastNintyDays = df.loc[nintyDays:today].count()['class']
        ytdDays = df.loc[ytd:today].count()['class']
        return html.Div([
            html.Div([
                html.Br(),
                html.H5('Total number of classes attended:'),
                html.H5(totalClasses),
                html.H5('Total number of classes attended in last 7 Days:'),
                html.H5(lastSevenDays),
                html.H5('Total number of classes attended in last 30 Days:'),
                html.H5(lastThirtyDays),
                html.H5('Total number of classes attended in last 60 Days:'),
                html.H5(lastSixtyDays),
                html.H5('Total number of classes attended in last 90 Days:'),
                html.H5(lastNintyDays),
                html.H5('Total number of classes attended year to date:'),
                html.H5(ytdDays),
            ]),
            html.Div([
                dash_table.DataTable(
                    id='stdRep',
                    columns=[{'name': i, 'id': i} for i in tbldf],
                    data=tbldf.to_dict('rows')
                ),
            ]),
            html.Br(),
            html.Br(),
            html.Br()
        ])



if __name__ == '__main__':
    app.run_server(debug=True)

import json
from time import strftime

import boto3
import decimal
import pandas as pd
import plotly
import datetime
import plotly.plotly as pl
import plotly.graph_objs as go
from analytics.stdLookup import stdLookup as slu



stdName = 'Ryan Schulte'
def tbl_pastDaysByStd(stdName):
    df = slu(username=stdName)
    today = datetime.date.today()
    sevenDays = today - datetime.timedelta(days=7)
    thirtyDays = today - datetime.timedelta(days=30)
    sixtyDays = today - datetime.timedelta(days=60)
    nintyDays = today - datetime.timedelta(days=90)
    ytd = today - datetime.timedelta(days=365)
    cd = str(today.strftime('%Y-%m-%d'))
    tw = str(sevenDays.strftime('%Y-%m-%d'))
    df = df.set_index('date')
    df = df.sort_index()
    lastSevenDays = df.loc[sevenDays:today].count()['class']
    lastThirtyDays = df.loc[thirtyDays:today].count()['class']
    lastSixtyDays = df.loc[sixtyDays:today].count()['class']
    lastNintyDays = df.loc[nintyDays:today].count()['class']
    ytdDays = df.loc[ytd:today].count()['class']


    trace = go.Table(
        header=dict(values=['7 Days', '30 Days', '60 Days', '90 Days', 'Year to Date']),
        cells=dict(values=[lastSevenDays, lastThirtyDays, lastSixtyDays, lastNintyDays, ytdDays])
    )
    data=[trace]
    plotly.offline.plot(data, filename='test.html')


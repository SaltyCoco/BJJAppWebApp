import json
import boto3
import pandas as pd
from boto3.dynamodb.conditions import Key, Attr
from assets.dynamoDB import db_bjjApp

def stdLookup(username):
    ddb = db_bjjApp()
    table = ddb.bjjDdb.Table(ddb.tblClass)
    response = table.scan(
        FilterExpression=Key('username').eq(username)
    )
    items = response['Items']
    rdJson = json.dumps(items)
    df = pd.read_json(rdJson)
    return df


#df = stdLookup(username='Ryan Schulte')
#date = df['date'].count()
#print(date)
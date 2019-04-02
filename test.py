import json
import pandas as pd
from assets.dynamoDB import db_bjjApp


ddb = db_bjjApp()
tbl = ddb.bjjDdb.Table(ddb.tblClass)
response = tbl.scan()
items = response['Items']
rdJson = json.dumps(items)
df = pd.read_json(rdJson)
print(df.head())
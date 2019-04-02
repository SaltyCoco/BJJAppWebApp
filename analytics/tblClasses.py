import json
import pandas as pd
import cufflinks as cf
from assets.dynamoDB import db_bjjApp

class tblClasses:
    def __init__(self):
        ddb = db_bjjApp()
        tbl = ddb.bjjDdb.Table(ddb.tblClass)
        response = tbl.scan()
        items = response['Items']
        rdJson = json.dumps(items)
        df_tblClass = pd.read_json(rdJson)
        df_tblClass = df_tblClass.sort_values('date', ascending=False)

        #bar_totalAttendByDay
        cf.set_config_file(offline=False, world_readable=True, theme='ggplot')
        series = df_tblClass.groupby('date')['class'].count().astype(int)
        series.iplot(kind='bar', filename='BJJApp/bar_totalAttendByDay.html')

        #bar_totalAttendByStudent.html
        cf.set_config_file(offline=False, world_readable=True, theme='ggplot')
        series = df_tblClass.groupby('username')['class'].count().astype(int)
        series.iplot(kind='bar', filename='BJJApp/bar_totalAttendByStudent.html')

        #full table
        trace0 = df_tblClass.Table(
            header=dict(values=['Date', 'Class', 'Student']),
            cells=dict(values=[df_tblClass['date'], df_tblClass['class'], df_tblClass['username']])
        )
        self.tbl_tblClassesdata = [trace0]
def tblClasses_var():
    return tblClasses()
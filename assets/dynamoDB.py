
import boto3
from configparser import ConfigParser


class BJJApp_DynDB:
    def __init__(self):
        cfg = ConfigParser()
        cfg.read('/Users/ryanschulte/PycharmProjects/BJJAppConsole/config')
        region = cfg.get('db', 'region_name')
        self.tblClass = cfg.get('db', 'tblClass')
        aws_access_key_id = cfg.get('db', 'aws_access_key_id')
        aws_secret_access_key = cfg.get('db', 'aws_secret_access_key')
        sesh = boto3.Session(aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
        self.bjjDdb = sesh.resource('dynamodb', region_name=region)
def db_bjjApp():
    return BJJApp_DynDB()



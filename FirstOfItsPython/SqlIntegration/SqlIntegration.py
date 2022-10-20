import pyodbc
from datetime import datetime, timedelta
import pandas as pd

class SqlIntegration():
    def __init__(self, connection_string):
        self.connection_string = connection_string

    def connect(self):
        self.connection = pyodbc.connect(self.connection_string)

    def disconnect(self):
        del self.connection

    def query(self, query):
        return pd.read_sql(query, self.connection)
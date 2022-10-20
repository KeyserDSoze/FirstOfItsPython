import pyodbc
from datetime import datetime, timedelta
import pandas as pd

class SqlIntegration():
    def __init__(self, connection_string):
        self.connection_string = connection_string

    def execute_query(self, query):
        connection = pyodbc.connect(self.connection_string)
        cursor = connection.cursor()
        cursor.execute(query)
        del connection

    def read_query(self, query):
        connection = pyodbc.connect(self.connection_string)
        var = pd.read_sql(query, connection)
        del connection
        return var
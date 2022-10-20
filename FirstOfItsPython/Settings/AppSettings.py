import json


class AppSettings:
    def __init__(self, path):
        settings = open(path, "r")
        data = json.load(settings)
        self.database_connection = data["database_connection"] 

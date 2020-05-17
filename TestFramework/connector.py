import sqlite3


class Connector:
    def __init__(self, database_url):
        connection = sqlite3.connect(database_url)
        self.cursor = connection.cursor()

    def execute(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchone()[0]

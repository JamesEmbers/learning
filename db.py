import sqlite3
from sqlite3 import Error
from .exceptions import ConnectionException


class Connection:
    _connection = None
    _driver = sqlite3

    def __init__(self, db_file='sqlite.db', driver=None):
        self.db_file = db_file
        if driver is not None:
            self._driver = driver

    def connect(self):
        try:
            self._connection = self._driver.connect(self.db_file)
        except Error as e:
            print(e)

    def execute(self, statement):
        self.cursor().execute(statement)
        self._connection.commit()

    def cursor(self):
        if self._connection:
            return self._connection.cursor()
        raise ConnectionException('No connection established.')

    def lastId(self):
        return self.cursor().lastrowid

    def close(self):
        self._connection.close()

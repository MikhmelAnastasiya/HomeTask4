import sqlite3
import logging
import re

logging.basicConfig(level=logging.INFO)


class DBConnector:
    def __init__(self):
        self.DB_NAME = 'Book.db'
        self.BOOK_INFO_TABLE = 'book_info'

    def add_book(self, model):
        self.create_book_info_table()
        self.insert_book(model)
        self.create_frequency_word_table(model)

    def create_book_info_table(self):
        sqlite_connection = ''
        try:
            sqlite_create_table_query = '''CREATE TABLE IF NOT EXISTS ''' + self.BOOK_INFO_TABLE + ''' (
                                                    book_name TEXT PRIMARY KEY,
                                                    number_of_paragraphs INT,
                                                    number_of_words INT,
                                                    number_of_letters INT,
                                                    words_with_capital_letters INT,
                                                    words_in_lowercase INT);'''

            sqlite_connection = sqlite3.connect(self.DB_NAME)
            logging.info("Database " + self.DB_NAME + " successfully connected to SQLite")

            cursor = sqlite_connection.cursor()
            cursor.execute(sqlite_create_table_query)
            sqlite_connection.commit()

            logging.info("Connection to " + self.BOOK_INFO_TABLE)

            cursor.close()

        except sqlite3.Error as error:
            logging.error("Cannot connect to SQLite or cannot create " + self.BOOK_INFO_TABLE + " table in SQLite.",
                          error)
        finally:
            if sqlite_connection:
                sqlite_connection.close()
                logging.info("SQLite connection is closed")

    def insert_book(self, model):
        sqlite_connection = ''
        try:
            insert_string = tuple(model.get_model())
            sqlite_insert_query = '''INSERT OR REPLACE INTO ''' + self.BOOK_INFO_TABLE + '''                               
                                          VALUES (?, ?, ?, ?, ?, ?);'''

            sqlite_connection = sqlite3.connect(self.DB_NAME)
            logging.info("Database " + self.DB_NAME + " successfully connected to SQLite")

            cursor = sqlite_connection.cursor()
            cursor.execute(sqlite_insert_query, insert_string)
            sqlite_connection.commit()
            logging.info("Total", cursor.rowcount, " records inserted successfully into " + self.BOOK_INFO_TABLE + " table")

            cursor.close()

        except sqlite3.Error as error:
            logging.error("Failed to insert record into SQLite table.", error)
        finally:
            if sqlite_connection:
                sqlite_connection.close()
                logging.info("The SQLite connection is closed")

    def create_frequency_word_table(self, model):
        sqlite_connection = ''
        try:
            table_name = model.get_frequency_of_words()[0]
            table_name = re.sub("\s+", "_", table_name.strip()).lower()
            insert_strings = model.get_frequency_of_words()[1]
            sqlite_create_table_query = '''CREATE TABLE IF NOT EXISTS ''' + table_name + ''' (
                                                                word TEXT PRIMARY KEY,
                                                                count INT,
                                                                count_uppercase INT);'''

            sqlite_connection = sqlite3.connect(self.DB_NAME)
            logging.info("Database " + table_name + " successfully connected to SQLite")

            cursor = sqlite_connection.cursor()
            cursor.execute(sqlite_create_table_query)
            sqlite_connection.commit()

            sqlite_insert_query_2 = '''INSERT OR REPLACE INTO ''' + table_name + '''                               
                                          VALUES (?, ?, ?);'''

            cursor.executemany(sqlite_insert_query_2, insert_strings)
            sqlite_connection.commit()
            logging.info("Total", cursor.rowcount, " records inserted successfully into " + table_name + " table")
            sqlite_connection.commit()
            cursor.close()

        except sqlite3.Error as error:
            logging.error("Failed to insert multiple records into sqlite table", error)
        finally:
            if sqlite_connection:
                sqlite_connection.close()
                logging.info("The SQLite connection is closed")


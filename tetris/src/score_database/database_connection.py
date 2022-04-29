import sqlite3
from score_database.config import DATABASE_FILE_PATH

connection = sqlite3.connect(DATABASE_FILE_PATH)


def get_database_connection():
    return connection

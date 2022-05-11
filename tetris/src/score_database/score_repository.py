import sqlite3
from score_database.database_connection import get_database_connection



class ScoreRepository:

    def __init__(self, connection):
        self._connection = connection

    def find_scores_desc(self):

        cursor = self._connection.cursor()

        try:
            cursor.execute(
                "select * from scores order by score desc limit 10"
            )

            return cursor.fetchall()

        except sqlite3.OperationalError:
            print("Database not found")
            return []

    def save_score(self, username, score):
        cursor = self._connection.cursor()

        try:
            cursor.execute(
                "insert into scores (username, score) values (?,?)",
                (username, score)
            )

            self._connection.commit()

        except sqlite3.OperationalError:
            print("Database not found")
            pass

    def delete_all(self):

        cursor = self._connection.cursor()

        try:
            cursor.execute("delete from scores")

            self._connection.commit()

        except sqlite3.OperationalError:
            print("Database not found")

score_repository = ScoreRepository(get_database_connection())

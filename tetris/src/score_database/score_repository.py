import database_connection


class ScoreRepository:

    def __init__(self, connection):
        self._connection = connection

    def find_all_desc(self, sorted_by="score", limit=10):

        cursor = self._connection.cursor()

        cursor.execute(
            "select * from scores order by (?) desc limit (?)",
            (sorted_by, limit)
        )

        return cursor.fetchall()

    def save_score(self, username, score):
        cursor = self._connection.cursor

        cursor.execute(
            "insert into scores (username, score) values (?,?)",
            (username, score)
        )

        self._connection.commit()

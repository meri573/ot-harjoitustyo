import database_connection


def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute("""
        drop table if exists scores;
    """
                   )


def create_tables(connetion):

    cursor = connection.cursor()

    cursor.execute("""
        create table scores (
            username text, 
            score integer
        );
    """)

    connection.commit()


def initialize_database():

    connection = database_connection.get_database_connection()

import os

dirname = os.path.dirname(__file__)

DATABASE_FILENAME = "database.sqlite"
DATABASE_FILE_PATH = os.path.join(
    dirname, "..", "..", "data", DATABASE_FILENAME)

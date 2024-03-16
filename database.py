import sqlite3
from sqlite3 import Connection

DATABASE_URL = "file:./db.db?mode=rwc"


def get_db() -> Connection:
    conn = sqlite3.connect(DATABASE_URL, uri=True)
    conn.row_factory = sqlite3.Row
    return conn

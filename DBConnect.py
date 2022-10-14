import contextlib
import mysql.connector

@contextlib.contextmanager
def mysql_connection(*args, **kwargs):
    conn = mysql.connector.connect(*args, **kwargs)
    try:
        yield conn
    finally:
        conn.close()


if __name__ == "__main__":
    pass
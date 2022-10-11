from mysql.connector import (connection)


def openConnection():
    conn = connection.MySQLConnection(user='root', password='*1234sj',
                                      host='127.0.0.1',
                                      database='nytimesdb')
    return conn


def closeConnection(conn):
    conn.close()

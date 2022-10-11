from mysql.connector import (connection)


def openConnection():
    con = connection.MySQLConnection(user='', password='',
                                     host='127.0.0.1',
                                     database='detector')
    return con

def closeConnection(con):
    con.close()


#add note
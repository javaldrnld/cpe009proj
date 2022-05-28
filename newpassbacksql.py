import mysql.connector

class Database:
    def __init__(self, host, user, passwd, port, database):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.port = port
        self.database = database

    var = mysql.connector.connect(
        host=self.host

    )







mydb = Database("localhost", "root", "Bellion_1", "3306", "userdb")
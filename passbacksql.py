import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Bellion_1",
    port="3306",
    database="userdb"
)


def submit(website, username, password):
    mycursor = mydb.cursor()
    mycursor.execute("INSERT INTO information (website, username, password) VALUES (%s, %s, %s)",
                     (website, username, password))
    mydb.commit()
    mydb.close()


def show():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM information")

    lst = mycursor.fetchall()
    mydb.commit()
    mydb.close()
    return lst


def updateRecord(website, username, password):
    mycursor = mydb.cursor()
    mycursor.execute("UPDATE information SET website=?, username=(?), password=(?) WHERE personID=(?)",
                     (website, username, password))

    mydb.commit()
    mydb.close()


def deleteRecord(password):
    mycursor = mydb.cursor()
    mycursor.execute("DELETE FROM information WHERE password=(?)", (password,))
    mydb.commit()
    mydb.close()


def checkdata():
    if len(show()) == 0:
        return False
    else:
        return True

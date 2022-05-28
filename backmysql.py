import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Bellion_1",
    database="information"
)

cur = mydb.cursor()

# cur.execute("""
#                 CREATE TABLE newuserinfo (
#                     personID int PRIMARY KEY AUTO_INCREMENT,
#                     website VARCHAR(255),
#                     username VARCHAR(255),
#                     password VARCHAR(255),
#                     PRIMARY KEY (personID)
#                 )
# """)

cur.execute("INSERT INTO newuserinfo (website, username, password) VALUES (%s, %s, %s)", ("Facebook", "Bellion", "Pass2231"))
mydb.commit()
cur.execute("SELECT * FROM newuserinfo")

for _ in cur:
    print(_)
import sqlite3

db = "NewUserinformation.db"


def connect():
    conn = sqlite3.connect(db)

    # Create cursor to fetch the data we need
    cur = conn.cursor()

    # Create a table
    cur.execute("""
                    CREATE TABLE IF NOT EXISTS information (
                        password text,
                        website text,
                        username text,
                        person_id text
                        )
    """)

    # commit changes
    conn.commit()
    # Close connection
    conn.close()


# Create function to submit in database

def submit(password, website, user, tag):
    conn = sqlite3.connect(db)
    cur = conn.cursor()

    # One by one execute the information in the table
    cur.execute("INSERT INTO information VALUES (?,?,?,?)", (password, website, user, tag))

    conn.commit()
    conn.close()


# Create function to show all the information

def show():
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute("SELECT * FROM information")

    # We need to a variable to store our fetch or information
    lst = cur.fetchall()
    conn.commit()
    conn.close()
    return lst


# Create function to update records

def updaterecord(password, website, user, tag,):
    conn = sqlite3.connect(db)
    cur = conn.cursor()

    # Update information for website where the password is same
    cur.execute("UPDATE information SET password=?, website=(?), username=(?) WHERE person_id=(?) ",
                (password, website, user, tag))
    conn.commit()
    conn.close()


# Create a function to delete records

def deleterecord(website):
    conn = sqlite3.connect(db)
    cur = conn.cursor()

    # Delete the record of the data
    cur.execute("DELETE FROM information WHERE website=(?)", (website,))
    conn.commit()
    conn.close()


# Create a function that check if the database is empty or not

def checktable():
    if len(show()) == 0:
        return False
    else:
        return True



connect()
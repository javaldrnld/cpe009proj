import sqlite3

db = "usersystem.db"


def connect():
    conn = sqlite3.connect(db)

    # Create cursor to fetch the data we need
    cur = conn.cursor()

    # Create a table
    cur.execute("""CREATE TABLE information(
                        website text,
                        username text,
                        password text
                        )
    """)

    # commit changes
    conn.commit()
    # Close connection
    conn.close()


# Create function to submit in database

def submit(website, user, password):
    conn = sqlite3.connect(db)
    cur = conn.cursor()

    # One by one execute the information in the table
    cur.execute("INSERT INTO information VALUES (?,?,?)", (website, user, password))

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

# C
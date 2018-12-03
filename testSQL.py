import sqlite3

def ConnectDataBase():
    conn = sqlite3.connect('/Users/Han/Documents/CS 4980 Child-Computer Interaction(2018 FALL)/Child_Computer_Interaction_Project/AppData.db')
    print("Opened database successfully")

    conn.close()

def CreateChoreTable():
    conn = sqlite3.connect('/Users/Han/Documents/CS 4980 Child-Computer Interaction(2018 FALL)/Child_Computer_Interaction_Project/AppData.db')
    conn.execute('''CREATE TABLE if not exists Kids
            (name text, time text)''')
    print ("Table created successfully")
    conn.close()

def InsertNewKid():
    conn = sqlite3.connect('AppData.db')
 #   Kids_sql = "INSERT INTO Kids (name,age) VALUES (?,?)"
    with conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO Kids VALUES ('Colin','9')")
        cur.execute("INSERT INTO Kids VALUES ('Peter','11')")
        cur.execute("INSERT INTO Kids VALUES ('Jim','12')")
    #print("Successfully insert "+ name + " into Kids Table")
    conn.close()

def where():
    conn = sqlite3.connect('AppData.db')
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT name FROM Kids WHERE time = 11")
        name = cur.fetchone()
        print(name[0])
'''
def get():
    conn = sqlite3.connect('AppData.db')
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT name from Kids")
        rows = cur.fetchall()
        for row in rows:
            print(row[0])'''

ConnectDataBase()
CreateChoreTable()
#InsertNewKid()
where()


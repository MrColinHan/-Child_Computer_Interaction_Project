import sqlite3

def ConnectDataBase():
    conn = sqlite3.connect('/Users/Han/Documents/CS 4980 Child-Computer Interaction(2018 FALL)/Child_Computer_Interaction_Project/AppData.db')
    print("Opened database successfully")

    conn.close()

def CreateChoreTable():
    conn = sqlite3.connect('/Users/Han/Documents/CS 4980 Child-Computer Interaction(2018 FALL)/Child_Computer_Interaction_Project/AppData.db')
    conn.execute('''CREATE TABLE Chore
            (name text, time text,status text)''')
    print ("Table created successfully")
    conn.close()

ConnectDataBase()
CreateChoreTable()

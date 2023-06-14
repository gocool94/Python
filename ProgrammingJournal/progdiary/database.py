import sqlite3



connection = sqlite3.connect("data.db")
#connection.row_factory = sqlite3.Row

def create_table():
    with connection:
        connection.execute("CREATE TABLE IF NOT EXISTS entries (content TEXT, date TEXT);")

def add_entry(entry_content,entry_date):
    with connection:
        #connection.execute(f"INSERT into entries values ('{entry_content}','{entry_date}')")
        connection.execute("INSERT into entries values ('?','?')",(entry_content,entry_date))

    """ 
    
    entries.append(
        {
            "Content":entry_content,
            "date":entry_date
        }
        )
        
    """



def get_entry():

    return connection.execute("select * from entries")
    #return cursor
    #return cursor.fetchall()



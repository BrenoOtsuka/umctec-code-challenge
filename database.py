import sqlite3

def create_activity_table(cursor):
    
    cursor.execute("""DROP TABLE IF EXISTS activity""")
    cursor.execute( """CREATE TABLE IF NOT EXISTS
            activity(
                activityID INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                subtitle TEXT NOT NULL,
                sla INTEGER NOT NULL
            )
        """
    )

def create_card_table(cursor):
    
    cursor.execute("""DROP TABLE IF EXISTS card""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS
            card(
                cardID INTEGER PRIMARY KEY AUTOINCREMENT,
                daysSinceCreated INTEGER NOT NULL,
                slaStatus TEXT NOT NULL,
                visitId INTEGER NOT NULL,
                numberOfDocuments INTEGER NOT NULL,
                numberOfNotReceivedDocuments INTEGER NOT NULL,
                numberOfChecklistItem INTEGER NOT NULL,
                numberOfDoneChecklistItem INTEGER NOT NULL
            )      
        """
    )

def create_an_empty_pegcontas_database(filename):
    
    conn = sqlite3.connect(filename)    
    cursor = conn.cursor()
    
    create_activity_table(cursor)
    create_card_table(cursor)
    
    conn.commit()
    conn.close()

def create_an_initialized_pegcontas_database(filename, activities = None, cards = None):
    
    conn = sqlite3.connect(filename)    
    cursor = conn.cursor()
    
    create_activity_table(cursor)
    if activities:
        
        for activity in activities:
            
            columns      = ', '.join(activity.keys())
            placeholders = ', '.join('?' * len(activity))
            query  = 'INSERT INTO activity ({}) VALUES ({})'.format(columns, placeholders)
            cursor.execute(query, tuple(activity.values()))
    
    create_card_table(cursor)
    
    if cards:
        
        for card in cards:
            
            columns      = ', '.join(card.keys())
            placeholders = ', '.join('?' * len(card))
            query  = 'INSERT INTO card ({}) VALUES ({})'.format(columns, placeholders)
            cursor.execute(query, tuple(card.values()))
            
    conn.commit()
    conn.close()

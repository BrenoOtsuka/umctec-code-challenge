import sqlite3

class CardRepository:
    
    def __init__(self, filename):
        
        self.filename = filename
    
    def get_all(self):
        
        conn = sqlite3.connect(self.filename)
        conn.row_factory = sqlite3.Row
        
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM card")
        
        cards = [dict(row) for row in cursor.fetchall()]
        
        conn.close()
    
        return cards

    
    
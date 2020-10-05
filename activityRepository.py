import sqlite3

class ActivityRepository:
    
    def __init__(self, filename):
        
        self.filename = filename
    
    def get_all(self):
        
        conn = sqlite3.connect(self.filename)
        conn.row_factory = sqlite3.Row
        
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM activity")
        
        activities = [dict(row) for row in cursor.fetchall()]
        
        conn.close()
    
        return activities
    
    def add(self, activity):
        
        conn = sqlite3.connect(self.filename)
        
        cursor = conn.cursor()
        
        columns      = ', '.join(activity.keys())
        placeholders = ', '.join('?' * len(activity))
        query  = 'INSERT INTO activity ({}) VALUES ({})'.format(columns, placeholders)
        
        try:
            
            cursor.execute(query, tuple(activity.values()))
            return 0        
        except sqlite3.IntegrityError:
            
            return 1
        finally:
            
            conn.commit()
            conn.close()

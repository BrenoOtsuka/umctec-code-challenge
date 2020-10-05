import sqlite3

class CardRepository:
    
    def __init__(self, filename):
        
        self.filename = filename
    
    def get_all(self):
        
        conn = sqlite3.connect(self.filename)
        conn.row_factory = sqlite3.Row
        
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Card")
        
        cards = [dict(row) for row in cursor.fetchall()]
        
        result = []
        
        def get_info_from(table, idname):
            
            id = card.pop(idname)
            cursor.execute("SELECT * FROM {} WHERE {} = {}".format(table, idname, id))
            return dict(cursor.fetchone())
        
        for card in cards:
            
            card['healthInsurance'] = get_info_from('HealthInsurance', 'healthInsuranceID')
            card['patient'        ] = get_info_from('Patient'        , 'patientID'        )
            card['bill'           ] = get_info_from('Bill'           , 'billID'           )
            result.append(card)
            
        conn.close()
    
        return result

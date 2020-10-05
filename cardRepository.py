import sqlite3

class CardRepository:
    
    def __init__(self, filename):
        
        self.filename = filename
    
    def get_all(self):
        
        conn = sqlite3.connect(self.filename)
        conn.row_factory = sqlite3.Row
        
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Card")
        
        cards = [ dict(row) for row in cursor.fetchall() ]
        
        def get_info_from(table, idname):
            
            id = card.pop(idname)
            cursor.execute("SELECT * FROM {} WHERE {} = {}".format(table, idname, id))
            return dict(cursor.fetchone())
        
        result = []
        
        for card in cards:
            
            card['healthInsurance'] = get_info_from('HealthInsurance', 'healthInsuranceID')
            card['patient'        ] = get_info_from('Patient'        , 'patientID'        )
            card['bill'           ] = get_info_from('Bill'           , 'billID'           )
            result.append(card)
                        
        conn.close()
    
        return result
    
    def add(self, card):
        
        conn = sqlite3.connect(self.filename)
        
        cursor = conn.cursor()
        
        bill = card.pop('bill')
        patient = card.pop('patient')
        healthInsurance = card.pop('healthInsurance')
        
        card['billID'           ] = bill['billID']
        card['patientID'        ] = patient['patientID']
        card['healthInsuranceID'] = healthInsurance['healthInsuranceID']
        
        def insert_in_table(table, entry):
        
            columns      = ', '.join(entry.keys())
            placeholders = ', '.join('?' * len(entry))
            query  = 'INSERT INTO {} ({}) VALUES ({})'.format(table, columns, placeholders)
            
            cursor.execute(query, tuple(entry.values()))
            
        insert_in_table('Card', card)
        insert_in_table('Bill', bill)
        insert_in_table('Patient', patient)
        insert_in_table('HealthInsurance', healthInsurance)
        
        return 0

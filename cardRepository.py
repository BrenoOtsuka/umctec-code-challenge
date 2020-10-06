import sqlite3

class CardRepository:
    
    def __init__(self, filename):
        
        self.filename = filename
    
    def build_cards(self, cursor, cards):
        
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
        
        return result
    
    def get_all(self):
        
        conn = sqlite3.connect(self.filename)
        conn.row_factory = sqlite3.Row
        
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Card")
        
        cards = [ dict(row) for row in cursor.fetchall() ]
        
        result = self.build_cards(cursor, cards)
                        
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
    
    def get_cards_by_some_ID(self, cursor, name, value):
        
        cursor.execute('SELECT * FROM Card WHERE {} = {}'.format(name, value))
        cards = [ dict(row) for row in cursor.fetchall() ]
        
        return self.build_cards(cursor, cards)

    def get_cards_by_billID(self, billID):
        
        conn = sqlite3.connect(self.filename)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        result = self.get_cards_by_some_ID(cursor, 'billID', billID)
        
        conn.close()
        
        return result

    def get_cards_by_visitID(self, visitID):
        
        conn = sqlite3.connect(self.filename)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM Card WHERE visitID = {}'.format(visitID))
        cards = [ dict(row) for row in cursor.fetchall() ]
        
        result = self.build_cards(cursor, cards)
        
        conn.close()
        
        return result

    def get_cards_by_patient_name(self, name):
        
        conn = sqlite3.connect(self.filename)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute('SELECT patientID FROM Patient WHERE name = "{}"'.format(name))
        patient = cursor.fetchone()
        
        result = self.get_cards_by_some_ID(cursor, 'patientID', patient['patientID'])
        
        conn.close()
        
        return result

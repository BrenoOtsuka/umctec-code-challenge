import sqlite3

def create_activity_table(cursor):
    
    cursor.execute("""DROP TABLE IF EXISTS Activity""")
    cursor.execute( """CREATE TABLE IF NOT EXISTS
            Activity(
                activityID INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                subtitle TEXT NOT NULL,
                sla INTEGER NOT NULL
            )
        """
    )

def create_card_table(cursor):
    
    cursor.execute("""DROP TABLE IF EXISTS Card""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS
            Card(
                cardID INTEGER PRIMARY KEY AUTOINCREMENT,
                daysSinceCreated INTEGER NOT NULL,
                slaStatus TEXT NOT NULL,
                visitID INTEGER NOT NULL,
                numberOfDocuments INTEGER NOT NULL,
                numberOfNotReceivedDocuments INTEGER NOT NULL,
                numberOfChecklistItem INTEGER NOT NULL,
                numberOfDoneChecklistItem INTEGER NOT NULL,
                healthInsuranceID INTEGER NOT NULL,
                patientID INTEGER NOT NULL,
                billID INTEGER NOT NULL,
                FOREIGN KEY(healthInsuranceID) REFERENCES HealthInsurance(healthInsuranceID),
                FOREIGN KEY(patientID) REFERENCES Patient(patientID),
                FOREIGN KEY(billID) REFERENCES Bill(billID)
            )      
        """
    )

def create_healthInsurance_table(cursor):

    cursor.execute("""DROP TABLE IF EXISTS HealthInsurance""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS
            HealthInsurance(
                healthInsuranceID INTEGER PRIMARY KEY AUTOINCREMENT,
                name  TEXT NOT NULL
            )
        """
    )
    
def create_patient_table(cursor):
    
    cursor.execute("""DROP TABLE IF EXISTS Patient""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS
            Patient(
                patientID INTEGER PRIMARY KEY AUTOINCREMENT,
                name  TEXT NOT NULL
            )
        """
    )
    
def create_bill_table(cursor):
    
    cursor.execute("""DROP TABLE IF EXISTS Bill""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS
            Bill(
                billID INTEGER PRIMARY KEY AUTOINCREMENT,
                billType TEXT NOT NULL,
                totalAmount REAL DEFAULT 0.0,
                numberOfPendencies INTEGER NOT NULL,
                numberOfOpenPendencies INTEGER NOT NULL
            )
        """
    )
               
def create_an_empty_pegcontas_database(filename):
    
    conn = sqlite3.connect(filename)    
    cursor = conn.cursor()
    
    create_activity_table(cursor)
    
    create_bill_table(cursor)
    create_patient_table(cursor)
    create_healthInsurance_table(cursor)
    
    create_card_table(cursor)
        
    conn.commit()
    conn.close()

def create_an_initialized_pegcontas_database(filename, activities=[], healthInjurances=[], patients=[], bills=[], cards=[]):
    
    create_an_empty_pegcontas_database(filename)
    
    conn = sqlite3.connect(filename)    
    cursor = conn.cursor()
    
    def insert_data_row_by_row(tablename, rows):
        
        for row in rows:
            
            columns      = ', '.join(row.keys())
            placeholders = ', '.join('?' * len(row))
            query  = 'INSERT INTO {} ({}) VALUES ({})'.format(tablename, columns, placeholders)
            cursor.execute(query, tuple(row.values()))
            
    insert_data_row_by_row('Activity', activities)    
    insert_data_row_by_row('HealthInsurance', healthInjurances)
    insert_data_row_by_row('Patient', patients)
    insert_data_row_by_row('Bill', bills)
    insert_data_row_by_row('Card', cards)
            
    conn.commit()
    conn.close()

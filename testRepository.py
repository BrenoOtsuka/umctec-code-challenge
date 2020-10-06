import unittest

from activityRepository import ActivityRepository
from cardRepository import CardRepository
from miniexamples import examples, outputs, test

import database

class TestActivityRepository(unittest.TestCase):
    
    def setUp(self):
        
        self.filename = 'pegcontas.db'

    def init_test_database(self):
        
        activities = examples.get('activities')
        
        cards = examples.get('cards')
        bills = examples.get('bills')
        patients = examples.get('patients')
        healthInsurances = examples.get('healthInsurances')
        
        database.create_an_initialized_pegcontas_database(self.filename,
                                                          activities= activities,
                                                          cards= cards,
                                                          healthInsurances= healthInsurances,
                                                          patients= patients,
                                                          bills= bills)
        
        data = { 
            'activities' : activities, 
            'cards' : cards, 
            'healthInsurances' : healthInsurances,
            'patients' : patients,
            'bills' : bills
        }
        
        return ActivityRepository(self.filename), CardRepository(self.filename), data
        
    def test_get_all_activities_with_empty_dataset(self):
        
        database.create_an_empty_pegcontas_database(self.filename)
        activity_repository = ActivityRepository(self.filename)
        
        activities = activity_repository.get_all()
        
        self.assertEqual(activities, [])
        
    def test_get_all_activities_with_not_empty_dataset(self):
        
        activity_repository, _, data = self.init_test_database()
        activities = activity_repository.get_all()
        self.assertEqual(activities, data['activities'])
    
    def test_add_an_activity_in_an_empty_dataset(self):
        
        database.create_an_empty_pegcontas_database(self.filename)
        activity_repository = ActivityRepository(self.filename)
        data = examples.get('activities')
        
        activity = data[0]
        result = activity_repository.add(activity)
        
        activities = activity_repository.get_all()
        
        self.assertEqual(result, 0)
        self.assertEqual(activities, [ activity ])
        
    def test_add_an_activity_with_repeated_ID_should_raise_Exception(self):
        
        activity_repository, _, data = self.init_test_database()
        result = activity_repository.add(data['activities'][0])
        self.assertEqual(result, 1)
        
    def test_add_an_activity_without_activityID(self):
        
        activity_repository, _, _ = self.init_test_database()
        result = activity_repository.add({ 'title': 'OPME', 'subtitle': 'Finalizar conta', 'sla': 5})
        self.assertEqual(result, 0)
    
    def test_add_an_activity_with_none_attributes(self):
        
        activity_repository, _, _ = self.init_test_database()
        result = activity_repository.add({ 'title': None, 'subtitle': None, 'sla': None})
        self.assertEqual(result, 1)
        
    def test_get_all_cards_with_empty_dataset(self):
        
        database.create_an_empty_pegcontas_database(self.filename)
        card_repository = CardRepository(self.filename)
        
        cards = card_repository.get_all()
        
        self.assertEqual(cards, [])
        
    def test_get_all_cards_with_not_empty_dataset(self):
        
        _, card_repository, _ = self.init_test_database()
        self.assertEqual(card_repository.get_all(), outputs.get('cards'))
    
    def test_add_card(self):
        
        _, card_repository, _ = self.init_test_database()
        self.assertEqual(card_repository.add(test[0].get('input')), 0)
        
    def test_get_card_by_patient_name(self):
        
        _, card_repository, _ = self.init_test_database()
        
        self.assertEqual(card_repository.get_cards_by_patientName(test[1].get('input')), test[1].get('output'))
        
    def test_get_card_by_billID(self):
            
        _, card_repository, _ = self.init_test_database()
        self.assertEqual(card_repository.get_cards_by_billID(test[2].get('input')), test[2].get('output'))
        
    def test_get_card_by_visitID(self):
            
        _, card_repository, _ = self.init_test_database()
        self.assertEqual(card_repository.get_cards_by_visitID(test[2].get('input')), test[3].get('output'))
            
if __name__ == "__main__":
    
    unittest.main()

import unittest

from activityRepository import ActivityRepository
from cardRepository import CardRepository
from miniexamples import examples, outputs, add_card_test

import database

class TestActivityRepository(unittest.TestCase):
    
    def setUp(self):
        
        self.filename = 'pegcontas.db'
        
    def test_get_all_activities_with_empty_dataset(self):
        
        database.create_an_empty_pegcontas_database(self.filename)
        activity_repository = ActivityRepository(self.filename)
        
        activities = activity_repository.get_all()
        
        self.assertEqual(activities, [])
        
    def test_get_all_activities_with_not_empty_dataset(self):
        
        data = examples.get('activities')
        
        database.create_an_initialized_pegcontas_database(self.filename, data)
        activity_repository = ActivityRepository(self.filename)
        
        activities = activity_repository.get_all()
        
        self.assertEqual(activities, data)
    
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
        
        data = examples.get('activities')
        database.create_an_initialized_pegcontas_database(self.filename, data[:1])
        activity_repository = ActivityRepository(self.filename)
        
        activity = data[0]
        result = activity_repository.add(activity)
        
        self.assertEqual(result, 1)
        
    def test_add_an_activity_without_activityID(self):
        
        data = examples.get('activities')
        database.create_an_initialized_pegcontas_database(self.filename, data)
        activity_repository = ActivityRepository(self.filename)
        
        activity = { 'title': 'OPME', 'subtitle': 'Finalizar conta', 'sla': 5}
        result = activity_repository.add(activity)
        
        self.assertEqual(result, 0)
    
    def test_add_an_activity_with_none_attributes(self):
        
        data = examples.get('activities')
        database.create_an_initialized_pegcontas_database(self.filename, data)
        activity_repository = ActivityRepository(self.filename)
        
        result = activity_repository.add({ 'title': None, 'subtitle': None, 'sla': None})
        
        self.assertEqual(result, 1)
        
    def test_get_all_cards_with_empty_dataset(self):
        
        database.create_an_empty_pegcontas_database(self.filename)
        card_repository = CardRepository(self.filename)
        
        cards = card_repository.get_all()
        
        self.assertEqual(cards, [])
        
    def test_get_all_cards_with_not_empty_dataset(self):
        
        cards = examples.get('cards')
        bills = examples.get('bills')
        patients = examples.get('patients')
        healthInjurances = examples.get('healthInsurances')
        
        database.create_an_initialized_pegcontas_database(self.filename,
                                                          cards = cards,
                                                          healthInjurances=healthInjurances,
                                                          patients=patients,
                                                          bills=bills)
        
        card_repository = CardRepository(self.filename)
        
        cards = card_repository.get_all()
        
        self.assertEqual(cards, outputs.get('cards'))
    
    def test_add_card(self):
        
        cards = examples.get('cards')
        bills = examples.get('bills')
        patients = examples.get('patients')
        healthInjurances = examples.get('healthInsurances')
        
        database.create_an_initialized_pegcontas_database(self.filename,
                                                          cards = cards,
                                                          healthInjurances=healthInjurances,
                                                          patients=patients,
                                                          bills=bills)
        
        card_repository = CardRepository(self.filename)
        
        self.assertEqual(card_repository.add(add_card_test[0].get('input')), 0)
            
if __name__ == "__main__":
    
    unittest.main()

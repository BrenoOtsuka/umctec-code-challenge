from flask import Flask
from flask import jsonify, request

from activityRepository import ActivityRepository
from cardRepository import CardRepository

from examples import examples
import database

app = Flask(__name__)

filename = 'pegcontas.db'

database.create_an_initialized_pegcontas_database(filename,
                                                  activities= examples['activities'],
                                                  cards= examples['cards'],
                                                  healthInsurances= examples['healthInsurances'],
                                                  patients= examples['patients'],
                                                  bills= examples['bills'])
activityRepository = ActivityRepository(filename)
cardRepository = CardRepository(filename)

@app.route('/api/v1/activity/all', methods=['GET'])
def get_all_activities():
    
    return jsonify(activityRepository.get_all())

@app.route('/api/v1/activity', methods=['POST'])
def add_activity():
    
    activity = request.json
    
    activityRepository.add(activity)
    
    return jsonify({})

@app.route('/api/v1/card', methods=['GET'])
def find_cards():
    
    query_  = request.args.get('q'     )
    filter_ = request.args.get('filter')
    key = request.json['key']
    
    result = []
    
    if query_ == 'patientName':
        
        result = cardRepository.get_cards_by_patientName(key)
    
    if query_ == 'visitId':
        
        result = cardRepository.get_cards_by_visitID(key)
        
    if query_ == 'billId':
        
        result = cardRepository.get_cards_by_billID(key)
        
    if filter_ == 'PRIORITY':
        pass
    
    if filter_ == 'TO_RECEIVE':
        
        result = list(filter(lambda card: card['numberOfNotReceivedDocuments'] > 0, result))
    
    if filter_ == 'TO_SEND':
        
        result = list(filter(lambda card: card['numberOfNotReceivedDocuments'] == 0 and 
                             card['numberOfDoneChecklistItem'] == card['numberOfChecklistItem'] and
                             card['bill']['numberOfOpenPendencies'] == 0, result))

    return jsonify(result)

@app.route('/api/v1/card', methods=['POST'])
def add_card():
    
    card = request.json
    
    cardRepository.add(card)
    
    return jsonify({})

app.run()
    
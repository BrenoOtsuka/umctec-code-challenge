from flask import request, jsonify, make_response
from routes import  app

from repository.card_repository import cards

@app.route('/api/v1/card/all', methods=['GET'])
def get_all_cards():
    
    return jsonify(cards)

@app.route('/api/v1/card', methods=['POST'])
def create_card():
    
    card = request.json
    cards.append(card)
    
    return make_response({}, 200)

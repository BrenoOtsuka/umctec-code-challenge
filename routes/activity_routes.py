from flask import request, jsonify, make_response
from routes import  app

from repository.activity_repository import activities

@app.route('/api/v1/activity/all', methods=['GET'])
def get_all_activities():
    
    return jsonify(activities)

@app.route('/api/v1/activity', methods=['POST'])
def create_activity():
    
    activity = request.json
    activities.append(activity)
    
    return make_response({}, 200)

import json

from flask import Flask
from flask import jsonify, request

app = Flask(__name__)

app.config['DEBUG'] = True

# templates
activities = [
    { 'title': 'OPME', 'subtitle': 'Finalizar conta', 'sla': 5},
    { 'title': 'Auditoria', 'subtitle': 'Limpar conta', 'sla': 3},
    { 'title': 'Berçario', 'subtitle': 'Organizar prontuário', 'sla': 2},
    { 'title': 'Centro Cirurgico', 'subtitle': 'Organizar prontuário', 'sla': 2}
]

@app.route('/api/v1/activity/all', methods=['GET'])
def get_all_activities():
    return jsonify(activities)

@app.route('/api/v1/activity', methods=['POST'])
def create_activity():
    
    activity = request.json
    activities.append(activity)
    
    return jsonify({'activities' : activities})
    
app.run()

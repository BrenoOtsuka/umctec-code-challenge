from flask import Flask

app = Flask(__name__)

from routes import activity_routes
from routes import card_routes
    
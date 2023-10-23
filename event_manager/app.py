import os

from flask import Flask
from flask_restful import Api
from flask_socketio import SocketIO
from event_manager.event import EventResource
from event_manager.models import db

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
api = Api(app)
socketio = SocketIO(app)
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'events.db')}"  # SQLite database
db.init_app(app)

with app.app_context():
    db.create_all()


def init_resources():
    api.add_resource(EventResource, '/events')


init_resources()

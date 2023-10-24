import os

from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_restful import Api
from flask_socketio import SocketIO

from event_manager import CONFIG
from event_manager.api.event import EventResource, BulkEventsResource
from event_manager.api.sort_by import SortByResource
from event_manager.api.subscribe import SubscribeResource, scheduler
from event_manager.models import db

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
# add rate limiter based on IP
# these values can be customized, plus we can add specific limits for each endpoint
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["200 per day", "50 per hour"],
    storage_uri="memory://"  # use the appropriate URL for your broker
)

api = Api(app)
socketio = SocketIO(app)
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'events.db')}"  # SQLite database
db.init_app(app)

with app.app_context():
    db.create_all()

app.config['MAIL_SERVER'] = CONFIG.smtp.ip
app.config['MAIL_PORT'] = CONFIG.smtp.port
app.config['MAIL_DEFAULT_SENDER'] = CONFIG.smtp.default_sender

if scheduler.running:
    scheduler.shutdown()
scheduler.init_app(app)
scheduler.start()


def init_resources():
    api.add_resource(EventResource, '/events')
    api.add_resource(SortByResource, '/sort_by/<string:sort_by>')
    api.add_resource(BulkEventsResource, '/bulk_events')
    api.add_resource(SubscribeResource, '/subscribe')


init_resources()

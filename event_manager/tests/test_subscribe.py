import unittest
from datetime import datetime

from event_manager.app import app
from event_manager.models import Event, db


class TestSubscribe(unittest.TestCase):
    def setUp(self):
        self.tester = app.test_client()

    def test_get_events(self):
        # create random event
        new_event = Event(
            title='test event',
            location='test location',
            date=datetime.date(datetime.strptime('2020-01-01', '%Y-%m-%d')),
            popularity=0
        )
        db.session.add(new_event)
        db.session.commit()
        # get the id of the event
        event_id = Event.query.filter_by(title='test event').first().id

        response = self.tester.post('/subscribe', json={
            "email": "stam@gmail.com",
            "event_id": event_id
        })
        # should get a message say event date has passed
        self.assertEqual(response.get_json().get('message'), "Event already passed")



import unittest

from event_manager.app import app
from event_manager.models import db, Event


class TestGetEvents(unittest.TestCase):
    def setUp(self):
        self.tester = app.test_client()

    def test_get_events(self):
        response = self.tester.get('/events')
        self.assertIsInstance(response.get_json(), list)
        events = Event.query.all()
        self.assertEqual(len(events), len(response.get_json()))

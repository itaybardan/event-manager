import unittest

from event_manager.app import app
from event_manager.models import Event


class TestSortBy(unittest.TestCase):
    def setUp(self):
        self.tester = app.test_client()

    def test_sort_by(self):
        response = self.tester.get('/sort_by/date')
        self.assertIsInstance(response.get_json(), list)
        events = Event.query.order_by(Event.date.desc()).all()
        self.assertEqual(len(events), len(response.get_json()))
        if len(events) > 0:
            self.assertEqual(events[0].id, response.get_json()[0]['id'])

        response = self.tester.get('/sort_by/popularity')
        self.assertIsInstance(response.get_json(), list)
        if len(events) > 0:
            self.assertEqual(events[0].id, response.get_json()[0]['id'])

        response = self.tester.get('/sort_by/creation_time')
        self.assertIsInstance(response.get_json(), list)
        if len(events) > 0:
            self.assertEqual(events[0].id, response.get_json()[0]['id'])

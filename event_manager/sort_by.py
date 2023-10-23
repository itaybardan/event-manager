from flask import request, jsonify
from flask_restful import Resource
from event_manager.models import Event
from event_manager.event import get_json_evens


class SortByResource(Resource):
    @staticmethod
    def get(sort_by):
        if sort_by in ['date', 'popularity']:
            events = Event.query.order_by(getattr(Event, sort_by).desc()).all()
            return get_json_evens(events)
        return jsonify({"message": "Invalid sort by parameter"})

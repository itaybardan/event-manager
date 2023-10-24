from flask import jsonify
from flask_restful import Resource

from event_manager.api.event import get_json_evens
from event_manager.models import Event


class SortByResource(Resource):
    @staticmethod
    def get(sort_by):
        if sort_by in ['date', 'popularity', 'creation_time']:
            if sort_by == 'creation_time':
                events = Event.query.order_by(Event.id.desc()).all()
            else:
                events = Event.query.order_by(getattr(Event, sort_by).desc()).all()
            return get_json_evens(events)
        return jsonify({"message": "Invalid sort by parameter"})

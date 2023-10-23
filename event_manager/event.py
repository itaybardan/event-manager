from datetime import datetime

from flask import request, jsonify
from flask_restful import Resource

from event_manager.models import db
from event_manager.models import Event


class EventResource(Resource):
    @staticmethod
    def post():
        data = request.get_json()
        new_event = Event(
            title=data['title'],
            location=data['location'],
            # convert string to python date object
            date=datetime.date(datetime.strptime(data['date'], '%Y-%m-%d')),
            popularity=data['popularity']
        )
        db.session.add(new_event)
        db.session.commit()
        return jsonify({"message": "Event scheduled successfully"})

    @staticmethod
    def get():
        event_id = request.args.get('id')
        if event_id:
            event = Event.query.filter_by(id=event_id).first()
            if event is None:
                return jsonify({"message": "Event not found"})
            result_dict = dict(event.__dict__)
            result_dict.pop('_sa_instance_state')
            return jsonify(result_dict)
        else:
            events = Event.query.all()
            result = []
            for event in events:
                result_dict = dict(event.__dict__)
                result_dict.pop('_sa_instance_state')
                result.append(result_dict)
            return jsonify(result)

    @staticmethod
    def put():
        data = request.get_json()
        event_id = data.get('id', None)
        if not event_id:
            return jsonify({"message": "Event id not provided"})
        event = Event.query.filter_by(id=event_id).first()
        if not event:
            return jsonify({"message": "Event not found"})
        event.title = data['title']
        event.location = data['location']
        event.date = data['date']
        event.popularity = data['popularity']
        db.session.commit()
        return jsonify({"message": "Event updated successfully"})

    @staticmethod
    def delete():
        event_id = request.args.get('id')
        event = Event.query.filter_by(id=event_id).first()
        if not event:
            return jsonify({"message": "Event not found"})
        db.session.delete(event)
        db.session.commit()
        return jsonify({"message": "Event deleted successfully"})

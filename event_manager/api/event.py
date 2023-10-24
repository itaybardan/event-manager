from datetime import datetime

from flask import request, jsonify
from flask_restful import Resource

from event_manager.models import Event
from event_manager.models import db

filter_dict = {
    'id': Event.id,
    'location': Event.location,
    'start_date': Event.date,
    'end_date': Event.date,
    'popularity': Event.popularity,
    'title': Event.title,
}


def get_json_evens(events):
    if not events:
        return jsonify({"message": "Events not found"})
    result_dict = []
    for event in events:
        print(f'event: {event}')
        d = dict(event.__dict__)
        d.pop('_sa_instance_state')
        result_dict.append(d)
    return jsonify(result_dict)


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
        filters = []
        query_parameters = ['id', 'location', 'title', 'start_date', 'end_date', 'popularity']
        for param in query_parameters:
            value = request.args.get(param)
            if value:
                print(param, value)
                if param in ['start_date', 'end_date']:
                    if param == 'start_date':
                        event_date = Event.date >= value
                    else:
                        event_date = Event.date <= value
                    filters.append(event_date)
                else:
                    filters.append(filter_dict[param] == value)
        if filters:
            events = Event.query.filter(*filters).all()
            return get_json_evens(events)
        else:
            events = Event.query.all()
            return get_json_evens(events)

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


class BulkEventsResource(Resource):
    @staticmethod
    def post():
        data = request.get_json()
        if not isinstance(data, list):
            return jsonify({"message": "Invalid data format"})
        for event_data in data:
            new_event = Event(
                title=event_data['title'],
                location=event_data['location'],
                # convert string to python date object
                date=datetime.date(datetime.strptime(event_data['date'], '%Y-%m-%d')),
                popularity=event_data['popularity']
            )
            db.session.add(new_event)
        db.session.commit()
        return jsonify({"message": "Events scheduled successfully"})

    @staticmethod
    def delete():
        data = request.get_json()
        if not isinstance(data, list):
            return jsonify({"message": "Invalid data format"})
        for event_data in data:
            event_id = event_data.get('id', None)
            if not event_id:
                return jsonify({"message": "Event id not provided"})
            event = Event.query.filter_by(id=event_id).first()
            if not event:
                return jsonify({"message": "Event not found"})
            db.session.delete(event)
        db.session.commit()
        return jsonify({"message": "Events deleted successfully"})


import logging
from datetime import timedelta, datetime
import atexit

from flask import jsonify, request
from flask_restful import Resource

from event_manager.models import Event
import logging
from flask_apscheduler import APScheduler
from flask_mail import Mail
import smtplib

from event_manager.models import Event
scheduler = APScheduler()
scheduler.start()
# host = "localhost"
# server = smtplib.SMTP(host)

mail = Mail()
# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())


def send_email_notification(event_id, user_email):

    with scheduler.app.app_context():
        logging.info(f'Sending email to {user_email} for event {event_id}')

        # Logic to send the email
        # You can use the Flask-Mail extension for this
        event = Event.query.filter_by(id=event_id).first()
        # server.sendmail("event_manager@example.com", user_email,
        #                 f"Reminder: You have an event in 30 minutes: {event.title}")
        mail.send_message(
            subject='Event notification',
            recipients=[user_email],
            body=f'Reminder: You have an event in 30 minutes: {event.title}'
        )
        logging.info(f'Email sent to {user_email} for event {event_id}')


class SubscribeResource(Resource):
    @staticmethod
    def post():
        data = request.get_json()
        event_id = data.get('event_id')
        email = data.get('email')
        if not event_id:
            return jsonify({"message": "Event id is required"})
        if not email:
            return jsonify({"message": "Email is required"})
        if '@' not in email:
            return jsonify({"message": "Invalid email"})

        event = Event.query.filter_by(id=event_id).first()
        if not event:
            return jsonify({"message": "Event not found"})

        # Calculate the time to send the email (30 minutes before the event)
        event_start_time = event.date
        email_send_time = event_start_time - timedelta(minutes=30)
        # temp just for testing
        email_send_time = datetime.now() + timedelta(seconds=5)
        logging.info(f'Email will be sent at {email_send_time}')
        scheduler.add_job(
            id=f'{event_id}-{email}-{datetime.now()}',
            func=send_email_notification,
            trigger='date',
            run_date=email_send_time,
            args=[event_id, email]
        )

        return jsonify({"message": "Subscribed successfully"})

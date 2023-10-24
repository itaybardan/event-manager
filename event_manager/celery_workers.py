import logging

from celery import Celery
from flask_mail import Mail

from event_manager.models import Event

mail = Mail()
celery = Celery(
    __name__,
    broker='memory://',
    hostname='localhost'
)


@celery.task
def send_email_notification(event_id, user_email):
    logging.info(f'Sending email to {user_email} for event {event_id}')
    # Logic to send the email
    # You can use the Flask-Mail extension for this
    event = Event.query.filter_by(id=event_id).first()
    mail.send_message(
        subject='Event notification',
        recipients=[user_email],
        body=f'Reminder: You have an event in 30 minutes: {event.title}'
    )
    logging.info(f'Email sent to {user_email} for event {event_id}')

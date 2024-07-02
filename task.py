from celery import Celery
from flask_mail import Message
from app import app, mail

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

@celery.task
def send_email(to, booking_info):
    with app.app_context():
        msg = Message(
            subject="Booking Confirmation",
            recipients=[to],
            body=f"Your booking is confirmed. Details: {booking_info}"
        )
        mail.send(msg)

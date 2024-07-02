from flask import Flask, request, jsonify
from celery import Celery
from flask_mail import Mail, Message
from tasks import send_email

app = Flask(__name__)

# Налаштування для Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.example.com'  # Вкажіть ваш SMTP-сервер
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your-email@example.com'
app.config['MAIL_PASSWORD'] = 'your-email-password'
app.config['MAIL_DEFAULT_SENDER'] = 'your-email@example.com'

mail = Mail(app)

# Налаштування для Celery
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)


@app.route('/book', methods=['POST'])
def book():
    data = request.get_json()
    user_email = data['email']
    booking_info = data['info']

    send_email.delay(user_email, booking_info)

    return jsonify({'message': 'Booking confirmed and email is being sent!'})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

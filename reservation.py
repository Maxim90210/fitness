from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/select-service-date', methods=['POST'])
def select_service_date():
    service = request.form['service']
    date = request.form['date']
    available_times = get_available_times(service, date)
    return render_template('available_times.html', service=service, date=date, available_times=available_times)

@app.route('/select-trainer-date', methods=['POST'])
def select_trainer_date():
    trainer = request.form['trainer']
    date = request.form['date']
    available_times = get_available_times(trainer, date)
    return render_template('available_times.html', trainer=trainer, date=date, available_times=available_times)

def get_available_times(service_or_trainer, date):
    return ['09:00', '10:00', '11:00']
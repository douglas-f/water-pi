from flask import Flask, render_template, jsonify
import RPi.GPIO as GPIO
import threading
valve = 37

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(valve, GPIO.OUT)

app = Flask(__name__)



def close_valve_after_delay(delay):
    threading.Timer(delay, lambda: GPIO.output(valve, False)).start()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/status')
def status():
    valve_status = GPIO.input(valve)
    return jsonify({'status': valve_status})

@app.route('/toggle')
def toggle():
    current_status = GPIO.input(valve)
    new_status = not current_status
    GPIO.output(valve, new_status)
    if new_status:  # If the valve is opened
        close_valve_after_delay(10)  # Close the valve after 10 seconds
    return '', 204

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

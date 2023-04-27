from flask import Flask, render_template, jsonify
import RPi.GPIO as GPIO
import threading

app= Flask(__name__)

valve_pin = 37

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(valve_pin, GPIO.OUT)
GPIO.output(valve_pin, 0)



def close_valve_after_delay(delay):
    threading.Timer(delay, lambda: GPIO.output(valve_pin, False)).start()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/status')
def status():
    try:
        valve_status = GPIO.input(valve_pin)
        return jsonify({'status': valve_status})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/toggle')
def toggle():
    try:
        current_status = GPIO.input(valve_pin)
        new_status = not current_status
        GPIO.output(valve_pin, new_status)
        if new_status:  # If the valve is opened
            close_valve_after_delay(10)  # Close the valve after 10 seconds
        return '', 204
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    try:
        app.run(debug=True, host='10.250.1.205', port=5000)
    except Exception as e:
        print('Error:', e)

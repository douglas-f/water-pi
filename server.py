from flask import Flask
from flask import render_template
import RPi.GPIO as rpi
import time

app= Flask(__name__)

valve=37

rpi.setwarnings(False)
rpi.setmode(rpi.BOARD)
rpi.setup(valve, rpi.OUT)
rpi.output(valve, 0)
print("Done")

@app.route('/')
def index():
    return render_template('webpage.html')

@app.route('/A')
def led1on():
    rpi.output(valve,1)
    return render_template('webpage.html')

@app.route('/a')
def led1off():
    rpi.output(valve,0)
    return render_template('webpage.html')

if __name__=="__main__":
    print("Start")
    app.run(debug=True, host='10.250.1.206')
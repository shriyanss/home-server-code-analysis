import RPi.GPIO as GPIO
from flask import *
from time import sleep
import os

app = Flask(__name__)

heater = 16
bulb = 18

GPIO.setmode(GPIO.BOARD)
GPIO.setup(bulb, GPIO.OUT)
GPIO.setup(heater, GPIO.OUT)

@app.route("/")
def handleIndex():
    return render_template("index.html")

@app.route("/schedule/bulb/<hour>/<minute>/<state>")
def handleScheduleBulb(hour, minute, state):
    os.system(("python3 schedulebulb.py " + hour + " " +  minute + " " + state + " &"))
    return "OK"

@app.route("/schedule/heater/<hour>/<minute>/<state>")
def handleScheduleHeater(hour, minute, state):
    os.system(("python3 scheduleheater.py " + hour + " " +  minute + " " + state + " &"))
    return "OK"

@app.route("/blink/<delay>/<number>")
def handleBlink(delay, number):
    num = int(number)
    rt = float(delay)
    for x in range(num):
        GPIO.output(bulb, True)
        sleep(rt)
        GPIO.output(bulb, False)
        sleep(rt)
        GPIO.output(bulb, True)
        sleep(rt)
    return "OK"

@app.route("/bulbon")
def handleBulbOn():
    GPIO.output(bulb, False)
    return "OK"

@app.route("/bulboff")
def handleBulbOff():
    GPIO.output(bulb, True)
    return "OK"

@app.route("/heateroff")
def handleHeaterOff():
    GPIO.output(heater, True)
    return "OK"

@app.route("/heateron")
def handleHeaterOn():
    GPIO.output(heater, False)
    return "OK"

if __name__ == "__main__":
    try:
        app.run("0.0.0.0", 80)
    except KeyboardInterrupt:
        GPIO.cleanup()


from flask import Flask, render_template, request, redirect, url_for
import time
import serial

arduino = serial.Serial('COM3', 9600, timeout=.1)  # Connecting to RPI - Change COM port if needed
print('Connected to Serial Port:', arduino.name)
time.sleep(5)
a_pos = arduino.read()


app = Flask(__name__)
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        if request.form['submit'] == 'submit_actuator':
            time.sleep(0.5)
            actuator_cmd = (request.form['actuator'])
            send_cmd = '<2,{}>'.format(actuator_cmd)
            arduino.write(send_cmd.encode())
        elif request.form['submit'] == 'submit_pump':
            time.sleep(0.5)
            pump_cmd = (request.form['pump'])
            send_pump_cmd = '<1,{}>'.format(pump_cmd)
            arduino.write(send_pump_cmd.encode())
        elif request.form['submit'] == 'submit_sequence':
            time.sleep(0.5)
            sequence_cmd = (request.form['sequence'])
            # send_pump_cmd = '<1,{}>'.format(pump_cmd)
            arduino.write(sequence_cmd.encode())
        else:
            pass
    return render_template('index.html')


if __name__ == '__main__':
    app.run()

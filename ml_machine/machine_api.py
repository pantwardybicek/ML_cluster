from flask import Flask
import ml_machine
app = Flask(__name__)


@app.route('/')
def machine_basic_response():
    if ml_machine.m:
        return "machine instantiated"
    else:
        return "machine present - waiting to run at /[machinenumber]run"

@app.route('/run')
def run_machine():
    return ml_machine.main()
app.run(host='0.0.0.0', port=8000)

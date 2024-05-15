from flask import Flask, render_template, request
import json
import param
import controller
import graphs
#import serial_script

app = Flask(__name__)

# Route to render the HTML form
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission and forward data to serial script
@app.route('/send_data', methods=['POST'])
def send_data():
    if request.method == 'POST':
        # Get data from the forms
        mode = request.form['mode']
        mp = request.form['mp']
        tr = request.form['tr']
        tp = request.form['tp']
        te = request.form['te']
        kp = request.form['kp']
        ki = request.form['ki']
        kd = request.form['kd']
        c = request.form['c']
        pwm = request.form['pwm']
        data = f"Datos Recibidos: mode={mode}, mp={mp},tr={tr},tp={tp},te={te}, kp={kp}, ki={ki}, kd={kd}, c={c}"
        parameters = param.calc(mode,mp,tr,tp,te)
        output = controller.calc(mode,c,parameters,pwm)
        outputFile = open("server/controllerData.json","w")
        json.dump(output,outputFile,indent=4)
        outputFile.close()

        print(parameters)
        graphs.make()
        return output

if __name__ == '__main__':
    app.run(debug=True)
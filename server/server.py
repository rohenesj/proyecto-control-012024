from flask import Flask, render_template, request
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
        # Get data from the form
        mode = request.form['mode']
        zita = request.form['zita']
        tr = request.form['tr']
        tp = request.form['tp']
        te = request.form['te']
        data = f"Datos Recibidos: mode={mode}, zita={zita},tr={tr},tp={tp},te={te}"

        # Forward data to the Python script handling serial communication
        #serial_script.send_data_to_arduino(data)
        print(data)
        # Return a response to the client
        return data

if __name__ == '__main__':
    app.run(debug=True)
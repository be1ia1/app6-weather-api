from flask import Flask, render_template
import pandas as pd

app = Flask('Website')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/api/<station>/<date>')
def about(station, date):
    # df = pd.read_csv('data.csv')
    # temperature = df.station(date)
    temperature = 23
    return str(temperature)

app.run(debug=True)
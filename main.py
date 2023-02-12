from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/api/<station>/<date>')
def api(station, date):
    long_station = "{:06d}".format(int(station))
    path = 'data_small/TG_STAID{}.txt'.format(long_station)
    df = pd.read_csv(path, skiprows=20, parse_dates=["    DATE"])
    temperature = df.loc[df['    DATE'] ==  date]['   TG'].squeeze() / 10
    return {'station': station,
            'date': date,
            'temperature': temperature
    }

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template
from datetime import datetime
from database import create_database, ingest_data, calculate_averages, get_weather_results, get_weather_data

app = Flask(__name__)

@app.route('/ingest')
def ingest():
    directory = r"C:\Users\DAY\Downloads\code-challenge-template-main (1)\code-challenge-template-main\wx_data"
    total_records = ingest_data(directory)
    return f'Successfully ingested weather data. Total records: {total_records}'

@app.route('/avg')
def calculate_avg():
    calculate_averages()
    return 'Successfully calculated average data.'

@app.route('/weat_res')
def show_weather_results():
    results = get_weather_results()
    return render_template('avg.html', SAM=results)

@app.route('/weat_data')
def show_weather_data():
    data = get_weather_data()
    return render_template('index.html', resu=data)

create_database()
app.run(debug=True)



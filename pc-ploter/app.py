#!bin/python
from flask import Flask, jsonify, request, abort, make_response
import pygsheets
import datetime
import urllib.parse as urlparse

app = Flask(__name__)

# http://8values.github.io/results.html?e=54.5&d=69.9&g=74.3&s=75.0'


@app.route('/pc-ploter/api/v1.0/upload', methods=['POST'])
def upload():
    if request.form['channel_id'] != 'G4YP0SJCU':
        abort(400)
    test_results = urlparse.parse_qs(request.form['text'])
    test_results = dict(test_results)
    gc = pygsheets.authorize(service_file='service_creds.json')
    sh = gc.open("ss-python")
    wks = sh.sheet1
    last_id = wks.get_value('A1')
    timestamp = datetime.datetime.now()
    wks.update_row(int(last_id), [str(timestamp), request.form['user_name'], float(test_results['e'][0]),
                                  float(test_results['d'][0]), float(test_results['g'][0]), float(test_results['s'][0])])
    wks.update_cell('A1', int(last_id)+1)
    return jsonify({'record_id': last_id}), 200


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(debug=True)
import flask
from flask import request, jsonify

import numpy as np
import pandas as pd

from cleanup import remove_special_characters

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/cleanup', methods=['POST'])
def make_predictions():
    request_data = request.get_json()
    results = {}
    results['OcrValue_cleaned'] = [remove_special_characters(i) for i in request_data['OcrValue']]
    return jsonify(results)

app.run(host='0.0.0.0', port='80') ##### cia aiskiai reiks pareguliuot
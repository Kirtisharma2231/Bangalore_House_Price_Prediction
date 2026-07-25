from flask import Flask, request, jsonify
import utils
from utils import get_prediction_price
from flask import render_template

app = Flask(__name__)
@app.route('/')
def home():
    return render_template("app.html")

@app.route('/get_location_names')
def get_location_names():

    print(utils.get_location_names())

    response = jsonify({
        'location_names': utils.get_location_names()
    })

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/get_prediction_price', methods=['POST'])
def predict_home_price():

    print("===== New Request =====")
    print(request.form)

    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    print(total_sqft, location, bhk, bath)

    estimated_price = get_prediction_price(location, total_sqft, bhk, bath)

    print("Prediction:", estimated_price)

    response = jsonify({
        'predicted_price': round(float(estimated_price), 2)
    })

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Running the server for house price prediction")

    utils.load_locations_artifacts()

    app.run()
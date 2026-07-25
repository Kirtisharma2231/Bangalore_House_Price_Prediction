import json
import pickle
import numpy as np
import os

__locations = None
__data_columns = None
__model = None


def get_prediction_price(location, sqft, bhk, bath):

    print("Location:", location)
    print("Sqft:", sqft)
    print("BHK:", bhk)
    print("Bath:", bath)

    try:
        loc_index = __data_columns.index(location)
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk

    if loc_index >= 0:
        x[loc_index] = 1

    prediction = __model.predict([x])[0]

    print("Prediction:", prediction)

    return round(prediction, 2)


def get_location_names():
    return __locations


import os

def load_locations_artifacts():
    print("Loading locations artifacts...")

    global __locations
    global __data_columns
    global __model

    base_path = os.path.dirname(__file__)
    artifact_path = os.path.join(base_path, "artifacts")

    with open(os.path.join(artifact_path, "columns.json"), "r") as f:
        __data_columns = json.load(f)["data_columns"]
        __locations = __data_columns[3:]

    with open(os.path.join(artifact_path, "bangalore_home_prices_model.pickle"), "rb") as f:
        __model = pickle.load(f)

    print("Artifacts loaded successfully")


if __name__ == "__main__":

    load_locations_artifacts()

    print(get_location_names())

    print(get_prediction_price('Kothanur', 1200, 2, 2))
    print(get_prediction_price('Whitefield', 1170, 2, 2))
    print(get_prediction_price('Chikka Tirupathi', 2600, 4, 5))
    print(get_prediction_price('Lingadheeranahalli', 1521, 3, 3))
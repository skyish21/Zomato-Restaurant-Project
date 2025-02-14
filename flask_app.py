from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load models
with open('zomato_clf_model.pkl', 'rb') as file:
    price_range_model = pickle.load(file)

with open('zomato_reg_model.pkl', 'rb') as file:
    avg_cost_model = pickle.load(file)

# Features used for prediction
FEATURES = [
    "Restaurant ID", "Country Code", "City", "Locality", "Longitude", "Latitude", 
    "Cuisines", "Currency", "Has Table booking", "Has Online delivery", "Is delivering now",
    "Aggregate rating", "Rating color", "Rating text", "Votes"
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = []
        missing_features = []  # Track missing features

        for feature in FEATURES:
            value = request.form.get(feature, "").strip()

            # Convert Yes/No values to binary
            if feature in ["Has Table booking", "Has Online delivery", "Is delivering now"]:
                value = 1 if value.lower() == "yes" else 0

            # Convert numeric values
            try:
                data.append(float(value))
            except ValueError:
                missing_features.append(feature)

        if missing_features:
            return jsonify({"Error": f"Missing or invalid input for: {', '.join(missing_features)}"})

        # Ensure correct data shape
        data = np.array(data).reshape(1, -1)

        # Predict using models
        price_range_pred = price_range_model.predict(data)[0]
        avg_cost_pred = avg_cost_model.predict(data)[0]

        return jsonify({
            "price_range": int(price_range_pred),
            "avg_cost": f"{int(avg_cost_pred):,.2f}"


        })
    except Exception as e:
        return jsonify({"Error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)






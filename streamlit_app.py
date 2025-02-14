import streamlit as st
import pickle
import numpy as np

# Load trained models
with open("zomato_clf_model.pkl", "rb") as file:
    price_range_model = pickle.load(file)

with open("zomato_reg_model.pkl", "rb") as file:
    avg_cost_model = pickle.load(file)

# Features used for prediction
FEATURES = [
    "Restaurant ID", "Country Code", "City", "Locality", "Longitude", "Latitude",
    "Cuisines", "Currency", "Has Table booking", "Has Online delivery", "Is delivering now",
    "Aggregate rating", "Rating color", "Rating text", "Votes"
]

# Streamlit UI
st.title("🍽️ Zomato Restaurant Price Predictor")

st.markdown("Enter the restaurant details below:")

# Create input fields dynamically
user_input = {}
for feature in FEATURES:
    if feature in ["Has Table booking", "Has Online delivery", "Is delivering now"]:
        user_input[feature] = st.radio(feature, ["Yes", "No"])
    elif feature in ["Aggregate rating", "Votes", "Longitude", "Latitude"]:
        user_input[feature] = st.number_input(feature, step=0.01)
    else:
        user_input[feature] = st.text_input(feature)

# Prediction button
if st.button("Predict"):
    try:
        data = []
        missing_features = []

        for feature in FEATURES:
            value = user_input[feature]  # Get value directly from user_input

            # Convert Yes/No to binary
            if feature in ["Has Table booking", "Has Online delivery", "Is delivering now"]:
                value = 1 if value.lower() == "yes" else 0

            # Convert numeric values
            try:
                data.append(float(value))  # Convert to float safely
            except ValueError:
                missing_features.append(feature)

        if missing_features:
            st.error(f"Missing or invalid input for: {', '.join(missing_features)}")
        else:
            # Convert to numpy array and reshape for model
            data = np.array(data).reshape(1, -1)

            # Make predictions
            price_range_pred = price_range_model.predict(data)[0]
            avg_cost_pred = avg_cost_model.predict(data)[0]

            # Display results
            st.success(f"🏷️ **Predicted Price Range:** {int(price_range_pred)}")
            st.success(f"💰 **Predicted Average Cost for Two:** ₹{int(avg_cost_pred):,.2f}")

    except Exception as e:
        st.error(f"Error: {str(e)}")


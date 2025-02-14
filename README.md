# Zomato Restaurant Price Prediction

## Overview
This project predicts the "Average Cost for Two" and "Price Range" of restaurants using machine learning techniques based on the Zomato dataset. The project is deployed using Flask for a web interface.

## Dataset
The dataset used in this project is from Zomato, which includes restaurant details such as location, ratings, cuisine type, and cost. It is merged with country code data for additional insights.

## Features Used
- **Restaurant name**
- **Country Code**
- **City**
- **Cuisines**
- **Average Cost for Two**
- **Price Range**
- **Rating and Votes**

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/zomato-restaurant-project.git
   cd zomato-restaurant-project

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt

3. Model Training
To train the machine learning model, run the following script:
```bash
python train_model.py
```
This script preprocesses the data and trains the model, saving it as model.pkl.

##  Running the Flask App
1. Start the Flask server:
```bash
python app.py
```
2. Open http://127.0.0.1:5000/ in your browser.

## Running the Streamlit App
1. Start the Streamlit server:

```bash
streamlit run app.py
```
2. Access the web app: Open http://localhost:8501 in your browser.

## Deployment
To deploy on a cloud platform, you can use Streamlit Cloud or any other cloud platform that supports Streamlit apps.

Push your code to a GitHub repository.

1. Deploy to Streamlit Cloud:

2. Go to Streamlit Cloud.
- Sign in with your GitHub account and deploy the app.
- Now, your application is live!



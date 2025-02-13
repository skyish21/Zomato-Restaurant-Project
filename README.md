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

## Deployment
To deploy on a cloud platform like Heroku:

1. Install the Heroku CLI and log in.
2. Create a Procfile with:
```bash
web: python app.py
```
3. Deploy using:
```bash
git init
git add .
git commit -m "Initial commit"
heroku create
git push heroku master



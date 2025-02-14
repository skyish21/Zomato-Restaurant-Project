# Zomato Restaurant Price Prediction

## 📄 Overview
This project predicts the "Average Cost for Two" and "Price Range" of restaurants using machine learning techniques based on the Zomato dataset. The project is deployed using Flask for a web interface.

## 📊 Dataset
The dataset used in this project is from Zomato, which includes restaurant details such as location, ratings, cuisine type, and cost. It is merged with country code data for additional insights.

## ⭐ Features Used

| **Feature**               | **Description**                                                                        |
|---------------------------|----------------------------------------------------------------------------------------|
| **Restaurant Id**         | Unique ID of every restaurant across various cities of the world.                     |
| **Restaurant Name**       | Name of the restaurant.                                                               |
| **Country Code**          | Country in which the restaurant is located.                                           |
| **City**                  | City in which the restaurant is located.                                              |
| **Address**               | Full address of the restaurant.                                                       |
| **Locality**              | Local area or neighborhood in the city.                                               |
| **Locality Verbose**      | Detailed description of the locality.                                                 |
| **Longitude**             | Longitude coordinate of the restaurant’s location.                                    |
| **Latitude**              | Latitude coordinate of the restaurant’s location.                                     |
| **Cuisines**              | The type(s) of cuisine offered by the restaurant.                                     |
| **Currency**              | Currency of the country where the restaurant is located.                              |
| **Has Table booking**     | Indicates if the restaurant provides table booking (Yes/No).                          |
| **Has Online delivery**   | Indicates if the restaurant provides online delivery (Yes/No).                        |
| **Is delivering**         | Indicates if the restaurant is currently delivering (Yes/No).                         |
| **Switch to order menu**  | Indicates if there is a switch to an ordering menu (Yes/No).                          |
| **Aggregate Rating**      | Average rating of the restaurant out of 5.                                            |
| **Rating color**          | Color corresponding to the average rating.                                            |
| **Rating text**           | Textual representation of the rating (e.g., Good, Very Good, Excellent).              |
| **Votes**                 | Number of ratings cast by customers.                                                  |

## 🏷️ Labels 
| **Labels**               | **Description**                                                                        |
|---------------------------|----------------------------------------------------------------------------------------|
| **Price range**           | Price range of the restaurant (e.g., 1-4).                                             |
| **Average Cost for Two**  | Cost for two people in different currencies.                                           |

## 🔧 Installation
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

##  🏃‍♂️ Running the Flask App
1. Start the Flask server:
```bash
python app.py
```
2. Open http://127.0.0.1:5000/ in your browser.

## 🏃‍♂️ Running the Streamlit App
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



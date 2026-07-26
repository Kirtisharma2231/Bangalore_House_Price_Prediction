# Bangalore House Price Prediction using Machine Learning

An end-to-end Machine Learning web application that predicts the estimated price of residential properties in Bangalore based on user inputs such as **Location**, **Total Square Feet**, **BHK**, and **Bathrooms**.

The project demonstrates the complete Machine Learning lifecycle—from data preprocessing and model training to building a Flask backend and an interactive web application.

---

# Project Overview

Real estate pricing depends on multiple factors such as property size, location, and amenities. This project uses Machine Learning techniques to estimate Bangalore house prices by learning patterns from historical housing data.

The application allows users to:

- 📍 Select a property location
- 📐 Enter the total area (Square Feet)
- 🏠 Choose the number of BHK
- 🚿 Select the number of bathrooms
- 💰 Instantly predict the estimated house price

---

# Features

- ✅ End-to-End Machine Learning Project
- ✅ Data Cleaning & Feature Engineering
- ✅ Outlier Detection and Removal
- ✅ One-Hot Encoding for Categorical Features
- ✅ Multiple Regression Models Evaluation
- ✅ Hyperparameter Tuning using GridSearchCV
- ✅ Cross Validation using ShuffleSplit
- ✅ Model Serialization using Pickle
- ✅ Flask REST API
- ✅ Interactive Frontend (HTML, CSS & JavaScript)
- ✅ Dynamic Location Dropdown
- ✅ Deployment Ready

---

# Dataset

**Dataset:** 
:- Bengaluru House Price Dataset

### Features

- Area Type
- Availability
- Location
- Size (BHK)
- Total Square Feet
- Bathrooms
- Balcony
- Price

---

# Tech Stack

## Programming Language

- Python

## Machine Learning

- Scikit-Learn
- NumPy
- Pandas

## Data Visualization

- Matplotlib

## Backend

- Flask

## Frontend

- HTML5
- CSS3
- JavaScript

## Model Serialization

- Pickle

## Version Control

- Git
- GitHub

---

# Machine Learning Workflow

Raw Dataset
      │
      ▼
Data Cleaning
      │
      ▼
Handling Missing Values
      │
      ▼
Feature Engineering
      │
      ▼
Outlier Removal
      │
      ▼
One-Hot Encoding
      │
      ▼
Model Training
      │
      ▼
Hyperparameter Tuning
      │
      ▼
Model Evaluation
      │
      ▼
Pickle Model
      │
      ▼
Flask API
      │
      ▼
Web Application

---

# Data Preprocessing

The following preprocessing techniques were applied:

- Removed unnecessary columns
- Handled missing values
- Converted range values in Total Sqft
- Extracted BHK values
- Created Price Per Square Foot feature
- Grouped rare locations
- One-Hot Encoding
- Removed statistical outliers
- Removed unrealistic entries

---

# Machine Learning Models Evaluated

The following regression models were trained and compared:

- Linear Regression
- Lasso Regression
- Decision Tree Regressor

Hyperparameter tuning was performed using **GridSearchCV**.

Cross-validation was performed using **ShuffleSplit**.

The best-performing model was serialized using **Pickle** for deployment.

---

# Project Structure

BHP
│
├── training
│   ├── code.py
│   ├── Bengaluru_House_Data.csv
│   └── (Optional Notebook)
│
├── server
│   ├── artifacts
│   │   ├── bangalore_home_prices_model.pickle
│   │   └── columns.json
│   │
│   ├── static
│   │   ├── app.css
│   │   └── app.js
│   │
│   ├── templates
│   │   └── app.html
│   │
│   ├── server.py
│   ├── utils.py
│   └── requirements.txt
│
├── images
│
├── README.md

---

# Application Screenshots

## Home Page

> <img width="934" height="871" alt="Screenshot 2026-07-27 at 12 18 05 AM" src="https://github.com/user-attachments/assets/9b140035-3c6a-46e9-a15c-31e91d09f52a" />


![Home](images/home.png)

---

## Location Dropdown

> <img width="764" height="873" alt="Screenshot 2026-07-27 at 12 18 38 AM" src="https://github.com/user-attachments/assets/b592d951-fd97-4c43-9ac5-f9314429aa2d" />

![Location](images/location-dropdown.png)

---

## House Price Prediction

> <img width="726" height="871" alt="Screenshot 2026-07-27 at 12 20 04 AM" src="https://github.com/user-attachments/assets/ee5256e5-9280-4682-ae7f-09d590eead44" />


![Prediction](images/prediction.png)

---

## Model Prediction (Terminal)

> <img width="812" height="870" alt="Screenshot 2026-07-27 at 12 23 10 AM" src="https://github.com/user-attachments/assets/31612465-7143-44b6-b8a9-c3a1e03936cb" />

![Model Output](images/model-output.png)

---

# 📡 REST API

## Get Available Locations

### Endpoint

```http
GET /get_location_names
```

### Response

```json
{
  "location_names": [
    "Whitefield",
    "Rajaji Nagar",
    "Kothanur"
  ]
}
```

---

## Predict House Price

### Endpoint

```http
POST /get_prediction_price
```

### Request

```json
{
  "location":"Whitefield",
  "total_sqft":1200,
  "bhk":2,
  "bath":2
}
```

### Response

```json
{
  "predicted_price":62.47
}
```

---

# Getting Started

## Clone the Repository

git clone https://github.com/YOUR_USERNAME/Bangalore-House-Price-Prediction.git

---

## Navigate to the Project

cd Bangalore-House-Price-Prediction

---

## Open in Browser

http://127.0.0.1:5000/


---

# Future Improvements

- Deploy the application on Render
- Containerize the application using Docker
- Deploy on AWS EC2
- Add CI/CD with GitHub Actions
- Improve prediction accuracy using XGBoost and CatBoost
- Add Interactive Maps
- Add Price Trend Analysis
- Add Authentication & User Profiles
- Build a Recommendation System
- Develop a Mobile-Friendly Responsive UI

---

# Learning Outcomes

This project demonstrates practical experience with:

- Machine Learning Model Development
- Data Cleaning & Feature Engineering
- Feature Encoding
- Regression Algorithms
- Model Evaluation
- Hyperparameter Tuning
- Flask Web Framework
- REST API Development
- Frontend Integration
- Pickle Model Deployment
- Git & GitHub
- End-to-End Machine Learning Project Development

---

# Project Status

🟢 Completed (Local Development)

🔄 Deployment on Render - Planned

☁️ AWS Deployment - Planned

---

# Author

Kirti Sharma

B.Tech | Computer Science | Engineering

Machine Learning | Data Science | Artificial Intelligence

GitHub:
https://github.com/YOUR_USERNAME

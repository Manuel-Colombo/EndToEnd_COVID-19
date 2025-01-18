# COVID-19 Prediction Using Machine Learning

## Project Description

The goal of this project is to develop and compare various machine learning techniques for predicting whether a person is positive for COVID-19, based on a dataset containing demographic, behavioral, and health-related information. Specifically, the following machine learning algorithms are tested and compared: **Logistic Regression**, **Support Vector Machine (SVM)**, **Random Forest**, **K-Nearest Neighbors (KNN)**, **Decision Tree**, **Gradient Boosting**, and **XGBoost**. The analysis focuses on key performance metrics for each model, including **accuracy**, **precision**, **recall**, and **F1 score**, to identify the most effective algorithm for predicting COVID-19 positivity.

### Project Phases

1. **Data Preprocessing**:
   - Clean the dataset, normalize the features, handle missing values, and encode categorical variables as needed.

2. **Model Training**:
   - Train each machine learning algorithm using the dataset and perform cross-validation to obtain performance metrics.

3. **Performance Evaluation**:
   - Evaluate the models using key performance metrics and compare the results to identify the best-performing model.

4. **Selection of the Optimal Model**:
   - Choose the model that demonstrates the best overall performance for predicting COVID-19 positivity.

5. **Model Deployment**:
   - Once the best model is selected, the project proceeds with deploying the model using a web application framework called **Flask**, exposing the model through a RESTful API. This allows real-time predictions to be made by sending input data through HTTP requests.

6. **API Creation**:
   - The model is exposed through an API that accepts input in JSON format and returns the prediction (COVID-19 positive or negative) as output. The API is designed to be easily integrated into other applications or systems.

### Final Objective:
The ultimate goal of this project is to provide an easily accessible platform for COVID-19 positivity prediction, leveraging the power of machine learning models and deploying them through a web application. This enables the model to be used in real-world scenarios, such as mass screening or situations that require rapid decision-making related to pandemic control.

## Technologies Used
- **Machine Learning Algorithms**: Logistic Regression, SVM, Random Forest, KNN, Decision Tree, Gradient Boosting, XGBoost
- **Web Framework**: Flask
- **Model Serialization**: Joblib
- **Python Libraries**: NumPy, Scikit-learn, Pandas



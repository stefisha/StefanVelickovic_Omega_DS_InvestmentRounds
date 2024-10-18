
# Machine Learning API for Predicting Funding Rounds and Series A Funding

This project provides an API for two purposes:

1. Predicting funding rounds (angel, seed, a, b, c) based on company data.
2. Returning the total and average amounts of all Series A funding from the dataset.

The API is built using **Flask**, and the machine learning model is implemented with **scikit-learn** and **XGBoost**. The project also includes Docker support for containerized deployment and SQL commands for running queries in MySQL which were part of the first task. The data used for the third task is stored inside an SQL database named `funding_data.db`.

## Requirements

- Python 3.8+
- Flask
- scikit-learn
- pandas
- joblib
- Docker (for containerization)
- MySQL (for SQL-related tasks)

## Setup and Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/stefisha/StefanVelickovic_Omega_DS_InvestmentRounds
   cd StefanVelickovic_Omega_DS_InvestmentRounds
   ```

2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Start the Flask API:
   ```bash
   python app.py
   ```

   The API will be accessible at `http://localhost:5000`.

## API Endpoints

1. **Predict Funding Rounds**
   - Endpoint: `/predict`
   - Method: POST
   - Input: JSON data with features like `numEmps`, `raisedAmt`, `fundedYear`, etc.
   - Example input:
     ```json
     {
       "numEmps": 50,
       "raisedAmt": 5000000,
       "fundedYear": 2020,
       ...
     }
     ```
   - Example using `curl`:
     ```bash
     curl -X POST http://localhost:5000/predict -H "Content-Type: application/json" -d '{"numEmps": 50, "raisedAmt": 500000, "fundedYear": 2020, "city": "New York", "category": "technology"}'
     ```
   - Windows equivalent:
     ```powershell
     Invoke-WebRequest -Uri http://localhost:5000/predict -Method Post -ContentType "application/json" -Body (@{numEmps=50;raisedAmt=500000;fundedYear=2020;city="New York";category="technology"} | ConvertTo-Json)
     ```

2. **Series A Funding Summary**
   - Endpoint: `/series_a_funding`
   - Method: GET
   - This route returns the **total** and **average** amounts of all Series A funding rounds from the dataset.

## Docker Instructions

1. Build the Docker image:
   ```bash
   docker build -t flask-ml-api .
   ```

2. Run the Docker container:
   ```bash
   docker run -p 5000:5000 flask-ml-api
   ```

3. Once the container is running, use the same API calls as mentioned above to interact with the service.

## SQL Queries and MySQL

This project also includes two SQL commands for tasks run in MySQL:
- The two SQL commands are located in the `/sql/` folder.

## Additional Comments

- The machine learning model was trained on a dataset containing features like `numEmps`, `raisedAmt`, and `fundedYear`. The model type used is **XGBoost**, with hyperparameter tuning, SMOTE, and minmax scaling applied for performance improvement.
- Future improvements could involve scaling the app to handle higher traffic by deploying it on cloud services such as **AWS** or **Azure**.

## Author

Stefan Veličković

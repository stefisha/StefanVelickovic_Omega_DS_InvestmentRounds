# Machine Learning API for Predicting Funding Rounds

This project provides an API to predict funding rounds (angel, seed, a, b, c) based on company data. The API is built using **Flask**, and the machine learning model is implemented with **scikit-learn**. The project also includes Docker support for containerized deployment.

## Requirements

- Python 3.8+
- Flask
- scikit-learn
- pandas
- joblib
- Docker (for containerization)

## Setup and Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/ml-api.git
   cd ml-api
   ```

2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Train the model (optional):
   - If you'd like to train your own model, add the training script and load your dataset to follow the structure mentioned in the notebook or provided code. After training, save the model using `joblib` or `pickle`:
     ```python
     import joblib
     joblib.dump(best_model, 'model.pkl')
     ```

4. Start the Flask API:
   ```bash
   python app.py
   ```

   The API will be accessible at `http://localhost:5000`.

## API Usage

- To make predictions, send a POST request to the `/predict` endpoint with the required input data in JSON format.
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
  curl -X POST http://localhost:5000/predict -H "Content-Type: application/json" -d '{"numEmps": 50, "raisedAmt": 5000000, "fundedYear": 2020}'
  ```

## Docker Instructions

1. Build the Docker image:
   ```bash
   docker build -t flask-ml-api .
   ```

2. Run the Docker container:
   ```bash
   docker run -p 5000:5000 flask-ml-api
   ```

3. Once the container is running, use the same API call as above to make predictions.

## Git Version Control

- Make sure you use **Git** for version control:
  ```bash
  git init
  git add .
  git commit -m "Initial commit"
  ```

  When making updates or changes, use appropriate commit messages:
  ```bash
  git add .
  git commit -m "Implemented Flask API"
  ```

- Push to a remote repository:
  ```bash
  git remote add origin https://github.com/yourusername/ml-api.git
  git push -u origin main
  ```

## Additional Comments

- The model was trained on a dataset with various features like `numEmps`, `raisedAmt`, `fundedYear`, etc. The model type is a **Random Forest Classifier**, and hyperparameter tuning was performed using **RandomizedSearchCV** to improve performance.
- The project is designed to be easily extendable. If additional features or more complex models are required, they can be added to the pipeline.
- Future improvements could involve scaling the app to handle higher traffic by deploying it on cloud services such as **AWS** or **Heroku**.

## Author

[Your Name]

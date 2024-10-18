from flask import Flask, request, jsonify
import sqlite3
import pandas as pd
import joblib  # or pickle for loading the model

app = Flask(__name__)

# Load the pre-trained model
model = joblib.load('model.pkl')  # Ensure 'model.pkl' contains your trained model

# Load the expected columns from your training data (you can save these during training)
expected_columns = joblib.load('expected_columns.pkl')  # Ensure to save your expected columns during training

# Define a route to make predictions
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the JSON request
        data = request.get_json()

        # Convert the input data into a DataFrame
        df = pd.DataFrame([data])

        # Preprocess the data (one-hot encoding)
        df = pd.get_dummies(df, columns=['city', 'category'], drop_first=True)

        # Ensure all expected columns are present
        missing_cols = [col for col in expected_columns if col not in df.columns]

        # Create a DataFrame for missing columns, all filled with zeros
        missing_df = pd.DataFrame(0, index=df.index, columns=missing_cols)

        # Use pd.concat to add the missing columns at once
        df = pd.concat([df, missing_df], axis=1)

        # Ensure the input data has the same order of columns as the training data
        df = df[expected_columns]

        # Convert data types to standard Python types
        df = df.astype(float)  # This converts all types to float (or use int if needed)

        # Perform prediction
        prediction = model.predict(df)
        predicted_round = prediction[0]

        # Return the predicted funding round (ensure it is serializable)
        return jsonify({'predicted_round': int(predicted_round)})

    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/series_a_funding', methods=['GET'])
def get_series_a_funding():
    try:
        # Connect to SQLite and retrieve the values
        conn = sqlite3.connect('funding_data.db')
        cursor = conn.cursor()

        # Fetch the pre-calculated values from the database
        cursor.execute('SELECT total_funding, average_funding FROM series_a_funding')
        result = cursor.fetchone()
        conn.close()

        # Extract the values from the result
        total_series_a_funding = result[0]
        average_series_a_funding = result[1]

        # Return the results as JSON
        return jsonify({
            'total_series_a_funding': round(total_series_a_funding, 2),
            'average_series_a_funding': round(average_series_a_funding, 2)
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

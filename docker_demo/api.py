import pickle
from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
from sklearn.datasets import load_iris

# Define the filename for the saved model
MODEL_FILENAME = 'iris_rf_model.pkl'

# Load target names from iris dataset for readable predictions
try:
    iris = load_iris()
    TARGET_NAMES = iris.target_names
except Exception as e:
    print(f"Could not load iris dataset target names: {e}")
    TARGET_NAMES = ['setosa', 'versicolor', 'virginica']

# Load the trained model from the pickle file
model = None
try:
    with open(MODEL_FILENAME, 'rb') as file:
        model = pickle.load(file)
    print(f"Model '{MODEL_FILENAME}' loaded successfully.")
except FileNotFoundError:
    print(f"Error: Model file '{MODEL_FILENAME}' not found.")
    print("It will be created during the Docker build process if using Docker.")

# Define the input data structure using Pydantic
class IrisFeatures(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# Create the FastAPI app
app = FastAPI(title="Iris Species Prediction API")

@app.get("/", summary="Root endpoint to check if API is running")
def read_root():
    return {"message": "Welcome to the Iris Prediction API! Navigate to /docs for the API documentation."}

@app.post("/predict", summary="Predict the Iris species")
def predict_species(features: IrisFeatures):
    if model is None:
        return {"error": f"Model '{MODEL_FILENAME}' is not loaded. The application might not have started correctly."}

    # Convert input data to a numpy array for the model
    input_data = np.array([[features.sepal_length, features.sepal_width, features.petal_length, features.petal_width]])

    prediction_index = model.predict(input_data)[0]
    prediction_name = TARGET_NAMES[prediction_index]

    return {"predicted_species_index": int(prediction_index), "predicted_species_name": prediction_name}
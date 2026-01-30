import pickle
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Define the filename for the saved model
MODEL_FILENAME = 'iris_rf_model.pkl'

def train_and_save_model():
    """Loads Iris data, trains a model, and saves it to a pickle file."""
    # 1. Load the Iris dataset
    print("Loading the Iris dataset...")
    iris = load_iris()
    X, y = iris.data, iris.target

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # 2. Train a Random Forest Classifier
    print("Training the Random Forest Classifier...")
    rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_classifier.fit(X_train, y_train)
    print("Model training complete.")

    # 3. Save the trained model to a pickle file
    print(f"Saving model to {MODEL_FILENAME}...")
    with open(MODEL_FILENAME, 'wb') as file:
        pickle.dump(rf_classifier, file)
    print("Model saved successfully.")

def load_and_predict():
    """Loads a model from a pickle file and makes a prediction."""
    print(f"\nLoading model from {MODEL_FILENAME}...")
    with open(MODEL_FILENAME, 'rb') as file:
        loaded_model = pickle.load(file)
    print("Model loaded successfully.")
    # You can now use loaded_model to make predictions
    # For example: loaded_model.predict(new_data)

if __name__ == "__main__":
    train_and_save_model()
    load_and_predict()
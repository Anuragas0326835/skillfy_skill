import mlflow
import pandas as pd

# --- Configuration ---
TRACKING_URI = "file:///C:/Users/dell/Desktop/skillfy links/New folder/skillfy_skill/mlruns"
EXPERIMENT_NAME = "Diabetes Prediction Experiment"
# This artifact path should match the one used in your training script
MODEL_ARTIFACT_PATH = "diabetes_model"


def load_latest_model(tracking_uri, experiment_name):
    """
    Loads the latest version of a model from a given MLflow experiment.
    The model is loaded from the 'diabetes_model' artifact path within the latest run.
    """
    mlflow.set_tracking_uri(tracking_uri)

    try:
        experiment = mlflow.get_experiment_by_name(experiment_name)
        if experiment is None:
            raise Exception(f"Experiment '{experiment_name}' not found.")

        # Search for the latest run in the experiment
        latest_run = mlflow.search_runs(
            experiment_ids=[experiment.experiment_id],
            order_by=["start_time DESC"],
            max_results=1
        ).iloc[0]

        run_id = latest_run.run_id
        print(f"Found latest run with ID: {run_id}")

        # Construct model URI using the run ID and artifact path
        model_uri = f"runs:/{run_id}/{MODEL_ARTIFACT_PATH}"

        # Load the model (which is a scikit-learn pipeline)
        loaded_model = mlflow.sklearn.load_model(model_uri)
        print(f"Model pipeline loaded successfully from {model_uri}")
        return loaded_model

    except Exception as e:
        print(f"An error occurred while loading the model: {e}")
        return None


def predict_on_new_data(model):
    """
    Makes a prediction on new sample data using the loaded model pipeline.
    """
    if model is None:
        print("Model not loaded, cannot make prediction.")
        return

    # Create a sample DataFrame for prediction.
    # The columns must match the training data features.
    sample_data = {
        'Pregnancies': [6, 1],
        'Glucose': [148, 85],
        'BloodPressure': [72, 66],
        'SkinThickness': [35, 29],
        'Insulin': [0, 0],
        'BMI': [33.6, 26.6],
        'DiabetesPedigreeFunction': [0.627, 0.351],
        'Age': [50, 31]
    }
    new_data_df = pd.DataFrame(sample_data)

    print("\n--- Predicting on New Data ---")
    print(new_data_df)

    # The loaded model is a pipeline, so it handles scaling internally.
    predictions = model.predict(new_data_df)
    print(f"\nPredictions (0=No Diabetes, 1=Diabetes): {predictions}")


if __name__ == "__main__":
    # 1. Load the latest model from MLflow
    model_pipeline = load_latest_model(TRACKING_URI, EXPERIMENT_NAME)

    # 2. Make predictions on new data
    predict_on_new_data(model_pipeline)
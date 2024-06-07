"""
Before running this script independently I have to run in the terminal this:

Launch the mlflow server locally by running the following command:

mlflow server --backend-store-uri sqlite:///backend.db
"""
import os
import pickle
import click

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

import mlflow
mlflow.set_tracking_uri("cd ..
                        ") # Here mlflow will be running and tracking
mlflow.set_experiment("hw-2")
mlflow.sklearn.autolog()

def load_pickle(filename: str):
    with open(filename, "rb") as f_in:
        return pickle.load(f_in)


@click.command()
@click.option(
    "--data_path",
    default="./output",
    help="Location where the processed NYC taxi trip data was saved"
)
def run_train(data_path: str):    
    #mlflow.set_tracking_uri("http://127.0.0.1:5000") # Here mlflow will be running and tracking
    #mlflow.set_experiment("hw-2")
    # Enable autologging
    #mlflow.sklearn.autolog()
    
    with mlflow.start_run():
        X_train, y_train = load_pickle(os.path.join(data_path, "train.pkl"))
        X_val, y_val = load_pickle(os.path.join(data_path, "val.pkl"))

        rf = RandomForestRegressor(max_depth=10, random_state=0)
        rf.fit(X_train, y_train)
        y_pred = rf.predict(X_val)

        rmse = mean_squared_error(y_val, y_pred, squared=False)


if __name__ == '__main__':
    run_train()
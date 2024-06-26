# Getting started with MLflow

## Installing MLflow
Before installing MLfLow I will create a virtual environment with Conda:\
**Create:**\
conda create -n exp-tracking-env python=3.9

**Activate:**\
conda activate exp-tracking-env  

Install requirements:\
pip install -r requirements.txt (if pip is not installed --> conda install pip)\
or\
conda install --file requirements.txt (in this file we have the MLflow, so here we are installing MLflow)

**Deactivate:**\
conda deactivate

**Note:** This environment (entorno) won't be in the same directory where I have my repo (like when I use venv), thus, I don't have to add it to my .gitignore.\
**Note 2:** I can do this from the VSCode terminal

## Running MLflow
Once you've installed MLflow, you may access the MLflow web UI by running the mlflow ui command from a terminal using your Conda environment; however, you will need to provide a backend 
in order to save and retrieve experiment data. We can use SQLite as a backend with the following command:

mlflow ui --backend-store-uri sqlite:///mlflow.db

This will create a mlflow.db file in the folder your run the command from. You should now be able to access the web UI by browsing to http://127.0.0.1:5000 (or the link I see after "Listening at:")

**Note:** I have to make sure tu run the previous command in the same folder where I have the notebook where I will run the experiments.

If I want to shut down the ui that is currently running:\
Kill the process\
pkill -f gunicorn

# Machine Learning lifecycle

![image](https://github.com/cvljubet/mlops_course_repo/assets/45463413/c310c70c-5ee8-41c8-b10c-d6fd34161103)

# Configuring MLflow
* Backend Store (where mlflow will save metadata about my experiments)
  * Local filesystem (by default if I don't configure a backend store)
  * SQLAlchemy compatible DB (e.g. SQLite)
* Artifacts store 
  * Local filesystem (by default if I don't specify an artifact store)
  * Remote (e.g. S3 bucket, GCS bucket)
* Tracking server (decide if I require to run a tracking server)
  * No tracking server (Ex. I'm by myself in a competition)
  * Localhost (Ex. a team)
  * Remote (Ex. a team




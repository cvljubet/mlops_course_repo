# Introduction to ML Pipelines and Mage
ML Pipeline --> A set of steps to run codes ir order tu create and use a model. We can call it also "Workflow orchestration".

We could have all of our functions for downloading data, preparing data, feature engineering, finding best model, training model in a same .py file and that .py file have a main function to call the other functions. This is more organized than a notebook (we can call it a pipeline) but using just this .py file there are some issues:
* How do we schedule this?
* Where do we run it?
* Where will be the instance to run the script?
* How do we scale this if we need more and more jobs?
* What happens if a function (step) fails? The rest will fail also.
* What if we have some temporary fails?
* If we work in a team will be difficult tu maintain.

Because of the mentioned questions we usually use tools for workflows orchestrations.

Some tools for general purposes (ex. data engineering, machine learning engineering):
* Airflow
* Prefect
* Mage
* Luigi

Some tools specifics to machine learning:
* Kubeflow pipelines
* MLflow pipelines

# What is MLOps
Operationalizing ML models involves moving them from development to production to drive business value.

## Step 1
Preparing the model for deployment involves optimizing performance, ensuring it handles real-world data, and packaging it for integration into existing systems.

## Step 2
Deploying the model involves moving it from development to production, making it accessible to users and applications.

## Step 3
Once deployed, models must be continuously monitored for accuracy and reliability, and may need retraining on new data and updates to maintain effectiveness.

## Step 4
The operationalized model must be integrated into existing workflows, applications, and decision-making processes to drive business impact.

Effective operationalization enables organizations to move beyond experimentation and drive tangible value from ML at scale, powering intelligent applications that personalize the customer experience and creates real business value.

# How Mage helps MLOps
## 1. Data preparation
Mage offers features to build, run, and manage data pipelines for data transformation and integration, including pipeline orchestration, notebook environments, data integrations, and streaming pipelines for real-time data.

## 2. Training and deployment
Mage helps prepare data, train machine learning models, and deploy them with accessible API endpoints.

## 3. Standardize complex processes
Mage simplifies MLOps by providing a unified platform for data pipelining, model development, deployment, versioning, CI/CD, and maintenance, allowing developers to focus on model creation while improving efficiency and collaboration.

# Running Mage on Windows with Docker-Compose
Supposing we have a project with Mage:
Launch Mage and the database service (PostgreSQL):\
./scripts/start.sh\
A web site interface will open (in localhost), then do this:
* Click on "Command center button".
* Write "text editor" and open.
* What I edit in this editor (that is, the changes I make inside Mage) will be reflected in my system (in my host machine), once I save it. 



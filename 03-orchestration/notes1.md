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




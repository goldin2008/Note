# Projects

## Work
#### Container/Kubernetes
<!-- https://github.com/https-deeplearning-ai/machine-learning-engineering-for-production-public/tree/main/course4/week2-ungraded-labs/C4_W2_Lab_2_Intro_to_Kubernetes -->

You will create a deployment that spins up containers that runs a model server. In this case, that will be from the tensorflow/serving image you already used in the previous labs. The deployment can be accessed by external terminals (i.e. your users) through an exposed service. This brings inference requests to the model servers and responds with predictions from your model.

Lastly, the deployment will spin up or spin down pods based on CPU utilization. It will start with one pod but when the load exceeds a pre-defined point, it will spin up additional pods to share the load.

#### Fraud Detection
<!-- https://shap.readthedocs.io/en/latest/index.html -->


#### Converse Quality Assurance
There are some problems we encountered in our qa converse project, and those pain points are actually for all NLP related tasks due to lack of existing platform and support.
1. data and model storage and security issue due to github capacity limit
2. experiments, data and model versioning
3. optimum parameters/hyperparameters selection trials
4. environment and outdated libraries, dependencies test and monitoring
5. one-time code and project

To Solve theses pain points, I built a ML pipeline including data ingestion, model training, testing, refitting, deployment, monitoring and reporting.

1. Data and Models Storage
Github is not a good place to store due to security and capacity limit.
Store our data and models in S3 bucket.

2. Automation
model training, testing, refitting and deployment, experiments comparison and optimum parameters/hyperparameters selection

3. Real production environment
Since we can not test application in production directly.
We use Fastapi and built an API to make inference and test model and make sure it works in real production evnironment.

4. Automatic Reporting
EDA, model performance, environments(ibraries and dependencies) and business value.

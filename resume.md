# Projects

## Work
#### Container/Kubernetes
<!-- https://github.com/https-deeplearning-ai/machine-learning-engineering-for-production-public/tree/main/course4/week2-ungraded-labs/C4_W2_Lab_2_Intro_to_Kubernetes -->

`Architecture`
You will create a deployment that spins up containers that runs a model server. In this case, that will be from the tensorflow/serving image you already used in the previous labs. The deployment can be accessed by external terminals (i.e. your users) through an exposed service. This brings inference requests to the model servers and responds with predictions from your model.
Lastly, the deployment will spin up or spin down pods based on CPU utilization. It will start with one pod but when the load exceeds a pre-defined point, it will spin up additional pods to share the load.

`Start Minikube`
You are now almost ready to start your Kubernetes cluster. There is just one more additional step. As mentioned earlier, Minikube runs inside a virtual machine. That implies that the pods you will create later on will only see the volumes inside this VM. Thus, if you want to load a model into your pods, then you should first mount the location of this model inside Minikube's VM.

`Creating Objects with YAML files`
In the official Kubernetes basics tutorial, you mainly used kubectl to create objects such as pods, deployments, and services. While this definitely works, your setup will be more portable and easier to maintain if you configure them using YAML files. We've included these in the yaml directory of this ungraded lab so you can peruse how these are constructed. The Kubernetes API also documents the supported fields for each object.

`Config Maps`
First, you will create a config map that defines a MODEL_NAME and MODEL_PATH variable. This is needed because of how the tensorflow/serving image is configured. If you look at the last layer of the docker file here, you'll see that it runs a /usr/bin/tf_serving_entrypoint.sh script when it starts the container.

`Create a Deployment`
You will now create the deployment for your application. Please open yaml/deployment.yaml to see the spec for this object. You will see that it starts up one replica, uses tensorflow/serving as the container image and defines environment variables via the envFrom tag. It also exposes port 8501 of the container because you will be sending HTTP requests to it later on. It also defines cpu and memory limits and mounts the volume from the Minikube VM to the container.

`Expose the deployment through a service`
As you learned in the Kubernetes tutorial before, you will need to create a service so your application can be accessible outside the cluster.

`Horizontal Pod Autoscaler`
As mentioned in the lectures, one of the great advantages of container orchestration is it allows you to scale your application depending on user needs. Kubernetes provides a Horizontal Pod Autoscaler (HPA) to create or remove replicasets based on observed metrics. To do this, the HPA queries a Metrics Server to measure resource utilization such as CPU and memory.

`Stress Test`
To test the autoscaling capability of your deployment, we provided a short bash script (request.sh) that will just persistently send requests to your application.

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

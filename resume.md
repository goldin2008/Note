# Projects

## 1. Container/Kubernetes/fastAPI
<!-- https://github.com/https-deeplearning-ai/machine-learning-engineering-for-production-public/tree/main/course4/week2-ungraded-labs/C4_W2_Lab_2_Intro_to_Kubernetes -->

<!-- https://github.com/https-deeplearning-ai/machine-learning-engineering-for-production-public/blob/main/course4/week2-ungraded-labs/C4_W2_Lab_1_FastAPI_Docker/README.md -->

<!-- https://github.com/https-deeplearning-ai/machine-learning-engineering-for-production-public/blob/main/course4/week2-ungraded-labs/C4_W2_Lab_3_Latency_Test_Compose/README.md -->

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

`Why and how to use Docker Compose`
In this lab you saw how to use Docker Compose to run multiple-container applications by setting a configuration file in YAML format. This is a much better alternative than spinning and linking the containers manually as it handles most of this for you. You also were exposed to Locust and how it can be leveraged to perform load testing on your servers.
You could manually spin up the 5 containers but you will need to find a way to link them together via a network. This can be achieved using regular Docker commands but it is much easier to accomplish using Docker Compose.
Instead of running each container in a separate terminal window you can simply define a configuration file in YAML format and use the docker-compose up command to run your multi-container application. In case you haven't worked with YAML files, these are usually for configuration and they work in a similar fashion to Python, by using indentation to specify scope.

`Understanding Locust`
By convention the file that handles the locust logic is named locustfile.py. Unlike Dockerfiles, this file is a regular python script. Remember you can take a look at the complete file in this repo.
The way locust works is by simulating users that will constantly send requests to your services. By doing this you can measure things like RPS (requests per second) or the average time each request is taking. This is great to understand the limitations of your servers and to test if they will work under the circumstances they will be exposed once they are launched into production.
Now you should have a clearer understanding of how to use these tools to create production-ready services that will endure the conditions they will be exposed to once deployed to the outside world.


## 2. Fraud Detection/Kubeflow
<!-- https://shap.readthedocs.io/en/latest/index.html -->

<!-- https://github.com/https-deeplearning-ai/machine-learning-engineering-for-production-public/blob/main/course4/week1-ungraded-labs/C4_W1_Optional_Lab_1_XGBoost_CAIP/C4_W1_Optional_Lab_1.md -->

<!-- https://colab.research.google.com/github/https-deeplearning-ai/machine-learning-engineering-for-production-public/blob/main/course4/week3-ungraded-labs/C4_W3_Lab_1_Intro_to_KFP/C4_W3_Lab_1_Kubeflow_Pipelines.ipynb#scrollTo=BE97DJ2_2gYM -->

In this lab, you will have some hands-on practice with `Kubeflow Pipelines`. As mentioned in the lectures, modern ML engineering is moving towards pipeline automation for rapid iteration and experiment tracking. This is especially useful in production deployments where models need to be frequently retrained to catch trends in newer data.
`Kubeflow Pipelines` is one component of the Kubeflow suite of tools for machine learning workflows. It is deployed on top of a `Kubernetes cluster` and builds an infrastructure for orchestrating ML pipelines and monitoring inputs and outputs of each component.
Platforms such as Kubeflow helps you to build ML pipelines that can be automated, reproducible, and easily monitored.
This lab demonstrated how you can use Kubeflow Pipelines to build and orchestrate your ML workflows. Having automated, shareable, and modular pipelines is a very useful feature in production deployments so you and your team can monitor and maintain your system more effectively.

`Docker` - platform for building and running containerized applications.
`kubectl` - tool for running commands on Kubernetes clusters.
`kind` - a Kubernetes distribution for running local clusters using Docker.
`Kubeflow Pipelines` (KFP) - a platform for building and deploying portable, scalable machine learning (ML) workflows based on Docker containers.

`One prediction per request`
- `Coding the server`
Begin by importing the necessary dependencies. You will be using pickle for loading the pre-trained model saved in the app/wine.pkl file, numpy for tensor manipulation, and the rest for developing the web server with FastAPI.
Now it is time to load the classifier into memory so it can be used for prediction. This can be done in the global scope of the script but here it is done inside a function to show you a cool feature of FastAPI.
Finally you need to create the function that will handle the prediction. This function will be run when you visit the /predict endpoint of the server and it expects a Wine data point.
Now the server's code is ready for inference, although you still need to spin it up. If you want to try it locally (given that you have the required dependencies installed) you can do so by using the command uvicorn main:app --reload while on the same directory as the main.py file. However this is not required as you will be dockerizing this server next.
- `Dockerizing the server`
Also you should create a directory called app and place main.py (the server) and its dependencies (wine.pkl) there as explained on the official FastAPI docs on how to deploy with Docker.
- `Create the Dockerfile`
The Dockerfile is made up of all the instructions required to build your image. 
Base Image, Installing dependencies, Exposing the port, Copying your server into the imag, Spinning up the server
- `Build the image`
Now that the Dockerfile is ready and you understand its contents, it is time to build the image. To do so, double check that you are within the no-batch directory and use the docker build command.
- `Run the container`
Now that the image has been successfully built it is time to run a container out of it.
- `Make requests to the server`
Now that the server is listening to requests on port 80, you can send POST requests to it for predicting classes of wine.

`Adding batching to the server`
<!-- https://github.com/https-deeplearning-ai/machine-learning-engineering-for-production-public/blob/main/course4/week2-ungraded-labs/C4_W2_Lab_1_FastAPI_Docker/with-batch/README.md -->

`Online prediction` is also known as `synchronous prediction`: predictions are generated in `synchronization` with requests, or on-demand prediction: predictions are generated after requests for these predictions, not before.
Traditionally, when doing online prediction, requests are sent to the prediction service via RESTful APIs
`Batch prediction` is also known as `asynchronous prediction`: predictions are generated `asynchronously` with requests arrive
The terms online prediction and batch prediction can be confusing. Both can make predictions for multiple samples (in batch) or one sample at a time. To avoid this confusion, people sometimes prefer the terms `synchronous prediction` and `asynchronous prediction`.


## 3. Converse Quality Assurance
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

## XGBoost model on Cloud AI Platform
<!-- https://github.com/https-deeplearning-ai/machine-learning-engineering-for-production-public/blob/main/course4/week1-ungraded-labs/C4_W1_Optional_Lab_1_XGBoost_CAIP/C4_W1_Optional_Lab_1.md -->

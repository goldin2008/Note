## MLOPS interview prep
APIs are simply endpoints that accept some sort of input and return some sort of output. Computers just want to share data. And so that’s what an API provides.

REST API. We’ll use the library Flask. Flask is a web framework, which is a fancy way of saying a library with a bunch of helper tools for building web applications.
I will go over how to productionize a Machine Learning model by building a normal website using the Flask web micro-framework.

#### Sagemaker
<!-- https://www.analyticsvidhya.com/blog/2020/11/deployment-of-ml-models-in-cloud-aws-sagemaker%E2%80%8Ain-built-algorithms/ -->
Creating a Notebook Instance: The whole process kicks start by creating a notebook instance where a virtual machine(EC2—Elastic cloud) and storage(EBS volume) get allocated for our objective. It is the user’s choice to pick the type & size of the EC2 as well as the capacity of EBS volume. Amazon Elastic Block Store (Amazon EBS) provides block level storage volumes for use with EC2 instances. EBS volumes behave like raw, unformatted block devices. You can mount these volumes as devices on your instances.
`Step1: Creating a Notebook Instance`
`Step2: Loading Datasets, EDA & Train validation split`
`Step3: Dataset upload in S3 bucket`
#boto3 => Pyhton library for calling up AWS services
`Step4: Training Process`
Since we are using in-built algorithms, we need to make a call to those algorithms for training. These algorithms are stored as containers in ECR (Elastic Container Registry) which are maintained for each region. The subsequent step is building the model using the docker container from ECR. Amazon Elastic Container Registry (ECR) is a fully managed container registry that makes it easy to store, manage, share, and deploy your container images and artifacts anywhere. Docker Hub is a service provided by Docker for finding and sharing container images with your team. During the training, the algorithm is accessed from ECR and the datasets are retrieved from the s3 bucket.
`Step5: Model Deployment and Endpoint Creation`
The final step in the whole process is deploying the finalized model and creating an endpoint that will be accessed by external interfaces.
The next step would be to use our own model rather than the one already present in the ECR that comes with Sagemaker.

<!-- https://medium.com/geekculture/84af8989d065 -->
- Training and deploying inside SageMaker , both using SageMaker’s own built-in algorithm containers (pls note these are AWS managed containers).
- Use SageMaker’s (AWS managed) built-in algorithms containers, but customize the training as per needs with our own scripts ( Bring Your Own Model type).


The notebook code does the following.
- Load the model file, open it and test and then upload it to a S3 bucket ( from where SageMaker will take the model artifacts).
- Create a SageMaker model object from the model stored in S3. We will use SageMaker built-in XGBoost container for this purpose, as the model was locally trained with XGBoost algorithm. Depending on the algorithm you use for modelling, you have to properly pick the corresponding built-in container and deal with the nuances associated with that..SageMaker developer guide should help in that.
- Create an Endpoint Configuration. Endpoint is the interface through which the outer world can use a deployed model for predictions. More details about Endpoints can be found in SageMaker documentation.
- Create an Endpoint for the model.
- Invoke the endpoint from within the deployment notebook to confirm the endpoint and the model are working fine.
After running the notebook till this point, you can see the endpoint created under
Sagemaker -> Inference -> Endpoints in AWS console.

The following diagram shows how the deployed model can be called using a server-less AWS architecture. A client script calls an Amazon `API Gateway` API action and passes parameter values. API Gateway is a layer that provides the API to the client. API Gateway passes the parameter values to the `Lambda` function. The Lambda function parses the value and invokes the `SageMaker model endpoint`, passing the parameters to the same. The model performs the prediction task and returns the prediction results to `Lambda`. The Lambda function parses the returned value and sends it back to `API Gateway`. API Gateway responds to the client with that value.

- `Training our model locally/outside SageMaker and then use SageMaker’s built-in algorithm container to just deploy the locally trained model (Bring Your Own Model type ).`
1. In local laptop, use Jupyter notebook and train a XGBoost classification model on the popular Iris flower data set.
2. Test the model and save the model file locally using joblib.
3. In AWS console, create a SageMaker notebook instance and open a Jupyter notebook.
4. Run the iris-model-deployment notebook in SageMaker.
5. Create a IAM role that includes the following policy, which gives your Lambda function permission to invoke a model endpoint.
6. Create a Lambda function with the below mentioned python code, that calls the SageMaker runtime invoke_endpoint and returns the prediction.
7. Create a REST API and integrate with the Lambda function
8. Finally, use Postman App in your laptop, to POST the Iris flower test data to API gateway and get the prediction result back from AWS cloud.


- `Train our model in whatever method / or our own algorithms as we want locally in our container (built and managed by us ) and then bring that container to SageMaker and deploy it for usage (BYOC- Bring Your Own Container).`
<!-- https://towardsdatascience.com/deploying-your-ml-models-to-aws-sagemaker-6948439f48e1 -->
It starts with putting your tarballed ML models into an AWS `S3 bucket`. Then you deploy your `Docker image` to `AWS ECR`, which will be consumed by your `SageMaker`. Docker is used to package your ML inference logic code into a containerized environment. SageMaker will also consume your models in S3 as well. As a client, you only interact with the SageMaker endpoint, which downloads your models from S3 first and invokes your ML inference code from ECR.

In summary, the idea is to create a docker container and deploy it to AWS ECR and create a SageMaker instance to use the ECR image. I hope you find this explanation and the attached code useful but it’s worth mentioning that this whole interaction with SageMaker was quite frustrating.

`Machine Learning Serverlessly Using AWS Lambda, Docker, ECR, S3 and API Gateway`
<!-- https://towardsdatascience.com/machine-learning-serverlessly-1a532685fa7c -->
We chose a serverless architecture so that we don’t have to provision, run and maintain servers but instead focus on developing a user-friendly application.






#### Docker
<!-- https://medium.datadriveninvestor.com/build-and-deploy-your-machine-learning-application-with-docker-f6ec5acdf2ff -->
<!-- https://github.com/raja-surya/aws-deployment-1/blob/main/Iris-model-deployment.ipynb -->
Create `Dockerfile` (txt file) -> Build `Docker Image` (docker build) -> Create `Docker Container` (docker run/docker ps) -> Serve as containers for your application
`Docker` is a tool that makes it easier to create, deploy, and run any application by using what is called a container. It’s also a software platform, which is used to create Docker images that will be referred to as a Docker container once it’s been deployed.
A `Docker Container` is an isolated environment which contains all the required dependencies for your application to run, it is often referred to as a running instance of a Docker image.
a Docker Image is a read-only file that contains our application along with the dependencies (like a blueprint) and a Docker container is a running image (we can run a number of containers using one image)
A `Docker Image` is a file(read-only), comprised of multiple layers, that is used to execute code in a Docker container. Docker images are found in a large hub which is referred to as Docker Hub. So you pull images from the hub or you build a custom image from a base image and when these images are being executed they serve as containers for your application.
So combining the pieces together we can simply define `Docker` as:
A Software platform which makes it easier to create and deploy any application by creating a Docker image which will then be a Docker container which contains all the dependencies and packages we need for our application to work once it’s been deployed.
`Benefits of Docker`
- Docker solves the problem of having an identical environment across various stages of development and having isolated environments in your individual applications.
- Docker allows you to run your application from anywhere as long as you have docker installed on that machine.
- Docker gives you the liberty to scale up quickly.
- Expand your development team painlessly.
A `Dockerfile` is a text file that defines a Docker image. You’ll use a Dockerfile to create your own custom Docker image when the base image you want to use for your project doesn’t meet your required needs.

Deploy that dockerized image to the cloud with AWS using `AWS EC2` instance
<!-- https://medium.datadriveninvestor.com/dockerize-and-deploy-your-machine-learning-application-on-aws-e2537bd3df21 -->
They talk of launching a AWS EC2 instance to host our own Flask App and ML model; where a client (browser) would be used to send the test data to the flask server hosted on EC2, which in turn invokes the model hosted on the same EC2 to get the prediction and then sends the prediction result to the client.

push your image to `Docker Hub` (container registry) -> Setting up `AWS EC2` -> Run the `Docker Image` on the `EC2`
<!-- https://www.machinelearningplus.com/deployment/deploy-ml-model-aws-ec2-instance/ -->
<!-- https://blog.dataiku.com/how-to-perform-basic-ml-serving-with-python-docker-kubernetes -->
- Setting up `AWS EC2`
- Create a Key Pair
A key pair is a file that is needed to connect to your AWS instance.
- Create a new security group in the Configure Security Group section.
A security group lets us control who can send requests to the server (instance).
- Connect to AWS EC2 instance using ssh
The SSH allows me to connect to my instance on my machine and the HTTP routes my server IP to the DNS for me to make the DNS accessible anywhere.
- Move your files (project folder) to AWS Ec2 using Secure Copy (scp)
- Install the necessary packages and run app.py to start the app
- Run app
Once the packages are installed, cd to the flask_classification directory and run python app.py. This should start the app and make it run from Amazon EC2 instance. Below is an intermediate example of just loading the model in the Flask App. If you want to learn a little bit more about Flask, try this out. If you just want to get to the Docker and Kubernetes goodness, skip ahead.
`OR`
Wrapping the inference logic into a `flask` application. Using `docker` to containerize the flask application. Hosting the docker container on an AWS ec2 instance and consuming the web-service.
- Run the `Docker Image` on the `EC2` instance
SSH to your EC2 instance on your machine
update your instance packages
Install Docker
After installation, pull the docker image we pushed to the repository.
sudo service docker start to docker daemon running
Then pull the image again

```python
$ docker run -it -p 5000:8080 serve-sklearn:0.1 python3 app.py
```

So `docker run` creates and starts our container and then executes the command python3 app.py which starts our Flask application. 

#### Kubernetes / Kubeflow
we used a saved version of our model to score records. We created a batch job to get predictions periodically. Now, we want to return predictions in real time. In order to do that, we will deploy our model as a REST API. 
Enterprise computing is moving to Kubernetes, and Kubeflow has long been talked about as the platform to solve MLOps at scale.

you created a deep learning model to be served as a REST API using Flask. It put the application inside a Docker container, uploaded the container to Docker Hub, and deployed it with Kubernetes. Then, with just a few commands, Kubermatic Kubernetes Platform deployed the app and exposed it to the world.

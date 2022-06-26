# MLOps
## Projects
`Udacity Machine Learning DevOps Engineer`
> https://github.com/goldin2008/mlops_clean_code

> https://github.com/goldin2008/mlops_model_workflow

> https://github.com/goldin2008/mlops_deploy_fastapi

> https://github.com/goldin2008/mlops_risk_system

`Udacity Data Engineering Nanodegree`
> https://github.com/goldin2008/nd-data-engineering

> https://github.com/goldin2008/project-ml-microservice-kubernetes


> https://github.com/danieldiamond/udacity-dend
> https://github.com/sbwhitney/data-pipelines-airflow
> https://github.com/chsanch/udacity-den-data-pipelines
> https://github.com/saurabhsoni5893/US-Immigration-Data-Lake
> https://github.com/HazalCiplak/Data-Pipelines-with-Airflow

`Udacity Data Scientist Nanodegree`
> https://github.com/goldin2008/nd-data-scientist

`Udacity Natural Language Processing Nanodegree`

`Udacity Data Streaming Nanodegree`
> https://github.com/goldin2008/nd-data-streaming

> https://github.com/goldin2008/SF_Crime_Statistics

`Cloud Developer`
> https://github.com/goldin2008/nd-cloud-developer

> https://github.com/goldin2008/cloud-c2-image-filter

> https://github.com/goldin2008/cloud-c3-microservices

> https://github.com/goldin2008/cloud-c4-serverless-todo

> https://github.com/goldin2008/cloud-capstone-final-project


> https://github.com/vicatar/Serverless-Todo
> https://github.com/trajkd/project-ml-microservice-kubernetes
> https://github.com/shalinivish001/Operationalize-a-Machine-Learning-Microservice-API-udacity

`Cloud DevOps`
> https://github.com/goldin2008/nd-cloud-devops

> https://github.com/goldin2008/project-devops-capstone

> https://github.com/goldin2008/project-c2-infrastructure-as-code

> https://github.com/goldin2008/project-c3-auto-deploy


> https://github.com/nilaychauhan/Cloud-Devops
> https://github.com/thom/aws-high-availability-web-app-cfn
> https://github.com/goldin2008/udacity_devops_project4
> https://github.com/shamimgeek/operationalize-a-machine-learning-microservice-api
> https://github.com/udacity/cdond-c3-projectstarter
> https://github.com/saadejorin/Udacity-High-Availability-WebApp-Deployment-using-cloudformation
> https://github.com/nagavenkateshgowru/udacity-clouddevops-project2
> https://github.com/simranluthra/Cloud-Devops-AutoDeploy-Project
> https://github.com/Sebastien-Hanicotte/Udacity-Cloud-DevOps-Deploy-a-high-availability-web-app-using-CloudFormation


## Online Courses
`Udacity`
> Machine Learning DevOps Engineer

> Data Engineering Nanodegree

> Data Scientist Nanodegree

> Data Streaming Nanodegree

> Natural Language Processing Nanodegree

`Coursera`
> Practical Data Science on the AWS Cloud (Amazon Web Services)

> Modern Application Development with Python on AWS (Amazon Web Services)

> DevOps on AWS (Amazon Web Services)

> Machine Learning Engineering for Production (MLOps) (DeepLearning.AI)

> Building Cloud Computing Solutions at Scale (Duke University)

## Container and Kubernetes
`What is Docker`
Docker is a container management system. Containers are objects that contain your application and it's environment, in a way that isolates it from your actual machine's operating system. Think of it as a computer-within-a-computer, but not as separated as a virtual machine. This way, you don't have to worry quite so much about getting the right environment or file system for your application to run--it will run anywhere that can host a container, which makes sharing and deploying your application a breeze.

If you've never used docker before, that's ok! We'll learn a bit today. I'd also encourage you to check out some other tutorials when you have some time, like this one or the first few sections of this one, or this mini-tutorial.

Installing docker
You will need to install some software onto your computer. This requires privileged access, so go ahead and request privileges from the Privileges App

For Mac:
Install Docker for Mac on Dockerhub or Artifactory or Install via homebrew.

```bash
brew upgrade
brew install --cask docker
```
If you haven't upgraded brew in a while, the first step may take some time.

`What is Kubernetes?`
Docker and other container technologies are currently taking the infrastructure world by storm. Ideal for microservice architectures and environments that scale rapidly or have frequent releases, [Docker has seen a rapid increase in usage](https://www.datadoghq.com/docker-adoption/#1) over the past two years. But containers introduce significant, unprecedented complexity in terms of orchestration. That’s where Kubernetes enters the scene.


> https://github.com/DataDog/the-monitor/blob/master/kubernetes/monitoring-in-the-kubernetes-era.md

## ML pipeline
> http://patrickhalina.com/posts/ml-systems-design-interview-guide/

> https://docs.google.com/document/d/1_-hKt2YmXxe3aJDb1Mk_lZpBBUq3Gk4OVIYrub_8b0Q/edit#heading=h.6ywr8ha9mniw

> https://medium.com/analytics-vidhya/fundamentals-of-mlops-part-1-a-gentle-introduction-to-mlops-1b184d2c32a8

> https://fullstackdeeplearning.com/spring2021/lab-1/

`Setup Jenkins pipeline`
> https://opensource.com/article/19/9/intro-building-cicd-pipelines-jenkins

### Model retrain and refit
> https://mlinproduction.com/model-retraining/

> https://storage.googleapis.com/pub-tools-public-publication-data/pdf/43146.pdf

> https://storage.googleapis.com/pub-tools-public-publication-data/pdf/45742.pdf

> https://machinelearningmastery.com/gentle-introduction-concept-drift-machine-learning/

> https://www.oreilly.com/radar/lessons-learned-turning-machine-learning-models-into-real-products-and-services/

> https://towardsdatascience.com/when-are-you-planning-to-retrain-your-machine-learning-model-5349eb0c4706

> https://aws.amazon.com/blogs/machine-learning/automate-model-retraining-with-amazon-sagemaker-pipelines-when-drift-is-detected/

> https://neptune.ai/blog/retraining-model-during-deployment-continuous-training-continuous-testing

> https://cloud.google.com/architecture/architecture-for-mlops-using-tfx-kubeflow-pipelines-and-cloud-build

> https://www.cienciadedatos.net/documentos/py37-forecasting-web-traffic-machine-learning.html

> https://towardsdatascience.com/how-to-answer-any-machine-learning-system-design-interview-question-a98656bb7ff0


Once the optimal model is found, it’s released out into the wild with the goal of generating accurate predictions on future unseen data. Ideally, we hope that our models predict these future instances as accurately as the data used during the training process. When we deploy models to production and expect to observe error rates like those we saw during model evaluation, we are making an assumption that future data will be similar to past observed data. Specifically, we are assuming that the distributions of the features and targets will remain fairly constant. But this assumption usually does not hold. Trends change over time, customer’s interests/behavior vary with the seasons, and frausder's behavior change. And so our models must adapt. Since we expect the world to change over time, model deployment should be treated as a continuous process. Rather than deploying a model once and moving on to another project, machine learning practitioners need to retrain their models if they find that the data distributions have deviated significantly from those of the original training set. This concept, known as model drift, can be mitigated but involves additional overhead in the forms of monitoring infrastructure, oversight, and process. In this post I’d like to define model drift and discuss strategies of identifying and tracking when a model drifts over time. I’ll then describe how to use model retraining to mitigate the effects of drift on predictive performance and suggest how frequently models should be retrained. Finally, I’ll mention a few ways to enable model retraining. At the end of this post you can download my Quickstart Guide to Model Retraining for a blueprint of how to retrain your model and set up an automated retraining pipeline on your own!

A machine learning model’s predictive performance is expected to decline as soon as the model is deployed to production. For that reason it’s imperative that practitioners prepare for degraded performance by setting up ML-specific monitoring solutions and workflows to enable model retraining. While the frequency of retraining will vary from problem-to-problem, ML engineers can start with a simple strategy that retrains models on a periodic basis as new data arrives and evolve to more complex processes that quantify and react to model drift. Now that you know why model retraining is important, you may be wondering how to setup and automate the retraining. I’ve put together a a guide showing you the exact steps you need to implement in order to automate model retraining.

`What is Model Drift?`
Model Drift refers to a model’s predictive performance degrading over time due to a change in the environment that violates the model’s assumptions. Model drift is a bit of a misnomer because it’s not the model that is changing, but rather the environment in which the model is operating. For that reason, the term concept drift may actually be a better name, but both terms describe the same phenomenon.

Notice that my definition of model drift actually includes several different variables that can change. Predictive performance will degrade, it will degrade over some period of time and at some rate, and this degradation will be due to changes in the environment that violate the modeling assumptions. Each of these variables should be taken into account when determining how to diagnose model drift and how to correct it through model retraining.

`How do you track model drift?`
`MODEL PERFORMANCE DEGREDATION`
The most direct way to identify model drift is to explicitly determine that predictive performance has deteriorated and to quantify this decline.

`EXAMINING THE FEATURE DISTRIBUTIONS OF TRAINING AND LIVE DATA`
Since model performance is expected to degrade as the distributions of the input features deviate from those of the training data, comparing these distributions is a great way to infer model drift. Notice that I said infer rather than detect model drift, since we aren’t observing an actual decline in predictive performance, but rather expecting that a decline will occur. This can be incredibly useful in cases where you can’t observe the actual ground truth due to the nature of the data generating process.

There are a number of different things to monitor per feature including:
- the range of possible values
- histograms of values
- whether the feature accepts NULLs and if so, the number of NULLs expected
- dashborad

`EXAMINING THE CORRELATIONS BETWEEN FEATURES`
Many models assume that the relationships between features must remain fixed. Therefore you’ll also want to monitor pairwise correlations between individual input features. As mentioned in What’s your ML Test Score? A rubric for ML production systems, you can do this by:
- monitoring correlation coefficients between features
- training models with one or two features
- training a set of models that each have one of the features removed

`EXAMINING THE TARGET DISTRIBUTIONS`
If the distributions of the target variables changes significantly, a model’s predictive performance will almost certainly deterioriate. The authors of Machine Learning: The High-Interest Credit Card of Technical Debt state that one simple and useful diagnostic is to track the target distribution. Deviations in this metric from the training data can mean that it’s time to reassess the quality of your deployed model. But keep in mind that "This is by no means a comprehensive test, as it can be met by a null model that simply predicts average values of label occurrences without regard to the input features.".

`What exactly do we mean by model retraining?`
At times, model retraining seems to be an overloaded operator. Does it only refer to finding new paramaters of an existing model architecture? What about changing the hyperparamater search space? What about searching over different model types (RandomForest, SVMs, etc)? Can we include new features or exclude previously used features? These are all good questions and it’s very important to be as explicit as possible. To answer these questions, it’s important to think directly about the problem we are trying to solve. That is, reducing the effect of model drift on our deployed models.

Prior to deploying a model to production data scientists go through a rigorous process of model validation which includes:

Assembling datasets – Gathering datasets from different sources such as different databases.
Feature Engineering – Deriving columns from raw data that will improve predictive performance.
Model Selection – Comparing different learning algorithms.
Error Estimation – Optimizing over a search space to find the best model and estimate its generalization error.
This process results in some best model which is then deployed to production. Since model drift refers specifically to the predictive performance of the selected model degrading due to the distributions of feature/target data changing, model retraining should not result in a different model generating process. Rather retraining simply refers to re-running the process that generated the previously selected model on a new training set of data. The features, model algorithm, and hyperparameter search space should all remain the same. One way to think about this is that retraining doesn’t involve any code changes. It only involves changing the training data set.

This is not to say that future iterations of the model shouldn’t include new features or consider additional algorithm types/architectures. I’m just saying that those types of changes result in a different type of model altogether – which you should test differently before deploying to production. Depending on the maturity of your machine learning organization, such changes would ideally be introduced with A/B tests that measure the impact of the new model on predetermined metrics of interest such as user engagement or retention.

`How can you retrain your model?`
Last but not least, let’s discuss the steps to consider for how to retrain a model successfully.

First, the approach you employ for retraining your model in machine learning is directly related to how often you decide to retrain.

Second, if you decide to retrain your model periodically, then batch retraining is perfectly sufficient. This approach involves scheduling model training processes on a recurring basis using a job scheduler such as Jenkins or Kubernetes CronJobs.

Third, if you’ve automated model drift detection, then it makes sense to trigger model retraining when drift is identified. For instance, you may have periodic jobs that compare the feature distributions of live data sets to those of the training data. When a significant deviation is identified, the system can automatically schedule model retraining to automatically deploy a new model. Again this can be performed with a job scheduler like Jenkins or by using Kubernetes Jobs.

Finally, it may make sense to utilize online learning techniques to update the model that is currently in production. This approach relies on "seeding" a new model with the model that is currently deployed. As new data arrives, the model parameters are updated with the new training data.

`How often should you retrain your model`
So far we’ve discussed what model drift is and a number of ways to identify it. So the question becomes, how do we remedy it? If a model’s predictive performance has fallen due to changes in the environment, the solution is to retrain the model on a new training set which reflects the current reality. How often should you retrain your model? And how do you determine your new training set? As with most difficult questions, the answer is that it depends. But what does it depend on?

Sometimes the problem setting itself will suggest when to retrain your model. For instance, suppose you’re working for a university admissions department and are tasked with building a student attrition model that predicts whether a student will return the following semester. This model will be used to generate predictions on the current cohort of students directly after midterms. Students identified as being at risk of churning will automatically be enrolled in tutoring or some other such intervention.

Let’s think about the time horizon of such a model. Since we’re generating predictions in batch once a semester, it doesn’t make sense to retrain the model any more often than this because we won’t have access to any new training data. Therefore we might choose to retrain our model at the start of each semester, after we’ve observed which students from the previous semester dropped out. This is an example of a periodic retraining schedule. It’s often a good idea to start with this simple strategy but you’ll need to determine exactly how frequently you’ll need to retrain. Quickly changing training sets might require you to train as often as daily or weekly. Slower varying distributions might require monthly or annual retraining.

If your team has the infrastructure in place to monitor the metrics discussed in the previous section, then it may make sense to automate the management of model drift. This solution requires tracking diagnostics and then triggering model retraining when the diagnostics on live data diverge from the training data diagnostics. But this approach is not without it’s own challenges. First, you need to determine a threshold of divergence that will trigger model retraining. If the threshold is too low you risk retraining too often which can result in high costs associated with the cost of compute. If the threshold is too high you risk not retraining often enough which leads to suboptimal models in production. This is more complicated than it seems because you are faced with determining how much new training data must be collected in order to represent the new state of the world. Even if the world has changed, there is no point in replacing the existing model with one whose training set size is too small.

Special considerations need to be taken if your model is operating in an adverserial environment. In settings such as fraud detection, the adversary changes the data distribution to profit themselves. These problems may benefit from online learning where the model is updated incrementally as new data becomes available.

`Solution`
0. Data Source (Batch/Live) and Label Source
1. What is retrain and refit?
2. Metric to decide whether to do it or not/fixed periodic interval
3. Monitor
4. Retrain or Refit (Get live data or batch data/label) Repeatability of Experiments: MLFlow, KubeFlow
5. Before and after comparison
6. Infra (Container, Kubernetes, Data ingestion, CI/CD)
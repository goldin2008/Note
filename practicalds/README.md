aws s3 cp --recursive s3://dlai-practical-data-science/labs/c2w2-824159/ ./

# Solutions on Practical Data Science Specialization

Access all courses in the Coursera [Practical Data Science Specialization](https://www.coursera.org/specializations/practical-data-science) Specialization offered by `deeplearning.ai`.


## Course keynotes and solutions of related quizzes, assignments

Practical Data Science Specialization on Coursera contains three courses:

### 1. [Course 1: Analyze Datasets and Train ML Models using AutoML](https://www.coursera.org/learn/automl-datasets-ml-models?specialization=practical-data-science)

#### Week 1:

<!-- - [x] Keynotes:

> 1. **Artificial Intelligence (AI)** mimics human behavior.

> 2. **Machine Learning (ML)** is a subset of AI that uses statistical methods and algorithms that are able to learn from data without being explicitly programmed.

> 3. **Deep learning (DL)** is a subset of machine learning that uses artificial neural networks to learn from data.

> 4. **AWS SageMaker** -->

- [x] Graded External Tool: [Register and visualize dataset](./course1/week1/C1_W1_Assignment.ipynb).

#### Week 2: 

<!-- - [x] Keynotes:

> 1. **Statistical Bias**: Training data does not comprehensively represent the underlying problem space.

> 2. **Statistical Bias Causes**: Activity Bias, Societal Bias, Selection Bias, Data Drift/Shift, ...

> 3. **Class Imbalance (CI)** measures the imbalance in the number of members between different facet values.

> 4. **Detecting Statistical Bias** by AWS SageMaker DataWrangler and AWS SageMaker Clarify.

> 5. **Feature Importance** explains the features that make up the training data using a score. How useful or valuable the feature is relative to other features?

> 5. **SHAP (SHapley Additive exPlanations)** -->

- [x] Graded External Tool: [Detect data bias with Amazon SageMaker Clarify](./course1/week2/C1_W2_Assignment.ipynb).

#### Week 3: 

<!-- - [x] Keynotes:

> 1. **Data Prepreration** includes Ingesting & Analyzing, Prepraring & Transforming, Training & Tuning, and Deploying & Managing. 

> 2. **AutoML** aims at automating the process of building a model.

> 3. **Model Hosting**. -->

- [x] Graded External Tool: [Train a model with Amazon SageMaker Autopilot](./course1/week3/C1_W3_Assignment.ipynb).

#### Week 4:

<!-- - [x] Keynotes

> 1. **Built-in Alogrithms** in AWS SageMaker supports Classification, Regression, and Clustering problems.

> 2. **Text Analysis Evolution**: Word2Vec (CBOW & Skip-gram), GloVe,  FastText, Transformer, BlazingText, ELMo, GPT, BERT, ... -->

- [x] Graded External Tool: [Train a text classifier using Amazon SageMaker BlazingText built-in algorithm](./course1/week4/C1_W4_Assignment.ipynb).

---

### 2. [Course 2: Build, Train, and Deploy ML Pipelines using BERT](https://www.coursera.org/learn/ml-pipelines-bert?specialization=practical-data-science)

#### Week 1 

<!-- - [x] Keynotes

> 1. **Feature Engineering** involves converting raw data from one or more sources into meaningful features that can be used for training machine learning models.

> 2. **Feature Engineering Step** includes feature selection, creation, and transformation.

> 3. **BERT** is Transformer-based pretrained language models that sucessfully capture bidirectional contexts in word representation.

> 4. **Feature Store**: centralized, reusable, discoverable. -->

- [x] Graded External Tool: [Feature transformation with Amazon SageMaker processing job and Feature Store](./course2/week1/C2_W1_Assignment.ipynb).

#### Week 2

<!-- - [x] Keynotes

> Learn how to train a customized **Pretrained BERT** and its variant models, debug, and profile with AWS SageMaker. -->

- [x] Graded External Tool: [Train a review classifier with BERT and Amazon SageMaker](./course2/week2/C2_W2_Assignment.ipynb).

#### Week 3
<!-- 
- [x] Keynotes

> 1. **MLOps** builds on DevOps practices that encompass people, process, and technology. MLOps also includes considerations and practices that are really unique to machine learning workloads. -->

- [x] Graded External Tool: [SageMaker pipelines to train a BERT-Based text classifier](./course2/week3/C2_W3_Assignment.ipynb).

---

### 3. [Course 3: Optimize ML Models and Deploy Human-in-the-Loop Pipelines](https://www.coursera.org/learn/ml-models-human-in-the-loop-pipelines?specialization=practical-data-science)

#### Week 1 

<!-- - [x] Keynotes

> 1. **Model Tuning** aims to fit the model to the underlying data patterns in your training data and learn the best possible parameters for your model.

> 2. **Automatic Model Tuning** includes grid search, random search, bayesian optimization, hyperband.

> 3. **Challenges**: checkpointing, distribution training strategy. -->

- [x] Graded External Tool: [Optimize models using Automatic Model Tuning](./course3/week1/C3_W1_Assignment.ipynb).


#### Week 2

<!-- - [x] Keynotes -->

- [x] Graded External Tool: [A/B testing, traffic shifting and autoscaling](./course3/week2/C3_W2_Assignment.ipynb).


#### Week 3

<!-- - [x] Keynotes -->

- [x] Graded External Tool: [Data labeling and human-in-the-loop pipelines with Amazon Augmented AI (A2I)](./course3/week3/C3_W3_Assignment.ipynb).

### Tools  
  - AWS S3 (Simple Storage Service)  
  - Amazon SageMaker:  
    - Amazon SageMaker Data Wrangler:  
      - Python library to load and unload data from data lakes and databases.
      - Dataset - Viz - Transform - Statistical Bias Report - Feature Importance  
    - Amazon SageMaker Clarify: Statistical Bias Report - Model Bias Report - Explainability - Drift. Good for dataset with millions of rows.  
    - Amazon SageMaker Autopilot: data exploration & transformation - identify ML problem - selecting ML algos - training and performing hyperparameter tuning. Containing Notebooks and source codes.  
      
   - AWS Glue: a serverless data integration service that makes registering, discovering, preparing, and combining data (fully managed ETL: extract, transform, and load service).   
  - Amazon Athena: to run SQL queries on S3 using a distributed SQL engine called Presto.  
  - Amazon SageMaker Ground Truth: Data lanbeling
- Open source  
  - Feature Importance: SHAP (SHapley Additive exPlanation) https://shap.readthedocs.io/en/latest/     
    - Shaply values based on game theory (attrubute the outcome of the game (win or loss) to individual players involved in the game.
    - Explain predictions of a ML model:  
      - Each feature value of training data instance is a player in a game  
      - ML prediction is the payout (outcome of the game)  
     - Using SHAP framework: can get local (how an individual feature contribute to final outcome) and global explanations (how data in its entirely contributes to the final outcome from ML model)  
     - SHAP can guarantee consistency and local accuracy  
     - But SHAP can be very time consuming   
 ### Built-in algos  
   - Classification: XGBoost, k-NN  
   - Regression: Linear Learner, XGBoost  
   - Time-series forcasting: DeepAR Forecasting (RNN models)  
   - Clustering:  
      - Dimensional reduction: PCA  
      - Anomaly detection: Random Cun Forest - RCF
      - Clustering / Grouping: k-means  
      - Topic modeling: Latent Dirichlet Allocation (LDA), Neural Topic Model (NTM)  
   - Image processing  
      - Image classification: CNN
      - Object detection:   
      - Computer vision: Semantic Segmentation  
   - Text analysis:  
      - Machine translation: Sequence to Sequence  
      - Text summarization: Sequence to Sequence   
      - Speech to text: Sequence to Sequence   
      - Text classification: Blazing Text       
  

---
	
## Disclaimer

The solutions here are **ONLY FOR REFERENCE** to guide you if you get stuck somewhere. Highly recommended to try out the quizzes and assignments yourselves first before referring to the solutions here.
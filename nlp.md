## Natural Language Processing
#### NLP Pipeline #### 
This step-by-step processing of text is known as a pipeline. Note that, in the real world, the process may not always be linear as it’s shown in the pipeline in Figure 2-1; it often involves going back and forth between individual steps (e.g., between feature extraction and modeling, modeling and evaluation, and so on). Also, there are loops in between, most commonly going from evaluation to pre-processing, feature engineering, modeling, and back to evaluation. There is also an overall loop that goes from monitoring to data acquisition, but this loop happens at the project level.

***Data acquisition***

Text cleaning

Pre-processing

Feature engineering

Modeling

Evaluation

Deployment

Monitoring and model updating
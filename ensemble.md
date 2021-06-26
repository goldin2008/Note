## Ensemble

Ensemble methods involve combining the predictions from multiple models. A key part of an ensemble learning method involves combining the predictions from multiple models. It is through the combination of the predictions that the benefit of the ensemble learning method is achieved, namely better predictive performance. As such, there are many ways that predictions can be combined, so much so that it is an entire field of study.

In stacking, an algorithm takes the outputs of sub-models as input and attempts to learn how to best combine the input predictions to make a better output prediction.

Unlike a weighted average ensemble, a stacked generalization ensemble can use the set of predictions as a context and conditionally decide to weigh the input predictions differently, potentially resulting in better performance.

It is important that the meta-learner is trained on a separate dataset to the examples used to train the level 0 models to avoid overfitting. A simple way that this can be achieved is by splitting the training dataset into a train and validation set. The level 0 models are then trained on the train set. The level 1 model is then trained using the validation set, where the raw inputs are first fed through the level 0 models to get predictions that are used as inputs to the level 1 model.

The predictions are then used as inputs to train the meta-learner. Level 0 models are then trained on the entire training dataset and together with the meta-learner, the stacked model can be used to make predictions on new data. In practice, it is common to use different algorithms to prepare each of the level 0 models, to provide a diverse set of predictions. A stacked generalization ensemble can be developed for regression and classification problems. In the case of classification problems, better results have been seen when using the prediction of class probabilities as input to the meta-learner instead of class labels.

This is desirable as it means that the problem is non-trivial and will allow a neural network model to find many different “good enough” candidate solutions, resulting in a high variance.

The problem is a binary-class classification problem, and we will model it using a softmax activation function on the output layer. This means that the model will predict a vector with two elements with the probability that the sample belongs to each of the two classes. Therefore, we must one hot encode the class values before we split the rows into the train and test datasets. We can do this using the Keras to_categorical() function. The model will expect samples with two input variables. The model then has a single hidden layer with 25 nodes and a rectified linear activation function, then an output layer with three nodes to predict the probability of each of the three classes and a softmax activation function. Because the problem is multi-class, we will use the categorical cross entropy loss function to optimize the model and the efficient Adam flavor of stochastic gradient descent.

The model is fit for 500 training epochs and we will evaluate the model each epoch on the test set, using the test set as a validation set. At the end of the run, we will evaluate the performance of the model on the train and test sets. Then finally, we will plot learning curves of the model accuracy over each training epoch on both the training and validation datasets. A line plot is also created showing the learning curves for the model accuracy on the train and test sets over each training epoch.

we will train multiple sub-models and save them to file for later use in our stacking ensembles. Finally, we can create multiple instances of the MLP and save each to the “models/” subdirectory with a unique filename. In this case, we will create five sub-models, but you can experiment with a different number of models and see how it impacts model performance. We can tie all of these elements together; the complete example of training the sub-models and saving them to file is listed below. Running the example creates the “models/” subfolder and saves five trained models with unique filenames. Next, we can look at training a meta-learner to make best use of the predictions from these submodels.

We can now train a meta-learner that will best combine the predictions from the sub-models and ideally perform better than any single sub-model. It would be useful to know how well the single models perform on the test dataset as we would expect a stacking model to perform better. We can easily evaluate each single model on the training dataset and establish a baseline of performance.

The meta-model is trained on the predictions made by base models on out-of-sample data. That is, data not used to train the base models is fed to the base models, predictions are made, and these predictions, along with the expected outputs, provide the input and output pairs of the training dataset used to fit the meta-model. The most common approach to preparing the training dataset for the meta-model is via k-fold cross-validation of the base models, where the out-of-fold predictions are used as the basis for the training dataset for the meta-model. The training data for the meta-model may also include the inputs to the base models, e.g. input elements of the training data. This can provide an additional context to the meta-model as to how to best combine the predictions from the meta-model. Once the training dataset is prepared for the meta-model, the meta-model can be trained in isolation on this dataset, and the base-models can be trained on the entire original training dataset.

Stacking is appropriate when multiple different machine learning models have skill on a dataset, but have skill in different ways. Another way to say this is that the predictions made by the models or the errors in predictions made by the models are uncorrelated or have a low correlation. Base-models are often complex and diverse. As such, it is often a good idea to use a range of models that make very different assumptions about how to solve the predictive modeling task, such as linear models, decision trees, support vector machines, neural networks, and more. Other ensemble algorithms may also be used as base-models, such as random forests. Base-Models: Use a diverse range of models that make different assumptions about the prediction task. The meta-model is often simple, providing a smooth interpretation of the predictions made by the base models. As such, linear models are often used as the meta-model, such as linear regression for regression tasks (predicting a numeric value) and logistic regression for classification tasks (predicting a class label). Although this is common, it is not required.

Stacking is designed to improve modeling performance, although is not guaranteed to result in an improvement in all cases. Achieving an improvement in performance depends on the complexity of the problem and whether it is sufficiently well represented by the training data and complex enough that there is more to learn by combining predictions. It is also dependent upon the choice of base models and whether they are sufficiently skillful and sufficiently uncorrelated in their predictions (or errors). If a base-model performs as well as or better than the stacking ensemble, the base model should be used instead, given its lower complexity (e.g. it’s simpler to describe, train and maintain).

### TF-IDF LOGIT ###





### 1D CNN ###





### LSTM ###





### References

https://machinelearningmastery.com/ensemble-machine-learning-algorithms-python-scikit-learn/

https://machinelearningmastery.com/combine-predictions-for-ensemble-learning/

https://machinelearningmastery.com/stacking-ensemble-machine-learning-with-python/

https://machinelearningmastery.com/blending-ensemble-machine-learning-with-python/

https://machinelearningmastery.com/stacking-ensemble-for-deep-learning-neural-networks/

https://machinelearningmastery.com/k-fold-cross-validation/


> TODO

https://machinelearningmastery.com/convolutional-layers-for-deep-learning-neural-networks/

https://machinelearningmastery.com/develop-word-embedding-model-predicting-movie-review-sentiment/

https://machinelearningmastery.com/sequence-classification-lstm-recurrent-neural-networks-python-keras/

https://machinelearningmastery.com/develop-n-gram-multichannel-convolutional-neural-network-sentiment-analysis/

https://machinelearningmastery.com/predict-sentiment-movie-reviews-using-deep-learning/
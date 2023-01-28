## ML DL interview questions and answers
> https://www.interviewbit.com/deep-learning-interview-questions/

> https://www.nicksingh.com/posts/30-machine-learning-interview-questions-ml-interview-study-guide

> https://github.com/khangich/machine-learning-interview

> https://towardsdatascience.com/how-to-answer-any-machine-learning-system-design-interview-question-a98656bb7ff0

1. `What are activation functions?`
- Activation Functions help in keeping the value of the output from the neuron restricted to a certain limit as per the requirement. If the limit is not set then the output will reach very high magnitudes. Most activation functions convert the output to -1 to 1 or to 0 to 1.
- The most important role of the activation function is the ability to add non-linearity to the neural network. Most of the models in real-life is non-linear so the activation functions help to create a non-linear model.
- The activation function is responsible for deciding whether a neuron should be activated or not.
Activation functions are entities in Deep Learning that are used to translate inputs into a usable output parameter. It is a function that decides if a neuron needs activation or not by calculating the weighted sum on it with the bias. Using an activation function makes the model output to be non-linear. There are many types of activation functions:
ReLU
Softmax
Sigmoid
Linear
Tanh

2. `What Are the Softmax and ReLU Functions?`
Softmax is an activation function that generates the output between zero and one. It divides each output, such that the total sum of the outputs is equal to one. Softmax is often used for output layers.
ReLU (or Rectified Linear Unit) is the most widely used activation function. It gives an output of X if X is positive and zeros otherwise. ReLU is often used for hidden layers.

3. `How would you choose the Activation Function for a Deep Learning model?`
- If the output to be predicted is real, then it makes sense to use a Linear Activation function.
- If the output to be predicted is a probability of a binary class, then a Sigmoid function should be used.
- If the output to be predicted has two classes, then a Tanh function can be used.
- ReLU function can be used in many different cases due to its computational simplicity.

4. `What Is the Cost Function?`
Also referred to as “loss” or “error,” cost function is a measure to evaluate how good your model’s performance is. It’s used to compute the error of the output layer during backpropagation. We push that error backward through the neural network and use that during the different training functions.
- Neural network requires a loss function to be chosen when designing and configuring the model.
- While optimizing the model, an objective function is either a loss function or its negative. The objective function is sought to be maximized or minimized (output which has the highest or lowest score respectively). Typically, in a neural network the error should be minimized.
- The loss function should reduce all the aspects of a complex model down to a single scalar value, which allows the candidate solutions to be ranked and compared.
- The loss function chosen by the designer should capture the properties of the problem and be motivated by concerns that are important to the project.

5. `What is the use of the loss function?`
The loss function is used as a measure of accuracy to see if a neural network has learned accurately from the training data or not. This is done by comparing the training dataset to the testing dataset. The loss function is a primary measure of the performance of the neural network. In Deep Learning, a good performing network will have a low loss function at all times when training.

6. `What are the steps to be followed to use the gradient descent algorithm?`
There are five main steps that are used to initialize and use the gradient descent algorithm:
Initialize biases and weights for the network
Send input data through the network (the input layer)
Calculate the difference (the error) between expected and predicted values
Change values in neurons to minimize the loss function
Multiple iterations to determine the best weights for efficient working

7. `What is forward propagation?`
Forward propagation is the scenario where inputs are passed to the hidden layer with weights. In every single hidden layer, the output of the activation function is calculated until the next layer can be processed. It is called forward propagation as the process begins from the input layer and moves toward the final output layer.

8. ??? `What is backpropagation?`
Backpropagation is used to minimize the cost function by first seeing how the value changes when weights and biases are tweaked in the neural network. This change is easily calculated by understanding the gradient at every hidden layer. It is called backpropagation as the process begins from the output layer, moving backward to the input layers.
This is one of the most frequently asked deep learning interview questions. Backpropagation is a technique to improve the performance of the network. It backpropagates the error and updates the weights to reduce the error.

9. `What are hyperparameters in Deep Learning?`
Hyperparameters are variables used to determine the structure of a neural network. They are also used to understand parameters, such as the learning rate and the number of hidden layers, and more, present in the neural network.

10. ??? `How can hyperparameters be trained in neural networks?`
Hyperparameters can be trained using four components as shown below:
Batch size: This is used to denote the size of the input chunk. Batch sizes can be varied and cut into sub-batches based on the requirement.
Epochs: An epoch denotes the number of times the training data is visible to the neural network so that it can train. Since the process is iterative, the number of epochs will vary based on the data.
Momentum: Momentum is used to understand the next consecutive steps that occur with the current data being executed at hand. It is used to avoid oscillations when training.
Learning rate: Learning rate is used as a parameter to denote the time required for the network to update the parameters and learn.

11. `What is the meaning of dropout in Deep Learning?`
Dropout is a technique that is used to avoid overfitting a model in Deep Learning. If the dropout value is too low, then it will have minimal effect on learning. If it is too high, then the model can under-learn, thereby, causing lower efficiency.

12. ??? `What Is Dropout and Batch Normalization?`
Dropout is a technique of dropping out hidden and visible units of a network randomly to prevent overfitting of data (typically dropping 20 percent of the nodes). It doubles the number of iterations needed to converge the network.
Batch normalization is the technique to improve the performance and stability of neural networks by normalizing the inputs in every layer so that they have mean output activation of zero and standard deviation of one.

13. `How to choose the features for a Neural Network?`
A very strong correlation between the new feature and an existing feature is a fairly good sign that the new feature provides little new information.
A low correlation between the new feature and existing features is likely preferable.
A strong linear correlation between the new feature and the predicted variable is a good sign that a new feature will be valuable, but the absence of a high correlation is not necessarily a sign of a poor feature, because neural networks are not restricted to linear combinations of variables.
If the new feature was manually constructed from a combination of existing features, consider leaving it out. The beauty of neural networks is that little feature engineering and preprocessing are required - features are instead learned by intermediate layers.
Whenever possible, prefer learning features to engineering them.

14. ??? `What is a CNN?`
CNNs are convolutional neural networks that are used to perform analysis on images and visuals. These classes of neural networks can input a multi-channel image and work on it easily. These Deep Learning questions must be answered in a concise way. So make sure to understand them and revisit them if necessary.

15. `What are the various layers present in a CNN?`
There are four main layers that form a convolutional neural network:
Convolution: These are layers consisting of entities called filters that are used as parameters to train the network.
ReLu: It is used as the activation function and is always used with the convolution layer.
Pooling: Pooling is the concept of shrinking the complex data entities that form after convolution and is primarily used to maintain the size of an image after shrinkage.
Connectedness: This is used to ensure that all of the layers in the neural network are fully connected and activation can be computed using the bias easily.

16. `What Are the Different Layers on CNN?`
There are four layers in CNN:
Convolutional Layer -  the layer that performs a convolutional operation, creating several smaller picture windows to go over the data.
ReLU Layer - it brings non-linearity to the network and converts all the negative pixels to zero. The output is a rectified feature map.
Pooling Layer - pooling is a down-sampling operation that reduces the dimensionality of the feature map.
Fully Connected Layer - this layer recognizes and classifies the objects in the image.

17. `What is Pooling on CNN, and How Does It Work?`
Pooling is used to reduce the spatial dimensions of a CNN. It performs down-sampling operations to reduce the dimensionality and creates a pooled feature map by sliding a filter matrix over the input matrix.

18. ??? `Why is a convolutional neural network preferred over a dense neural network for an image classification task?`
The number of parameters in a convolutional neural network is much more diminutive than that of a Dense Neural Network. Hence, a CNN is less likely to overfit.
CNN allows you to look at the weights of a filter and visualize what the network learned. So, this gives a better understanding of the model.
CNN trains models in a hierarchical way, i.e., it learns the patterns by explaining complex patterns using simpler ones.

19. ??? `How can you convert a Dense Layer of a CNN into a Fully Convolutional Layer?`
If you have a CNN with some dense layers on top, you can convert these dense layers to convolutional layers to create an FCN in the following way:
- Replace the lowest dense layer with a convolutional layer with a kernel size equal to the layer's input size, with one filter per neuron in the dense layer, and use valid padding.
- Generally, the stride should be 1, but you can set it to a higher value if you want.
- The activation function should be the same as the dense layer's.
- The other dense layers should be converted the same way, but using 1 × 1 filters.
- It is actually possible to convert a trained CNN this way by appropriately reshaping the dense layers' weight matrices.

20. `What Is the Difference Between a Feedforward Neural Network and Recurrent Neural Network?`
In this deep learning interview question, the interviewee expects you to give a detailed answer.
A Feedforward Neural Network signals travel in one direction from input to output. There are no feedback loops; the network considers only the current input. It cannot memorize previous inputs (e.g., CNN).
A Recurrent Neural Network’s signals travel in both directions, creating a looped network. It considers the current input with the previously received inputs for generating the output of a layer and can memorize past data due to its internal memory.

21. `What is an RNN in Deep Learning?`
RNNs stand for recurrent neural networks, which form to be a popular type of artificial neural network. They are used to process sequences of data, text, genomes, handwriting, and more. RNNs make use of backpropagation for the training requirements.

22. `What's the difference between Convolutional Neural Networks (CNN) and Recurrent Neural Networks (RNN) and in which cases would use each one?`
Convolutional neural nets apply a convolution to the data before using it in fully connected layers.
They are best used in cases where you want positional invariance, that is to say, you want features to be captured regardless of where they are in the input sample.
Think of a picture with all sorts of animals in it. If you apply a convolutional neural net to classify whether there is a cat in the picture, it will identify the cat no matter what position in the picture the cat is (at the top, the bottom, left or right). This is very useful for image classification.
Recurrent neural nets are neural networks that keep state between input samples. They remember previous input samples and use those to help classify the current input sample.
They are most useful when the order of your data is important. So for instance in speech (previous words do help identify the current word), video (frames are ordered) and also text processing.
Generally speaking, problems related to time-series data (data with a timestamp on them) are good candidates to be solved well with recurrent neural nets.

23. ??? `How Does an LSTM Network Work?`
Long-Short-Term Memory (LSTM) is a special kind of recurrent neural network capable of learning long-term dependencies, remembering information for long periods as its default behavior. There are three steps in an LSTM network:
Step 1: The network decides what to forget and what to remember.
Step 2: It selectively updates cell state values.
Step 3: The network decides what part of the current state makes it to the output.

24. `What Are Vanishing and Exploding Gradients?`
While training an RNN, your slope can become either too small or too large; this makes the training difficult. When the slope is too small, the problem is known as a “Vanishing Gradient.” When the slope tends to grow exponentially instead of decaying, it’s referred to as an “Exploding Gradient.” Gradient problems lead to long training times, poor performance, and low accuracy.

The vanishing gradient problem is encountered in artificial neural networks with gradient-based learning methods and backpropagation. In these learning methods, each of the neural networks weights receives an update proportional to the partial derivative of the error function with respect to the current weight in each iteration of training. Sometimes when gradients become vanishingly small, this prevents the weight to change value.
If the neural network has many hidden layers, the gradients in the earlier layers will become very low as we multiply the derivatives of each layer. As a result, learning in the earlier layers becomes very slow. This can cause the neural network to stop learning.
This problem of vanishing gradient descent happens when training neural networks with many layers because the gradient diminishes dramatically as it propagates backwards through the network.
Many fixes and workarounds have been proposed and investigated to fix the vanishing gradient problem, such as
alternate weight initialization schemes,
unsupervised pre-training,
layer-wise training, and
variations on gradient descent.
Perhaps the most common change is the use of the rectified linear activation function that has become the new default, instead of the hyperbolic tangent activation function that was the default through the late 1990s and 2000s.


25. `What is a vanishing gradient when using RNNs?`
Vanishing gradient is a scenario that occurs when we use RNNs. Since RNNs make use of backpropagation, gradients at every step of the way will tend to get smaller as the network traverses through backward iterations. This equates to the model learning very slowly, thereby, causing efficiency problems in the network.

26. `How to know whether your model is suffering from the problem of Vanishing Gradients?`
- The model will improve very slowly during the training phase and it is also possible that training stops very early, meaning that any further training does not improve the model.
- The weights closer to the output layer of the model would witness more of a change whereas the layers that occur closer to the input layer would not change much (if at all).
- Model weights shrink exponentially and become very small when training the model.
- The model weights become 0 in the training phase.

27. `What is exploding gradient descent in Deep Learning?`
Exploding gradients are an issue causing a scenario that clumps up the gradients. This creates a large number of updates of the weights in the model when training.
The working of gradient descent is based on the condition that the updates are small and controlled. Controlling the updates will directly affect the efficiency of the model.
Exploding gradient problem is a problem in a neural network where a large error gradient accumulates which results in very large updates to the neural network model weights during training.
This causes the neural network to stop learning.
In deep multilayer perceptron networks, this problem creates an unstable network that can not learn from the training data, or at its worst, it creates a NaN weight value that can not be updated.
In recurrent neural networks, this problem causes the network to be unable to learn from long input sequences of data.

28. `How to know whether your model is suffering from the problem of Exploding Gradients?`
There are some subtle signs that you may be suffering from exploding gradients during the training of your network, such as:
- The model is unable to get traction on your training data (e g. poor loss).
- The model is unstable, resulting in large changes in loss from update to update.
- The model loss goes to NaN during training.
If you have these types of problems, you can dig deeper to see if you have a problem with exploding gradients. There are some less subtle signs that you can use to confirm that you have exploding gradients:
- The model weights quickly become very large during training.
- The model weights go to NaN values during training.
- The error gradient values are consistently above 1.0 for each node and layer during training.

29. `What is the use of LSTM?`
LSTM stands for long short-term memory. It is a type of RNN that is used to sequence a string of data. It consists of feedback chains that give it the ability to perform like a general-purpose computational entity.

30. `What Is Gradient Descent?`
Gradient Descent is an optimal algorithm to minimize the cost function or to minimize an error. The aim is to find the local-global minima of a function. This determines the direction the model should take to reduce the error.

31. `What are the variants of gradient descent?`
There are three variants of gradient descent as shown below:
Stochastic gradient descent: A single training example is used for the calculation of gradient and for updating parameters.
Batch gradient descent: Gradient is calculated for the entire dataset, and parameters are updated at every iteration.
Mini-batch gradient descent: Samples are broken down into smaller-sized batches and then worked on as in the case of stochastic gradient descent.

32. `What Is the Difference Between Batch Gradient Descent and Stochastic Gradient Descent?`
Batch Gradient Descent
The batch gradient computes the gradient using the entire dataset.
It takes time to converge because the volume of data is huge, and weights update slowly.

Stochastic Gradient Descent
The stochastic gradient computes the gradient using a single sample.
It converges much faster than the batch gradient because it updates weight more frequently.

33. ??? `Why is mini-batch gradient descent so popular?`
Mini-batch gradient descent is popular as:
It is more efficient when compared to stochastic gradient descent.
Generalization is done by finding the flat minima.
It helps avoid the local minima by allowing the approximation of the gradient for the entire dataset.
Mini-batch gradient is highly efficient compared to stochastic gradient descent.
It lets you attain generalization by finding the flat minima.
Mini-batch gradient helps avoid local minima to allow gradient approximation for the whole dataset.

34. `Can we initialize the weights of a network to start from zero?`
Yes, it is possible to begin with zero initialization. However, it is not recommended to use because setting up the weights to zero initially will cause all of the neurons to produce the same output and the same gradients when performing backpropagation. This means that the network will not have the ability to learn at all due to the `absence of asymmetry between each of the neurons`.
There are two methods here: we can either initialize the weights to zero or assign them randomly.
Initializing all weights to 0: This makes your model similar to a linear model. All the neurons and every layer perform the same operation, giving the same output and making the deep net useless.
Initializing all weights randomly: Here, the weights are assigned randomly by initializing them very close to 0. It gives better accuracy to the model since every neuron performs different computations. This is the most commonly used method.

35. `Explain why the Initialization process of weights and bias is important for NN?`
The initialization step can be critical to the model's performance, and it requires the right method.
Initializing the weights to zero leads the network to learn zero output which makes the network not learn anything.
Initializing the weights to be too large causes the network to experience exploding gradients.
Initializing the weights to be too small causes the network to experience vanishing gradients.
To find the perfect initialization, there are a few rules of thumb to follow:
The mean of activations should be zero.
The variance of activations should stay the same across every layer.

36. `Explain the Adam optimization algorithm.`
Adaptive Moment Estimation or Adam optimization is an extension to the stochastic gradient descent. This algorithm is useful when working with complex problems involving vast amounts of data or parameters. It needs less memory and is efficient. 
Adam optimization algorithm is a combination of two gradient descent methodologies - Momentum and Root Mean Square Propagation.

37. `Which strategy does not prevent a model from over-fitting to the training data?`
Dropout
Pooling
Data augmentation
Early stopping
Answer: b) Pooling - It’s a layer in CNN that performs a downsampling operation.

38. ??? `Explain two ways to deal with the vanishing gradient problem in a deep neural network.`
Use the ReLU activation function instead of the sigmoid function
Initialize neural networks using Xavier initialization that works with tanh activation.

39. `Why is a deep neural network better than a shallow neural network?`
Both deep and shallow neural networks can approximate the values of a function. But the deep neural network is more efficient as it learns something new in every layer. A shallow neural network has only one hidden layer. But a deep neural network has several hidden layers that create a deeper representation and computation capability.

40. ??? `What are Generative Adversarial Networks?`
A Generative Adversarial Network (GAN) is a type of neural network architecture for generative modeling.
GAN has the capability to generate examples for image datasets, photographs, characters, etc.
Generative adversarial networks are a model of data generation that can create a generative model of a base data set by using an adversarial game between two players. The two players correspond to a generator and a discriminator.
The generator takes Gaussian noise as input and produces an output, which is a generated sample like the base data.
The discriminator is a probabilistic classifier like logistic regression whose job is to distinguish real samples from the base dataset and the generated sample.
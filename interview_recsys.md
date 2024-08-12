## RecSys powered by LLMs interview prep

### a movie recommender application powered by LLMs
In this chapter, we explored how LLMs could change the way we approach a recommendation system task. We started from the analysis of the current strategies and algorithms for building recommendation applications, differentiating between various scenarios (collaborative filtering, content-based, cold start, etc.) as well as different techniques (KNN, matrix factorization, and NNs).

We then moved to the new, emerging field of research into how to apply the power of LLMs to this field, and explored the various experiments that have been done in recent months.

Leveraging this knowledge, we built a movie recommender application powered by LLMs, using LangChain as the AI orchestrator and Streamlit as the front-end, showing how LLMs can revolutionize this field thanks to their reasoning capabilities as well as their generalization. This was just one example of how LLMs not only can open new frontiers, but can also enhance existing fields of research.

A recommendation system is a computer program that recommends items for users of digital platforms such as e-commerce websites and social networks. It uses large datasets to develop models of users’ likes and interests, and then recommends similar items to individual users.

There are different types of recommendation systems, depending on the methods and data they use. Some of the common types are:
- Collaborative filtering: This type of recommendation system uses the ratings or feedback of other users who have similar preferences to the target user. It assumes that users who liked certain items in the past will like similar items in the future. For example, if user A and user B both liked movies X and Y, then the algorithm may recommend movie Z to user A if user B also liked it.
Collaborative filtering can be further divided into two subtypes: user-based and item-based:
  - User-based collaborative filtering finds similar users to the target user and recommends items that they liked.
  - Item-based collaborative filtering finds similar items to the ones that the target user liked and recommends them.
- Content-based filtering: This type of recommendation system uses the features or attributes of the items themselves to recommend items that are similar to the ones that the target user has liked or interacted with before. It assumes that users who liked certain features of an item will like other items with similar features. The main difference with item-based collaborative filtering is that, while this latter item-based uses patterns of user behavior to make recommendations, content-based filtering uses information about the items themselves. For example, if user A liked movie X, which is a comedy with actor Y, then the algorithm may recommend movie Z, which is also a comedy with actor Y.
- Hybrid filtering: This type of recommendation system combines both collaborative and content-based filtering methods to overcome some of their limitations and provide more accurate and diverse recommendations. For example, YouTube uses hybrid filtering to recommend videos based on both the ratings and views of other users who have watched similar videos, and the features and categories of the videos themselves.
- Knowledge-based filtering: This type of recommendation system uses explicit knowledge or rules about the domain and the user’s needs or preferences to recommend items that satisfy certain criteria or constraints. It does not rely on ratings or feedback from other users, but rather on the user’s input or query. For example, if user A wants to buy a laptop with certain specifications and budget, then the algorithm may recommend a laptop that satisfies those criteria. Knowledge-based recommender systems work well when there is no or little rating history available, or when the items are complex and customizable.

`K-nearest neighbors`
K-nearest neighbors (KNN) is an ML algorithm that can be used for both classification and regression problems. It works by finding the k closest data points (where k refers to the number of nearest data point you want to find, and is set by the user before initializing the algorithm) to a new data point and using their labels or values to make a prediction. KNN is based on the assumption that similar data points are likely to have similar labels or values.

Generally speaking, KNN is recommended in scenarios with small datasets with minimal noise (so that outliers, missing values and other noises do not impact the distance metric) and dynamic data (KNN is an instance-based method that doesn’t require retraining and can adapt to changes quickly).

`Matrix factorization`
Matrix factorization is a technique used in recommendation systems to analyze and predict user preferences or behaviors based on historical data. It involves decomposing a large matrix into two or more smaller matrices to uncover latent features that contribute to the observed data patterns and address the so-called “curse of dimensionality.”

Matrix factorization aims to break down this matrix into two matrices: one for users and another for movies, with a reduced number of dimensions (latent factors). These latent factors could represent attributes like genre preferences or specific movie characteristics. By multiplying these matrices, you can predict the missing ratings and recommend movies that the users might enjoy.

There are different algorithms for matrix factorization, including the following:
- `Singular value decomposition (SVD)` decomposes a matrix into three separate matrices, where the middle matrix contains singular values that represent the importance of different components in the data. It’s widely used in data compression, dimensionality reduction, and collaborative filtering in recommendation systems.
- Principal component analysis (PCA) is a technique to reduce the dimensionality of data by transforming it into a new coordinate system aligned with the principal components. These components capture the most significant variability in the data, allowing efficient analysis and visualization.
- Non-negative matrix factorization (NMF) decomposes a matrix into two matrices with non-negative values. It’s often used for topic modeling, image processing, and feature extraction, where the components represent non-negative attributes.

`Neural networks`
NNs are used in recommendation systems to improve the accuracy and personalization of recommendations by learning intricate patterns from data. Here’s how neural networks are commonly applied in this context:
- Collaborative filtering with neural networks: Neural networks can model user-item interactions by embedding users and items into continuous vector spaces. These embeddings capture latent features that represent user preferences and item characteristics. Neural collaborative filtering models combine these embeddings with neural network architectures to predict ratings or interactions between users and items.
- Content-based recommendations: In content-based recommendation systems, neural networks can learn representations of item content, such as text, images, or audio. These representations capture item characteristics and user preferences. Neural networks like convolutional neural networks (CNNs) and recurrent neural networks (RNNs) are used to process and learn from item content, enabling personalized content-based recommendations.
- Sequential models: In scenarios where user interactions have a temporal sequence, such as clickstreams or browsing history, RNNs or variants such as long short-term memory (LSTM) networks can capture temporal dependencies in the user behavior and make sequential recommendations.
- Autoencoders and variational autoencoders (VAEs) can be used to learn low-dimensional representations of users and items.



## References

RAG:
>

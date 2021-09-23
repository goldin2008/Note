## MLE interview
### Amazon
#### 1st Interview

1. Talk about linear regression, why it is called linear?
2. Talk about logistic regression, is it linear? 
3. If we can use one non-linear neuron to train a model, why do we need a lot of layers in our model
4. How do we detect if model is overfitting?
5. Talk about one project that you did, what was the objective function, limitations, future scope
6. Decision trees → do they capture non-linearity? 
7. Can you use decision tree to make a non-linear boundaries like a quadratic one
8. Explain k-nearest neighbour algo
9. Gates can be implemented in 1 or 2 hidden layers, don't need more layers
    - concept of making gates using neural network

#### 2nd Interview

1. Travelling Salesman Project
    1. Open MP how did you parallelise the algorithm exactly?
    2. why cant you parallelise stuff in python?
    3. Some synchronisation stuff 
2. Community Detection Algorithms
    1. what is modularity expression?
    2. What is condition for convergence of modularity based algorithm?
3. Page Rank Project
    1. What is the condition for convergence of page rank?
    2. ergodicity of a matrix
    3. laplacian of a graph
4. Satellite Image
    1. Attention in Images in a CNN
    2. how is attention added in a CNN?
    3. 16 images of a town for the same class, how will you use so many images
        1. wanted to use attention
        2. other methods → random cropping, reshaping, different images in different epochs
    4. Image as word vector can be fed row wise with ordering information
    5. CNN vs Bert of 16 images → what is the difference?
    6. Sequence to Sequence model in Vision Scenario


ML相关问题：Recall/precision tradeoff， SVM VS LR， support vector如何产生的，Kmeans 是什么和什么的tradeoff（问题问的非常无语，答案是k和purity的tradeoff，面试官期望你说出purity这个单词），通过KNN考察bias/variance tradeoff， 以及工作中有没有遇到过模型选择的问题（比如有哪些system constraint，为什么选该模型）

ML depth：主要是presentation，需要做ppt，顺带问了GBDT和XGboost的异同（推荐看一下XGBoost的论文），以及lightGBM和XGboost的异同

Coding：手写一个KNN。找出最受欢迎的topk个商品 （两道题思路是一摸一样的，都是用heap）

### Microsoft

MS 电面，一个西雅图小哥，没有coding，纯ml探讨，要推写公式。
闲聊了聊自己的项目，推了一遍arcface 的loss，楼主英语表达一般，纯靠公式和画图给面试官讲明白了
聊了聊各个loss function，relu 0处求导怎么办等等
batch norm 作用，公式，batch size 不同时mean值不同怎么处理
l1和l2，公式，作用，特性，推导
最后了简单‍聊了下attention

train的时候把mean保存下来，inference的时候用保存的值
0处出现的情况极小，可以忽略不计，一旦出现直接取0

## MLE interview
https://madewithml.com/

到时候把Grokking the Coding Interview: Patterns for Coding Questions也学一下。感觉这两门课，对Machine learning engineer的面试可能就够了（当然，还有机器学习专业方面的你还需要去好好准备） 

> https://www.1point3acres.com/bbs/thread-652770-1-1.html

* Grokking the Coding Interview: Patterns for Coding Questions
* Grokking-the-system-design-interview
* Designing Data-intensive Applications
* 【Grokking Dynamic Programming Patterns for Coding Interviews】
* 【Data Structures for Coding Interviews in Java】
* 【Grokking the Object Oriented Design Interview】

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

第一题，modeling，design buy it again model
https://assets.amazon.science/40/e5/89556a6341eaa3d7dacc074ff24d/buy-it-again-modeling-repeat-purchase-recommendations.pdf?tag=1p3a-api-20

### Microsoft

MS 电面，一个西雅图小哥，没有coding，纯ml探讨，要推写公式。
闲聊了聊自己的项目，推了一遍arcface 的loss，楼主英语表达一般，纯靠公式和画图给面试官讲明白了
聊了聊各个loss function，relu 0处求导怎么办等等
batch norm 作用，公式，batch size 不同时mean值不同怎么处理
l1和l2，公式，作用，特性，推导
最后了简单‍聊了下attention

train的时候把mean保存下来，inference的时候用保存的值. 0处出现的情况极小，可以忽略不计，一旦出现直接取0

### Facebook

细桶射击是个印度大姐，题目就是给一堆机子去爬一个网站，我把sql，nosql，redis，filesystem还有log-message queue这些都说了一大通，还有如何parition和sharding巴拉巴拉，基本都是我在说，我中途问了一下有什么问题对方说没事我知道你说的，然后中间提了一些问题关于data model，我大概说了下怎么做index，我看她也没什么反应。然后又问了一些具体大概爬虫算法是个什么逻辑，还画了个testcase的 bfs 例子。。。最后问还有什么补充的，然后又加了个监控，check point 调度系统，因为机子可能不稳定会挂之类的。。。然后又问bottleneck 答完后就没了。。。也不知道怎么样

ML system design面的是设计search engine相关的， system design面的设计fee

### Linkedin

接下来问probability，用什么样的distribution来model这些event最好：扔硬币，掷骰子，接线员下午4-5点接到了10个电话，5-6点会接到几个电话，股票走势等等，可能问了十来个。这里因为不知道要考probability，所以也没有复习到，可能有些没有答对。

再来就是挑一个算法，从头到尾讲。我讲了logistic regression，包括loss function，optimization，regularization。follow-up了两个问题，一是如果MLE换成MAP，求的是什么。二是，为什么logistic regression对于correlated features表现不好。我‍觉得我第二个follow up没答好，也请教各位会如何回答这个问题。

### Others

5) ML Sys Design
Build and serve a DL model with given feature engineering logics
a) how to distributed training
b) online batch inferencingn
c) online real-time inferencing, includes data flow design
d) completeness of all pipelines and how to guarantee consistency of batching inferencing and real-time inferencing.

第一个面官问了linear regression的各种，还有各种Optimizer。哎，各种oprimizer的区别，我真的只有考试前背过一下，后来就再也没看过。由于签了NDA, 不详细展开了，大家可以参考往这方面复习。
第二轮跟面官一起解决一个ml的问题，期间他提到能不能用image features加入现有model. 因为楼主自己做过structured feature + free text + image的multi-modality model, 我说根据我的经验，加入Image embedding效果不会提升太多。（可能我是不是不应该跟面试官唱反调，而应该顺着他的意思来回答？但因为我正好做过类似Model，加了图像确实效果提升很小，所以就直接脱口而出了。）然后就开始聊的很不顺利。

KL divergence 和 maximum likelihood的关系，SVM实现，LSTM vs transformer


第一轮店面， Alien Dictionary
和三个ml问题，有一个是logistic regression, random forest, LSTM, NN 哪些是linear的
其他两个问题不太记得了， 很简单

第二轮店面，手写precision, recall， 和三个ml问题：
1. sigmoid, relu哪个能解决gradient的啥问题
2. AUC ?

ML基础，考了多标签和多任务，loss func的不同。最后问了解决过拟合的办法。

问的其实都是非常基础的ML问题：model evaluation, precision&recall, ROC, AUC, logistic regression, comments on different methods such as decision tree, logistic regression, SVM, neural network. 

1. 他问我AUC该如何理解，我就说AUC越大越好，确实不知道有什么解释。他又问是不是说AUC=1就比AUC=0好？我觉得是肯定的
2. AUC=0.7意味着什么？如何跟别人解释这个prediction？我答不上来，只说model挺好，比0.5好。
3. 两个不同的models，binary classification的gap一个小一个大，哪个AUC大？我犹豫了一会说是gap大的那个，也没解释。
4. logistic regression跟linear regression的比较。没答上来，我就说两个差不多。logistic不就是linear加了个sigmoid activation吗？还有啥？
5. high level评价一下各种方法(就是我上面写的那几个)？该用哪个？我毫无准备，就简要说了一下各个方法存在的问题，并没有对他们比较。感觉答的很失败。

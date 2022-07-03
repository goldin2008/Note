## MLE interview
`面试总结`
> https://zhuanlan.zhihu.com/p/58434325

> https://zhuanlan.zhihu.com/p/82105066

> https://www.zhihu.com/question/56676679

> https://msank00.github.io/blog/

`机器学习面试笔试求职必背！八股文`
> https://zhuanlan.zhihu.com/p/404809298

> https://zhuanlan.zhihu.com/p/405194507

> https://zhuanlan.zhihu.com/p/405197734

> https://blog.csdn.net/qq_18822147/article/details/120243772

> https://www.cnblogs.com/ljygoodgoodstudydaydayup/category/2074962.html

`机器学习八股文`
> https://www.1point3acres.com/bbs/thread-713903-1-1.html

> https://northern-dracopelta-98c.notion.site/5b22e124e16d4b2d937940367ca20eb0?v=19feabb85e9e4b54bc498579b3c7f1c5

> https://www.1point3acres.com/bbs/thread-714090-1-1.html

> https://www.1point3acres.com/bbs/thread-714558-1-1.html

> https://www.zhihu.com/people/is-aze/posts

> https://zhuanlan.zhihu.com/p/405194507

> https://zhuanlan.zhihu.com/p/405196671

> https://zhuanlan.zhihu.com/p/405197734

> https://zhuanlan.zhihu.com/p/405199136

> https://fullstackdeeplearning.com/spring2021/lecture-6/

> https://madewithml.com/

> https://eugeneyan.com/writing/testing-ml/

> https://completedesigninterviewcourse.com/system-design-interview/

> https://www.1point3acres.com/bbs/thread-652770-1-1.html

imbalanced class 看主要优化的目标是啥，可以是 precision, recall, 如果二者兼具的话就是F1.

到时候把Grokking the Coding Interview: Patterns for Coding Questions也学一下。感觉这两门课，对Machine learning engineer的面试可能就够了（当然，还有机器学习专业方面的你还需要去好好准备）

* Grokking the Coding Interview: Patterns for Coding Questions
* Grokking-the-system-design-interview
* Designing Data-intensive Applications
* 【Grokking Dynamic Programming Patterns for Coding Interviews】
* 【Data Structures for Coding Interviews in Java】
* 【Grokking the Object Oriented Design Interview】

![Diagram of deployment.](pic/connect.png)

![Diagram of deployment.](pic/dataops.png)

![Diagram of deployment.](pic/model.png)

![Diagram of deployment.](pic/update.png)

### System Design for Recommendations and Search
https://eugeneyan.com/writing/system-design-for-discovery/

1. `The offline environment` largely hosts batch processes such as model training (e.g., representation learning, ranking), creating embeddings for catalog items, and building an approximate nearest neighbors (ANN) index or knowledge graph to find similar items. It may also include loading item and user data into a feature store that is used to augment input data during ranking.
2. `The online environment` then uses the artifacts generated (e.g., ANN indices, knowledge graphs, models, feature stores) to serve individual requests. A typical approach is converting the input item or search query into an embedding, followed by candidate retrieval and ranking. There are also other preprocessing steps (e.g., standardizing queries, tokenization, spell check) and post-processing steps (e.g., filtering undesirable items, business logic) though we won’t discuss them in this writeup.
3. `Candidate retrieval` is a fast—but coarse—step to narrow down millions of items into hundreds of candidates. We trade off precision for efficiency to quickly narrow the search space (e.g., from millions to hundreds, a 99.99% reduction) for the downstream ranking task. Most contemporary retrieval methods convert the input (i.e., item, search query) into an embedding before using ANN to find similar items. Nonetheless, in the examples below, we’ll also see systems using graphs (DoorDash) and decision trees (LinkedIn).
4. `Ranking` is a slower—but more precise—step to score and rank top candidates. As we’re processing fewer items (i.e., hundreds instead of millions), we have room to add features that would have been infeasible in the retrieval step (due to compute and latency constraints). Such features include item and user data, and contextual information. We can also use more sophisticated models with more layers and parameters.


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


分享一个四月的AS 店面，Deep Learninig 组
自我介绍+why amazon+简历
ML
1) assumption of MSE (clarify 之后发现其实是想问assumption of linear regression， 我就说了linear regression那几个假设，什么linearity, normality 这种的
2) XGBoost 是啥，为啥这东西比其他ensemble model好，fine-tune时候考虑哪些params
DL
1) Transformer & Fully connected Neural net 的区别，优缺点
2) BERT 和 RNN 的区别，优缺点
3) CNN 和 Fully connected Neural net 的区别
4) how to fine-tune a deep learning model (想问fine-tune learning rate, optimizer 这些东西
而酒屋 没写出那个最优解不过也过了

### Microsoft
MS 电面，一个西雅图小哥，没有coding，纯ml探讨，要推写公式。
闲聊了聊自己的项目，推了一遍arcface 的loss，楼主英语表达一般，纯靠公式和画图给面试官讲明白了
聊了聊各个loss function，relu 0处求导怎么办等等
batch norm 作用，公式，batch size 不同时mean值不同怎么处理
l1和l2，公式，作用，特性，推导
最后了简单‍聊了下attention

train的时候把mean保存下来，inference的时候用保存的值. 0处出现的情况极小，可以忽略不计，一旦出现直接取0

比如说如何选择metrics， 对于不 balanced数据怎么办。为什么要用cnn 等等。

### Linkedin
接下来问probability，用什么样的distribution来model这些event最好：扔硬币，掷骰子，接线员下午4-5点接到了10个电话，5-6点会接到几个电话，股票走势等等，可能问了十来个。这里因为不知道要考probability，所以也没有复习到，可能有些没有答对。

再来就是挑一个算法，从头到尾讲。我讲了logistic regression，包括loss function，optimization，regularization。follow-up了两个问题，一是如果MLE换成MAP，求的是什么。二是，为什么logistic regression对于correlated features表现不好。我‍觉得我第二个follow up没答好，也请教各位会如何回答这个问题。

data coding: K means

后来问了一些recommendation system bias的问题。bias有多种，比如positional bias还有online/offline data distribution bias. 另外还问到一些fairness的问题，比如新的creator/post没有很多engagement应该怎么办。

半小时coding，地里出现过多次，如下：
"""
Input:
A method getRandom01Biased() that generates a random integer in [0, 1], where 0 is generated with probability p and 1 is generated
with probability (1-p)
Output:
A method getRandom06Uniform() that generates a random integer in [0, 6] with uniform probability
"""
半小时ML八股文：
比如Logistics Regression怎么estimate coefficents，loss function解释和推导。Decision Tree怎么prune之类的

ML: 一题ML model设计＆问logistic regression推导
coding: 刷题网参六邻

上周刚面完的凌鹰的AI Engineer 岗，现在还不知道结果，先回馈一下版上，同时为自己攒人品。
大概是4月被Recruiter 找到，本来想面staff，无奈recruiter说LinkedIn Senior对标G 和F的Senior, 最后就是面了现在的岗位。
面试大概等了3-4天才安排好，L家是到了最后面试前一天通知你面试官的信息，是个国人小哥，人很nice.
上来显示15-20分钟的工作经历聊天，简单介绍了一下自己的项目，找了找共同点。
然后是第二轮写码，是地理和蠡口超高频 三路领。大概确认了一下没有额外的变数，大概10分钟做完。
之后是第二部分机器学习八股。涉及到了各个方面，线性回归，逻辑回归，regularization L1和L2区别，表达式。随机森林和GBDT区别，scale和transform对它的影响。如何处理overfitting, 如何处理imbalanced dataset, 什么是unsupervised learning. 涉及的内容很细，但是并没有其他版友碰到的推公式的地步。如果是想复习机器学习基本概念，包括公式推导，楼主最近看了一个知乎叫 阿泽的 复旦计算机博主总结的 经典机器学习的各种知识点，从逻辑回归，到PCA， 树模型，甚至到XGBOOST和LIGHTGBM的公式都有。觉得受益匪浅。‍‌‌‍‌‍‌‍‍‌
保佑自己🙏🏻，同时也希望能帮助到大家。

### Twitter
coding部分：
1. 给出一些tweets，找出meaningful的组：很open的问题，要自己定义什么是meaningful，tweets的有用的features
问了如何encode tweets，用Bert有什么好处之类的
我先说了特别简单的one-hot / tf-idf / word2vec 提了一嘴可以train your own version of embedding用word2vec或者bert
2. Clustering有哪些算法，我说我只知道kmeans，然后就是kmeans的实现，可以用numpy，pandas之‍‌‌‍‌‍‌‍‍‌类的数据处理的包

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

上上周我参加了Uber MLE L4的onsite。一共四轮，一轮系统设计（bar raiser），一轮BQ，一轮ML coding 以及一轮general coding。
1. 系统设计：设计一个uber eats的餐厅推荐系统。 都可以，基本上还是讲架构和模型。使用什么的模型架构，数据怎么使用，怎么分割数据，怎么制作负样本。对于底层不是特别的关心。感谢！有信心了！最怕架构 database, in memory cache, message queue, 这些都不会
2. ML coding：实现Kmeans，允许使用numpy。
3. General coding：L‍‌‌‍‌‍‌‍‍‌C399
4. BQ：经典BQ问题

ML CASE: 每一个用户在app ui上会看到一个视频矩阵， 每一行是一个channel, 每一行的内容是这个channel下推荐的视频。现在的推荐系统分别独立训练 推荐channel, 和推荐每一个channel下的内容 ， 这样做可以吗， 有什么劣势？
ML system design: feed ranking.
我当时答的就是对具体用户的用Recommendation system， global的用一些features做ranking.毕竟店面也没有时间展开太多

System Design 1:
一道在ML背景下的系统设计，要求设计一个user activity tracking system来追踪给user推荐了广告之后怎么样搜集user和它们的activities并用于后续的training.
没有考察具体的model的设计，但考察了每一步storage的选择，data flow，时效性，以及如何筛选出没有被interact过的推荐并同样把它们作为signals。
System Design 2
设计一个类似youtube的视频推荐系统，同样也是以考察系统为主，而没有专注于model的设计，同时也问了一些和设计第一轮里的提到的如何做数据收‍‌‌‍‌‍‌‍‍‌集和清洗最后用来继续做model training的一些东西。

### Google

### Facebook
`一轮ML Design, 一轮System design, 2轮coding`
细桶射击是个印度大姐，题目就是给一堆机子去爬一个网站，我把sql，nosql，redis，filesystem还有log-message queue这些都说了一大通，还有如何parition和sharding巴拉巴拉，基本都是我在说，我中途问了一下有什么问题对方说没事我知道你说的，然后中间提了一些问题关于data model，我大概说了下怎么做index，我看她也没什么反应。然后又问了一些具体大概爬虫算法是个什么逻辑，还画了个testcase的 bfs 例子。。。最后问还有什么补充的，然后又加了个监控，check point 调度系统，因为机子可能不稳定会挂之类的。。。然后又问bottleneck 答完后就没了。。。也不知道怎么样

ML system design面的是设计search engine相关的， system design面的设计fee

SD. 设计一个系统, 将用户的状态更新推送给该用户的好友.
ML SD. 向用户推荐某类东西, 很常规了.
考得完全不一样吧, 可以参考grokking的system design interview以及machine learning interview.

sys design:search/update status 和 search most popular status 

ml design：resolve member complain about bad content

设计yelp, 设计instagram

一轮system design， 一轮machine learning design, 并没有给别的选择。
至于system design有两个track一个product，一个backend，backend就是偏向于distrubuted system design，product就是纯api design, recruiter没说而我呢自己也是没问，按照那个guide里面准备的，而guide基本就是那种distributed system design，再结合别人的面经，只按distributed system准备的。

E5 MLE是两轮coding、一轮system design、一轮ML system design、两轮behavioral。Leetcode要求能秒medium，能做hard。

SD. 设计一个系统, 将用户的状态更新推送给该用户的好友.
ML SD. 向用户推荐某类东西, 很常规了.
考得完全不一样吧, 可以参考grokking的system design interview以及machine learning interview.

ML design。 国人小哥。ads recomendation

ML design。国人女生。event recommendation

ML sys design: restaurant recommendations
老题，ml八股文，没什么难度

ML design 国人小哥，给了一堆user的log data和一个可以知道user当前location的real time API，要求recommend next place to go。问了可以用哪些feature，用什么model，怎么生成label data，用什么metric等。条件给的很模糊，需要多问来clarify。自我感觉答的还不错，事后feedback说ML不够strong。。。

System Design，东南亚小哥，CV specialist。让设计iphone的stocks app里面每个股票点进去后，下面推荐的articles。问了API设计，爬虫和read/write等等。感觉面的不错哦，feedback说非常strong。。。醉了

SWE SD: 在instagram中设计auction system

ML SD: 设计model identify weapon ads

ML design 一班会是一轮rank

我的理解是这道题的特点在于数据来源/label获取，detection entry point以及enforcement都是灵活的，如果思维局限了的话作为E5就会差点意思

bq着重问了我teamwork以及处理conflict的事情，并且有问怎么看待meta的vision以及privacy相关问题。面试官感觉是个大manager但是人很nice，甚至教了我一些有用的teamwork小技巧。

系统设计 国人大哥 typeahead: 心中窃喜 然后刚说到qps 大哥问你是不是看过这道题 一下子怔住了不知道怎么回答 后来实诚的说 确实以前见过 然后就换了道题 是关于如何search fb的post (比如搜apple,出来苹果公司消息的post) 全程阴着脸 不苟言笑 最后这轮好像也没过

ML 设计 国人大姐 问一些以前的项目经历 然后问的是 怎么设计fb的page模块的 search,比如搜san jose 出来的是地名 搜lady gaga 出来的是人的page.

2 design a personalized location recommendation system
基本上就是把recommendation的流程说一遍，candidate generation到ranking，是e5
tree base 的ranker: 问的重点就是解释一下什么是tree model，有哪些tree model，怎么build tree之类

3 behavior: conflict with other, most challenging, received sharp feedback, most ambiguous project,
4 tree based model, neural net, bias ‍‌‌‍‌‍‌‍‍‌variance, overfitting, regularizations, evaluation metrics,

系统设计:  ticket master，卖演唱会的票
ML 设计： 给定news ‍‌‌‍‌‍‌‍‍‌feed和所有的评论，抽取top3 评论
一点拙见，请各位大佬指正。input feature可以包括几大类 一是 评论本身features：quality index，length，relevence to the news feed，time等；二是评论者的features：average historic comments scores，impact （like number of fans），location等；三是互动的feature，点赞数，comment的回复数。用这些所有的做个mlp
我是当成recommendation问题处理的，推荐王喆那本“深度学习推荐系统”，里面有不少reference的paper值得看。也可以根据那些paper的引用以及关键词找一些更新的文章。
这一轮不用聊system design，纯ML就行。这题不涉及news feed本身的ranking，是rank 那些feed下面的comments，top 3这个跟面试官沟通了一下，是个soft number也可以自己定义，比如某个feed只有两个评论，那就都show出来就行了。
比如对于一些popular的帖子comments比较多，我们就需要挑一些出来显示，我是formulate成一个recommendation的问题（用classification的方法算每个comment的score，然后挑分高的显示

system design 是 推荐广告，和 手机 NLP 相关的推荐.

ML design: Design a classifier for bad ads
BQ: A time you had conflict with others, most challenge project, peer you felt difficult to work with, a time you provided constructive feedback

Sys design: 唯一的国人 web crawler 感觉尚佳

ML Sys Design: Recommend job posts to facebook users (什么时候fb也做linkedin的事了？？）

ML design - 名人推荐
ML system design, 就是要设计一个end to end的推荐系统，推荐的内容是名人的page, 不知道这样说清楚没有。

ML research - ML 教科书知道‍‌‌‍‌‍‌‍‍‌，但问得很细，也有涉及到NLP，Deep NN

ML Sys design deep dive会具体问到哪些方面呢?
如果你面senior, 最好主导conversation, 从需求分析，框架构建，数据收集，特征提取，建模，offline online 评估等各方面去讨论。
据我理解，要全面（覆盖关键的component)，多种方法以及trade-off，能提到一些与主题相关(也就是domain specific)的实用的点是个plus。

ML sys design: ads ranking

Round3(ML)：ML system design，case是关于Facebook Event的推荐系统，target是判断user是否会参加这些event，难点在于得判断他们是否是physically attendance，其他地方没什么特别的），印度小哥，态度还行；
    Round4(BQ)：constructive feedback，collaboration with different teams，challengest work，the personality you never want to work for，why not stay in academia，总共问了八九个问题，其他实在记不起来了，白人小哥，非常活泼；
我觉得可以先看看FB的那个event里都有什么，我之前完全不了解，把它当成一个类似广告的东西说。其实里面有个find ticket，可能还有其他的内容。另外如果能得到一个相对小但是比较precise的labeled set，semi-supervised也可能是个思路。面完我问面试官，他说这是个brainstorm，没有什么标准答案。
因为我把它当成类似广告的东西，所以分成了engagement(click) 和 satisfaction(rating, like/dislike, comments)来做的，面的时候我主要当成multitask learning来说的。

3. nearby places recommendation system - 跟面試官聊得挺開心的, hr feedback時說了表現的excellent
4. Design 一個像Kaggle的平台, 能做各種project competition
5. 中規中距, 自介, conflict, why leave your current job, etc
nearby place 就是基本的recommendation system那一套拿出來講 沒啥特別的 有稍微多講一點deep learning的部分
Design Kaggle 面試官有要求要有leader board的function, 能看哪個user排名高, 還有說系統必須要能抵抗malicious code, 問怎麼做到, 我感覺並不是read> write 吧？

1. ML System Design。问了Algo Expert的ML system design的其中一个，主要问了数据，feature，model，metrics，AB testing等方面
2. Behavior。就很普通的聊天，没什么可具体展开的
3. NLP Specialized System Design。因为本人不是CS出身，所以把System Design换成了这个。问了NLP的某个场景的design以及细节，很多问题都比较open ended
conversational ai （比如echo，google home）的end to end component。然后问了一些比较具体的conversation设计方法，比较open ended。还有intent detection，slot filling之类的。

第一轮ml design国人小哥，ecommerce推荐系统，这轮感觉一般面的，小哥水平倒是不错，overall structure没怎么说完就dive deep了，如果国人小哥也上这个论坛求高抬贵手，不求别的给个hire就好，感恩
最后一轮ml设计，看不出国籍的外国小哥，做nlp的，问的设计语音助手，不是我的domain，不知道答得在不在他的点上，虽然给出了一个基本solution但是感觉摸不到头绪get不到他想考的点，好在小哥态度还比较nice

ML Design
面试官三哥。交流不算很顺畅。
Design a harmful content detection system.

system d‍‌‌‍‌‍‌‍‍‌esign. 广告ctr

第二轮，ml 设计，四十岁国人，题目是推荐附近地点给用户，一直challenge我，问我数据从哪里来，估计是想我问我数据库的问题，然后让我设计feature，我大概设计了七八个，最后我拿出deep and wide那一套做框架做上去，从测试到最后问冷启动，一直challenge我，中途一度想摔键盘，应该是挂在这轮了吧。
第三轮，bq，普通问题，问了一些工作conflict啥的然后就普普通通，也有可能挂在了这一轮。
我感觉general idea上没啥大问题。我觉得是不是需要两个model，一个model负责candidate generation，一个model负责ranking。这是一个可能需要增加的点。可以参考google的recommender system tutorial。第二个点是不是可以input可以更多种类的data，比如item那边的data【，就是店家的information比如地址，电话，店家的id】user那边的data（context or query，比如你的信息，你的id，地址，你用的device， 你和商家的互动，你有没有给商家打过分，或者浏览过，甚至消费过，你浏览时长这些信息）。感觉这个真的无法猜测因何而挂，每个人在意的点真的差距很大，有些人会很烦你老沟通，有些人则是怕你不沟通，唉真的是，有些人觉得函数名写的不工业化都可能给你weak hire，贼坑
model 我就是和你是一个意思，一个用作处理nonlinear data，一个最后负责ranking，是谷歌那套deep wide的recommender算法，我非科班出身且是ng，至于feature那边我还想说很多，然后面试官说他觉得这些feature已经够了，good enough是原话，面到最后很不耐烦地样子，语气也不是很友好，本来45分钟的面试迟到了快十分钟，最后准时结束，然后还定了15分钟的buffer他说有啥要问的，我也没啥要问的，就象征性的问了下，然后一句祝你在其他面试中有好运就挂了，coding基本上是全秒的而且很明显感觉到两个小哥都挺positive的，最后连加面都没有，思来想去可能也是挂在这里了吧，谢谢你还特意看了我的note。也希望对大家有所帮助
楼主我觉得你做附近饭店推荐的还按deep&wide来可能有些冗余，一开始的KNN做的candidate generation step可以去掉，因为一个人附近本来就没几个饭店，重点可能是如何精排吧
不是饭店，是所有place，任何地点都可以

ML design 这一轮面试官是oculus research的，我问是不是fair，他说不是。题目是做一个 video search engine，input是用户upload一段 video clip（只有视频没有任何文字query），output是一堆排好序的 video list（我们存好的视频，有metadata），总而言之就是youtube 但是把搜索的输入从文本query替换成视频clip。
我的解决方案大概是先把 video clip 选一些frame放到CNN里获得一个embedding，然后pooling之后先用kNN召回（因为库里也存了现有视频的embedding），然后用MLP精排。
他问得很 detail，比如 train CNN的时候如果遇到未知的分类怎么办，问了半天最后告诉我 locality sensitivity hashing；还有正负样本怎么选择的问题，我觉得我答得也差不多但是他最后一定要问我知不知道有个 term 叫 triplet loss。这俩词我听都没听过，搜了一下发现其实挺intuitive的。另外沟通也不是很流畅（听不太懂越南口音），应该就是这一轮挂了。
System design 是个印度人，还挺nice的。问的是让我设计一个 leetcode，只要支持能存储和浏览题目、用户作答、自动检验有没有通过的功能。按常规流程来就行，算peak qps要考虑leetcode主要用户分布在某几个国家而不是全球均匀分布；难点主要是记得考虑一下用户可以submit不同语言的代码、submit后是怎么compile/run，然后状态存在哪、怎么返回给用户，万一崩了或者用户代码里死循环怎么办之类的就行了。
BQ 很常规，可能因为面我的是个华人，最后还留了十分钟做题（好像是 fb 惯例了）。

ml设计广告系统
sd设计ins

ML system design面的是设计search engine相关的， system design面的设计feed

细桶射击是个印度大姐，题目就是给一堆机子去爬一个网站，我把sql，nosql，redis，filesystem还有log-message queue这些都说了一大通，还有如何parition和sharding巴拉巴拉，基本都是我在说，我中途问了一下有什么问题对方说没事我知道你说的，然后中间提了一些问题关于data model，我大概说了下怎么做index，我看她也没什么反应。然后又问了一些具体大概爬虫算法是个什么逻辑，还画了个testcase的 bfs 例子。。。最后问还有什么补充的，然后又加了个监‍‌‌‍‌‍‌‍‍‌控，check point 调度系统，因为机子可能不稳定会挂之类的。。。然后又问bottleneck 答完后就没了。。。也不知道怎么样

Round 1: ML Design: 设计自动检测带武器内容的广告
Round2: BQ + LC238简化版，可以用除法。
Round3: ML Design: nearby place recommendation
Round4: ML Design: Instagram 推荐来自非好友的帖子
个人觉得location, time这些应该都是constraints，用于进行filtering, 是个deterministic的东西。如果candidate generation stage直接用这些constraint是不是顺序会有些不正确？假如说你用了Collaborative Filtering,通过Matrix Factorization得到了query&item embedding, 找到和你最感兴趣的k个餐厅，那如果这个用户走到新的地方是不是还需要跑一遍CF->MF再重新计算similarity找nearest neighors?
我个人觉得正确的顺序应该是offline的时候把CF完成(对于所有user和item)， 产生M（M>>K）个candidates，这样query and item embedding就都是static的了，当这个user发起新的query就可以通过constraints实时地得到k个items。
还是说以上这个过程就是LZ所说的粗排？然后再训练一个独立的模型用于精排？我比较纠结的就是filtering应该放在哪一层，个人觉得如果是像yelp一样的餐厅推荐app，如果先取离你最近的所有餐厅做训练是不是不可能达到real-time的标准？所以这个filter是不是应该放在最后一步来做。
最近正在0基础学习推荐系统，如果不对请多多指正。
我说的不一定对啊。我当时回答的时候还是按照ml design的标准套路来的。先画个图，然后列几个要讲的话题。本质上还是推荐系统的那一套，要预测的应该是用户会不会点开推荐的place， binary classifier, sort by probability。 一般的推荐系统都会有个粗排-》精排的分步，这个问题因为place跟用户的相对位置是相关的，利用距离信息直接filter就可以完成candidate generation, 不需要再train 粗排的model. 精排的模型就是基本套路了。值得注意的是时间信息(time of day)非常重要，要确保推荐的place是在当时是营业的。
是跟abusive一个套路，预测结果都是最终交给人工审核。那么怎么在保证准确率的基础上减少人工的工作量就是这个系统的business goal. 可以做成一个多分类问题，让分类器把目标分成三类：非常确定有武器，非常确定没有武器，中间类。系统自动排出非常确定的两类，只把中间类交给人工审核。
另外面试官还提出了一个问题，怎么cold start。我当时答的是可以去第三方专门卖武器的网站上去爬一些广告作为系统的初始training data。
感觉这个作为binary classification 更好吧？最后logistic function threshold >=0.9的就是肯定不行，0.65 到0.9之间（或者更小）的就送去人工检测，0.65以下的就都是ok没问题的，感觉这种更 make sense？不然你分三类的话，你怎么给你的model 去feed 给人工审核的data？你没办法优化这一块啊？
请问楼主能详细讲讲怎么解决positive example少的问题吗？感觉positive training data极其少（尤其还限定了是武器）
我想得到的可能用一些curator已经label的，用户mark的，或者用一些heuristic来filter一些已有的广告，或者自己generate一些。 楼主有什么好的想法吗？谢谢

第一轮：机器学习系统设计，广告推荐系统
第二轮：行为问题。问完以后还有时间就写了道题，蠡口 旧疤
第三轮：系统设计，聊天软件的群聊如何实现

第四轮： design auto comments suggestion system
第五轮： walk through ‍‌‌‍‌‍‌‍‍‌an ml project (present like in a conference, what's new? trade-off? why A not B?)

第二轮 设计instagram，一半system design 一半ml design, 先各种scalability 然后是ml如何提高instagram ( search, recommendation, push notification, image recognization....etc)
第三轮 hm bq， q&a的时候hm直接给我讲了未来12 month都要做什么 当时感觉有戏了。。男人的直觉果然不准= =
第四轮 ml design + ml deep dive 设计游戏对战机器人，提高玩家engagement，先说了如何用ml做匹配系统，匹配游戏玩家和游戏机器人的type，然后followup如何在游戏中提高，我就说了reinforcement learning，用td lambda，面试官好像不是很懂rl，没有follow

3) BQ: 激动的工作、什么时候需要其他组帮忙、不好合作的同事、和别人有异议、组长给你的反馈，没时间code
4) sys design
此次面试最大的惊讶，需要跟地里请教一下。题目原话“有三个组要用到一个功能：给URL之后下载文件。现在让你设计有这个功能的library的API和architect”。 我听完有点懵（说好的分布式系统呢、说好的scalability/availability呢），不知道他具体想问什么。给了一个简单的get_url(url, dest=None) -> response之类的简单接口，他暗示user experience不好，特别是在下载大文件的情况，一直揪着不放。我也提到了authentication, multipart-download, queue for async call, tempfile/atomic write， 但对方说这些都是好考虑但请回到API设计上。到了最后还是不知道他想问什么，最后反馈也是这轮不好。
5) ML sys design
设计FB广告推送系统。大部分时间在找feature，对方还一直问我有什么FB specific feature。 跟地里以及prep session里说的不一样的是：考官一直在让我写原理、写公式。我提到一开始可以用别人训练好的w2v/bert来给文字提取特征，对方就让我画w2v怎么训练的、损失函数是什么，最后怎么预测（我提了这模型本身不用来预测，不知道他是不是故意挖坑），bert是怎么训练的，两者变成vec有什么不一样。特征提取完了后我提了可以从简单模型到复杂模型循序剪辑，考官让我比较线性、树模型，提到RF的feature是random set还被他质‍‌‌‍‌‍‌‍‍‌疑说是random data但fix feature set,不知道是不是挖坑+1

System: messenger
ML: 推荐locat‍‌‌‍‌‍‌‍‍‌ions

2. System Design #1
是设计一个location based search。这一轮画风就比较非主流了。我因为看过一些uber/lyft的talk，也准备过geohash的知识，想说开心这都准备到了哈，上来讨论了一下需求，就说先画个架构图吧，本来计划每个component都大概讲一下，再落实到具体的schema design什么的，结果画完以后面试官说其他都不重要，咱直接说geohash怎么用，为什么用geohash，我就解释它为什么可以在密集地区持续split啊，找相邻block是O(1) time啊什么的，然后面试官一直追问geohash的细节，比如为什么每一层是划4x8个格子而不是比如8x8，直接给我问蒙了，这我确实不知道啊！在这个上面纠结到了只剩五分钟，最后只能草草讲一下返回结果怎么排序，就结束了。
个人反思是不是一开始不说geohash比较好？先讲讲even grid为什么不行，再讲讲quad tree这样？另一个失误的点是时间控制的不好，生平第一次面大厂design，有点被牵着鼻子走，其实不知道的细节可以申请先放一放，把大框架讲完了以后再回头抠细节？
3. ML Design
这一轮是一个非常常规的recommendation问题，被推荐的东西（item）不经常变，用户的interest变化比较快。用collaborative filtering或者binary classification都能做，分析了一下两个方案，觉得用classification比较合适，有一些比较明显的优点，面试官也同意，就开始讨论metrics，feature engineering，不同算法的优缺点，然后就是些model serving上面的工程问题，比如怎么monitor，online表现明显有问题的时候怎么debug，因为工作中都遇到过，感觉答得也不错，面试官全程I like it, fantastic。唯一没有想到的是可以用好友graph来扩展feature解决冷启动问题，这个是面试官提醒了以后才想到的。
这一轮就和上一轮画风相反。全程感觉很顺，但是还是给了个borderline，求大佬们指点一下，这是挂在哪了？
4. System Design #2
这一轮没有计入面试结果，但也挺有意思的。和第一轮Design一样，不按套路出牌，我把框架画完之后面试官说，这个设计很好，但是如果不用Cassandra或者任何s‍‌‌‍‌‍‌‍‍‌torage layer你要怎么设计，Redis也不用的话要怎么办，message queue也不用的话要怎么做，而且不是明着说的，就是说 “我们想尽量减少server间的networking”，反复沟通了很久，最后才明白他的意图原来就是不用任何轮子设计一个啥都有的monolith。明白了这个以后进展就很快，最终结果他也非常满意，后半程明显语气快乐得多（其实我想说这种设计挺糟糕的，拣了芝麻丢了西瓜）。。。
geohash 4*8是因为用base32编码，8*8也可以，就是base64了。
我面脸系统设计的反馈说是一开始problem exploration和clarification没答好。recruiter给我读了feedback，感觉广度，深度，量化和dive deep是几个主要考察的点。比如他抓问geohash就可能是想考察你dive deep
用binary classification来做推荐，天然就能处理用户兴趣的快速变化，因为推荐的item和对应的排序都不是提前算好的，而是在query time实时算出来的，比如（随便举个例子）你看YouTube，连续看了几个美食节目以后，下一次回到主页，首页需要做一次推荐，这时候在feature extraction的时候你最最近的浏览记录都会被包含进去，所以虽然model没有变，model evaluation的结果会和你看美食节目之前有很大差别。
相比之下，像CF的推荐结果经常是提前算好存在user profile里的，这就最多几个小时更新一次。
我都已经挂了，理解得不一定对，工作中没用过CF，说得不一定对，仅供参考！
我个人理解是deep dive是需要靠自己引导话题到一个自己熟悉/擅长的方面，比如我遇到这题我就会把话题引导到spatial index上，然后展开讨论。
哦我这一条回复说的不严谨，应该限定成“输出normalized probability的classification模型”，包括logreg，nn之类。我看一些Netflix的论文，以及自己做ad recommendation，都是用输出的概率做ranking，应该是挺常见的做法吧？是有什么问题我没有意识到？
同在做推荐，感谢楼主分享这么多细节！有个地方想讨论一下，用binary classification output probability 来ranking 我可以理解， 如果user和item都很多的话，楼主会先做candidate generation减少一下item的量级嘛？ 比如这个例子，user interest一直在变，之前一直看fashion style突然改cooking video，可是有millions of cooking videos, 需不需要减少到hundreds of 然后再用binary classification处理，这样online推荐会快一点？ PS, 我自己的亲身体验是youtube的recommendation多刷新几下的话，推荐内容基本上不怎么变化，只有位置变了。感觉都是些提前被cache住的推荐？
哈哈这个问题就复杂了，说实话我也没有太多实际经验。我面试的时候遇到的问题是item数量比较少的，所以没有这方面问题，像YouTube这样的item超多的系统肯定是要做个initial filtering/candidate generation吧。可能这也是我fail的一个点，我完全没有提candidate generation，其实应该至少提一嘴为什么用不上。
以我广告行业的工作经验来说，open exchange ad bidding就算用最简单的log reg，一次evaluate一两百个广告就是极限了，因为timeout限制是很短的，算上路上的时间总共能有个两三百毫秒就不错了。但是如果是自家平台的广告或者视频推荐就非常不一样，比如YouTube，可能可以在你看视频的时候，在后台发一个ajax query要求更新首页推荐列表，这个返回时限就不是卡的很死。但是不管是哪种情况，initial filtering肯定是要做的。
感谢参与讨论，在这个帖子里越讨论好像就越明白自己fail在了哪里。还是论文blog读得太少，对自己工作领域以外的推荐系统懂得还是太浅。本来以为懂一点high level的东西就够了，毕竟不可能在每个领域都有实际工作经验，看起来还是要多学习，bar比我想的高。
依旧是随便想的哈，没有实战经验。
我的想法是完全不在用户访问首页的时候试图更新rec list，而是每次用户点开一个视频，或者视频播放到某个位置的时候，因为有了新的观看记录，这时候送一个async call给server要求更新rec list，甚至可以在这些观看记录被发到server的时候，server顺便就把rec list更新了。因为更新的结果是存在server端的，不用马上返回给客户端，用户下一次回首页的时候直接读这个新的list就可以了。
这样虽然不是实时更新，但是只要你有新的观看记录，几秒几十秒之内rec list就能被更新好，除非你经常点开一个视频看几秒立马关掉回主页，不然基本上可以保证下次回主页的时候能看到新的推荐。

2. System design. Autocomplete system.
5. ML design。abusive comments
ml meet bar，system design不达标（not scalable）

一轮系统（爬虫），一轮ML设计（滥用）
anti-abuse, 像虚假账号

4. System Design
Design a system that returns nearby places (similar to Yelp Design)
5. ML System Design
Design a ML system for delecting / hiding violent posts
6. System Design (Shadow Interview)
Design a system that crawls websites

system design 这个也问了一堆 如何处理model 的问题.   
你如何确定你的 model 是 ok 的, 你如何 debug 你的 model, 你有多个目标如何优化

3. Distributed System Design: 给FB设计一个搜索引擎，给你FB月活数自己估计flow。LZ作为DS，这些姿势在3周内突击的。只能扯一些从知乎看来的教科书做法（帖子末尾有准备介绍）。结果这轮根据feedback非常positive
4. Machine Learning Design:  根据用户习惯推荐用户附近的商家。LZ机器学习功底算比较好，这轮也是比较positive的feedback
5. Behavior Question: 问了很多针对senior的问题，比如你对你搞过的product的评价。有什么你成功/失败的经验。Cross functional.末了还有个小coding，LZ啰嗦所以没时间code

第三轮系统设计，设计feeds，具体到一个senario：一个人正看着别人的主页呢，别人新发了贴，这时候怎么更新页面。问的比较细，这一轮感觉不太好
第四轮ML设计，设计垃圾网页识别的系统，感觉对模型不太关心，更关心工程方面

2.两轮design.
一轮是闲聊，聊各种AI相关技术， 比如cv一些比较popular的模型，RCNN是什么，怎么解决data稀疏问题。之前项目经历，模型怎么选的，tradeoff是什么。
这一轮比较随意，聊到哪问到哪。不过问的都是深度学习一些基本概念，关于数据，流行的算法比如cnn,lstm, transformer。。 很重要一点是有些模型/算法 面试官不了解，怎么解释清楚教会他。
另一轮典型ml desig‍‌‌‍‌‍‌‍‍‌n题，确切说是ai design。 偏nlp。  问题是如何根据文字做一些基本的fake news检测。 这里没有标准答案了. 一些基础的nlp context extraction方法。楼主不是纯nlp出身，这轮答得不好。

第三轮：ML research：一个资深的做NLP的（崇拜脸）。 问怎么用computer vision 优化FB的ads 推荐系统。用Deep learning 的common sense解释想法，让他听得懂。image segmentation 被他challenge了一下，不大记得paper细节了，讲得不是清楚。sparse，dense feature vectors。deep learning model上线的时候怎样提高计算速度。
第四轮：ML design：fb location based user recommendation. 先画整个ML 系统，然后每个部分深挖。feature和data比较重要。data 要设计schema，怎么存储。f‍‌‌‍‌‍‌‍‍‌eature部分最好答出一些亮点（像amazon的ads一个比较重要的feature是position）。 cold start 问题：如果user从来没有到过该location怎么办？你也不知道user喜欢什么怎么办？怎么判断你的model是最好的？online vs. offline training

第一轮 ml design
就是给用户推荐地点，感觉面试官没什么反应，每次我问有没有什么问题，is everything making sense， 她要么说没问题，要么没反应， 感觉我说话都占聊99%。 最后recruiter好像这轮最weak， 说没有ask the right questions和没有给具体都例子。我觉得两方面吧， 一是自己确实之前没有做过推荐系统，可能很多东西没问到点上，另一方面感觉面试官在guiding方面并不是很effective，跟其他面试官比起来还是挺不一样。
第二轮 ml research
问题是如何identify user interest， 挺有趣都问题， 不过这个也是一个很大都问题，所以肯定没有时间讨论所有方面，high level讨论以后， 就focus on 其中一个点，然后讨论另可以用都模型，具体问另模型都各种细节， 比如lstm和logistic 都training都细节啊之类。feedback还行
第三轮 bq
这轮feedback说overall都挺好，但是有些问题给都答案比较weak， 比如处理conflict都具体例子等等，这个确实对我来说有点难，因为之前对公司大家都和和气气，基本没啥conflict，偶尔有大家也都很心平气和地讨论和解决，真是没有啥好说的。。
第四，五轮
基本都是medium的原题，有一个hard 的dp原题，没时间写code，只写了transition的公式。feedback挺好
有一轮ml design 的follow up
因为说第一轮的ml design没有体现我的experience， 但是不知道咋回事，这一轮还是问的general的ml design，而不是之前说的我domain里的ml design，不过最后feedback也还可以。

ml：就是知道用户的location，让设计一个推荐系统推荐附近的point of interest 给用户，可以是酒店，景点等等

ml论坛上有几个总结的帖子写的很全面了。我个人觉得有两篇文章很有用：Wide & Deep Learning for Recommender Systems；Deep Neural Networks for YouTube Recommendations，ml system里面重要的部分文章都有讲到。我面试的时候基本上就是按照这两个的框架讲的。

3. ML 设计：新鲜事排序
4. bq，就各种故事各种聊（还问，你作为女生，觉得在cs最大的挑战是什么），连扣腚的时间都没有了
对方不怎么和我互动，所以一个人独角戏唱到了最后。讲的内容也就是之前地里总结的四个部分：数据，预处理，模型，metric

ML system design，基本上按照prep上面说的准备就行，面试过程基本就是给一个scenario，然后问你怎么design这个系统，比如news feed或者ads recommendation，然后聊下去，各个design component可能会比较随机的聊一些不同的方法和pros cons，比如feature engineer什么的打算怎么用什么feature，怎么处理这些feature之类的。基本上都是‍‌‌‍‌‍‌‍‍‌比较常规的ML问题。我准备上主要是看了一些相关的post和youtube视频，了解下这些系统，其实这些系统本质上都是差不多的，感觉基本上都是一个套路准备就行。

一篇文章下面有很多评论，怎么排序，从data到online inference都有问
问了很多ML的基础知识，然后‍‌‌‍‌‍‌‍‍‌是一道design：推荐热门文章

第四轮ML page recommendation
第五轮System Newsfeed ranking

第四轮 system design
设计在线text autocomplete，要求reliability，low latency
第五轮 ML
ML basics +
用户有很多query，怎么对query进行topic分类，假设我们已经有‍‌‌‍‌‍‌‍‍‌20个topic的label

ML design：问了一个怎么推荐附近的餐厅，主要考察recommendation system。建议看一下地里面的神贴，可以循序渐进，从简单的统计方法，比如最hot的地方，到content based方法，最后讲讲collaborative-filtering, 最忌讳的是上来就用很复杂的模型，然后不知所云。注意跟面试官交流也很重要，时不时要check一下进度，不要一个人滔滔不绝讲一大堆。

第三轮: nlp design: 假定现在有个机器翻译系统上线了，如何评估翻译质量.
第四轮: ml design: newsfeed.
比如在fb的feed里，自动把英文翻译成了德语，如何知道现在这个系统的翻译质量。 <= 我的想法适用user 的behavior 当作feedback 比如说 user preference 是德文 看了翻译的之后 就有做post or like 等等action , 这就是ㄍㄧ个质量的说明 ? 不知到lz 怎答的?
和你的答复差不多， 构建一个机器模型预测用户feedback的置信度。

第四轮是distributed system design，疑似国人或者ABC小哥
给一个地点和一个距离，和一大堆places，设计一个service返回这个距离内所有的places，重点focus在如何存储这些places和如何query，以及如何把这么多数据分别存储
第五轮是ml design，依然是国人小哥
news feed，不过重点在于如何给一个用户能看到的story排序，先问选什么feature，如何处理data，选什么Model, 不同模型的对比，以及最后如何measure你的结果。用我残存的记忆大概讲了一些，具体到model的部分就不太会了，只能说我不知道= =
加面题目是，设计一个service，每天给每个用户推荐一条最符合他兴趣的广告，没有讨论具体的feature selection或者model这种ml问题，主要就是讨论如何把广告存起来，如何handle很多用户，service的interface之类

machine learning面的是newsfeed，其中有一问是怎么推荐用户兴趣以外的post，楼主不太会就说可以randomly推荐一下。这问我现在也不清楚，请大家讨论一下吧
如果是我我会把user 没有warch 过的post category 当作我们的target , 带入reccommendation 的system 也就是说简单的方法是CF 搜寻相似的user 找到共同兴趣的post 然后就可以产生new feed 这因该是最简单的做法

第二轮：ML系统设计。比较坑的一轮，之前那么多人的ML engineer面经，都是News Feed ranking, Ads ranking，我也按这个准备。。。结果考了一个用Machine learning来做Facebook的好友推荐功能。。这轮回答的磕磕绊绊，有可能会挂。。

第二轮ML设计：国人小哥。要求设计一个NLP分类器，输入为搜索语句，输出为归类。比如是体育类，新闻类，音乐类等。本人工作中没做过NLP，但是平时注重学习，对NLP有所了解。标准ML设计流程，讨论data性质，给出NLTK包做data filter，bag of words做feature extraction，模型选择选用了LR和SVM，并讨论了模型的推导，优缺点，必考的overfitting underfitting问题。最后讨论了一些优化。由于紧张，混淆了一个概念，小哥纠正以后才意识到。如果60分hire，80分strong，自我感觉表现在70分左右。小哥并没有帮忙提一格，给了hire，没有给strong。
又想起来一些细节，补充一下。第二轮ML设计，小哥提了一个问题，说如何做可以使SVM来predict连续值，而不仅用作binary classification
针对第二轮ML系统设计，baca推荐的学习资料如下，希望对大家有用：NLP特征提取Query Intent understanding和Query rewrite， 书籍《美团机器学习实践》，知乎美团，达观文化的技术文章
楼主那个NLP的问题，我感觉应该是class 场景分类，类似于Google搜索歌名，能自动给出歌曲歌词，MV之类的搜索。。如果回答是一个命名识别问题NER 是不是会加分？其实标准做法应该是LSTM + CRF....个人理解是这样的。。面试官了解你不是完全了解这个领域，你的做法可行，但不是公司会用的做法。。。
第五轮distributed system design：也是阿三。题目比较刁钻，要求设计news feed，返回一个区域范围内所有的news，针对这个2D空间的范围搜索进行设计。我给的是用K-D tree可以做二位空间搜索，然后一些常规的分布式优化等。有一个负载平衡的优化问题没说清楚，这轮自我感觉也是在hire和strong之间，最后给了hire。
第五轮distributed system design：给的数据量是10亿个news的地理位置，qps是每秒十万次。
10亿个news的地理位置，qps每秒十万次。数据存储和CPU单机都解决不了，需要分布。我当时给的解法用AWS EC2和ELB服务，这个解CPU分布很容易，但是解不了数据分布。用nosql数据库，我给他按照每个item最大32kb估的，也有几十个TB了。我给的解是数据按照地理位置分开存储，比如搜索纽约，就到专门存纽约的库里找。每个单机存两到三个地区库，平时主要服务一个区域。开机的时候可以把主库加载到memcached。既可以多备份保证安全，也可以在局部出现热点的时候，这样可以用非热点服务器帮忙接一下。
但个人感觉这个解太复杂，实际并不太现实。

design: FB news feed
ML design: ‍‌‌‍‌‍‌‍‍‌POI , features, models
这个是个看上去很累而且漫不经心的小哥面的， 所以我就简答带过了因为poi 多数情况是作为general system design出现的，我遇到的可能比较特殊， 要求personalize, 然后看我之前做过的项目集中问了怎么产生user level embedding, location level embedding, 如何采集negative example, pos example, 对 neg example 怎么sample, model 选择上LR, XGB, NN 各自有啥优缺点。总之问的很随意发散， 和大多数同学遇到的有点不一样， 可能是个例/

Prob 4: ML design. Some NLP prediction task. Basic questions about data collection, loss function design, and so on. Don't remember the details.
Prob 5: ML design. FB newsfeed ranking design. Basic questions ‍‌‌‍‌‍‌‍‍‌about data collection, loss function design, and so on.

3，设计facebook newsfeed
后面把我转到distributed system 组，加面一轮system design, 给10k个server 和一个url, 要求设计一个distributed ‍‌‌‍‌‍‌‍‍‌system 从给定的url进去，来crawl 10^9 urls。我对系统设计完全没概念，所以毫无悬念地再次挂了。
ml设计一开始就问怎么设计 newsfeed，我准备不充分，不知道这种问题有没什么套路。面试官问了一些 metric, 模型之类的问题，具体有点不记得了，都是跟newsfeed想关的问题。
new feeds 是click -through rate 的optimize 还是只是相关性的recommendatio system ?
click, like, comment, share 这边是偏向feature engineering 吧? 那主要是考察什么呢? 算法 or 储存 or 公式推倒?
面试官没说，我是按CTR这种来做的，算click, like, comment, share这些的概率
没有问存储这种，都是ml的相关的比如feature, model这些

不好意思回的晚了点。他当初提的问题是这样的，given一个用户点击了一个网页，如何给他推荐相关的网页。总体来说应该要求你design一个完整的system，包括用什么做feature，用什么算法，model evaluation之类的。但是我的面试过程比较纠结，因为我提的算法似乎有点问题，我们就纠结了很久这个。所以没太来得及到后面的部分。
反正整个过程就是随时可能被打断问各种的问题，然后很可能没法按照原定的计划讲下去。
第一个点就是用什么algorithm，我说可以把点击其他网页的概率用logistics regression，然后我们就在logistics regression的算法上面纠结了许久。比如定义，kernel之类的东西。剩5分钟的时候才提了feature selection和model evaluation的问题

系统设计，设计记录手机用户浏览和点击广告，并用来算点击率。主要是写的部分，用户读手机不用管
ml 设计，facebook marketplace， 基本上是ranking的问题

d). （噩梦开始）12:30， 一个白人大哥很犀利的样子（背景也很牛），爬虫设计，10k的机子爬1B的wiki，不能爬重复的page。本人准备的设计题中恰巧没注重这方面，所以答的很磕绊。大哥先问了单机子多线程怎么实现，怎么加锁，然后到了分布式。其实核心思想是hash url，然后进行更even的分配负载。
e). 1:15，很nice的国人小哥，问的是ML design关于POI（point of interest). 注重点是ML的整体思路，从问题的描述道最后的service搭建，过程中会涉及到‍‌‌‍‌‍‌‍‍‌database的query，categorical feature的降唯（embedding）等等细节。这轮楼主表示面的一般，但不至于挂。

1. System design: typeahead. 问得很详细，比如DB里面存什么内容，如何index，如何对suggestion排序，如何更新排序等等。并不太清楚trie是怎么存在DB里面的，所以只答了trie在cache里面。DB里面就存排序好的words。
3. ML design: 设计marketplace的recommendation，主要讲了选什么样的feature和model overfitting了怎么办

round 2: machine learning design:  in youtube search engineer： 如果你想search key word “machine”， 当你type “ma”时， 可能多种选择 “map”， “mat”。。。how to rank it。 how to search in database。
round 5: system design： goe 题： 给你 p（latitude，longitude） search 一个 半径 n miles 的circle 内所有 p（latitude，longitude）。 如何get database， 怎么存 database，设计怎么search。 map reduce 之类
我个人觉得是 search 和ranking 如何 ranking in database ， 如何search
请问楼主第二轮ml design是用machine learning 做ranking吗？主要考察什么？考察的是 trie structure 和 search enigeer

1. 设计 亚麻 商品 推荐系统，
2. 设计 推特 状态 搜索
系统设计偏重infra吧
ML 特征选取，特征工程，评估，模型 之类的

3. 系统：爬虫
4. 系统：机器学习rank page

4. system design：国人，typeahead，面的还行，貌似帮忙。hr反馈回来不是strongest，估计bar高。
5. system design：国人，friend recommendation。hr反馈回来不是strongest，估计bar高。

第三轮是system design，上来先问了我一下有没有tradeoff的experience。然后system design的问题是design a geo info system which provides service to find the nearest n locations from 50M point of interest
第四轮是machine learning system design，让我design一个public video recommendation system
我觉得你可以搜一搜point of interests system design就会有很多相关的介绍。

第二轮：ML system design. Newsfeed ranking. 这一轮是论坛里讨论的比较少的一个类型。我复习的方式是先复习一遍一些ML的经典算法，然后学习Facebook的ML视频（来自FB blog和YouTube搜索）。看得多了，会发现总结起来答题有章可循的。
我自己准备的时候在白板上对空气讲过几遍，但是面试的时候其实问题会特别发散，跳来跳去的，比如我提到“训练效果。。。”，对方就问“怎么知道好不好”。但是大体上都是很常规的问题。
ML design: 把基础打好，多了解一下工业界的操作，总结一个ML系统的组成部分和每个部分的design要点。

Round1: ML System Design: 设计一个系统来识别广告或者post里面有没有违禁的内容（色情，暴力）。如果看文字要怎么做，如何筛选关键词，如果用naive bayes怎么做，如果用deep learning怎么做。如何根据图片来做，DL。用什么feature，performance metric，如果case比例很低怎么办，等等
Round2: ML Theory：在没有label的情况下，如何根据post里的文字来分类（聚类）。K-means原理，如何判断post里某个聚类的中心更近。
如果case比例很低，就用skewed sampling，就是对case over-sampling，对control under-sampling，让他们尽量balance，另外，好像cross entropy可以较好的处理这种情况，因为里面有个log，这一点我也不太确定，还请大神来解答。面试节奏很快，就想到什么说什么了。
feature selection有这么几种方法，统计上喜欢用forward, backward, stepwise selection。 L1 会把一些coefficient 压缩到0，所以有feature selection的作用。另外，用PCA把维数降低，应该也算。最后有一些package 比如我知道H2O.ai里面有一些模型比如RF，可以把每个feature的importance算出来，从而帮助feature selection。我就能想到这些，还请大神门帮忙补充。
thanks for sharing 我是NLP 领域 我司常用的是PCA or auto encoer, word embedding 也是常用的技术 当然怎么tune 这些skill 又是另一件事

3. 系统设计 国人大哥 typeahead: 心中窃喜 然后刚说到qps 大哥问你是不是看过这道题 一下子怔住了不知道怎么回答 后来实诚的说 确实以前见过 然后就换了道题 是关于如何search fb的post (比如搜apple,出来苹果公司消息的post) 全程阴着脸 不苟言笑 最后这轮好像也没过
4. ML 设计 国人大姐 问一些以前的项目经历 然后问的是 怎么设计fb的page模块的 search,比如搜san jose 出来的是地名 搜lady gaga 出来的是人的page.

ML system design，基本上按照prep上面说的准备就行，面试过程基本就是给一个scenario，然后问你怎么design这个系统，比如news feed或者ads recommendation，然后聊下去，各个design component可能会比较随机的聊一些不同的方法和pros cons，比如feature engineer什么的打算怎么用什么feature，怎么处理这些feature之类的。基本上都是比较常规的ML问题。我准备上主要是看了一些相关的post和youtube视频，了解下这些系统，其实这些系统本质上都是差不多的，感觉基本上都是一个套路准备就行。

第二轮：ML system design. Newsfeed ranking. 这一轮是论坛里讨论的比较少的一个类型。我复习的方式是先复习一遍一些ML的经典算法，然后学习Facebook的ML视频（来自FB blog和YouTube搜索）。看得多了，会发现总结起来答题有章可循的。
我自己准备的时候在白板上对空气讲过几遍，但是面试的时候其实问题会特别发散，跳来跳去的，比如我提到“训练效果。。。”，对方就问“怎么知道好不好”。但是大体上都是很常规的问题。

1. Friend recommendation
2. Video recommendation
3. Design market place
4. Amazon recommendations
5. Ad click through rate
6. Text clustering
7. Text classification
8. Point of interest
9. Newsfeed randking

ML Design I:
Design video recommendation system.
Follow-up: How to maximize the video watching duration.
嗯，Collaborative Filtering（CF）可以做。但是CF不太容易使用用户及video的特征。此外还要考虑scalability 的问题。可以参考[1], [2].
关于video duration的问题，可以定义一个新的loss function，比如累加用户$u_j$ 观看的video $x_i$概率与video长度$length(x_i)$的乘积等.
$\sum_i_{length(x_i) * P(x_i|u_j, ...)}$  
[1] Paul Covington et al., Deep Neural Networks for YouTube Recommendations, RecSys 2016.
[2] Xinran He, Practical lessons from predicting clicks on ads at facebook, PAKDD  2014.
还有个问题 如果是到youtube这个量级 矩阵的规模都在亿乘以亿水平 那么像spark这种mr也没法完成分解 可能要使用到parameter server. 目前的推荐系统都是召回加精排 召回多用cf 而非youtube的dnn 当然阿里的可能更复杂如din这些 cf可以看spark mahout这些 精排就各显神通了 但是复杂模型的线上推理也是个大难题 用lgb xgboost做embedding 后接lr是主流做法 还有就是谷歌的wide and deep

ML Design II:
Design Ads security system, detecting non-appropriate ads.

一轮system design：我第一次面真的system design轮，相对的弱项。不过recruiter说ML candidate一般都比较弱，会考虑进去。跟我之前看得常见系统设计题不一样，还是偏analytics的。需要设计算法来计算某种metric，这部分也相对传统的system design可能更open-ended一点。问了些data base access pattern啥的，我确实不太懂。。就直接说不是很熟悉哈哈。。
- 不需要state-of-the-art的fancy ML model，但是需要正确formulate问题。也就是明确这是个classification/regression/ranking problem，且解释为什么。
- 基于选择的problem formulation来思考如何拿到labeled data。事先熟悉面试公司的业务，然后思考如何巧妙利用他们现有的数据。这几个公司基本都是social platform，所以可以有很多user intention的signal。往这方面思索一下，基本思路都是hybrid 的semi-supervised approach。
- 有用的feature可以从你得intuition出发，然后讨论能否获得那些数据，处理的复杂程度之类的。feature engineering和embedding approach都可以讨论下。
- 那些大厂会注重scalability，所以可以讨论下如何sample data， train的时候估计需要多少data points。
- model serving的时候讨论是real-time prediction呢还是batch job这种
- 讨论下offline/online metrics。这里也最好结合业务本身propose relevant metrics。
我也还需要提升呢，不过我觉得宗旨就是要凸显你的在project里的leadership，过程中遇到了什么困难，如何解决一些conflicts，deliver了如何的result，对公司业务有怎样的impact。总之故事要娓娓道来，然后一个故事涵盖体现你的综合实力。
不过我觉得还是要实事求是比较重要，可以适当夸大，但是如果真的没什么太厉害的project或者本身经验不足，硬给你个过高的level，入职后也会很艰辛。但是一定要争取到体现自身价值的position和package。
梳理一下简历，回顾一下过往。我确实有几次面完了，想起来还有个更好的例子，或者当时还有些困难的解决，可是面试的时候临时没想起来。事先多做点self reflection，也可以帮助自己建立信心哦。
以前觉得behavioural round就是闲聊，后来发现其实大有学问。还需要继续钻研
请问面试中手动run thru test case来debug是指什么呢？ 我的理解是自己写一个test case，然后把程序里每一行做了什么，中间结果自己手动算出来嘛？这样是不是太难了，对于有些复杂的dfs problems..
对，是你理解的没错。有些test case确实比较复杂，所以我猜测选择有代表性的有比较简单的test case来检验也是考核的一部分？不过我拿到的题没有dfs的所以相对容易些

现在这两家公司都有单独的ml track engineer 的面试。和普通的swe的区别是可以不考常规的system design，而是更加侧重于ml的相关问题。
我觉得这个帖子里面提到的paper都非常有帮助：https://www.teamblind.com/article/ML-design-interview-3cYD0vdM
特别是 youtube recommendation, wide and deep, rules of machine learning, 基本涵盖了大部分相关的知识点。其实很多问题归根结底都是推荐问题，本质都差不多，比如ads，news feed，product recommendations, etc
其他几篇我感觉很有用的是：
tfx: https://www.kdd.org/kdd2017/pape ... e-learning-platform  侧重于整个ml workflow
linkedin 的tutorial ：https://engineering.linkedin.com ... p-learning-tutorial    deep learning recommendation很好的总结
对常用的sgd的方法和变种的总结：an overview of gradient descent optimization algorithms
[backcolor=rgb(255, 24‍‌‌‍‌‍‌‍‍‌7, 160)]
最后，面哪家公司可以多看看那个公司最近发的paper，engineer blog神马的 （e.g. https://medium.com/airbnb-engineering）。总体的感觉是，如果准备方法得当，在短时间内还是可以取得不错的成效的。

4. Design Twitter
Pull + push model, nosql, multi-level cache, load balancing, using queue to prevent leaky requests, db separate read/write, request cross region route vs request local route, data cross regiona sync, data sharding, photo support
5. Design Feeds Ranking, feeds include a mix of friend feeds, news feed
Learning to rank framework -> chose pairwise, just because it's more familiar
post embedding, user embedding
feature engineering, feature engineering, feature engineering
pairwise scoring function architecture -> any binary classifier (nn tower + sigmod, fb btst + log regression, google long and wide, linkedin modified version of long and wide)
embedding cold start -> global average, airbnb bucket overage, cron job re-train
ab test, sticky session, maybe you can a‍‌‌‍‌‍‌‍‍‌lso talk about session vs tracking during ab testing
metrics: ndcg vs map vs mrr, how to calculate
这个问题原来问的是，如果新的用户我们怎么办。所以我理解为user embedding cold start的问题。YouTube和Airbnb的论文里都有一些类似的解决方案。说实话我自己并没啥很好的想法，就很直白的说YouTube怎么做的，airbnb怎么做的，我觉得都可以尝试一下。
Airbnb embedding: https://astro.temple.edu/~tua95067/kdd2018.pdf
feed每一个post自身的embedding我感觉还是蛮固定的，我给的方法虽然在production中可能很不切实际，但是感觉只要有post就能算出post embedding来，所以这个方面好像没有特别的cold start的问题。
synthetic data我从来没真正试过，隐约感觉在这个环境下生成数据有一定挑战性，但很可能是一个不错的切入角。如果是我给面试的话我会想了解一下你准备怎么生成。
都是open ended question，没有正确答案，只要能讲得通，大家觉得理论上make sense就好了。
我也不是很清楚人家想问多么细节，一般都是我在说，他在听，偶尔问下问题。我觉得大约就是看看你了解多少，能不能把问题阐述清楚。
如果你想了解ranking具体的细节的话，ml推荐阅读的第四篇是关于ranking的，内容有点多，讲了非常多的ranking architecture，但不是所有的内筒都要很仔细的看。如果只是为了面试的话我推荐把其中一种弄得很明白，剩下的大概了解一下。有基础的话，每天一两个小时，一个星期就够了。
面试的时候我建议double check with your interviewers看他们有没有明白你在说什么，问问哪说的不够清楚，需要具体讲一下。说实话特别是ml，一个方向的有些细节做另一个方向的人很可能并不完全清楚。如果你能像讲课一样然别人明白的话，interviewer一定对你印象很好。
楼主本来是做search和ranking的
btst是手残到家了……我想说的是fb gbdt + logistic regression……感谢帮忙指出，ml推荐阅读的第三个就是facebook的那个architecture
我觉得feed ranking更多的是一个personalized ranking problem，我没有按recommendation system的方式去想过。pairwise ranking的话就是拿两个两个documents相互比，看哪个应该排在前面，最后还是需要从pair order生成total order。前面做post embedding和user embedding的时候那些embedding应该包含相似度信息，我就没有从score function的角度再考虑相似度。
不过我觉得只要你能说得通应该都行，感觉和system design一样都是open ended questions
multi-level cache <＝ 这边的multi-level cache 的应用能说一下吗? request cross region route vs request local route => 我想这边跟根据user 的region 用比较近的CDN or data center support?
multi-level cache就是给几个cache layer再搞一层cache layer，fb live是这么做的。
request cross region route就是user read write不一定是local，有可能根据business logic把你route到另外一个region，netflix就是这么干的。这样regional data center之间不需要sync，也没有直接的communication。
相反的，就是read write是在local data center，然后regional data center之间互相sync，github是这么干的。不过这个需要比较复杂coordination和distributed lock，github还因此出过一次20+h的outage。
两种方法其实都可行，各有利弊，而且在不同公司都在production里面用，只是有不同的trade off
原来是问新用户 那用history 其他的用户资料 ＋cluster or 相似度的想法 可能比synthetic data 好（虽然synthetic data 也是near neighbor 的概念） 跟lz 讨论学习了!

第四關 system design：設計 Yelp，100M 餐廳位置資訊，每秒可能會有 10K requests 要拿最近 200 個點，暫不討論新增餐廳的問題。這個問題我從來沒想過，所以就慌了。現場瞎掰一個 geo encoding 的方法，但由於分佈不均，所以會有某個 hash 太多點的問題。後來回去查，發現這是個正確的起點，接下來只要用 Quad-tree 的概念去切 encoding 就可以解決問題，但面試當時我只想到用好幾個 level 的 geo encoding。想當然爾這個解法就非常混亂，面試官一直聽不懂我的 approach，連帶壓縮到講系統架構設計的時間，於是就草草結束。
第五關 ML Design：設計 news feed ranking algorithm，但很可能那時候已經餓昏頭了，加上被上一關震撼教育，這關也回答的不好。開頭本來想要用 contextual bandit 來解，還寫好 cost function。解果不知怎的，講到後面居然變成 logistic regression
完全對不到一開始的 cost function。甚至還不是 ranking 的演算法。
他們的 engineer manager，考了我怎麼設計 instagram newsfeed ，提供了使用者量，平均有多少照片上傳，active user 佔比多少，peak load 多少等等。我自覺
講的還蠻順的，initial approach 雖然頗糟的，但後面的修改就都有達到系統需求。只是因為我前面問問題問太久（～15 min），中間因為邊講邊思考，語速太慢，導致根本沒談到 scalling 和 ranking algorithm 的地方。
ml的newsfeed ranking design和instagram newsfeed 还蛮像的
是啊，不過考 instagram 那次面試官問比較多關於 scaling 的問題，所以就沒碰太多設計推薦系統的部份


Educative.io Grokking Machine the Learning Interview + blogs on machine learning design from Medium.com

Wide & Deep Learning for Recommender Systems

Deep Neural Networks for YouTube Recommendations
> https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/45530.pdf

The Netflix Recommender System

From RankNet to LambdaRank

Predictive Model Performance: Offline and Online Evaluation

Practical Lessons from Predicting Clicks on Ads at Facebook

> https://towardsdatascience.com/recommender-systems-in-practice-cef9033bb23a

> https://towardsdatascience.com/introduction-to-recommender-systems-6c66cf15ada

> https://www.kdnuggets.com/2019/04/text-preprocessing-nlp-machine-learning.html

> https://medium.com/@MSalnikov/text-clustering-with-k-means-and-tf-idf-f099bcf95183

> https://stats.stackexchange.com/questions/263429/how-to-run-linear-regression-in-a-parallel-distributed-way-for-big-data-setting

> https://engineering.fb.com/2015/06/02/core-data/recommending-items-to-more-than-a-billion-people/

> https://www.youtube.com/watch?v=mhUQe4BKZXs&list=PLkQkbY7JNJuBoTemzQfjym0sqbOHt5fnV

> https://www.youtube.com/watch?v=0DYQzZp68ok

> https://www.youtube.com/watch?v=Xpx5RYNTQvg

> https://www.youtube.com/watch?v=nxhCyeRR75Q&list=PLIG2x2RJ_4LTF-IIu7-J3y_yg8LRe1WZq&index=2

> https://igotanoffer.com/blogs/product-manager/behavioral-interview-questions-tech-companies

> https://leetcode.com/explore/

> https://ai.facebook.com/blog/powered-by-ai-instagrams-explore-recommender-system/

> http://highscalability.com/;jsessionid=BB3A3CFAC4FDBDE62CD99D810F4337B3.v5-web020

> https://research.facebook.com/research-areas/machine-learning/


### Machine Learning System Design Framework (page recommendation/fraud)
• Design a personalized news ranking system.
• Design a product recommendation system.
• Design an evaluation framework for ads ranking.

• Can you visualize the entire problem and solution space?
• Can you come up with relevant ML features for your model?
• Can you detect flaws in ML systems and suggest improvements?
• Can you design consistent evaluation and deployment techniques?
• Do you understand architecture requirements (storage, perf etc.) of your system?
• Can you model product requirements into your ML system?
• Are you able to overcome common ML problems such as overfitting, cold start, data collection and logging?

• Problem formulation:
    • Optimization function.
    • Supervision signal.
• Feature engineering:
    • Data source.
    • Representation.
• Model architecture.
• Evaluation metrics.
• Deployment (A / B testing).

`Problem Statement: Clarify question/senario/feature/background`
understand the problem and ask clarifying questions
Let’s take an example of an advertising platform that uses a machine-learning algorithm to display relevant ads to the user. The success of this system can be measured using the users’ engagement rate with the advertisement and the overall revenue generated by the system.

`System Goal: Identify metrics and requirements`
During the development phase, we need to quickly test model performance using offline metrics. You can start with the popular metrics like logloss and AUC for binary classification, or RMSE and MAPE for forecast.
How do we train models to handle an imbalance class?
How do we monitor and make sure models don’t go stale?
How do we design inference components to provide high availability and low latency?
Once models are deployed, we want to run inference with low latency (<100ms) and scale our system to serve millions of users.

`Cold Start`
- boost new movies based on their similarity with the watched movies
- increse their relevance scores a little

`Train and evaluate model`
`1. Data extraction/Data collection:`
You have to understand the problem and figure out possible data you can collect.
1. target variable construction:
- Deduplication
- EDA(0,1 ratio), imbalance data
2. Feature engineering:
- What should be feature: page metadata, user metadata, friend metadata
- Important feature distribution
Data generation 这块可能还要考虑下用什么data 做training， label 是什么
`2. Feature engineering/Preprocessing(why preprocess):`
One hot encoding, Feature hashing, Numeric features, Crossed feature, Embedding
1.Text embedding 2. Categorical feature 3. Date Parse 4. Missing value 5. Outlier detector
categorical feature, numerical feature, text feature (TF-IDF, word2vec), image (Use pre-trained CNN model like VGG as feature extractor)
Dimension reduction (optional): SVD based ALS (useful for TF-IDF), PCA
Preprocessing 可能还需要做standardization跟normalize data
我好像记得linear regression  和logistics regression是scale invariant? 所以也可以不做normalize?
当然Ridge 和lasso是有影响的
KNN 里面非常需要normalize data，因为这个会用到距离。

`3. Model selection: There are 3 widely-use classification model`
- Logistic regression is a linear classifier(linear combination + sigmoid function(Monotonically increasing)). The model output is the predicted probability of label being 1. It requires assumptions: each data point independent. No correlation between features. It’s fast to train and easy to interpret because of it is a parametric model. This is a simple, robust, low variance model compared to tree classifiers and other non-parametric classifiers.
- Bagging method such random forest tree classifier does not need assumption to data. It randomly bootstrap features to parallelly train n models and take average of each model’s output. Random forest will result in low variance because low correlation between each tree. It’s relatively quick to train because each tree is independent.
- Boosting method such as gradient boosting tree classifier does not need assumption either. It sequentially trains n trees, using residuals between actual y and predicted probability. This is a complicated, high variance, low bias model. Relatively slow to train because we have to wait until the first tree complete before training the second tree. And it requires relatively large data amount, otherwise easy to overfit.

In practice, I would train a logistic regression model as baseline model. Also try random forest and gradient boosting tree to see which one has the best performance. According to my experience, gradient boosting tree usually works better, regarding to the large-scale data. So I would choose gradient boosting tree for this problem.

To find best parameters for gradient boosting tree, I need to split data to train, test dataset.
- Split by timestamp by 90/10
- Important feature and target variable distribution should be close for both data set. If not close, do data extraction again
- Imbalance data: up sample

What I do is to convert a recommendation system problem to one of the following models:
1. A simple distance metric (for example, number of shared friends in friend recommendation)
2. Logistic regression (Best and simplest one)
3. Matrix factorization (Netflix)
4. Neutral network using Triplet loss function (If you have a lot of text and/or image)

一个是关于Deep Learning。大神的帖子里说面试时不推荐用Deep learning的model，这个我同意。但是一定要准备。有时候你能听的出来Interviewer就是想让你说DL‍‌‌‍‌‍‌‍‍‌，不说就挂了。还有时候不得不用，比如Data是图片的情况，那么必须用CNN把Image转成Vector，然后可以用LR什么的。第二个是Distributed training。不管用什么模型，都要想一下怎么用多个Machine做distributed training。模型越简单考官越喜欢问这个。

`4. Train/Hyper parameter tuning: grid search, random search, Bayesian opti‍‌‌‍‌‍‌‍‍‌mization`
Based on my experience, these parameters are quite important: N_estimator, learning rate, max_depth, min_split, regularization
Cross validation 90/10

`5. Model evaluation`
In practice, it’s common that the model performs well during offline evaluation but does not perform well when in production. Therefore, it is important to measure model performance in both on and offline environments.
- Offline evaluation/Offline metrics
1. F1 score
2. AUC
3. A/B testing if interviewer ask for business evaluation

Metrics 这块如果是个ranking problem， 那就不仅是AUC，要用些专用的metric 比如 MAP@K , NDCG
If test AUC >= 0.8, move to next step. If not, could be multiple reason. Overfitting, redo data extraction (train, test data set distribution not close).
Retrain model based on whole data set.
Model Calibration if necessary.

- Online evaluation/Online metrics
Use A/B testing to compare Click Through Rates, watch time, and Conversion rates.
Before model deployment, I would do a A/B test to compare existing policy and using new model as recommendation policy.

Metrics: num of like
Two proportion sample test, z statics, 5% significant level

`Model Deployment`

`Model iteration/enhancement:`
- Batch model: monthly retrain, better solution is to monitor AUC
- Online retrain: using latest hour/daily data to partially update model parameter (add a tree with smaller learning rate)

`Design high level system`
In this stage, we need to think about the system components and how data flows through each of them. The goal of this section is to identify a minimal, viable design to demonstrate a working system. We need to explain why we decided to have these components and what their roles are.
For example, when designing Video Recommendation systems, we would need two separate components: the Video Candidate Generation Service and the Ranking Model Service.

`Scale the design`
In this stage, it’s crucial to understand system bottlenecks and how to address these bottlenecks. You can start by identifying:
Which components are likely to be overloaded?
How can we scale the overloaded components?
Is the system good enough to serve millions of users?
How we would handle some components becoming unavailable, etc.

During inference, one common pattern is to split workloads onto multiple inference servers. We use similar architecture in Load Balancers. It is also sometimes called an Aggregator Service.

For any business-driven system, it’s important to be able to change logic in serving models. For example, in an Ad Prediction system, depending on the type of ad candidates, we will route to a different model to get a score.

Exploration vs. exploitation: Thompson Sampling
We can introduce randomization in the Ranking Service. For example, 2% of requests will get random candidates, and 98% will get sorted candidates from the Ranking Service.

High availability#
Solution 1: Use model-as-a-service, each model will run in Docker containers.
Solution 2: We can use Kubernetes to auto-scale the number of pods.
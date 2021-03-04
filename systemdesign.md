## System Design

> https://www.1point3acres.com/bbs/thread-169343-1-1.html

> https://www.1point3acres.com/bbs/thread-559285-1-1.html

> https://www.1point3acres.com/bbs/thread-683982-1-1.html

> https://eng.uber.com/observability-at-scale/

> https://medium.com%2F@medium.com/@cfpinela/recommender-systems-user-based-and-item-based-collaborative-filtering-5d5f375a127f

>  https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=698113&extra=page%3D1%26filter%3Dsortid%26sortid%3D311%26sortid%3D311

> https://github.com/donnemartin/system-design-primer/blob/master/README-zh-Hans.md

> https://1o24bbs.com/t/topic/4487

## ML System Design

> https://www.educative.io/blog/cracking-machine-learning-interview-system-design

> https://github.com/kuhung/machine-learning-systems-design

> https://github.com/chiphuyen/machine-learning-systems-design

> https://leetcode.com/discuss/interview-question/system-design/566057/machine-learning-system-design-a-framework-for-the-interview-day

> https://www.linkedin.com/pulse/tips-machine-learning-interviews-karthik-mohan/

> https://www.springboard.com/blog/machine-learning-interview-questions/

> https://www.1point3acres.com/bbs/thread-490321-1-1.html

> https://blog.nowcoder.net/n/11b85636258b49b09eb116084d0d67f1

> https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=462348&extra=page%3D1

1. Build a recommendation system that shows relevant products to users
2. Build a visual understanding system for a self-driving car
3. Build a search-ranking system

Performance and Capacity Considerations
- Training time: How much training data and capacity is needed to build our predictor?
- Evaluation time: What are the SLA that we have to meet while serving the model and capacity needs?

Online experimentation
- A/B testing
In an A/B experiment, a webpage or screen is modified to create a second version of it. The original version is known as the control, and the modified version is the variation. From here, we can formulate two hypothesis:
- The null hypothesis
- The alternative hypothesis

1. `Setting up the problem`
- This will help you narrow down the scope of the problem and ensure your system’s requirements closely match the interviewer’s.
- Your conversation should also include questions about performance/speed and capacity considerations of the system.
2. `Defining the metrics of the problem`
- The next step is to carefully choose your system’s performance metrics for both online and offline testing. The metrics you choose will depend on the problem your system is trying to solve.
3. `Architecture discussion`
- The next step is to design your system’s architecture. You need to think about the components of the system and how the data will flow through those components. In this step, you need to be careful to design a model that can scale easily.


Background:
I am a Software Engineer with ~4 years of Machine Learning Engineering (MLE) and Data Scientist (DS) experience working at Fintech Company. Seeing the recent requirements in big tech companies for MLE roles and our confusion around it, I decided to create a framework for solving any ML System Design problem during the interview. Depending on your expertise and interviewers guide, you might want to emphasize on one section vs. the other (e.g. Data Engineering vs Modeling).

I would love your feedback, specially around the scaling. Also if any interviewer from FANG is looking into this, please provide your feedback.

***Overview***
- Clarify Requirements
- How the ML system fits into the overal product backend
- Data Related Activites
- Model Related Activities
- Scaling

***Details***
1. Clarify Requirements
    - What is the goal? Any secondary goal?
        - e.g. for CTR - maximizing the number of clicks is the primary goal. A secondary goal might be the quality of the ads/content
    - Ask questions about the scale of the system - how many users, how much content?
2. How the ML system fits into the overall product backend
    - Think/draw a very simple diagram with input/output line between system backend and ML system
3. Data Related Activites
    - Data Explore - whats the dataset looks like?
    - Understand different features and their relationship with the target
        - Is the data balanced? If not do you need oversampling/undersampling?
        - Is there a missing value (not an issue for tree-based models)
        - Is there an unexpected value for one/more data columns? How do you know if its a typo etc. and decide to ignore?
    - Feature Importance - partial dependency plot, SHAP values, dataschool video (reference)
    - (ML Pipeline: Data Ingestion) Think of Data ingestion services/storage
    - (ML Pipeline: Data Preparation) Feature Engineering - encoding categorical features, embedding generation etc.
    - (ML Pipeline - Data Segregation) Data split - train set, validation set, test set
4. Model Related Activities
    - (ML Pipeline - Model Train and Evaluation) Build a simple model (XGBoost or NN)
        - How to select a model? Assuming its a Neural Network
            1. NLP/Sequence Model
                - start: LSTM with 2 hidden layers
                - see if 3 layers help,
                - improve: check if Attention based model can help
            2. Image Models - (Don't care right now)
            3. Other
                - start: Fully connected NN with 2 hidden layers
                - Improve: problem specific
    - (ML Pipeline - Model Train and Evaluation) What are the different hyperparameters (HPO) in the model that you chose and why?
    - (ML Pipeline - Model Train and Evaluation) Once the simple model is built, do a bias-variance tradeoff, it will give you an idea of overfitting vs underfitting and based on whether overfit or underfit, you need different approaches to make you model better.
    - Draw the ML pipeline (reference #3)
    - Model Debug (reference #1)
    - Model Deployment (reference#3)
    - (ML Pipeline: Performance Monitoring) Metrics
    - AUC, F1, MSE, Accuracy, NDCG for ranking problems etc.
    - When to use which metrics?
5. Scaling

Be in charge and tradeoffs, tradeoffs, tradeoffs...

System Design面试的例子

我在自己面试的过程中 曾经被问到过许多System Design的题目，在这里我挑出几个典型的供大家参考:

公司A: Design URL Shorten Service
公司B: Design SQS(i.e. AWS's queue service)
公司C: Design Uber(frontend app views + backend service)
下面我来详细解释一下每一题的考点:

Design URL Shortening Service

这一题是非常经典的System Design题目，可以考的很浅，也可以考的很深。由于特别适合初学者入门，建议每个想学习System Design的同学都要把这道题的可能的条件和解法过一遍。比如说:

If your website is the top URL shortening service in the world(i.e. handling 70% of world URL shortening traffic) How do you handle it?
How do you handle URL customization?
What if you have very hot URLs? How do you handle it?
How do you track the top N popular URLs?
Design SQS

这一题是非常geeky的一道题，完全深度考察distributed system的各种知识。难度比URL Shortening Service高，原因在于后者已经成为常规考题，变种变来变去就那么几个，所以你死记硬背也能过关。而前者是非常见题 考查点对于没有系统学习过System Design的同学来讲难以琢磨。

同时这道题也是道好题，因为如果你有realtime backend system经验，多半可能会用到queue service。那考察的就是你有没有抽出自己的spare time去理解queue service的具体原理呢?

Design Uber

这是一道极其抽象的题，难易全凭面试官把握。

我被问到的具体情形是，根据手机app上的view transition design出整个后台service群以及互相交互的情况。我当时在白板上一口气写了10+个service的交互图，最后临走前还专门拍照留念，现在想来还是很自豪...

100个人会design出100个Uber，没有谁对谁错，只要能自圆其说就可以。

System Design积木的例子

System design的另一大块是我前面所谈到的“积木”，也就是别人已经搭好的framework或product。

业界的Framework非常之多，你并不需要每个都掌握。只要可以做到知道某方面的几个option，并在需要用到的时候快速ramp up就可以了。下面做一个小分类供大家参考:

In-memory Cache: Guava cache
Standalone Cache: Memcached, Redis
Database: DynamoDB, Cassandra
Queue: ActiveMQ, RabbitMQ, SQS, Kafka
Data Processing: Hadoop, Spark, EMR
Stream Processing: Samza, Storm

***Netflix Recommender System competition***
基本这个问题可以抽象为你有很多user，很多item，一定的历史数据(user买item后的rating)，现在你要决定推荐哪些新的东西给每个user
具体到你被问的问题，可能会有一定的变种，举几个例子
1. Yelp饭馆的推荐，涉及到了geolocation information
2. Facebook Newsfeed推荐，涉及到了不同user之前的networking
3. Ins Story推荐，每条Story是独一无二的并且是有时间性的
4. Spotify音乐推荐，怎么把音乐做个embedding


***Reference:***

Model Debug http://josh-tobin.com/assets/pdf/troubleshooting-deep-neural-networks-01-19.pdf

Data School Video on Feature Selection https://www.youtube.com/watch?v=YaKMeAlHgqQ

ML Pipeline https://towardsdatascience.com/architecting-a-machine-learning-pipeline-a847f094d1c7

***Questions in Interview***

```
1. What size of data are you dealing with?

2. Do you need to be able to serve predictions in real time? 

3. How often do you expect to update your models?

4. How large and experienced is your team — including data scientists, engineers and DevOps?

```
> https://medium.com/acing-ai/machine-learning-system-design-c3a35c7df07d

> https://medium.com/acing-ai/machine-learning-system-design-models-as-a-service-32666eba0e6

> https://www.1point3acres.com/bbs/thread-490321-1-1.html

### FB
We take the two coding interviews first. And then two team match interviews.

Interview Questions

Q: Give me an example of a project where you used data and machine learning.
Q: Given a binary tree, write a function to find if this tree is a search binary tree or not.
Q: Given an array, write a function that returns a samples from the array.  

Given two sets
words ["cat", "bat", "mat" )
ordering = [c,b,a,t]
Return TRUE when the words in words[] are sorted in lexographic order as in ordering[]  

Python example:

```python
word = "cat"
ordering = ['c', 'b', 'a', 't']

def check_ordering(word, ordering):
    """Recursive approach O(len(ordering))"""
    # Base cases
    if not word:
        return True
    # Recursion
    else:
        letter = word.pop(0)
        print(letter)
        for char in ordering:
            if letter == char:
                index = ordering.index(char)
                print(ordering[index:])
                return check_ordering(word, ordering[index:])
        return False

print(check_ordering(list(word), ordering))
```

Given an infinite chessboard, find shortest distance for a knight to move from position A to position B  
given a binary image, count the number of 4-directional connected components.  
Serialize and de-serialize a binary tree  
Given two sparse matrices, how would you compute the dot product? 
Given a DAG, write a function to return the length of the longest path. 
Given a tree, write a function to return the sum of the max-sum path which goes through the root node. 
implement functions of constructing binary tree
One problem is implement a trie tree.
How would you build, train, and deploy a system to detect if multimedia and/or ads contents being posted violate terms or contains offensive materials?
How you test your ML models for production scale?
Variation of the number of islands LC question. You have a House, Well & Tree arranged in a large grid with empty spaces in between to show where you can go. How will you go from house to nearest well without hitting a tree? Assume you can only go up.down/left/right and not diagonally and cannot hit a tree else you backtrack.  

***Interview Questions:***

2. System Design #1
是设计一个location based search。这一轮画风就比较非主流了。我因为看过一些uber/lyft的talk，也准备过geohash的知识，想说开心这都准备到了哈，上来讨论了一下需求，就说先画个架构图吧，本来计划每个component都大概讲一下，再落实到具体的schema design什么的，结果画完以后面试官说其他都不重要，咱直接说geohash怎么用，为什么用geohash，我就解释它为什么可以在密集地区持续split啊，找相邻block是O(1) time啊什么的，然后面试官一直追问geohash的细节，比如为什么每一层是划4x8个格子而不是比如8x8，直接给我问蒙了，这我确实不知道啊！在这个上面纠结到了只剩五分钟，最后只能草草讲一下返回结果怎么排序，就结束了。

个人反思是不是一开始不说geohash比较好？先讲讲even grid为什么不行，再讲讲quad tree这样？另一个失误的点是时间控制的不好，生平第一次面大厂design，有点被牵着鼻子走，其实不知道的细节可以申请先放一放，把大框架讲完了以后再回头抠细节？

3. ML Design
这一轮是一个非常常规的recommendation问题，被推荐的东西（item）不经常变，用户的interest变化比较快。用collaborative filtering或者binary classification都能做，分析了一下两个方案，觉得用classification比较合适，有一些比较明显的优点，面试官也同意，就开始讨论metrics，feature engineering，不同算法的优缺点，然后就是些model serving上面的工程问题，比如怎么monitor，online表现明显有问题的时候怎么debug，因为工作中都遇到过，感觉答得也不错，面试官全程I like it, fantastic。唯一没有想到的是可以用好友graph来扩展feature解决冷启动问题，这个是面试官提醒了以后才想到的。

这一轮就和上一轮画风相反。全程感觉很顺，但是还是给了个borderline，求大佬们指点一下，这是挂在哪了？

4. System Design #2
这一轮没有计入面试结果，但也挺有意思的。和第一轮Design一样，不按套路出牌，我把框架画完之后面试官说，这个设计很好，但是如果不用Cassandra或者任何storage layer你要怎么设计，Redis也不用的话要怎么办，message queue也不用的话要怎么做，而且不是明着说的，就是说 “我们想尽量减少server间的networking”，反复沟通了很久，最后才明白他的意图原来就是不用任何轮子设计一个啥都有的monolith。明白了这个以后进展就很快，最终结果他也非常满意，后半程明显语气快乐得多（其实我想说这种设计挺糟糕的，拣了芝麻丢了西瓜）。。。

 ML design。abusive comments
第四轮：design music playlist to display top music
第五轮：design friends recommendation system


 这段时间面试了脸书的码工职位，整理了一下最近地里和朋友那里打听出来的系统设计题目，分享出来换大米，换大米~~~
- Push notification
- Search status，或者叫twitter search，一般要求real time，仅限text post。可以参考 https://blog.twitter.com/enginee ... rch-experience.html
- Aggregation system，一般会考虑到fast和slow两种cases
- Design Yelp，经典题目，quadtree或者grid，geohash我自己没多看，觉着重点不在这里
- Translation syste，两种思路，一个是google translate这种，你可以assume已经有一个现成可用的translation service，然后你要设计一个系统满足三高。另外一个思路可以借鉴一下airbnb的翻译系统 https://medium.com/airbnb-engine ... atform-45cf0104b63c
- News feed
- Design Netflix
- i18n，参见上面说的airbnb的翻译系统
- Collaborative doc editing，就是设计个google doc
- Subscription system，比如说youtube的subscription
- Hashtag trend，类似于topK，YouTube上有个视频讲的挺好 https://www.youtube.com/watch?v=kx-XDoPjoHw&t=53s，另外我也很推荐这个哥们儿的channel
- Live commenting system，个人感觉这个地方偏重考database
- KV store，经典题，主要靠怎么满足三高
- Design Facebook Messenge，要求能做到group chat
- Design Instagram
- Proximity server backend，参考design Yelp
- Design load balancer，要求包含balance servers的workload的功能
- Ad click counter，参考前面的hashtag trend，只是有相似之处并不完全相同，考虑slow和fast两种实现可能都需要
- Web crawler，看到大家提到的都是需要跑在botnet上，我自己能想到的就是中控server负责存储、判重，还有负责给bot们发命令，命令里面包括url。Bots们接收命令，下载网页，解析文字和urls，然后把网页文字内容和URLs发回给中控server。另外中控server要能做到三高。
- Design typeahead suggestions，也就是autocomplete，经典题
- Design privacy settings at Facebook，几个privacy类型，比如说public可见，只能朋友看，只能朋友和朋友的朋友看，只能自己看

我个人的经验是45~60分钟不可能回答到完美，只能尽量做到战前做好准备工作，正所谓凡事预则立不预则废，尽人事听天命而已。实战中需要注意的一点是把握好时间和节奏，如果一个面试官不断的打断你打乱你的节奏，只能尽力往回带了不然会漏掉该讲出来的东西，总之不要给这种面试官机会质疑你不会这个不知道那个。
简而言之，自己盯着点时间，别说的自己都搂不住了用光了时间：
- clarification: 5 min
- high level: 15 min，给出一个大体结构，然后做data volume的估计，然后从最需要改进的地方开始deep dive
- deep dive：剩下的时间就全是这一块儿了，包括你自己的深入解释和回答interviewer的问题。
最后这一部分interviewer问的问题一定要说清楚，觉着有不懂的不要瞎说，毕竟是模拟一个工作环境。他不问的情况下你要知道下一步该往哪里走，多多交流总是没错的，随时问问牛逼你觉着我这样做一下怎么样啊？我如果下一步专注这部分你开心不？到现在为止有啥问题或者concern没有啊？这些问题也随时问出来显得我们真的很想让interviewer加入讨论，总之interviewer爽了你才会爽。

看到新题再补充吧，另外我买了Alex Xu出的system design Interview，相当入门非常好读。

最后还是求加米，一亩三分地是个好地方，但是穷就啥也干不了。怎么加米呢？轻点帖子下方的“评分”按钮，然后输入你想打赏的米数，评分打赏的大米并不会消耗自己的大米数，所以请放开了打赏 O(∩_∩)O哈哈~




补充内容 (2021-2-23 03:24):
这里还有一篇帖子加两个youtube视频很好的总结了几个热门系统设计题： https://medium.com/the-interview ... stions-ec976c6cdaa9
 这段时间面试了脸书的码工职位，整理了一下最近地里和朋友那里打听出来的系统设计题目，分享出来换大米，换大米~~~
- Push notification
- Search status，或者叫twitter search，一般要求real time，仅限text post。可以参考 https://blog.twitter.com/enginee ... rch-experience.html
- Aggregation system，一般会考虑到fast和slow两种cases
- Design Yelp，经典题目，quadtree或者grid，geohash我自己没多看，觉着重点不在这里
- Translation syste，两种思路，一个是google translate这种，你可以assume已经有一个现成可用的translation service，然后你要设计一个系统满足三高。另外一个思路可以借鉴一下airbnb的翻译系统 https://medium.com/airbnb-engine ... atform-45cf0104b63c
- News feed
- Design Netflix
- i18n，参见上面说的airbnb的翻译系统
- Collaborative doc editing，就是设计个google doc
- Subscription system，比如说youtube的subscription
- Hashtag trend，类似于topK，YouTube上有个视频讲的挺好 https://www.youtube.com/watch?v=kx-XDoPjoHw&t=53s，另外我也很推荐这个哥们儿的channel
- Live commenting system，个人感觉这个地方偏重考database
- KV store，经典题，主要靠怎么满足三高
- Design Facebook Messenge，要求能做到group chat
- Design Instagram
- Proximity server backend，参考design Yelp
- Design load balancer，要求包含balance servers的workload的功能
- Ad click counter，参考前面的hashtag trend，只是有相似之处并不完全相同，考虑slow和fast两种实现可能都需要
- Web crawler，看到大家提到的都是需要跑在botnet上，我自己能想到的就是中控server负责存储、判重，还有负责给bot们发命令，命令里面包括url。Bots们接收命令，下载网页，解析文字和urls，然后把网页文字内容和URLs发回给中控server。另外中控server要能做到三高。
- Design typeahead suggestions，也就是autocomplete，经典题
- Design privacy settings at Facebook，几个privacy类型，比如说public可见，只能朋友看，只能朋友和朋友的朋友看，只能自己看

我个人的经验是45~60分钟不可能回答到完美，只能尽量做到战前做好准备工作，正所谓凡事预则立不预则废，尽人事听天命而已。实战中需要注意的一点是把握好时间和节奏，如果一个面试官不断的打断你打乱你的节奏，只能尽力往回带了不然会漏掉该讲出来的东西，总之不要给这种面试官机会质疑你不会这个不知道那个。
简而言之，自己盯着点时间，别说的自己都搂不住了用光了时间：
- clarification: 5 min
- high level: 15 min，给出一个大体结构，然后做data volume的估计，然后从最需要改进的地方开始deep dive
- deep dive：剩下的时间就全是这一块儿了，包括你自己的深入解释和回答interviewer的问题。
最后这一部分interviewer问的问题一定要说清楚，觉着有不懂的不要瞎说，毕竟是模拟一个工作环境。他不问的情况下你要知道下一步该往哪里走，多多交流总是没错的，随时问问牛逼你觉着我这样做一下怎么样啊？我如果下一步专注这部分你开心不？到现在为止有啥问题或者concern没有啊？这些问题也随时问出来显得我们真的很想让interviewer加入讨论，总之interviewer爽了你才会爽。

看到新题再补充吧，另外我买了Alex Xu出的system design Interview，相当入门非常好读。

这里还有一篇帖子加两个youtube视频很好的总结了几个热门系统设计题： https://medium.com/the-interview ... stions-ec976c6cdaa9

### Google
Interview Questions

Given two strings, A and B, of the same length n, find whether it is possible to cut both strings at a common point such that the first part of A and the second part of B form a palindrome.
have two pointers, first on A and second on end of B. move the pointer l and r (l++, r--) until both values are same( A[l] == B[r]) or l == r. if at any point both are not same just switch the pointer r from B to A and continue. If then it breaks then it is not a palindrome.

You have 52 playing cards (26 red, 26 black). You draw cards one by one. A red card pays you a dollar. A black one fines you a dollar. You can stop any time you want. Cards are not returned to the deck after being drawn. What is the expected payoff following this optimal rule? for this, u need to find what is the optimal stopping rule in terms of maximizing expected payoff.
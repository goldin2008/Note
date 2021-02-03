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

### Google
Interview Questions

Given two strings, A and B, of the same length n, find whether it is possible to cut both strings at a common point such that the first part of A and the second part of B form a palindrome.
have two pointers, first on A and second on end of B. move the pointer l and r (l++, r--) until both values are same( A[l] == B[r]) or l == r. if at any point both are not same just switch the pointer r from B to A and continue. If then it breaks then it is not a palindrome.

You have 52 playing cards (26 red, 26 black). You draw cards one by one. A red card pays you a dollar. A black one fines you a dollar. You can stop any time you want. Cards are not returned to the deck after being drawn. What is the expected payoff following this optimal rule? for this, u need to find what is the optimal stopping rule in terms of maximizing expected payoff.
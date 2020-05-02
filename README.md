# Presentation and Note 

AWS Account:
```
udacitystudylei@gmail.com
nigama7@gmail.com
```


>Project
```
1. Install env
2. Install packages
3. Create requirements.txt
4. 
```

>Project Command: 
```
python3 -m venv env
source env/bin/activate
pip list
pip freeze > requirements.txt
cat requirements.txt
```




>Udacity Data Streaming: 
1) OPT: 
``` 
List all topics
/usr/bin/kafka-topics --list --zookeeper localhost:2181

/usr/bin/kafka-console-consumer --bootstrap-server localhost:9092 --partition 0 --topic org.chicago.stations --from-beginning
org.chicago.cta.station.arrivals
org.chicago.cta.weather.v1
org.chicago.stations

/usr/bin/kafka-console-consumer --bootstrap-server localhost:9092 --partition 0 --topic org.chicago.cta.weather.v1 --from-beginning


Show content in the topic
/usr/bin/kafka-console-consumer --bootstrap-server localhost:9092 --partition 0 --topic org.chicago.cta.stations.table.v1 --from-beginning

Weather.rest_proxy_url}/topics/weather

Running the Simulation
1. cd producers
2. python simulation.py

To run the Faust Stream Processing Application:
1. cd consumers
2. faust -A faust_stream worker -l info

To run the KSQL Creation Script:
1. cd consumers
2. python ksql.py

To run the consumer: (NOTE: Do not run the consumer until you have reached Step 6!)
1. cd consumers
2. python server.py

``` 
2) SF Crime: 

``` 
1./usr/bin/zookeeper-server-start config/zookeeper.properties
2./usr/bin/kafka-server-start config/server.properties
3.python kafka_server.py
4.kafka-console-consumer --bootstrap-server localhost:9092 --topic com.udacity.project.sfcrimes --from-beginning

/usr/bin/kafka-console-consumer --bootstrap-server localhost:9092 --topic org.chicago.cta.stations.table.v1 --from-beginning

root@7aafb549a58e:/home/workspace/consumers# kill -15 1625
root@7aafb549a58e:/home/workspace/consumers# pgrep -lf python
``` 

>ML presentation 

***Intro: 
AI is changing the way we work and live. Whether you want to know what's behind the buzzwords or whether you want to perhaps use AI yourself either in a personal context or in a corporation, Today's talk will give you a realistic view of what AI really is.

***Relationship between ML, DL and AI:
You might have heard terminology from AI, such as machine learning or neural networks or deep learning. What do these terms mean?
If we were to draw a Venn diagram showing how all these concepts put together, this is what it may look like. AI is this huge set of tools for making computers behave intelligently. Off AI, the biggest subset is prairie tools from machine learning, but AI does have other tools than machine learning, such as some of buzzwords you might also hear in the media, graphical models, planning, knowledge graph, and so on. (unsupervised learning, reinforcement learning) The part of machine learning that's most important these days is neural networks or deep learning, which is a very powerful set of tools for carrying out supervised learning, which is also called A to B mappings, as well as some other things. But there are also other machine learning tools that are not just deep learning tools, like linear regression, logistic regression, decision tree and so on.

***Machine Learning:
machine learning is the field of study that gives computers the ability to learn without being explicitly programmed. This is a definition by Arthur Samuel many decades ago. Arthur Samuel was one of the pioneers of machine learning, who was famous for building a checkers playing program.

***Deep Learning:
You have also heard of deep learning. So, what is deep learning? The terms deep learning and neural network are used almost interchangeably in AI. And even though they're great for machine learning, there's also been a bit of hype and mystique about them. Let’s demystify deep learning, so that you have a sense of what deep learning and neural networks really are. 
Let's say you want to predict housing prices, you want to price houses. So, you will have an input that tells you the size of the house, number of bedrooms, and number of bathrooms. Maybe location and whether it's newly renovated. One of the most effective ways to price houses, given this input A, would be to feed it to this thing here in order to have it output the price. This big thing in the middle is called a neural network, and sometimes we also called an artificial neural network. That's to distinguish it from the neural network in your brain. The human brain is made up of neurons. So, when we say artificial neural network, that's just to emphasize that this is not the biological brain, but this is a piece of software. What a neural network does is takes this input A, which is all of these three things, and then output B, which is the estimated price of the house. 
But all of human cognition is made up of neurons in your brain passing electrical impulses, passing little messages each other. When we draw a picture of an artificial neural network, there's a very loose analogy to the brain. These little circles are called artificial neurons, or just neurons for short. That also passes neurons to each other. This big artificial neural network is just a big mathematical equation that tells it given the inputs A, how do you compute the price B. 

The key takeaways are that a neural network is a very effective technique for learning A to B or input-output mappings. As I said early, Today, the terms neural network and deep learning are used almost interchangeably, they mean essentially the same thing. Many decades ago, this type of software was called a neural network. But in recent years, we found that deep learning was just a much better sounding brand, and so that for better or worse is a term that's been taken off recently. So, what do neural networks or artificial neural networks have to do with the brain? Unfortunately, it turns out almost nothing. Neural networks were originally inspired by the brain, but the details of how they work are almost completely unrelated to how biological brains work.

One of the wonderful things about using neural networks is that to train a neural network, all you have to do is give it the input A and the output B. And it figures out all of the things in the middle by itself. So to build a neural network, what you would do is feed it lots of data, or the input A, and have a neural network that just looks like this. And then you have to give it data with the price B as well. And it's the software's job to figure out what these neurons should be computing, so that it can completely automatically learn the most accurate possible function mapping from the input A to the output B. And it turns out that if you give this enough data and train a neural network that is big enough, this can do an incredible good job mapping from inputs A to outputs B. So that's a neural network, is a group of artificial neurons each of which computes a relatively simple function. But when you stack enough of them together like Lego bricks, they can compute incredibly complicated functions that give you very accurate mappings from the input A to the output B.

***Limitation
But AI has other limitations, as well. One of the limitations of AI is that explainability is hard and many high-performing AI systems are black boxes. Meaning that it works very well but the AI doesn't know how to explain why it does what it does. Now, to be fair, humans are also not very good at explaining how we make decisions ourselves. 

***Techniques: 
There are a lot of AI and machine learning techniques today. And while supervised learning, that is learning A to B mappings, is the most valuable one, at least economically today, there are many other techniques that are worth knowing about. 
== Supervised Learning ==
The rise of AI has been largely driven by one tool in AI called machine learning. The most commonly used type of machine learning is a type of AI that learns A to B, or input to output mappings. This is called supervised learning. Let's see some examples. If the input A is an email and the output B one is email spam or not, zero one. Then this is the core piece of AI used to build a spam filter. Or if the input is an audio clip, and the AI's job is to output the text transcript, then this is speech recognition. More examples, if you want to input English and have it output a different language, Chinese, Spanish, something else, then this is machine translation. Or if you want to build a self-driving car, one of the key pieces of AI is in the AI that takes as input an image, and some information from their radar, or from other sensors, and output the position of other cars, so your self-driving car can avoid the other cars. This set of AI called supervised learning, just learns input to output, or A to B mappings. On one hand, input to output, A to B it seems quite limiting. But when you find a right application scenario, this can be incredibly valuable. Now, the idea of supervised learning has been around for many decades. But it's really taken off in the last few years, due to the rise of neural networks and deep learning.
== Unsupervised Learning ==
The best known example of unsupervised learning is clustering, here's an example. A clustering algorithm looks at data like this, and automatically groups the data into two  or more clusters, and is commonly used for market segmentation. And this can help you market differently to these market segments. The reason this is called unsupervised learning is the following. Whereas supervised learning algorithms run an A to B mapping, and you have to tell the algorithm what is the output B that you want, an unsupervised learning algorithm doesn't tell the AI system exactly what it wants. Instead it gives the AI system a bunch of data such as this customer data, and it tells the AI to find something interesting in the data, find something meaningful in the data. Instead, it just tries to find what are the different market segments without being told in advance what they are. So unsupervised learning algorithms, given data without any specific design output labels, without the target label B, can automatically find something interesting about the data. 
Even though supervised learning is an incredibly valuable and powerful technique, one of the criticisms of supervised learning is that it just needs so much labeled data. Which is why AI researchers hold a lot of hope out for unsupervised learning as way, maybe in the future, for AI to learn much more effectively in a more human like way, and more biological like way for much less labeled data.  Now, we have pretty much no idea how the biological brain works, and so to realize this vision, we'll take major breakthroughs in AI than none of us know yet today how to realize.
== Reinforcement Learning ==
You may also have heard of a technique called reinforcement learning. So, what is reinforcement learning?  Let me illustrate with another example. I think of reinforcement learning as similar to how you might train a pet dog to behave. So, how do you train a dog to behave itself? Well, we let the dog do whatever it wanted to do, and then whenever it behaved well we would praise it. You go, good dog, and whenever it does something bad you would go, bad dog. And overtime it learns to do more of the, good dog, things, and fear of the bad dog things. This means that whenever it's doing well, you give it a large positive number to give it a large positive reward. And whenever it's doing really bad job, you send it a negative number to give it a negative reward. And it's the AI's job to the automatically learn to behave so  as to maximize the rewards. So, good dog responds to giving a positive number, and bad dog, corresponds to you giving a negative number. 
You might have heard of AlphaGo, which did a very good job of playing Chess using reinforcement learning. And reinforcement learning has also been very effective at playing video games. One of the weaknesses of reinforcement learning algorithms is that they can require a huge amount of data. and get a huge amount of data to learn how to behave better.

***How to choose an AI project: 
The steps might be involved in “technical diligence” process:
ensuring that the envisioned AI technology is feasible. 
Defining an engineering timeline 
Making sure you can get enough data for this project 
Making sure that the ML system can meet the desired performance

“business diligence”:
Business diligence is the process of ensuring that the AI technology, if it is built, is valuable for your business.

What we would like to do is try to select projects that are at the intersection of these two sets, so you select projects hopefully that are both feasible for ML, and valuable for our business. ML experts will tend to have a good sense of what is and what isn't in the set on the left. And domain experts, will have the best sense of what is actually valuable for our business. When brainstorming projects that ML can do and are valuable for our business, we can bring together a team comprising both people knowledgeable of AI, as well as experts in your business area. By understanding the main pain points in the business and feasible technology we can build, that will allow us to select the most fruitful project for automation in the near term.

***Workflow of a Machine Learning Project: 
Machine learning is an “iterative” process, meaning that an AI team often has to try many ideas before coming up with something that’s good enough, rather than have the first thing they try work. Say you want to use Machine Learning to help your sales team with automatic lead sorting. I.e., Input A (a sales prospect) and output B (whether your sales team should prioritize them). The 3 steps of the workflow, in scrambled order, are: (i) Deploy a trained model and get data back from users (ii) Collect data with both A and B (iii) Train a machine learning system to input A and output B.
Machine learning algorithms can learn input to output mappings. So, how do you build a machine learning project? Let’s take a look what is the workflow of machine learning projects. I'm going to use speech recognition as a running example. So, some of you may have an Amazon Echo or Google Home or Apple Siri device in your homes. So, how do you build a speech recognition system that can recognize when you say, "Alexa," or "Hey, Google," or "Hey, Siri" ? Let's go through the key steps of a machine learning project. Just for simplicity, I'm going to use Amazon Echo or detecting the Alexa keywords as this running example. If you want to build an AI system or build a machine learning system to figure out when a user has said the word “Alexa”,
the First Step is to collect data. So, that means, you would go around and get some people to say the word "Alexa" for you and you record the audio of that.  You'll also get a bunch of people to say other words like "Hello," or say lots of other words and record the audio of that as well. Having collected a lot of audio data, a lot of these audio clips of people saying either "Alexa" or saying other things,
Step Two is to then train the model. This means you will use a machine learning algorithm to learn an input to output mapping, where the input A would be an audio clip. In the case of the first audio clip above, hopefully,  it will tell you that the user said "Alexa," and in the case of audio clip two,  shown on the right, hopefully, the system will learn to recognize that the user has said "Hello." Whenever an AI team starts to train the model, meaning to learn the input-output mapping, what happens, pretty much every time,  is the first attempt doesn't work well. So invariably, the team will need to try many times or in AI, we call this iterate many times. You have to iterate many times until, hopefully, the model looks like is good enough.
The Third Step is to then actually deploy the model. 


***Technical tools for AI teams and Resources:
When you work with AI teams, you may hear them refer to the tools that they're using to build these AI systems. In this video, I want to share with you some details and names of the most commonly used AI tools, so that you'd be able to better understand what these AI engineers are doing.
We're fortunate that the AI world today is very open, and many teams will openly share ideas with each other. There are great machine learning open source frameworks that many teams will use to build their systems. So, if you hear of any of these: TensorFlow, PyTorch, Keras, MXNet, CNTK, Caffe,  PaddlePaddle, Scikit-learn, R or Weka, all of these are open source machine  learning frameworks that help AI teams be much more efficient in terms of writing software. 
Along with AI technology breakthroughs are also publish freely on the Internet on this website called Arxiv. Spelled like this. I hope that other academic communities also freely share their research since I've seen firsthand how much this accelerates progress in the whole field of AI.  
Finally, many teams will also share their code freely on the Internet, most commonly on a website called GitHub. By using appropriately licensed open-source software, many teams can get going much  faster than if they had to build everything from scratch. Finally, you might hear about Cloud versus On-prem deployments. Cloud deployments refer to if you rent  compute servers such as from Amazon's AWS, or Microsoft's Azure, or Google's GCP in order to use someone else's service to do your computation. Whereas, an On-prem deployment means buying your own compute servers and running the service locally in your own company. A lot of the world is moving to Cloud deployments. Whether you search online you find many articles talking about the pros and cons of Cloud versus On-prem deployments.





https://www.sumologic.com/blog/machine-learning-deep-learning/

1. Intro: AI is changing the way we work and live and this nontechnical 
presentation will teach you how to navigate the rise of AI. Whether you want to 
know what's behind the buzzwords or whether you want to perhaps use AI yourself 
either in a personal context or in a corporation, this course will teach you 
how. Today's talk will give you a realistic view of what AI really is. 

There is a lot of excitement but also a lot of unnecessary hype about AI. 
Almost all the progress we are seeing in the AI today is artificial narrow 
intelligence. These are AIs that do one thing such as a smart speaker or a self-
driving car, etc. However, AI also refers to a second concept of AGI or 
artificial general intelligence. That is the goal to build AI. They can do 
anything a human can do or maybe even be superintelligence and do even more 
things than any human can. I'm seeing tons of progress in ANI, artificial 
narrow intelligence and almost no progress to what AGI or artificial general 
intelligence. Both of these are worthy goals and unfortunately the rapid 
progress in ANI which is incredibly valuable, that has caused people to 
conclude that there's a lot of progress in AI, which is true. But that has 
caused people to falsely think that there might be a lot of progress in AGI as 
well which is leading to some irrational fears about evil clever robots coming 
over to take over humanity anytime now. I think AGI is an exciting goal for 
researchers to work on, but it'll take most for technological breakthroughs 
before we get there and it may be decades or hundreds of years or even 
thousands of years away. Given how far away AGI is, I think there is no need to 
unduly worry about it. 

In this talk, I will introdue what ANI can do and how to apply them to some 
problems. Later in this talk you'll also see some case studies of how ANI can 
be used to build really valuable applications such as smart speakers and self-
driving cars. You may have heard of machine learning and the next video will 
teach you what is machine learning. You also learn what is data and what types 
of data are valuable but also what does the data are not valuable. You learn 
what it is that makes a company an AI company or an AI first company so that 
perhaps you can start thinking if there are ways to improve your company or 
other organizations ability to use AI and importantly, you also learned this 
week what machine learning can and cannot do. 

In our society, newspapers as well as research papers tend to talk only about 
the success stories of machine learning and AI and we hardly ever see any 
failure stories because they just aren't as interesting to report on. But for 
you to have a realistic view of what AI and what machine learning can or cannot 
do, I think is important that you see examples of both so that you can make 
more accurate judgements about what you may and maybe should not try to use 
these technologies for. 

Finally, a lot of the recent rise of, machine learning has been driven through 
the rise of Deep Learning. Sometimes also called Neural Networks. You can also 
see an intuitive explanation of deep learning so that you will better 
understand what they can do particularly for a set of narrow ANI tasks. Now we 
have a sense of AI technologies and what they can and cannot do. Next we'll see 
how these AI technologies can be used to build valuable projects. We also need 
to know what we should do to make sure we select projects that are technically 
feasible as well as valuable to our business. After learning what it takes to 
build AI projects, in the third week you'll learn how to build AI in your 
company. In particular, if you want to take a few steps toward making your 
company good at AI, you see the AI transformation playbook and learn how to 
build AI teams and also built complex AI products. Now, one of the major 
technologies driving the recent rise of AI is Machine Learning. But what is 
Machine Learning? Let's take a look in the next video. 

2. What is Machine Learning: 

The rise of AI has been largely driven by one tool in AI called machine 
learning. The most commonly used type of machine learning is a type of AI that 
learns A to B, or input to output mappings. This is called supervised learning. 
Let's see some examples. If the input A is an email and the output B one is 
email spam or not, zero one. Then this is the core piece of AI used to build a 
spam filter. Or if the input is an audio clip, and the AI's job is to output 
the text transcript, then this is speech recognition. More examples, if you 
want to input English and have it output a different language, Chinese, 
Spanish, something else, then this is machine translation. I'll define these 
terms more precise in later video, so don't worry too much about what it means 
for now. The most important idea in AI has been machine learning, has basically 
supervised learning, which means A to B, or input to output mappings. 

Or if you want to build a self-driving car, one of the key pieces of AI is in 
the AI that takes as input an image, and some information from their radar, or 
from other sensors, and output the position of other cars, so your self-driving 
car can avoid the other cars. 

This set of AI called supervised learning, just learns input to output, or A to 
B mappings. On one hand, input to output, A to B it seems quite limiting. But 
when you find a right application scenario, this can be incredibly valuable. 
Now, the idea of supervised learning has been around for many decades. But it's 
really taken off in the last few years. 

AI has really taken off recently due to the rise of neural networks and deep 
learning. I'll define these terms more precise in later video, so don't worry 
too much about what it means for now. 

with neural networks and deep learning, what we saw was that, if you train a 
small neural network, then the performance looks like this, where as you feed 
them more data, performance keeps getting better for much longer. If you train 
a even slightly larger neural network, say medium-sized neural net, then the 
performance may look like that. If you train a very large neural network, then 
the performance just keeps on getting better and better. For applications like 
speech recognition, online advertising, building self-driving car, where having 
a high-performance, highly accurate, say speech recognition system is 
important, enable these AI systems get much better, and make speech recognition 
products much more acceptable to users, much more valuable to companies and to 
users. Now, a few couple of implications of this figure. If you want the best 
possible levels of performance, then you need two things: One is, it really 
helps to have a lot of data. So that's why sometimes you hear about big data. 
Having more data almost always helps. The second thing is, you want to be able 
to train a very large neural network. So, the rise of fast computers, including 
Moore's law, but also the rise of specialized processors such as graphics 
processing units or GPUs, make many many other companies to be able to train 
large neural nets on a large enough amount of data in order to get very good 
performance and drive business value. The most important idea in AI has been 
machine learning, has basically supervised learning, which means A to B, or 
input to output mappings. What enables it to work really well is data. 

We need to know what data we have and how to feed this data into AI system. 

3. Data: It's up to you to decide what is A and what is B, and how to choose 
these definitions of A and B to make it valuable for your business. But how do 
you get data? How do you acquire data? Well, one way to get data is manual 
labeling. For example, you might collect a set of pictures like these over 
here, and then you might either yourself or have someone else go through these 
pictures and label each of them. Another way to get a dataset is from observing 
user behaviors or other types of behaviors. So, for example, let's say you run 
a website that sells things online. So, an e-commerce or an electronic commerce 
website where you offer things to users at different prices, and you can just 
observe if they buy your product or not. So, just through the act of either 
buying or not buying your product, you may be able to collected a data set like 
this, where you can store the user ID, the time the user visited your website, 
the price you offer the product to the users as well as whether or not they 
purchased it. So, just by using your website, users can generate this data from 
you. The third and very common way of acquiring data is to download it from a 
website or to get it from a partner. Finally, if you're working with a partner, 
say you're working with a factory, then they may already have collected a big 
dataset, machines, and temperatures, and pressure into the machines fail not 
that they could give to you. once you've started collecting some data, go ahead 
and start showing it or feeding it to an AI team. Because often, the AI team 
can give feedback to your IT team on what types of data to collect and what 
types of IT infrastructure to keep on building. For example, maybe an AI team 
can look at your factory data and say, "Hey. You know what? If you can collect 
data from this big manufacturing machine, not just once every ten minutes, but 
instead once every one minute, then we could do a much better job building a 
preventative maintenance systems for you." So, there's often this interplay of 
this back and forth between IT and AI teams, and my advise is usually try to 
get feedback from AI earlier, because it can help you guide the development of 
your IT infrastructure. More data is usually better than less data, but I 
wouldn't take it for granted that just because you have many terabytes or 
gigabytes of data, that an AI team can actually make that valuable. 

4. Terminology: You might have heard terminology from AI, such as machine 
learning or data science or neural networks or deep learning. What do these 
terms mean? The boundaries between these two terms, machine learning and data 
science are actually little bit buzzy, and these terms are not used 
consistently even in industry today. 

machine learning is the field of study that gives computers the ability to 
learn without being explicitly programmed. This is a definition by Arthur 
Samuel many decades ago. Arthur Samuel was one of the pioneers of machine 
learning, who was famous for building a checkers playing program. So, a machine 
learning project will often results in a piece of software that runs, that 
outputs B given A. In contrast, data science is the size of extracting 
knowledge and insights from data. So, the output of a data science project is 
often a slide deck, the PowerPoint presentation that summarizes conclusions for 
executives to take business actions or that summarizes conclusions for a 
product team to decide how to improve a website. Let me give an example of 
machine learning versus data science in the online advertising industry. Today, 
to launch our platforms, all have a piece of AI that quickly tells them what's 
the ad you are most likely to click on. So, that's a machine learning system. 
This turns out to be incredibly lucrative AI system to inputs enrich about you 
and about the ad and outputs where you click on this or not. These systems are 
running 24-7. These are machine learning systems that drive our gravity for 
these companies, such as a piece of software that runs. In contrast, I have 
also done data science projects in the online advertising industry. If 
analyzing data tells you, for example, that the travel industry is not buying a 
lot of ads, but if you send more salespeople to sell ads to travel companies, 
you could convince them to use more advertising, then that would be an example 
of a data science project and the data science conclusion the results and the 
executives deciding to ask a sales team to spend more time reaching out to the 
travel industry. So, even in one company, you may have different machine 
learning and data science projects, both of which can be incredibly valuable. 

You have also heard of deep learning. So, what is deep learning? Let's say you 
want to predict housing prices, you want to price houses. So, you will have an 
input that tells you the size of the house, number of bedrooms, number of 
bathrooms and whether it's newly renovated. One of the most effective ways to 
price houses, given this input A would be to feed it to this thing here in 
order to have it output the price. This big thing in the middle is called a 
neural network, and sometimes we also called an artificial neural network. 
That's to distinguish it from the neural network that is in your brain. So, the 
human brain is made up of neurons. So, when we say artificial neural network, 
that's just to emphasize that this is not the biological brain, but this is a 
piece of software. What a neural network does, or an artificial neural network 
does is takes this input A, which is all of these four things, and then output 
B, which is the estimated price of the house. But all of human cognition is 
made up of neurons in your brain passing electrical impulses, passing little 
messages each other. When we draw a picture of an artificial neural network, 
there's a very loose analogy to the brain. These little circles are called 
artificial neurons, or just neurons for short. That also passes neurons to each 
other. This big artificial neural network is just a big mathematical equation 
that tells it given the inputs A, how do you compute the price B. In case it 
seems like there a lot of details here, don't worry about it. We'll talk more 
about these details later. But the key takeaways are that a neural network is a 
very effective technique for learning A to B or input-output mappings. Today, 
the terms neural network and deep learning are used almost interchangeably, 
they mean essentially the same thing. Many decades ago, this type of software 
was called a neural network. But in recent years, we found that deep learning 
was just a much better sounding brand, and so that for better or worse is a 
term that's been taken off recently. So, what do neural networks or artificial 
neural networks have to do with the brain? It turns out almost nothing. Neural 
networks were originally inspired by the brain, but the details of how they 
work are almost completely unrelated to how biological brains work. So, I 
choose very courses today about making any analogies between artificial neural 
networks and the biological brain, even though there was some loose inspiration 
there. 

You might also hear in the media other buzzwords like unsupervised learning, 
reinforcement learning, graphical models, planning, knowledge graph, and so on. 
You don't need to know what all of these other terms mean, but these are just 
other tools to getting AI systems to make computers act intelligently. 

But the most important tools that I hope you know about are machine learning 
and data science as well as deep learning and neural networks, which are a very 
powerful way to do machine learning, and sometimes data science. If we were to 
draw a Venn diagram showing how all these concepts put together, this is what 
it may look like. AI is this huge set of tools for making computers behave 
intelligently. Off AI, the biggest subset is prairie tools from machine 
learning, but AI does have other tools than machine learning, such as some of 
these buzzwords, are listed at the bottom. The part of machine learning that's 
most important these days is neural networks or deep learning, which is a very 
powerful set of tools for carrying out supervised learning or A to B mappings 
as well as some other things. But there are also other machine learning tools 
that are not just deep learning tools. So, how does data science fit into this 
picture? There is inconsistency in how the terminology is used. Some people 
will tell you data science is a subset of AI. Some people will tell you AI is a 
subset of data science. So, it depends on who you ask. But I would say that 
data science is maybe a cross-cutting subset of all of these tools that uses 
many tools from AI machine learning and deep learning, but has some other 
separate tools as well that solves a very set of important problems in driving 
business insights. I hope this gives you a sense of the most common and 
important terminology using AI, and you can start thinking about how these 
things might apply to your company. 



5. What makes an AI company: But eventually, you then need to do step two which 
is the building in house AI team and provide broad AI training, not just to the 
engineers but also to the managers, division leaders and executives and how 
they think about AI. After doing this or as you're doing this, you have a 
better sense of what AI is and then is important for many companies to develop 
an AI strategy. AI transformation playbook which I'll go into much greater 
detail on in a later week as a road-map If you're interested, there is also 
published online an AI transformation playbook that goes into these five steps 
in greater detail for you see more of these in the later weeks as well. 

6. What machine learning can and cannot do: Now, one of the challenges of doing 
AI projects such as the pilot projects in step one is understanding what AI can 
and cannot do. I want to show you and give you some examples of what AI can and 
cannot do, to help you better select projects AI that there may be effective 
for your company. I hope to help you develop intuition about what AI can and 
cannot do. In practice, before I commit to a specific AI project, I'll usually 
have either myself or engineers do technical diligence on the project to make 
sure that it is feasible. This means: looking at the data, look at the input, 
and output A and B, and just thinking through if this is something AI can 
really do. One of the challenges is that the media, as well as the academic 
literature, tends to only report on positive results or success stories using 
AI, and we see a string of success stories and no failure stories, people 
sometimes think AI can do everything. Unfortunately, that's just not true. what 
I want to do in this and in the next video, is to show you a few examples of 
what today's AI technology can do, but also what it cannot do, and I hope that 
this will help you, hone your intuition about what might be more or less 
promising projects to select for your company. 

I usually end up having to ask engineering teams to sometimes spend a few weeks 
doing deep technical diligence to decide for myself if a project is feasible. 
But to hone your intuitions to help you quickly filter feasible or not feasible 
projects, here are a couple of other rules of thumb about what makes a machine 
learning problem easier or more likely to be feasible. One, learning a simple 
concept is more likely to be feasible. Well, what does a simple concept mean? 
There's no formal definition of that but it is something that takes you less 
than a second of mental thought or a very small number of seconds of mental 
thought to come up with a conclusion then that would lean to whether it being a 
simple concept. So, you're looking outside the window of a self-driving car to 
spot the other cars that would be a relatively simple concept. Whereas how to 
write an empathetic response, so a complicated user complaints, that would be 
less of a simple concept. Second, a machine learning problem is more likely to 
be feasible if you have lots of data available. Here, our data means both the 
input A and the output B, that you want the AI system to have in your A to B, 
input to output mapping. So for example, in the customer support application, 
the input A would be examples of emails from customers and B could be labeling 
each of these customer emails as to whether it's a refund requests or a 
shipping query, or some other problem, one of three outcomes. Then if you have 
thousands of emails with both A and B, then the odds of you building a machine 
learning system to do that would be pretty good. 

What I hope to do, both in the previous video and in this video is to quickly 
show you a few examples of AI successes and failures, or what it can and cannot 
do so that in a much shorter time, you can see multiple concrete examples to 
help hone your intuition and select valuable projects. So, let's take a look at 
a few more examples. Let's say you're building a self-driving car, here's 
something that AI can do pretty well, which is to take a picture of what's in 
front of your car and maybe just using a camera, maybe using other senses as 
well such as radar or lidar. Then to figure out, what is the position, or where 
are the other cars. So, this would be an AI where the input A, is a picture of 
what's in front of your car, or maybe both a picture as well as radar and other 
sensor readings. The output B is, where are the other cars? So, that's what the 
AI today can do. Here's an example of something that today's AI cannot do, or 
at least would be very difficult using today's AI, which is to input a picture 
and output the intention of whatever the human is trying to gesture at your 
car. So, here's a construction worker holding out a hand to ask your car to 
stop. Here's a hitchhiker trying to wave a car over. Here is a bicyclist 
raising the left-hand to indicate that they want to turn left. So, if you were 
to try to build a system to learn the A to B mapping, where the input A is a 
short video of our human gesturing at your car, and the output B is, what's the 
intention or what does this person want, that today is very difficult to do. 
Part of the problem is that the number of ways people gesture at you is very, 
very large. Imagine all the hand gestures someone could conceivably use asking 
you to slow down or go, or stop. The number of ways that people could gesture 
at you is just very, very large. So, learning from a video to what this person 
wants, it's actually a somewhat complicated concept. In fact, even people have 
a hard time figuring out sometimes what someone waving at your car wants. I 
think it's quite hard today to build an AI system to recognize humans 
intentions from their gestures at the very high level of accuracy needed in 
order to drive safely around these people. So, that's why today, many self-
driving car teams have some components for detecting other cars, and they do 
rely on that technology to drive safely. But very few self-driving car teams 
are trying to count on the AI system to recognize a huge diversity of human 
gestures and counting just on that to drive safely around people. 

To summarize, here are some of the strengths and weaknesses of machine 
learning. Machine learning tends to work well when you're trying to learn a 
simple concept, such as something that you could do with less than a second of 
mental thought, and when there's lots of data available. Machine learning tends 
to work poorly when you're trying to learn a complex concept from small amounts 
of data. A second underappreciated weakness of AI is that it tends to do poorly 
when it's asked to perform on new types of data that's different than the data 
it has seen in your data set. 

In case the boundary between what it can or cannot do still seems fuzzy to you, 
don't worry. It is completely normal, completely okay. In fact even today, I 
still can't look at a project and immediately tell is something that's feasible 
or not. I often still need weeks or small numbers of weeks of technical 
diligence before forming strong conviction about whether something is feasible 
or not. But I hope that these examples can at least help you start imagining 
some things in your company that might be feasible and might be worth exploring 
more. 

7. Deep Learning: The terms deep learning and neural network are used almost 
interchangeably in AI. And even though they're great for machine learning, 
there's also been a bit of hype and bit of mystique about them. This video will 
demystify deep learning, so that you have a sense of what deep learning and 
neural networks really are. 

Let's use an example from demand prediction. Let's say you run a website that 
sells t-shirts. And you want to know, based on how you price the t-shirts, how 
many units you expect to sell, how many t-shirts you expect to sell. You might 
then create a dataset like this, where the higher the price of the t-shirt, the 
lower the demand. So you might fit a straight line to this data, showing that 
as the price goes up, the demand goes down. Now demand can never go below zero, 
so maybe you say that the demand will flatten out at zero, and beyond a certain 
point you expect pretty much no one to buy any t-shirts. It turns out this blue 
line is maybe the simplest possible neural network. You have as input the 
price, A, and you want it to output the estimated demand, B. So the way you 
would draw this as a neural network is that the price will be input to this 
little round thing there, and this little round thing outputs the estimated 
demand. In the terminology of AI, this little round thing here is called a 
neuron, or sometimes it's called an artificial neuron, and all it does is 
compute this blue curve that I've drawn here on the left. Start transcript at 1 
minute 50 seconds1:50 This is maybe the simplest possible neural network with a 
single artificial neuron, that just inputs the price and outputs the estimated 
demand. If you think of this orange circle, this artificial neuron as a little 
Lego brick, all that a neural network is, if you take a lot of these Lego 
bricks and stack them on top of each other until you get a big power, a big 
network of these neurons. Let's look at a more complex example. Suppose that 
instead of knowing only the price of the t-shirts, you also have the shipping 
costs that the customers will have to pay to get the t-shirts. May be you spend 
more or less on marketing in a given week, and you can also make the t-shirt 
out of a thick, heavy, expensive cotton or a much cheaper, more lightweight 
material. These are some of the factors that you think will affect the demand 
for your t-shirts. Let's see what a more complex neural network might look 
like. You know that your consumers care a lot about affordability. So let's say 
you have one neuron, and let me draw this one in blue, whose job it is to 
estimate the affordability of the t-shirts. And so affordability is mainly a 
function of the price of the shirts and of the shipping cost. A second thing 
though affecting demand for your t-shirts is awareness. How much are consumers 
aware that you're selling this t-shirt? So the main thing that affects 
awareness, is going to be your marketing. So let me draw here a second 
artificial neuron that inputs your marketing budget, how much you spend on 
marketing, and outputs how aware are consumers of your t-shirt. Finally, the 
perceived quality of your product will also affect demand, and perceived 
quality would be affected by marketing. The marketing tries to convince people 
this is a high quality t-shirt, and sometimes the price of something also 
affects perceived quality. So I'm going to draw here a third artificial neuron 
that inputs price, marketing and material, and tries to estimate the perceived 
quality of your t-shirts. Finally, now that the earlier neurons, these three 
blue neurons, have figured out how affordable, how much consumer awareness and 
what's the perceived quality, you can then have one more neuron over here that 
takes as input these three factors and outputs the estimated demand. So this is 
a neural network, and its job is to learn to map from these four inputs, that's 
the input A, to the output B, to demand. So it learns this input output or A to 
B mapping. This is a fairly small neural network with just four artificial 
neurons. In practice, neural networks used today are much larger, with easily 
thousands, tens of thousands or even much larger than that numbers of neurons. 
Now, there's just one final detail of this description that I want to clean up, 
which is that in the way I've described the neural network, it was as if you 
had to figure out that the key factors are affordability, awareness and 
perceived quality. One of the wonderful things about using neural networks is 
that to train a neural network, in other words, to build a machine learning 
system using neural network, all you have to do is give it the input A and the 
output B. And it figures out all of the things in the middle by itself. So to 
build a neural network, what you would do is feed it lots of data, or the input 
A, and have a neural network that just looks like this, with a few blue neurons 
feeding to a yellow open neuron. And then you have to give it data with the 
demand B as well. And it's the software's job to figure out what these blue 
neurons should be computing, so that it can completely automatically learn the 
most accurate possible function mapping from the input A to the output B. And 
it turns out that if you give this enough data and train a neural network that 
is big enough, this can do an incredible good job mapping from inputs A to 
outputs B. So that's a neural network, is a group of artificial neurons each of 
which computes a relatively simple function. But when you stack enough of them 
together like Lego bricks, they can compute incredibly complicated functions 
that give you very accurate mappings from the input A to the output B. 

In the last video, you saw how a neural network can take as input four numbers 
corresponding to the price, shipping costs, amounts of marketing, and cloth 
material of a T-shirt and output demand. Similar to before, you will have many 
many of these artificial neurons computing various values, and it's not your 
job to figure out what these neurons should compute. The neural network will 
figured out by itself. Again, part of the magic of neural networks is that you 
don't really need to worry about what it is doing in the middle. All you need 
to do is give it a lot of data of pictures like this, A, as well as the correct 
identity B and the learning algorithm will figure out by itself what each of 
these neurons in the middle should be computing. 



How to choose an AI project: Machine learning is an “iterative” process, 
meaning that an AI team often has to try many ideas before coming up with 
something that’s good enough, rather than have the first thing they try work. 
Say you want to use Machine Learning to help your sales team with automatic 
lead sorting. I.e., Input A (a sales prospect) and output B (whether your sales 
team should prioritize them). The 3 steps of the workflow, in scrambled order, 
are: (i) Deploy a trained model and get data back from users (ii) Collect data 
with both A and B (iii) Train a machine learning system to input A and output B 

Say you want to build an AI system to help recruiters with automated resume 
screening. Which of these steps might be involved in “technical diligence” 
process?  (Select all that apply.) Defining an engineering timeline Making sure 
you can get enough data for this project Ensuring that this is valuable for 
your business (e.g., estimating the project ROI) Making sure that an AI system 
can meet the desired performance 

Which of these statements about “business diligence” do you agree with? 
Business diligence is the process of ensuring that the envisioned AI technology 
is feasible. Business diligence is the process of ensuring that the AI 
technology, if it is built, is valuable for your business. 

Say you want to build an AI system to help recruiters with automated resume 
screening. Which of these steps might be involved in “technical diligence” 
process?  (Select all that apply.) Defining an engineering timeline Making sure 
you can get enough data for this project Making sure that an AI system can meet 
the desired performance 

Ensuring that this is valuable for your business (e.g., estimating the project 
ROI) 

week2 

Pitfall: Before wrapping up this video one pitfall I want to urge you to avoid 
is expecting a 100% accuracy from your AI software. Here's what I mean, let's 
say this is your test set which you've already seen on the last slide. But, let 
me add a few more examples to this test set. Here are some of the reasons it 
may not be possible for a piece of AI software to be a 100% accurate. First, 
machine learning technology today despite being very powerful still has 
limitations and they just can't do everything. So, you may be working on a 
problem that it's just very difficult even for today's machine learning 
technology. Second, insufficient data. If you don't have enough data 
specifically if you don't have enough training data for the AI software to 
learn from it may be very difficult to get a very high level of accuracy. 
Third, data is messy and sometimes data can be mislabeled. For example, this 
green coffee mug here looks perfectly okay to me, so, the label of it being a 
defect looks like an incorrect label and that would hurt the performance of 
your AI software. Data can also be ambiguous. 

AI technical tools: Finally, you might hear about Cloud versus On-premises, or 
for short, On-prem deployments. Cloud deployments refer to if you rent compute 
servers such as from Amazon's AWS, or Microsoft's Azure, or Google's GCP in 
order to use someone else's service to do your computation. Whereas, an On-prem 
deployment means buying your own compute servers and running the service 
locally in your own company. A detailed exploration of the pros and cons of 
these two options is beyond the scope of this video. A lot of the world is 
moving to Cloud deployments. Whether you search online you find many articles 
talking about the pros and cons of Cloud versus On-prem deployments. 

Workflow of a Machine Learning Project: Machine learning algorithms can learn 
input to output or A to B mappings. So, how do you build a machine learning 
project? Let’s take a look what is the workflow of machine learning projects. 
As a running example, I'm going to use speech recognition. So, some of you may 
have an Amazon Echo or Google Home or Apple Siri device or a Baidu DuerOS 
device in your homes. So, how do you build a speech recognition system that can 
recognize when you say, "Alexa," or "Hey, Google," or "Hey, Siri," or "Hello, 
Baidu"? Let's go through the key steps of a machine learning project. Just for 
simplicity, I'm going to use Amazon Echo or detecting the Alexa keywords as 
this running example. If you want to build an AI system or build a machine 
learning system to figure out when a user has said the word Alexa, 

the first step is to collect data. So, that means, you would go around and get 
some people to say the word "Alexa" for you and you record the audio of that. 
You'll also get a bunch of people to say other words like "Hello," or say lots 
of other words and record the audio of that as well. Having collected a lot of 
audio data, a lot of these audio clips of people saying either "Alexa" or 
saying other things, 

step two is to then train the model. This means you will use a machine learning 
algorithm to learn an input to output or A to B mapping, where the input A 
would be an audio clip. In the case of the first audio clip above, hopefully, 
it will tell you that the user said "Alexa," and in the case of audio clip two, 
shown on the right, hopefully, the system will learn to recognize that the user 
has said "Hello." Whenever an AI team starts to train the model, meaning to 
learn the A to B or input-output mapping, what happens, pretty much every time, 
is the first attempt doesn't work well. So invariably, the team will need to 
try many times or in AI, we call this iterate many times. You have to iterate 
many times until, hopefully, the model looks like is good enough. 

The third step is to then actually deploy the model. What that means is you put 
this AI software into an actual smart speaker and ship it to either a small 
group of test users or to a large group of users. What happens in a lot of AI 
products is that when you ship it, you see that it starts getting new data and 
it may not work as well as you had initially hoped. So, for example, I am from 
the UK. So, I'm going to pick on the British. But let's say you had trained 
your speech recognition system on American-accented speakers and you then ship 
this smart speaker to the UK and you start having British-accented people say 
"Alexa." They may find that it doesn't recognize the speech as well as you had 
hoped. When that happens, hopefully, you can get data back of cases such as 
maybe British-accented speakers was not working as well as you're hoping, and 
then use this data to maintain and to update the model. 

So, to summarize, the key steps of a machine learning project are to collect 
data, to train the model, the A to B mapping, and then to deploy the model. 
Throughout these steps, there is often a lot of iteration, meaning fine-tuning 
or adapting the model to work better or getting data back even after you've 
shipped it to, hopefully, make the product better, which may or may not be 
possible depending on whether you're able to get data back. using new data to 
maintain and update the model so that, hopefully, you can have your AI software 
continually get better and better to the point where you end up with a software 
that can do a pretty good job detecting other cars from pictures like these. 

Job functions: Data is transforming many different job functions, whether you 
work in recruiting or sales or marketing or manufacturing or agriculture, data 
is probably transforming your job function. What's happened in the last few 
decades is the digitization of our society. So, rather than handing out papers 
surveys like these, surveys are more likely to be done in digital format or 
doctors still write some handwritten notes but doctors handwritten note is 
increasingly likely to be a digital record and so to this in just about every 
single job function. This availability of data means that there's a good chance 
that your job function could be helped with tools like data science or machine 
learning. I want to run through many different job functions and discuss how 
data science and machine learning can or will impact these different types of 
jobs. One of the steps of this manufacturing process is the final inspection. 
In fact today, in many factories there can be hundreds or thousands of people 
using the human eye to check over objects, maybe coffee mugs, maybe other 
things to see if they're scratches or dents and that's called inspection. So, 
machine learning can take this input, a dataset like this, and learn to 
automatically figure out if a coffee mug is defective or not. By automatically 
finding scratches or dents, it can reduce labor costs and also improve quality 
in your factory. This type of automated visual inspection is one of the 
technologies that I think will have a big impact on manufacturing. Let's see 
more examples. How about recruiting? When recruiting someone to join your 
company, there may be a pretty predictable sequence of steps where your 
recruiter or someone else would send an email to a candidate and then you'd 
have a phone call with them, bring them on-site for an interview and then 
extend an offer and maybe close the offer. Similar to how data science can be 
used to optimize a sales funnel, recruiting can also use data science to 
optimize a recruiting funnel and in fact many recruiting organizations are 
doing so today. For example, if you find that hardly anyone is making it from 
phone screen step to the on-site interviews step then you may conclude that 
maybe too many people are getting into the phone screen stage or maybe the 
people doing the phone screen are just being too tough and you should let more 
people get to the onsite interview stage. This type of data science is already 
having an impact on recruiting. What about machine learning projects? Well, one 
of the steps of recruiting is to screen a lot of resumes to decide who to reach 
out to you. So, you may have to look at one resume and say, "Yes, let's email 
them", look at a different one to say, "No, let us not move ahead with this 
candidate." Machine learning is starting to make its way into automated resume 
screening. Does raise important ethical questions such as making sure that your 
AI software does not exhibit undesirable forms of bias and treats people 
fairly, but machine learning is starting to make inroads into this and I hope 
can do so while making sure that the systems are ethical and fair. 

you saw how all of these job functions, everything from sales, recruiting to 
marketing to manufacturing to farming agriculture, how all of these job 
functions are being affected by data, by data science and machine learning. 

How to choose an AI project: Let's say you want to build an AI project for your 
business. You've already seen that AI can't do everything, and so there's going 
to be a certain set of things that is what AI can do. So let's let the circle 
represent the set of things that AI can do. Now, there's also going to be a 
certain set of things that is valuable for your business. So let's let this 
second circle represent a set of things that are valuable for your business. 
What you would like to do is try to select projects that are at the 
intersection of these two sets, so you select projects hopefully that are both 
feasible, that can be done with AI, and that are also valuable for your 
business. So AI experts will tend to have a good sense of what is and what 
isn't in the set on the left. And domain experts, experts in your business, be 
it sales and marketing, or agriculture or something else, will have the best 
sense of what is actually valuable for your business. So when brainstorming 
projects that AI can do and are valuable for your business, I will often bring 
together a team comprising both people knowledgeable of AI, as well as experts 
in your business area to brainstorm together. So that together they can try to 
identify projects at the intersection of both of these two sets. 

And it's by looking at all these tasks that the group of employees do and 
selecting one that may allow you to select the most fruitful project for 
automation in the near term. And so it's by looking at all of these tasks that 
a radiologist does that you may Identify one of them, let's say AI assistance 
or AI automation for reading x-rays, that allows you to select the most 
fruitful projects to work on. So what I would recommend is, if you look at your 
business, think about the tasks that people do, to see if you can identify just 
one of them, or just a couple of them, that may be automatable using machine 
learning. 

When I'm meeting CEOs of large companies to brainstorm AI projects for the 
company, a common question I'll also ask is, what are the main drivers of 
business value? And sometimes finding AI solutions or data science solutions to 
augment this can be very valuable. Finally, a third question that I've asked 
that sometimes let to valuable project ideas is, what are the main pain points 
in your business? Some of them could be solved with AI, some of them can't be 
solved with AI. But by understanding the main pain points in the business, that 
can create a useful starting point for brainstorming AI projects as well. The 
amount of data you need is very problem dependent, and speaking with an AI 
engineer or AI expert would help you get better sense. There are some problems 
where 1,000 images may not be enough, where you do need big data to get good 
performance. But my advice is, don't give up just because you don't have a lot 
of data to start off with. And you can often still make progress, even with a 
small dataset. In this video, you saw a brainstorming framework, and a set of 
criteria for trying to come up with projects that hopefully can be doable with 
AI, and are also valuable for your business. 



Maybe you have a lot of ideas for possible AI projects to work on. But before 
committing to one, how do you make sure that this really is a worthwhile 
project? If it's a quick project that might take you just a few days maybe just 
jump in right away and see if it works or not, but some AI projects may take 
many months to execute. In this video, I want to step you through the process 
that I use to double-check if a project is worth that many months of effort. 
Before committing to a big AI project, I will usually conduct due diligence on 
it. Due diligence has a specific meaning in the legal world. But informally, it 
just means that you want to spend some time to make sure you've already seen 
how the best AI projects are ones that are feasible. So, it's something that AI 
can do, as well as valuable. We really want to choose projects to that the 
intersection of these two sets. So, to make sure a project is feasible, I will 
usually go through technical diligence, and make sure that the project is 
valuable, I will usually go through a business diligence process. Technical 
diligence is the process of making sure that the AI system you hope to build 
really is feasible. So, you might talk to AI experts about whether or not the 
AI system can actually meet the desired level of performance. For example, if 
you are hoping to build a speech system that is 95 percent accurate, consulting 
of AI experts or perhaps reading some of the trade literature can give you a 
sense of whether this is doable or not. Or if you want a system to inspect 
coffee mugs in a factory and you need your system to be 99 percent accurate. 
Again, is this actually doable with today's technology? A second important 
question for technical diligence is how much data is needed to get to this 
desired level of performance, and do you have a way to get that much data. 
Third, would be engineering timeline to try to figure out how long it will take 
and how many people it will take to build a system that you would like to have 
built. In addition to technical diligence, I will often also conduct business 
diligence to make sure that the project you envision really is valuable for the 
business. So, a lot of AI projects will drive value through lowering costs. For 
example, by automating a few tasks or by squeezing more efficiency onto the 
system. A lot of AI systems can also increase revenue. For example, driving 
more people to check out in your shopping cart or you may be building an AI 
system to help you launch a new product or a new line of business. So, business 
diligence is the process of thinking through carefully for the AI system that 
you're building such as a speech recognition system that's 95 percent accurate 
or a visual inspection system that's 99.9 percent accurate, would allow you to 
achieve your business goals. Whether your business goal is to improve your 
current business or to even create brand new businesses in your company. 

When conducting business diligence, I'll often end up building spreadsheet 
financial models to estimate the value quantitatively such as estimate how many 
dollars are actually saved or what do we think is a reasonable assumption in 
terms of entries revenue, and to model out the economics associated with a 
project before committing to many months of effort on a project. So, when 
there's a massive force of an industry standard solution that is been built, 
you might be better off just embracing an industry standard or embracing 
someone else's platform rather than trying to do everything in-house. We all 
live in a world of limited resources, limited time, limited data, limited 
engineering resources, and so, I hope you can focus those resources on the 
projects with our most unique and will make the biggest difference to your 
company. Through the process of technical diligence as well as business 
diligence, I hope you can start to identify projects that are potentially 
valuable or that seem promising for your business. If the project is a big 
company, maybe it'll take many months to do. It's not unusual for me to spend 
even a few weeks conducting this type of diligence before committing to a 
project. 

First, machine learning technology today despite being very powerful still has 
limitations and they just can't do everything. So, you may be working on a 
problem that it's just very difficult even for today's machine learning 
technology. Second, insufficient data. If you don't have enough data 
specifically if you don't have enough training data for the AI software to 
learn from it may be very difficult to get a very high level of accuracy. 
Third, data is messy and sometimes data can be mislabeled. Some of these 
problems can be ameliorated. For example, if you don't have enough data maybe 
you can try to collect more data and more data will often help. Or you can also 
try to clean up mislabeled data or try to get your factories experts to come to 
better agreement about these ambiguous labels. So, there are ways to try to 
make these things better, but, a lot of AI systems are incredibly valuable even 
without achieving a 100% accuracy. So, I will urge you to discuss with your AI 
engineers what is a reasonable level of accuracy to try to accomplish? 

Technical tools for AI teams: When you work with AI teams, you may hear them 
refer to the tools that they're using to build these AI systems. In this video, 
I want to share with you some details and names of the most commonly used AI 
tools, so that you'd be able to better understand what these AI engineers are 
doing. We're fortunate that the AI world today is very open, and many teams 
will openly share ideas with each other. There are great machine learning open 
source frameworks that many teams will use to build their systems. So, if you 
hear of any of these: TensorFlow, PyTorch, Keras, MXNet, CNTK, Caffe, 
PaddlePaddle, Scikit-learn, R or Weka, all of these are open source machine 
learning frameworks that help AI teams be much more efficient in terms of 
writing software. Along with AI technology breakthroughs are also publish 
freely on the Internet on this website called Arxiv. Spelled like this. I hope 
that other academic communities also freely share their research since I've 
seen firsthand how much this accelerates progress in the whole field of AI. 
Finally, many teams will also share their code freely on the Internet, most 
commonly on a website called GitHub. This has become the de facto repository 
for open source software in AI and in other sectors in AI. And by using 
appropriately licensed open-source software, many teams can get going much 
faster than if they had to build everything from scratch. AI engineers talk 
about CPUs and GPUs. Here's what these terms mean. A CPU is the computer 
processor in your computer, whether it's your desktop, your laptop, or a 
computer server off in the Cloud. CPU stands for the central processing unit, 
and CPUs are made by Intel, and AMD, and a few other companies. This does a lot 
of the computation in your computer. GPU stands for graphics processing unit. 
Historically, the GPU was made to process pictures. So, if you play a video 
game, it's probably a GPU that is drawing the fancy graphics. But what we found 
several years ago was that the hardware that was originally built for 
processing graphics turns out to be very, very powerful for building very large 
neural networks. So very large deep learning algorithms. Given the need to 
build very large deep learning or very large neural network systems, the AI 
community has had this insatiable hunger for more and more computational power 
to train bigger and bigger neural networks. And GPUs have proved to be a 
fantastic fit to this type of computation that we need to have done to train 
very large neural networks. So, that's why GPUs are playing a big role in the 
rise of deep learning. Finally, you might hear about Cloud versus On-premises, 
or for short, On-prem deployments. Cloud deployments refer to if you rent 
compute servers such as from Amazon's AWS, or Microsoft's Azure, or Google's 
GCP in order to use someone else's service to do your computation. Whereas, an 
On-prem deployment means buying your own compute servers and running the 
service locally in your own company. A lot of the world is moving to Cloud 
deployments. Whether you search online you find many articles talking about the 
pros and cons of Cloud versus On-prem deployments. 

AI pitfalls to avoid: I hope you'll be able to use AI to build exciting and 
valuable projects either for yourself or for your company and make life better 
both for yourself and for others. Along the way, I hope you also manage to 
avoid some of the pitfalls I've seen some AI teams fall into. Let's go over a 
five don'ts and dos for if you're trying to build AI for your company. First 
one, don't expect AI to solve everything. You already know that AI can do a lot 
but there's also lots AI cannot do. Instead, you should be realistic about what 
AI can or cannot do, given the limitations of technology, data, and engineering 
resources. That's why I think technical diligence in addition to business 
diligence is important for selecting feasible and valuable AI projects. Second, 
don't just hire two or three machine learning engineers and count solely on 
them to come up with use cases for your company. Machine learning engineers are 
a scarce resource but you should instead air the engineer talents with business 
talent and work cross-functionally to find feasible and valuable projects. Is 
often the combination of the machine-learning talents worked to business talent 
that can select the most valuable and feasible projects. Third, don't expect AI 
project to work the first time. As you've already seen, AI development is often 
an iterative process so should plan for it through an iterative process with 
multiple attempts needed to succeed. Fourth, don't expect traditional planning 
processes to apply without changes. Instead, you should work with the AI team 
to establish timeline estimates, milestones, KPIs or metrics that do make 
sense. The types of timeline estimates, milestones, and KPIs or metrics 
associated with AI projects are a bit different than the same things associated 
with non AI projects. So, hopefully working with some individuals knowledge 
about AI can help you come up with better ways of planning AI projects. 
Finally, don't think you need superstar AI engineers before you can do 
anything. Instead, keep building the team and get going with a team you have 
realizing that there are many AI engineers in the world today including many 
that have learned primarily from online courses. They can do a great job 
building valuable and feasible projects. If you can avoid these AI pitfalls, 
you already be ahead of the game compared to many other companies. The 
important thing is to get started. You're second AI project would be better 
than your first. Your third AI project would better than your second. So, the 
important thing is to get started and to attempt your first AI project. In the 
final video for this week, I want to share with you some concrete first steps 
you can take in AI. Let's go on to the next video. 

major AI techniques and application areas: Applications: AI today is being 
successfully applied to image and video data, to language data, to speech data, 
to many other areas. you see a survey of AI applied to these different 
application areas and I hope that this may spark off some ideas of how you 
might be able to use these techniques someday for your own projects as well. 
One of the major successes of deep learning has been Computer Vision. Let's 
take a look at some examples of computer vision applications. Image 
classification and object recognition refer to taking as input a picture like 
that and telling us what is in this picture. In this case, it'd be a cat. 
Rather than just recognizing cats, I've seen AI algorithms able to recognize 
specific types of flowers, AI able to recognize specific types of food and the 
ability to take as input a picture and classify it into what type of object, 
and this is being used in all applications. A different type of computer vision 
algorithm is called object detection. So, rather than just tried to classify or 
recognize an object, you're trying to detect if the object appears. For 
example, in building a self-driving car, we've seen how an AI system can take 
as input a picture like this and not just tell us yes or no, is there a car. 
Yes or no, is there pedestrian but actually tells us the position of the cars 
as well as the positions of the pedestrians in this image, and object detection 
algorithm can also take as input a picture like that and just say, no I'm not 
finding any cars or any pedestrians in that image. So rather than taking a 
picture and labeling the whole image which is image classification, instead an 
object detection algorithm will take us input an image and tell us where in the 
picture different objects are as was what are the types of those objects. Image 
segmentation takes this one step further. Given an image like this, an image 
segmentation algorithm we output, where it tells us not just where the cars and 
pedestrians but tells us for every single pixel, is this pixel part of this car 
or is this pixel part of a pedestrian. So it doesn't just draw rectangles 
around the objects and detects, instead it draws very precise boundaries around 
the objects that it finds. Computer vision can also deal with video and one 
application of that is tracking. In this example, rather than just detecting 
the runners in this video, it is also tracking in a video whether runners are 
moving over time. So, those little tails below the red boxes show how the 
algorithm is tracking different people running across several seconds in the 
video. So, the ability to track people and cars and maybe other moving objects 
in a video helps a computer figure out where things are going. If you're using 
a video camera to track wildlife for example, say birds flying around, a 
tracking algorithm will also be the helper track individual birds flying across 
the frames of your video. These are some of the major areas of computer vision 
and perhaps some of them will be useful for your projects. AI and deep learning 
specifically is also making a lot of progress in Natural Language Processing. 
Natural Language Processing or NLP refers to AI understanding natural language, 
meaning the language that you and I might use to communicate with each other. 
One example is text classification where the job of the AI is to input a piece 
of texts such as an email and tell us what is the cause or what is the category 
of this email, such as a spam or non-spam email. One type of text 
classification that has had a lot of attention is sentiment recognition. For 
example, a sentiment recognition algorithm can take as input a review like this 
of a restaurant, the food was good and automatically tries to tell us how many 
stars this review might get. The food was good as a pretty good review maybe 
that's four over five-star review. Whereas if someone writes service was 
horrible, then the sentiment recognition algorithm should be able to tell us 
that this corresponds maybe to a one-star review. A second type of NLP or 
Natural Language Processing is information retrieval. Web search is perhaps the 
best known example of information retrieval where you type in the text query 
and you want the AI to help you find relevant documents. Many corporations will 
also have internal information retrieval systems where you might have an 
interface to help you search just within your company's set of documents for 
something relevant to a query that you might enter. Name entity recognition is 
another natural language processing technology. If you want to find all the 
location names, all the place names in a sentence like that, a named entity 
recognition system can also do so. Name entity recognition systems can also 
automatically extract names of companies, phone numbers, names of countries, 
and so, if you have a large document collection and you want to find 
automatically all the company names, or all the company names the occur 
together or all the people's names, then a name entity recognition system would 
be the tool you could use to do that. 

Another major AI application area is machine translation. So, for example, if 
you see this sentence in Japanese, AI [inaudible]. Then hopefully a machine 
translation system can input that and output the translation AI is in the 
electricity. The four items on this slide: text classification, information 
retrieval, name entity recognition, and machine translation, are four major 
categories of useful NLP applications. 

I hope this survey of AI application areas gives you a sense that the wide 
range of data that AI is successfully applied to today, and maybe this even 
inspire you to think of how some of these application areas may be useful for 
your own projects. Now, so far the one AI technique we've spent the most time 
talking about is supervised learning. That means learning inputs, output, or A 
to B mappings from labeled data where you give the AI system both A and B. But 
that's not the only AI technique out there. In fact, the term supervised 
learning almost invites the question of what is unsupervised learning, or you 
might also have heard from media articles, from the news about reinforcement 
learning. So, what are all these other techniques? 

Techniques: There are a lot of AI and machine learning techniques today. And 
while supervised learning, that is learning A to B mappings, is the most 
valuable one, at least economically today, there are many other techniques that 
are worth knowing about. The best known example of unsupervised learning is 
clustering, here's an example. A clustering algorithm looks at data like this, 
and automatically groups the data into two clusters or more clusters, and is 
commonly used for market segmentation. And this can help you market differently 
to these market segments. The reason this is called unsupervised learning is 
the following. Whereas supervised learning algorithms run an A to B mapping, 
and you have to tell the algorithm what is the output B that you want, an 
unsupervised learning algorithm doesn't tell the AI system exactly what it 
wants. Instead it gives the AI system a bunch of data such as this customer 
data, and it tells the AI to find something interesting in the data, find 
something meaningful in the data. Instead, it just tries to find what are the 
different market segments without being told in advance what they are. So 
unsupervised learning algorithms, given data without any specific design output 
labels, without the target label B, can automatically find something 
interesting about the data. Even though supervised learning is an incredibly 
valuable and powerful technique, one of the criticisms of supervised learning 
is that it just needs so much labeled data. So, AI systems today require much 
more labeled data to learn than when a human child or than would most animals. 
Which is why AI researchers hold a lot of hope out for unsupervised learning as 
way, maybe in the future, for AI to learn much more effectively in a more human 
like way, and more biological like way for much less labeled data.  Now, we 
have pretty much no idea how the biological brain works, and so to realize this 
vision, we'll take major breakthroughs in AI than none of us know yet today how 
to realize. 

Another important AI technique is transfer learning. Let's look an example. 
Let's say you bought a self driving car, and you've trained your AI system to 
detect cars. But you didn't deploy your vehicle to a new city and somehow this 
new city has a lot of golf carts travelling round, and so you need to also 
build a golf cart detection system. You may have your car detection system with 
a lot of images, say 100,000 images, but in this new city where you just start 
operating, you may have a much smaller number of images of golf carts. Transfer 
learning is the technology that lets you from a task A, such as car detection, 
and use the knowledge to help you on a different task B, such as golf cart 
detection. Where transfer learning really shine is if having learn from a very 
large dataset of car detection, task A, you can now do pretty well on golf cart 
detection, even though you have a much smaller golf cart dataset. Because some 
of the knowledge it has learned from the first task, of what the vehicles look 
like, what the wheels look like, how the vehicles move. Maybe that will be 
useful also for golf cart detection. Transfer learning doesn't get a lot of 
press, but it is one of the very valuable techniques in AI today. And for 
example, many computer vision systems are built using transfer learning, and 
this makes a big difference to their performance. You may also have heard of a 
technique called reinforcement learning. So, what is reinforcement learning? 
Let me illustrate with another example. 

I think of reinforcement learning as similar to how you might train a pet dog 
to behave. My family, when I was growing up, had a pet dog. So, how do you 
train a dog to behave itself? Well, we let the dog do whatever it wanted to do, 
and then whenever it behaved well we would praise it. You go, good dog, and 
whenever it does something bad you would go, bad dog. And overtime it learns to 
do more of the, good dog, things, and fear of the bad dog things. Reinforcement 
learning takes the same principle and applies it to a helicopter or two other 
things. a reinforcement learning algorithm uses a reward signal, to tell the AI 
when it's doing well or poorly. This means that whenever it's doing well, you 
give it a large positive number to give it a large positive reward. And 
whenever it's doing really bad job, you send it a negative number to give it a 
negative reward. And it's the AI's job to the automatically learn to behave so 
as to maximize the rewards. So, good dog responds to giving a positive number, 
and bad dog or bad helicopter, corresponds to you giving a negative number. You 
might have heard of AlphaGo, which did a very good job of playing Go using 
reinforcement learning. And reinforcement learning has also been very effective 
at playing video games. One of the weaknesses of reinforcement learning 
algorithms is that they can require a huge amount of data. and get a huge 
amount of data to learn how to behave better. 

And AI is advancing so rapidly that all of us certainly hope that there will be 
breakthroughs in all of these areas that we're talking about. GANs, or 
generative adversarial networks, are another exciting new AI technique. GANs 
are very good at synthesizing new images from scratch. Let me show you a video 
generated by a team from NVIDIA, that used GANs to synthesize pictures of 
celebrities. And these are all pictures of people that had never existed 
before. But by learning what's celebrities look like from a databases celebrity 
images, it's able to synthesize all these brand new pictures. There's exciting 
work by different things right now on applying GANs to the entertainment 
industry. 



Building AI in your company: week3 

As you can tell both from this rather complex example of an AI pipeline, as 
well as the early example of the four-step AI pipeline for the smart speaker, 
sometimes it takes a team to build all of these different components of a 
complex AI product. What I'd like to do in the next video is share with you 
what are the key roles in large AI teams. If you're either a one-person or 
small AI team now, that's okay, but I want you to have a vision of what 
building a large AI team, maybe in the distant future, might look like. 

I hope this survey of AI application areas gives you a sense that the wide 
range of data that AI is successfully applied to today, and maybe this even 
inspire you to think of how some of these application areas may be useful for 
your own projects. Now, so far the one AI technique we've spent the most time 
talking about is supervised learning. That means learning inputs, output, or A 
to B mappings from labeled data where you give the AI system both A and B. But 
that's not the only AI technique out there. In fact, the term supervised 
learning almost invites the question of what is unsupervised learning, or you 
might also have heard from media articles, from the news about reinforcement 
learning. So, what are all these other techniques? In the next video, the final 
optional video for this week, we'll do a survey of AI techniques, and I hope 
that through that maybe you'll see if some of these other AI techniques and 
supervised learning could be useful for your projects as well. Let's go on to 
the final optional video for the week. 

There are a lot of AI and machine learning techniques today. And while 
supervised learning, that is learning A to B mappings, is the most valuable 
one, at least economically today, there are many other techniques that are 
worth knowing about. Let's take a look. The best known example of unsupervised 
learning is clustering, here's an example. Let's say you run a grocery store 
that specializes in selling potato chips. 

For example, if you're trying to use supervise learning to get the AI system to 
recognized coffee mugs, then you may give it 1000 pictures of coffee mug, or 10,
000 pictures of mug coffee mug. And that's just a lot of picture of coffee mugs 
coffee mug we will be giving our AI systems. For those of you that are parents, 
I can almost guarantee to you that no parent on this planet, no matter how 
loving and caring, has ever pointed out 10,000 unique coffee mugs to their 
children, to try to teach the children what is a coffee mug. So, AI systems 
today require much more labeled data to learn than when a human child or than 
would most animals. Which is why AI researchers hold a lot of hope out for 
unsupervised learning as way, maybe in the future, for AI to learn much more 
effectively in a more human like way, and more biological like way for much 
less labeled data. 

Why is developing an AI strategy NOT the first step in the AI Transformation 
Playbook? Without having some practical AI experience and knowing what it feels 
like to build an AI project, a company usually does not know enough to 
formulate a sound strategy. 

week4 limitations: In fact, there's a lot it cannot do but it will transform 
industries and society. When you speak with friends about AI, I hope you also 
tell them about this Goldilocks rule for AI, so, that they too can have a more 
realistic view of AI. There are many limitations of AI. You have already seen 
earlier some of the performance limitations. For example, given a small amount 
of data, a pure AI probably cannot fully automate a call center and give very 
flexible responses to whatever customers are emailing you with. But AI has 
other limitations, as well. One of the limitations of AI is that explainability 
is hard and many high-performing AI systems are black boxes. Meaning that it 
works very well but the AI doesn't know how to explain why it does what it 
does. Now, to be fair, humans are also not very good at explaining how we make 
decisions ourselves. For example, you've already seen this coffee mug in the 
last weeks videos but how do you know it's a coffee mug? How does a human look 
at this and say, that's a coffee mug? You know there are some things you can 
point to like, there's a room for liquid and it has a handle. But we humans are 
not very good at explaining, how we can look at this and decide what it is. But 
because AI is a relatively new thing, the lack of explainability is sometimes a 
barrier to its acceptance. Also, sometimes if an AI system isn't working then 
its ability to explain itself would also help us figure out how to go in and 
make the AI system work better. So, explainability is one of the major open 
research areas. A lot of researchers are working on. What I see in practice, is 
that when an AI team wants to deploy something, that AI team must often able to 
come up with an explanation that is good enough to enable the system to work 
and be deployed. So, explainability is hotbed, its often not impossible but we 
do need much better tools to help the AI systems explain themselves. 

One question now sometimes asked is what should you do if you want to work in 
AI? Recently, a radiologist resident served radiologists near the start of his 
career. He actually asked me. He said, "Hey, Andrew, I'm hearing a lot about 
the coming impacts of AI on radiology." He said, "Should I quit my profession 
and just learn AI and do AI instead?" My answer to him was no. You could do 
that. You can actually quit whatever you are doing and pick up AI from scratch. 
It is entirely possible to do that. Many people have done that. This one other 
alternative that you could consider though, which is, I said to this radiology 
resident consider doing work in AI plus radiology because with your knowledge 
of radiology, if in addition you learned something about AI, you would be 
better positioned to do work at the intersection of radiology and AI than most 
other people. So, if you want to do more work in AI, it is possible in today's 
world to learn AI from scratch through online courses and other resources. But 
if you take whatever you are already knowledgeable in and learn some AI and do 
your area plus AI, then you might be more uniquely qualified to do very 
valuable work by applying AI to whatever area you are already an expert in. So, 
I hope this video helps you navigate the coming impacts of AI in jobs. Let's go 
on to the next and final video of this course. 

Congratulations on coming to the last video of this course. AI is a super 
power, and understanding it allows you to do things that very few people on the 
planet can. Let's summarize what you've seen in this course. In the first week, 
you learned about AI technology, what is AI and what is machine learning? 
What's supervised learning, that is learning inputs, outputs, or A to B 
mappings. As well as what is data signs, and how data feeds into all of these 
technologies? Importantly, you also saw examples of what AI can and cannot do. 
In the second week, you learned what it feels like to build an AI project. You 
saw the workflow of machine learning projects, of collecting data, building a 
system and deploying it, as well as the workflow of data science projects. And 
you also learned about carrying out technical diligence to make sure a project 
is feasible, together with business diligence to make sure that the project is 
valuable, before you commit to taking on a specific AI project. In the third 
week, you learned how such AI projects could fit in the context of your 
company. You saw examples of complex AI products, such as a smart speaker, a 
self-driving car, the roles and responsibilities of large AI teams. And you 
also saw the AI transmission playbook, the five step playbook for helping a 
company become a great AI company. I hope these materials throughout these 
first three weeks can help you brainstorm AI projects or think about how you 
might want to use AI in your company or in your organization. In this week, 
week four, you learned about AI and society. You saw some of the limitations of 
AI beyond just technical limitations, and also learned about how AI is 
affecting developing economies and jobs worldwide. You've learned a lot in 
these four weeks, but AI is a complex topic. So I hope you will keep on 
learning, whether through additional online courses, through Coursera or 
deeplearning.ai, or books, or blogs, or just by talking to friends. If you ever 
want to try your hand at building AI technology, it is now easier than ever to 
learn to code and learn how to implement AI technology through these resources. 
If you'd like to keep on receiving information about AI, you can also sign up 
for the deeplearning.ai mailing list, by going to the deeplearning.ai website 
and signing up there. I'll occasionally send you useful information about AI 
through that mailing list. Start transcript at 2 minutes 51 seconds2:51 
Congratulations on finishing this course. You're now significantly ahead of 
many large companies' CEOs in your understanding of AI and your ability to plan 
for the rise of AI. So I hope that you provide leadership to others as well 
that are trying to navigate these issues. Lastly, I want to say to you, thank 
you very much for taking this course. I know that you're busy with your own 
work or school, and friends and family, and I'm grateful that you spend so much 
time with me and in this course learning these complex issues relating to both 
the technology and the impact of AI. So thank you very much for both the time 
and the effort you put Into this course. 
 

http://solutionoptimist.com/2013/12/28/awesome-github-tricks/ 

>1

Hello everyone. The topic of my presentation today is Machine Learning at XX. We know ML is changing the way we work and live. Whether you want to know what's behind the buzzwords or whether you want to perhaps use ML yourself either in a personal context or in a corporation, I hope Today's talk will give you a realistic view of what ML really is.

>2

So what is ML? You might have heard some buzzwords in the media, such as machine learning, deep learning or neural networks. What do these terms mean? What is relationship between them?

>3

If we were to draw a Venn diagram showing how all these concepts put together, this is what it may look like. AI is this huge set of tools for making computers behave intelligently and it includes explicit programming. ML is part of AI and DL is a very specific class of algorithms within ML.

>4

So let's go back to this question. What is ML? Machine learning is the field of study that gives computers the ability to learn without being explicitly programmed. This is a definition by Arthur Samuel many decades ago. Arthur Samuel was a pioneer in the field of machine learning, who was famous for building a checkers playing program. Actually, There are several definitions of ML, but in general, ML allows a machine to learn from data and improve its classification and predictive performance.

>5

Instead of using statements to explain what ML is, let me use an example ot explain it in another way. For example, we give a computer the answer key from existing data and train it to replicate that answer. Traditional programming will feed data and explicit program to machine, then the machine will give us output. However, in ML style, machine will receive input and output data and learn from them itself, and then output program. 

>6

Now, what is deep learning? The terms deep learning and neural network are used almost interchangeably in AI. And even though they're great for machine learning, there's also been a bit of hype and mystique about them. Let’s demystify deep learning, so that you have a sense of what deep learning and neural networks really are. Let's say you want to predict housing prices. So, you will have an input that tells you the size of the house, number of bedrooms, and number of bathrooms. Maybe location and whether it's newly renovated. To simplify the problem, let's just consider these three factors here. The most effective way to price houses would be to feed the input to a network in order to have it output the price. This big thing in the middle is called a neural network, and sometimes we also called it an artificial neural network. That's to distinguish it from the neural network in your brain. `The human brain is made up of neurons.` So, when we say artificial neural network, that's just to emphasize that this is not the biological brain, but a piece of software. What a neural network does is taking this input, which is all these three factors, and producing output, which is the estimated price of the house. Acutally, the big neural network is just a big mathematical equation that tells us given the inputs, how do you compute the price.

As I said early, Today, the terms neural network and deep learning are used almost interchangeably, they mean essentially the same thing. Neural network is a very effective technique for learning input-output mappings.  

When you train a neural network, all you have to do is give it the input and output. And then the NN will figure out all of the things in the middle by itself. So to build a neural network, what you would do is feed it lots of data including input and output data, and have a neural network that just looks like this. And then it's the software's job to figure out what these neurons should be computing, so that it can completely learn the most accurate possible function mapping from the input to the output automatically. And it turns out that if you give this enough data and train a neural network that is big enough, this can do an incredible good job mapping from inputs to outputs. So that's a neural network, is a group of artificial neurons each of which computes a relatively simple function. But when you stack enough of them together like Lego bricks, they can compute incredibly complicated functions that give you very accurate mappings from the input to the output.

`
Many decades ago, this type of software was called a neural network. But in recent years, we found that deep learning was just a much better sounding brand, and so that for better or worse is a term that's been taken off recently. So, what do neural networks or artificial neural networks have to do with the brain? Unfortunately, it turns out almost nothing. Neural networks were originally inspired by the brain, but the details of how they work are almost completely unrelated to how biological brains work.
`

>7

>8

Before going to the use cases, let me introduce the types of machine learning. Once we have a solid understanding of these types, it will be easier for us to understand the ways they have been applied at XX.

- Supervised Learning is a type of ML which assumes data to be labeled with a predefined class or value, and the goal is to predict class or value label. Kind of like you have the "answer key" and you are classifying something or figuring out a value.

- Unsupervised Learning is a type of ML without any knowledge of output class or value. Like you don't have an "answer key" and you are looking for a measure of similarity or difference. For example, spending data can identify whether people are big spenders, do a lot of smaller transactions, do fewer but larger transactions, etc. In supervised learning, you have the desired outcome while with unsupervised learning, there is no desired outcome. You are asking the machine to process the data from which you can draw conclusions. 

- Reinforcement Learning is a type of ML with algorithms learning a policy of how to act in a given environment, which is close to human. It examines all possible actions, make a policy that will maximize benefit. When you make the initial policy, you may be wrong (this is the reinforcement). Put the reinforcement back into the algorithm, try again, and continue to do this until you reach the optimal policy. Confusing, right? Let me give you an analogy. You can think of reinforcement learning as similar to how you might train a pet dog to behave. So, how do you train a dog to behave itself? Well, we let the dog do whatever it wanted to do, and then whenever it behaved well we would praise it. You go, good dog, and whenever it does something bad you would go, bad dog. And overtime it learns to do more of the, good dog, things, and fear of the bad dog things. This means that whenever it's doing well, you give it a large positive number to give it a large positive reward. And whenever it's doing really bad job, you send it a negative number to give it a negative reward. And it's the ML's job to the automatically learn to behave so  as to maximize the rewards. So, good dog responds to giving a positive number, and bad dog, corresponds to you giving a negative number.  You might have heard of AlphaGo, which did a very good job of playing Chess using reinforcement learning. And reinforcement learning has also been very effective at playing video games. One of the weaknesses of reinforcement learning algorithms is that they require a huge amount of data to learn how to behave better.

>9

Use cases.

>10

Let use detecting fraudulent transactions as an example.
Questions we may ask:
- How many attempted XX credit card transactions per day? Branded book card has over 10 million card transactions per day.
- How fast do we need to decide whether or not to approve? Have only about 10 milliseconds to make a fraud decision.
- What percent of authorizations are fraudulent? Only about 0.15% of transactions are fraudulent (need to be very careful when training data)
- Annual loss budget for fraudulent transactions? Transactional loss budget was $172 million for Branded Book in 2018; Partnerships added another $20 million.

>11 Opportunities for ML

There are usually two types of use cases.

>12 What is GOOD ML problems?

>13 What is GOOD ML projects?

To make a good ML project, we need to make sure projects are both feasible for ML technology, and valuable for our business. There are two things we need to do.
“technical diligence” is ensuring that the envisioned ML technology is feasible, Defining an engineering timeline, Making sure we can get enough data for this project and the ML system can meet the desired performance.
“business diligence” is the process of ensuring that the ML technology, if it is built, is valuable for your business.
When brainstorming projects, we can bring together a team comprising both people knowledgeable of ML, as well as experts in the business area. By understanding the main pain points in the business and feasible technology we can build, that will allow us to make the most fruitful project for automation in the near term.

>14 Modeling Workflow of ML project

Machine learning is an “iterative” process, meaning that an ML team often has to try many ideas before coming up with something that’s good enough, rather than have the first thing they try work. Let’s take a look what is the workflow of machine learning projects. I'm going to use speech recognition as a running example. Some of you may have an Amazon Echo in your homes. So, how do you build a ML system that can recognize when a user has said the word “Alexa”? Let's go through the key steps of this machine learning project.

The First Step is to collect and preprocess data. So, that means, you would go around and get some people to say the word "Alexa" for you and you record the audio of that. You'll also get a bunch of people to say other words like "Hello," or say lots of other words and record the audio of that as well. Having collected a lot of audio data, in most situations, it need to be cleaned and preprocessed before ready for use. And this is an “iterative” process.

Step Two is to train the model. Then you will use a machine learning algorithm to learn an input to output mapping, where in our running example the input would be an audio clip. In the case of the audio clip above, hopefully, the system will learn to recognize that the user has said "Alexa". Whenever an ML team starts to train the model, what happens, I will say pretty much every time, is the first attempt doesn't work well. So the team will need to iterate many times until the model looks like is good enough. 

The Third Step is to actually deploy the model. What that means is you put this ML software into an actual smart speaker and ship it to users.

Throughout these steps, there are often many iterations of fine-tuning or adapting the model to make the product better.

>15 Modeling

The hard part is getting the data and cleansing it to be ready for modeling. Once you have the data you can try a number of algorithms to determine which is the most successful. You typically whittle down the number of features once you determine which ones are the most successful. For example, in my previous fishing email detection project we start with hundreds of features and in the model there will only be about 50. Parameters and hyper-parameters tuning is an iterative process and it is the most compute-intensive part of the model building process. 

>16 Engineering Workflow of ML project

>17 ML code

The ML model fitting code is often less than a couple of hundred lines of code. Model validation code is often much more than that. Maybe you can find blog posts that talk about "ML in 5 lines of code." They assume that your data has already been prepared and are only doing the model fitting. In practice, you will find a lot of dirty work need to be done only when you touch it. 

>18 ML Team

As you can tell from the rather complex example of a ML pipeline, as well as the early example of Alexa speech recognition on the previous slides, it usually takes a team to build these different components of a complex ML product. Now I'd like to share with you what are the key roles and responsibilities in a typical ML team. Now, even if you will be working in a much smaller team, maybe a four or five person team for the near future, I want you to have a sense of what building a typical ML team might look like, maybe in the distant future.

Many ML teams will have Software Engineers in them. For exampke, you're building a self-driving car to make sure that your self-driving car software is reliable and doesn't crash. These are software engineering tasks. 

The second common role is the Machine Learning Engineer. So, Machine Learning Engineer might write the software responsible for generating algorithms for your product. Like in a self-driving car projet, they might gather the data of pictures of cars and positions of cars, train a deep learning model and work iteratively to make sure that the model can give accurate outputs.

Another role that you sometimes hear about is Data Scientist. Usually the primary responsibility of Data Scientist is to examine data, provide insights, and make presentations to teams or the executives in order to help drive business decision-making.

With the rise of big data, there are also more and more Data Engineers whose main role is to help organize data, build data pipeline to make sure data is stored in a easy accessible, secure and cost-effective way. 


`
The role of Data Scientist is not very well defined today.
There are also a lot of Data Scientists working in industries.
Another role that you sometimes hear about is the Machine Learning Researcher. The typical row of the Machine Learning Researcher is to extend the state of the art in machine learning. Machine learning and AI more broadly are still advancing rapidly. So, many companies for profit and non-profit, more have Machine Learning Researchers responsible for extending the state-of-the-art. Some Machine Learning Researchers will publish papers, but many companies also have Machine Learning Researchers that do research, but are less focused on publishing. There's one other job title that's sort of in-between these two which is the Applied Machine Learning Scientists, which live somewhere between Machine Learning Engineer and Machine Learning Researcher. The Machine Learning Scientists kind of does a bit of both. They are often responsible for going to the academic literature or the research literature and finding the steady VR techniques and finding ways to adapt them to the problem they are facing such as how to take the most cutting edge, trigger where the wicker detection algorithm and adapt that to your smart speaker. 
`

`
Finally, you'll also hear some people referred to AI Product Managers whose job is to help decide what to build. In other words, they help to figure out what's feasible and valuable. Traditional Product Manager's job was already to decide what to build as well as sometimes some other roles, but the AI Product Manager now has to do this in the AI era and they're needing new skill sets to figure out what's feasible and valuable in light of what AI can and cannot do today.
`

>19 Tools

When you work with ML teams, you may hear them refer to the tools that they're using to build these ML systems. We do not need to create building bricks or reinvent the wheels. Fortunately, the world today is very open, and many teams will openly share ideas and frameworks with each other. XX's ML is probably 70% or more based on Python. The UK and some of finance modeling teams prefer R. Deployment are frequently in JAVA either wrapped Python or exported directly to a JAVA object.

>20 Framework at XX

Before you begin your own ML project, leverage what's already been built! Make sure to look at the repo to find out the last time it was updated to make sure it's still beiing updated and supported. Some of these are beiing folded into the new ML platform maybe. Once again, don't reinvent the wheels and save your time on the most importnat things.

>21-24 Resources

Modeling and Analytics Conference, IEEE digital library, arXiv, and Team confluence page. 

Along with AI technology breakthroughs are also publish freely on the Internet on this website called Arxiv. Many teams will also share their code freely on GitHub. By using appropriately licensed open-source software, you can get going much faster than if you had to build everything from scratch.

>25 Future Work

These are common ML algorithms. The top 3 are supervised learning and are very common at XX. You can take multiple days classes in each of these courses but we're just going to give you an overview so you can better understand the types of algorithms that underlie ML.

>26 Bye

Just shoot us an email if you have any questions about ML. Thanks for attending my talk today.

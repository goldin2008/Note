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

Now, what is deep learning? The terms deep learning and neural network are used almost interchangeably in AI. And even though they're great for machine learning, there's also been a bit of hype and mystique about them. Let’s demystify deep learning, so that you have a sense of what deep learning and neural networks really are. Let's say you want to predict housing prices. So, you will have an input that tells you the size of the house, number of bedrooms, and number of bathrooms. Maybe location and whether it's newly renovated. To simplify the problem, let's just consider these three factors here. The most effective way to price houses would be to feed the input to a network in order to have it output the price. This big thing in the middle is called a neural network, and sometimes we also called it an artificial neural network. That's to distinguish it from the neural network in your brain. The human brain is made up of neurons. So, when we say artificial neural network, that's just to emphasize that this is not the biological brain, but this is a piece of software. What a neural network does is taking this input A, which is all these three factors, and producing output B, which is the estimated price of the house. Acutally, This big artificial neural network is just a big mathematical equation that tells it given the inputs A, how do you compute the price B.

As I said early, Today, the terms neural network and deep learning are used almost interchangeably, they mean essentially the same thing. Neural network is a very effective technique for learning A to B or input-output mappings.  

`
Many decades ago, this type of software was called a neural network. But in recent years, we found that deep learning was just a much better sounding brand, and so that for better or worse is a term that's been taken off recently. So, what do neural networks or artificial neural networks have to do with the brain? Unfortunately, it turns out almost nothing. Neural networks were originally inspired by the brain, but the details of how they work are almost completely unrelated to how biological brains work.
`

When you train a neural network, all you have to do is give it the input and output. And then the NN will figure out all of the things in the middle by itself. So to build a neural network, what you would do is feed it lots of data, or the input A, and have a neural network that just looks like this. And then you have to give it data with the price B as well. And it's the software's job to figure out what these neurons should be computing, so that it can completely learn the most accurate possible function mapping from the input to the output automatically. And it turns out that if you give this enough data and train a neural network that is big enough, this can do an incredible good job mapping from inputs to outputs. So that's a neural network, is a group of artificial neurons each of which computes a relatively simple function. But when you stack enough of them together like Lego bricks, they can compute incredibly complicated functions that give you very accurate mappings from the input to the output.

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

How many attempted XX credit card transactions per day? Branded book card has over 10 million card transactions per day.

How fast do we need to decide whether or not to approve? Have only about 10 milliseconds to make a fraud decision.

What percent of authorizations are fraudulent? Only about 0.15% of transactions are fraudulent (need to be very careful when training data)

Annual loss budget for fraudulent transactions? Transactional loss budget was $172 million for Branded Book in 2018; Partnerships added another $20 million.

>11


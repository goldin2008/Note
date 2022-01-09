### Behavior Questions
https://www.indeed.com/hire/c/info/behavioral-interview-questions-to-ask-candidates


15 top behavioral interview questions
Depending on the position you’re conducting an interview for, you can incorporate some or all of the following 15 behavioral interview questions into the process. Doing so will help you identify the right candidate for your organization.

1. Can you give me an example of a difficult problem you solved at work? How did you go about reaching a solution?


2. Tell me about a time when you made a mistake. How did you handle this experience?


3. Please share a time when you faced an unexpected challenge. How did you overcome this challenge?


4. Can you tell me about a time when things didn’t work out well?


5. Tell me about a time when you had to develop a new skill. How do you approach the learning process?
- The best way to pick it up is via learning by doing
If you’re still keen on becoming more end-to-end, we’ll now discuss how to do so. Before that, without going into specific technology, here are the buckets of skills that end-to-end data scientists commonly use:
Product: Understand customer problems, define and prioritize requirements
Communication: Facilitate across teams, get buy-in, write docs, share results
Data engineering: Move and transform data from point A to B
Data analysis: Understand and visualize data, A/B testing & inference
Machine learning: The usual plus experimentation, implementation, and metrics
Software engineering: Production code practices including unit tests, docs, logging
Dev Ops: Basic containerization and cloud proficiency, build and automation tools
(This list is neither mandatory nor exhaustive. Most projects don’t require all of them.)
Here are four ways you can move closer to being an end-to-end data scientist:
- Study the right books and courses. (Okay, this is not learning by doing but we all need to start somewhere). I would focus on courses that cover tacit knowledge rather than specific tools. While I’ve not come across such materials, I’ve heard good reviews about Full Stack Deep Learning.
- Do your own projects end-to-end to get first-hand experience of the entire process. At the risk of oversimplifying it, here are some steps I would take with their associated skills. I hear and I forget. I see and I remember. I do and I understand. – Confucius
Start with identifying a problem to solve and determining the success metric (product). Then, find some raw data (i.e., not Kaggle competition data); this lets you clean and prepare the data and create features (data engineering). Next, try various ML models, examining learning curves, error distributions, and evaluation metrics (data science).
Assess each model’s performance (e.g., query latency, memory footprint) before picking one and writing a basic inference class around it for production (software engineering). (You might also want to build a simple user interface). Then, containerise and deploy it online for others to use via your preferred cloud provider (dev ops).
Once that’s done, go the extra mile to share about your work. You could write an article for your site or speak about it at a meetup (communication). Show what you found in the data via meaningful visuals and tables (data analysis). Share your work on GitHub. Learning and working in public is a great way to get feedback and find potential collaborators.
- Volunteer through groups like DataKind. DataKind works with social organizations (e.g., NGOs) and data professionals to address humanitarian issues. By collaborating with these NGOs, you get the opportunity to work as part of a team to tackle real problems with real(ly messy) data.
While volunteers may be assigned specific roles (e.g., PM, DS), you’re always welcome to tag along and observe. You’ll see (and learn) how PMs engage with NGOs to frame the problem, define solutions, and organize the team around it. You’ll learn from fellow volunteers how to work with data to develop working solutions.
- Join a startup-like team. Note: A startup-like team is not synonymous with a startup. There are big organizations that run teams in a startup-like manner (e.g., two-pizza teams) and startups made up of specialists. Find a lean team where you’re encouraged, and have the opportunity, to work end-to-end.


6. Please share a time when you had to share or pitch an idea to someone in a more senior position. How did you go about this task, and what was the outcome?


7. Tell me about a time when you had a task to complete with a tight deadline.


8. How do you resolve situations with difficult clients?


9. Tell me about a time when you experienced conflict at work. How did you overcome it?


10. What’s one thing you’ve done in your professional history that you wish you would have handled differently?


11. As a leader, how do you motivate those who follow you?


12. Tell me about a time when you were under a lot of stress. How did you handle this pressure?


13. Please share a time when you set a goal for yourself and achieved it.
https://eugeneyan.com/writing/end-to-end-data-science/
- being end-to-end
I found this worrying. It’s difficult to be effective when the data science process (problem framing, data engineering, ML, deployment/maintenance) is split across different people. It leads to coordination overhead, diffusion of responsibility, and lack of a big picture view.
IMHO, I believe data scientists can be more effective by being end-to-end. Here, I’ll discuss the benefits and counter-arguments, how to become end-to-end, and the experiences of Stitch Fix amakend Netflix. An end-to-end data scientist can identify and solve problems with data, to deliver value. To achieve the goal, they’ll wear as many (or as little) hats as required. They’ll also learn and apply whatever tech, methodology, and process that works. Throughout the process, they ask questions such as:
What is the problem? Why is it important?
Can we solve it? How should we solve it?
What is the estimated value? What was the actual value?
For most data science roles, being more end-to-end improves your ability to make meaningful impact.
Working end-to-end provides increased context. While specialized roles can increase efficiency, it reduces context (for the data scientist) and leads to suboptimal solutions. The trick to forgetting the big picture is to look at everything close-up. – Chuck Palahniuk
It’s hard to design a holistic solution without full context of the upstream problem.
Similarly, it’s risky to develop a solution without awareness of downstream engineering and product constraints. There’s no point:
Building a near-real time recommender if infra and engineer cannot support it
Building an infinite scroll recommender if it doesn’t fit in our product and app
By working end-to-end, data scientists will have the full context to identify the right problems and develop usable solutions. It can also lead to innovative ideas that specialists, with their narrow context, might miss. Overall, it increases the ability to deliver value.
Iteration and learning rate is increased. With greater context and lesser overhead, we can now iterate, fail (read: learn), and deliver value faster.

- Communication and coordination:
Communication and coordination overhead is reduced. With multiple roles comes additional overhead. Let’s look at an example of a data engineer (DE) cleaning the data and creating features, a data scientist (DS) analysing the data and training the model, and a machine learning engineer (MLE) deploying and maintaining it. What one programmer can do in one month, two programmers can do in two months.
The DE and DS need to communicate on what data is (and is not) available, how it should be cleaned (e.g., outliers, normalisation), and which features should be created. Similarly, the DS and MLE have to discuss how to deploy, monitor, and maintain the model, as well as how often it should be refreshed. When issues occur, we’ll need three people in the room (likely with a PM) to triage the root cause and next steps to fix it.
It also leads to additional coordination, where schedules need to be aligned as work is executed and passed along in a sequential approach. If the DS wants to experiment with additional data and features, we’ll need to wait for the DE to ingest the data and create the features. If a new model is ready for A/B testing, we’ll need to wait for the MLE to (convert it to production code) and deploy it.
While the actual development work may take days, the communication back-and-forth and coordination can take weeks, if not longer. With end-to-end data scientists, we can minimize this overhead as well as prevent technical details from being lost in translation.
(But, can an end-to-end DS really do all that? I think so. While the DS might not be as proficient in some tasks as a DE or MLE, they will be able to perform most tasks effectively. If they need help with scaling or hardening, they can always get help from specialist DEs and MLEs.)
But as a PM, BA, and additional members are included, this leads to greater than linear growth in communication and coordination costs. Thus, while each additional member increases total team productivity, the increased overhead means productivity grows at a decreasing rate.

- multiple roles
Iteration and learning rate is increased. With greater context and lesser overhead, we can now iterate, fail (read: learn), and deliver value faster.
There’s greater ownership and accountability. Having the data science process split across multiple people can lead to diffusion of responsibility, and worse, social loafing.
If things get lost-in-translation or if results are unexpected, who is responsible? With a strong culture of ownership, everyone steps up to contribute in their respective roles. But without it, work can degenerate into ass-covering and finger-pointing while the issue persists and customers and the business suffers.
Having the end-to-end data scientist take ownership and responsibility for the entire process can mitigate this. They should be empowered to take action from start to finish, from the customer problem and input (i.e., raw data) to the output (i.e., deployed model) and measurable outcomes.
Diffusion of responsibility: We are less likely to take responsibility and act when there are others present. Individuals feel less responsibility and urgency to help if we know that there are others also watching the situation.
Social loafing: We exert less effort when we work in a group vs. working alone. In the 1890s, Ringelmann made people pull on ropes both separately and in groups. He measured how hard they pulled and found that members of a group tended to exert less effort in pulling a rope than did individuals alone.

For (some) data scientists, it can lead to increased motivation and job satisfaction, which is closely tied to autonomy, mastery, and purpose.
Autonomy: By being able to solve problems independently. Instead of waiting and depending on others, end-to-end data scientists are able to identify and define the problem, build their own data pipelines, and deploy and validate a solution.
Mastery: In the problem, solution, outcome from end-to-end. They can also pick up the domain and tech as required.
Purpose: By being deeply involved in the entire process, they have a more direct connection with the work and outcomes, leading to an increased sense of purpose.

- specialist experts
Being end-to-end is not for everyone (and every team) though, for reasons such as:
Wanting to specialize in machine learning, or perhaps a specific niche in machine learning such as neural text generation (read: GPT-3 primer). While being end-to-end is valuable, we also need such world-class experts in research and industry who push the envelope. Much of what we have in ML came from academia and pure research efforts.
No one achieves greatness by becoming a generalist. You don’t hone a skill by diluting your attention to its development. The only way to get to the next level is focus. – John C. Maxwell
Lack of interest. Not everyone is keen to engage with customers and business to define the problem, gather requirements, and write design documents. Likewise, not everyone is interested in software engineering, production code, unit tests, and CI/CD pipelines.
Others have also made arguments for why data scientists should specialize (and not be end-to-end).


14. Tell me about your proudest professional accomplishment and why this achievement is significant to you.


15. Tell me about your greatest professional failure and how you recovered.
Allocate tasks to team members in parallel to avoid blockers. Set up reasonable deadline as use advantages of everyone.

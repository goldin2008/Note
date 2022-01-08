### Behavior Questions
https://www.indeed.com/hire/c/info/behavioral-interview-questions-to-ask-candidates


15 top behavioral interview questions
Depending on the position you’re conducting an interview for, you can incorporate some or all of the following 15 behavioral interview questions into the process. Doing so will help you identify the right candidate for your organization.

1. Can you give me an example of a difficult problem you solved at work? How did you go about reaching a solution?


2. Tell me about a time when you made a mistake. How did you handle this experience?


3. Please share a time when you faced an unexpected challenge. How did you overcome this challenge?


4. Can you tell me about a time when things didn’t work out well?


5. Tell me about a time when you had to develop a new skill. How do you approach the learning process?


6. Please share a time when you had to share or pitch an idea to someone in a more senior position. How did you go about this task, and what was the outcome?


7. Tell me about a time when you had a task to complete with a tight deadline.


8. How do you resolve situations with difficult clients?


9. Tell me about a time when you experienced conflict at work. How did you overcome it?


10. What’s one thing you’ve done in your professional history that you wish you would have handled differently?


11. As a leader, how do you motivate those who follow you?


12. Tell me about a time when you were under a lot of stress. How did you handle this pressure?


13. Please share a time when you set a goal for yourself and achieved it.
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

- Communication and coordination:
Communication and coordination overhead is reduced. With multiple roles comes additional overhead. Let’s look at an example of a data engineer (DE) cleaning the data and creating features, a data scientist (DS) analysing the data and training the model, and a machine learning engineer (MLE) deploying and maintaining it. What one programmer can do in one month, two programmers can do in two months.
The DE and DS need to communicate on what data is (and is not) available, how it should be cleaned (e.g., outliers, normalisation), and which features should be created. Similarly, the DS and MLE have to discuss how to deploy, monitor, and maintain the model, as well as how often it should be refreshed. When issues occur, we’ll need three people in the room (likely with a PM) to triage the root cause and next steps to fix it.
It also leads to additional coordination, where schedules need to be aligned as work is executed and passed along in a sequential approach. If the DS wants to experiment with additional data and features, we’ll need to wait for the DE to ingest the data and create the features. If a new model is ready for A/B testing, we’ll need to wait for the MLE to (convert it to production code) and deploy it.
While the actual development work may take days, the communication back-and-forth and coordination can take weeks, if not longer. With end-to-end data scientists, we can minimize this overhead as well as prevent technical details from being lost in translation.
(But, can an end-to-end DS really do all that? I think so. While the DS might not be as proficient in some tasks as a DE or MLE, they will be able to perform most tasks effectively. If they need help with scaling or hardening, they can always get help from specialist DEs and MLEs.)

14. Tell me about your proudest professional accomplishment and why this achievement is significant to you.


15. Tell me about your greatest professional failure and how you recovered.
Allocate tasks to team members in parallel to avoid blockers. Set up reasonable deadline as use advantages of everyone.

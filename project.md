## Project

### Work
#### Converse Quality Assurance
There are some problems we encountered in our qa converse project, and those pain points are actually for all NLP related tasks due to lack of existing platform and support.
1. data and model storage and security issue due to github capacity limit
2. experiments, data and model versioning
3. optimum parameters/hyperparameters selection trials
4. environment and outdated libraries, dependencies test and monitoring
5. one-time code and project

To Solve theses pain points, I built a ML pipeline including data ingestion, model training, testing, refitting, deployment, monitoring and reporting.

1. Data and Models Storage
Github is not a good place to store due to security and capacity limit.
Store our data and models in S3 bucket.

2. Automation
model training, testing, refitting and deployment, experiments comparison and optimum parameters/hyperparameters selection

3. Real production environment
Since we can not test application in production directly.
We use Fastapi and built an API to make inference and test model and make sure it works in real production evnironment.

4. Automatic Reporting
EDA, model performance, environments(ibraries and dependencies) and business value.

#### Fraud
> https://shap.readthedocs.io/en/latest/index.html


#### Underwriting
Underwriting is an essential part of the insurance through which insurers assess risk and determine premiums to accept it. Evaluating and pricing risk requires extensive research on the risk profile of the customer. Consequently, manual underwriting is time-consuming, prone to errors, and can lead to inefficient pricing. This is why AI is well suited for underwriting and risk pricing processes.

> https://research.aimultiple.com/ai-underwriting/


### Code Quality Standards
> https://peps.python.org/pep-0008/ 

Python 3 cookie cutter template
===============================

.. image:: https://img.shields.io/badge/python-3.8%20%7C%203.9-green
    :target: https://www.python.org
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black

Batteries Included
------------------

The following tools are pre-configured for you if you use this ``cookiecutter`` for your project:
1. [Python packaging](https://packaging.python.org/): automatic ``pip`` install!
2. [Pre-commit](https://pre-commit.com/): automatic formatting on every commit.
3. [Pytest](https://pytest.org/en/latest/): robust Python testing framework.
4. [Mypy](http://mypy-lang.org/): static typing scanning and configuration.
5. [Pylint](https://www.pylint.org/): code analysis, and a requirement for Surge model migration.
6. [Sphinx](http://www.sphinx-doc.org/en/master/) and the
   [Furo theme](https://pradyunsg.me/furo/): build pages for your code!
7. [Black](https://black.readthedocs.io/en/stable/) and
   [isort](https://isort.readthedocs.io/en/latest/): opinionated code formatting.
8. [Check-Manifest](https://pypi.org/project/check-manifest/): never forget a static file.
9. [Tox](https://tox.readthedocs.io/en/latest/): run all of your test environments!
10. [Dockerfile](https://hub.docker.com/_/python) and
    [Jenkinsfile](https://jenkins.io/doc/book/pipeline/jenkinsfile/): continuous integration ready to go, including Checkmarx/WSD and Artifactory publishing.


### Docker and Kubernetes
> https://www.datadoghq.com/blog/monitoring-kubernetes-era/

> https://www.cncf.io/phippy/the-childrens-illustrated-guide-to-kubernetes/

> https://docs.docker.com/get-started/


### setup
https://eugeneyan.com/writing/setting-up-python-project-for-automation-and-collaboration/

1. Install a Python Version Manager
2. Set Up A Virtualenv and Install Packages
3. Set Up a Consistent Project Structure
4. Add Some Basic Methods
5. Write Some Unit Tests `pytest`, `pytest.fixture`
6. Check for Coverage `coverage run -m pytest`
7. Lint to Ensure Consistency `pylint`
8. Check For Type Errors `mypy src`
9. Build a Wrapper For Developer Experience `Makefile`
10. Automate Checks with each `git push`

### ssh
> https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent

### ml testing
https://github.com/eugeneyan/testing-ml

https://eugeneyan.com/writing/testing-ml/

### ml design doc
https://github.com/eugeneyan/ml-design-docs

### Onboarding
DjangoCon 2014 - Technical Onboarding, Training, and Mentoring
> https://av.tib.eu/media/32852

> https://www.youtube.com/watch?v=B1dZ3AjRJJI

### ### Retain DS
> https://www.techrepublic.com/article/7-guerrilla-tactics-for-retaining-data-scientists/


1. Overview:
A summary of the doc's purpose, problem, solution, and desired outcome, usually in 3-5 sentences.

2. Motivation:
Why the problem is important to solve, and why now.

3. Success metrics:
Usually framed as business goals, such as increased customer engagement (e.g., CTR, DAU), revenue, or reduced cost.

4. Requirements & Constraints:
Functional requirements are those that should be met to ship the project. They should be described in terms of the customer perspective and benefit. (See [this](https://eugeneyan.com/writing/ml-design-docs/#the-why-and-what-of-design-docs) for more details.)

Non-functional/technical requirements are those that define system quality and how the system should be implemented. These include performance (throughput, latency, error rates), cost (infra cost, ops effort), security, data privacy, etc.

Constraints can come in the form of non-functional requirements (e.g., cost below $`x` a month, p99 latency < `y`ms)
- 4.1 What's in-scope & out-of-scope?
Some problems are too big to solve all at once. Be clear about what's out of scope.

5. Methodology
- 5.1. Problem statement:
How will you frame the problem? For example, fraud detection can be framed as an unsupervised (outlier detection, graph cluster) or supervised problem (e.g., classification).
- 5.2. Data:
What data will you use to train your model? What input data is needed during serving?
- 5.3. Techniques:
What machine learning techniques will you use? How will you clean and prepare the data (e.g., excluding outliers) and create features?
- 5.4. Experimentation & Validation:
How will you validate your approach offline? What offline evaluation metrics will you use?

If you're A/B testing, how will you assign treatment and control (e.g., customer vs. session-based) and what metrics will you measure? What are the success and [guardrail](https://medium.com/airbnb-engineering/designing-experimentation-guardrails-ed6a976ec669) metrics?
- 5.5. Human-in-the-loop:
How will you incorporate human intervention into your ML system (e.g., product/customer exclusion lists)?

6. Implementation
- 6.1. High-level design:
![](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2e/Data-flow-diagram-example.svg/1280px-Data-flow-diagram-example.svg.png)

Start by providing a big-picture view. [System-context diagrams](https://en.wikipedia.org/wiki/System_context_diagram) and [data-flow diagrams](https://en.wikipedia.org/wiki/Data-flow_diagram) work well.
- 6.2. Infra:
How will you host your system? On-premise, cloud, or hybrid? This will define the rest of this section
- 6.3. Performance (Throughput, Latency):
How will your system meet the throughput and latency requirements? Will it scale vertically or horizontally?
- 6.4. Security:
How will your system/application authenticate users and incoming requests? If it's publicly accessible, will it be behind a firewall?
- 6.5. Data privacy:
How will you ensure the privacy of customer data? Will your system be compliant with data retention and deletion policies (e.g., [GDPR](https://gdpr.eu/what-is-gdpr/))?
- 6.6. Monitoring & Alarms:
How will you log events in your system? What metrics will you monitor and how? Will you have alarms if a metric breaches a threshold or something else goes wrong?
- 6.7. Cost:
How much will it cost to build and operate your system? Share estimated monthly costs (e.g., EC2 instances, Lambda, etc.)
- 6.8. Integration points:
How will your system integrate with upstream data and downstream users?
- 6.9. Risks & Uncertainties:
Risks are the known unknowns; uncertainties are the unknown unknows. What worries you and you would like others to review?

7. Appendix:
- 7.1. Alternatives:
What alternatives did you consider and exclude? List pros and cons of each alternative and the rationale for your decision.
- 7.2. Experiment Results:
Share any results of offline experiments that you conducted.
- 7.3. Performance benchmarks:
Share any performance benchmarks you ran (e.g., throughput vs. latency vs. instance size/count).
- 7.4. Milestones & Timeline:
What are the key milestones for this system and the estimated timeline?
- 7.5. Glossary:
Define and link to business or technical terms.
- 7.6. References:
Add references that you might have consulted for your methodology.

---
### Other templates, examples, etc
- [A Software Design Doc](https://www.industrialempathy.com/posts/design-doc-a-design-doc/) `Google`
- [Design Docs at Google](https://www.industrialempathy.com/posts/design-docs-at-google/) `Google`
- [Product Spec of Emoji Reactions on Twitter Messages](https://docs.google.com/document/d/1sUX-sm5qZ474PCQQUpvdi3lvvmWPluqHOyfXz3xKL2M/edit#heading=h.554u12gw2xpd) `Twitter`
- [Design Docs, Markdown, and Git](https://caitiem.com/2020/03/29/design-docs-markdown-and-git/) `Microsoft`
- [Pitch for To-Do Groups and Group Notifications](https://basecamp.com/shapeup/1.5-chapter-06#examples) `Basecamp`
- [The Anatomy of a 6-pager](https://writingcooperative.com/the-anatomy-of-an-amazon-6-pager-fc79f31a41c9) and an [example](https://docs.google.com/document/d/1LPh1LWx1z67YFo67DENYUGBaoKk39dtX7rWAeQHXzhg/edit) `Amazon`

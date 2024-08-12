## LLMs interview prep

### LLM based application
Besides just building our LLM application, we’re also going to be focused on scaling and serving it in production. Unlike traditional machine learning, or even supervised deep learning, scale is a bottleneck for LLM applications from the very beginning. Large datasets, models, compute intensive workloads, serving requirements, etc. We’ll develop our application to be able to handle any scale as the world around us continues to grow. We’re also going to be focused on evaluation and performance. Our application involves many moving pieces: embedding models, chunking logic, the LLM itself, etc. and so it's important that we experiment with different configurations to optimize for the best quality responses. However, it's non-trivial to evaluate and quantitatively compare different configurations for a generative task. We’re going to break down evaluation of individual parts of our application (retrieval given query, generation given source), also assess the overall performance (end-to-end generation) and share findings towards an optimized configuration.
With large data sources, models and application serving needs, scale is a day-1 priority for LLM applications. We want to build our applications in such a way that they can scale as our needs grow without us having to change our code later.

#### evaluating Large language models

`Evaluation metrics`
Evaluation metrics for LLM can be broadly classified into traditional and nontraditional metrics. Traditional evaluation metrics rely on the arrangement and order of words and phrases in the text and are used in combination where a reference text (ground truth) exists to compare the predictions against. Nontraditional metrics make use of semantic structure and capabilities of language models for evaluating generated text. These techniques can be used with and without a reference text.

`Traditional metrics`
In this section, we will review some of the popular traditional metrics and their use cases. These metrics operate on the character/word/phrase level.
- WER (Word Error Rate): There is a family of WER-based metrics which measure the edit distance 𝑑 (𝑐, 𝑟), i.e., the number of insertions, deletions, substitutions and, possibly, transpositions required to transform the candidate into the reference string.
- Exact match: measures the accuracy of candidate text by matching the generated text with the reference text. Any deviation from reference text will be counted as incorrect. This is only suitable in the case of extractive and short-form answers where minimal or no deviation from the reference text is expected.
- BLEU (Papineni et al.): evaluates candidate text based on how many ngrams in the generated text appear in reference text. This was originally proposed to evaluate machine translation systems. Multiple n-gram scores (2gram/3gram) can be calculated and combined using geometric average (BLEU-N). Since it is a precision-based metric, it does not penalize False negatives.
- ROGUE (Lin et al. 2004): This is similar to BLEU-N in counting n-gram matches but is based on recall. A variation of ROGUE, ROUGE-L measures the longest common subsequence (LCS) between a pair of sentences.
Other than these, there are other metrics like METEOR, General Text Matcher (GTM), etc. These metrics are very much constrained and do not go along with the current generational capabilities of large language models. Even though these metrics are currently only suited for tasks and datasets with short-form, extractive, or multi-choice answers, these methods or derivatives are still used as evaluation metrics in many of the benchmarks.

`Nontraditional metrics`
Nontraditional metrics for evaluating generated text can be further classified as embedding-based and LLM-assisted methods. While embedding-based methods leverage token or sentence vectors produced by deep learning models LLM assisted methods to form paradigms and leverage language models' capabilities to evaluate candidate text.
- Embedding based methods
The key idea here is to leverage vector representation of text from DL models that represent rich semantic and syntactic information to compare the candidate text to reference text. The similarity of candidate text with reference text is quantified using methods such as cosine similarity.
  - BERTScore (Zhang et al. 2019): This is a bi-encoded-based approach, ie the candidate text and reference text are fed into the DL model separately to obtain embeddings. The token-level embeddings are then used to calculate the pairwise cosine similarity matrix. Then similarity scores of most similar tokens from reference to candidates are selected and used to calculate precision, recall, and f1 score.
  - MoverScore (Zhao et al. 2019): uses the concept of word movers distance which suggests that distances between embedded word vectors are to some degree semantically meaningful ( vector(king) - vector(queen) = vector(man) ) and uses contextual embeddings to calculate Euclidean similarity between n-grams. In contrast to BERTscore which allows one-to-one hard matching of words, MoverScore allows many-to-one matching as it uses soft/partial alignments.
  Even though embeddings-based methods are robust they assume that training and test data are identically distributed which may not always be the case.

- Other Language model-based metrics
  - Entailment score: This method leverages the natural language inference capabilities of language models to judge NLG. There are different variants of this method but the basic concept is to score the generation by using an NLI model to produce the entailment score against the reference text. This method can be very useful to ensure faithfulness for text-grounded generation tasks like text summarization.
  - BLEURT (Sellam et al.): Introduces an approach to combine expressivity and robustness by pre-training a fully learned metric on large amounts of synthetic data, before fine-tuning it on human ratings. The method makes use of the BERT model to achieve this. To generalize the model for evaluating any new task or domain a new pre-training approach was proposed which involves an additional pre-training on synthetic data. Text segments from Wikipedia are collected and then augmented with techniques like word-replacements, back-translation, etc to form synthetic pairs $(x,x')$ and then trained on objectives like BLUE, ROGUE scores, back-translation probability, natural language inference, etc.
  - `Question Answering - Question generation (QA-QG)` (Honovich et. al): This paradigm can be used to measure the consistency of any candidate with reference text. The method works by first forming pairs of (answer candidates, questions) from the candidate text and then comparing and verifying the answers generated for the same set of questions given the reference text.

- LLM assisted methods
As the name indicates the methods discussed in this section make use of large language models to evaluate LLM generations. The caveat here is to leverage LLMs capabilities and form paradigms to minimize the effect of different biases that LLMs might have like preferring one’s own output over other LLMs' output.
  - G-Eval (Liu et al. 2023) is also a very similar approach to GPTscore as the generated text is evaluated based on the criteria but unlike GPTscore directly performs evaluation by explicitly instructing the model to assign a score to generated text in the 0 to 5 range. LLMs as known to have some bias during score assignment like preferring integer scores and bias towards particular numbers in the given range (for example 3 in 0-5 scale). To tackle the output score is multiplied by the token probability
  Even though both of these methods can be used for multi-aspect evaluating including factuality, a better method to detect and quantify hallucinations without a reference text was proposed in SelfCheckGPT (Manakul et al. 2023) which leverages the simple idea that if an LLM has knowledge of a given concept, sampled responses are likely to be similar and contain consistent facts. To measure information consistency between the generated responses one can use the QA-QG paradigm, BERTScore, Entailment score, n-gram, etc.

- Tools
  - OpenAI Evals
  Evals is an open-source framework for evaluating LLM generations. Using this framework you can evaluate the completions for instructions against a reference ground truth that you have defined. It gives the flexibility to modify and add datasets, and new completions (for example, chain of thoughts). An eval dataset should be in the format shown
  - Ragas
  Ragas is a framework that helps you evaluate your Retrieval Augmented Generation (RAG) pipelines. RAG denotes a class of LLM applications that use external data to augment the LLM’s context. There are existing tools and frameworks that help you build these pipelines but evaluating it and quantifying your pipeline performance can be hard. This is where Ragas (RAG Assessment) comes in.
  Ragas provides you with the tools based on the latest research for evaluating LLM-generated text to give you insights about your RAG pipeline. Ragas can be integrated with your CI/CD to provide continuous checks to ensure performance.


#### Prompt engineering
`Elements of Prompt`
A prompt may contain the following:
- Instruction: Task or instruction for the model (eg: classify, summarize, …)
- Input: Input statement or question for the model to generate a response.
- Context: Additional relevant information to guide the model’s response (eg: examples to help the model better understand the task.)
- Output Format: Specific type or format of the output generated by the model.
Not all four elements are necessary for a prompt, and the format depends on the specific task being performed.

`Type of Prompting Techniques`
- `Zero-shot Prompting`
Zero-shot prompting refers to the ability of an AI model to generate meaningful responses or complete tasks without any prior training on specific prompts. The larger and more capable the LLM, the better results zero-shot prompting will yield.
Note that in the prompt above we didn't provide the model with any examples of text alongside their classifications, the LLM already understands "sentiment" -- that's the zero-shot capabilities at work.
When zero-shot doesn't work, it's recommended to provide demonstrations or examples in the prompt which leads to few-shot prompting.
- `Few-shot Prompting`
In contrast to zero-shot prompting, few-shot prompting involves training an AI model with only a small amount of data or examples (also called "shots")
This technique allows the model to quickly adapt and generate responses based on limited examples, plus the instructions provided by the user.
Examples can guide the model, but do not always enhance its performance. Sometimes a well crafted zero short prompt can be more effective than providing multiple examples.
- `Chain-of-Thought Prompting`
Chain-of-Thought (CoT) prompting is technique that breaks down complex tasks through intermediate reasoning steps. This allows LLMs to overcome difficulties with some reasoning tasks that require logical thinking and multiple steps to solve, such as arithmetic or commonsense reasoning questions.
This encourages model to explain it’s reasoning process by decomposing the solution into a series of steps, mimicking human-like conversation flow. This behaviour can be facilitated through various strategies (Zero shot, few short, etc).
This is a basis for other prompting techniques such as ReAct which separates out the task’s decomposition and it’s solving.
- `ReAct Prompting`
CoT aims to imitate how humans think about problems, but it lack access to the external world or inability to update its knowledge which lead to issues like fact hallucination and error propagation, which is where ReAct Prompting is useful.
ReAct allows language models to generate verbal reasoning traces and text actions concurrently.
Actions receive feedback from the external environment ("Env"), while reasoning traces update the model's internal state by reasoning over the context and incorporating useful information for future reasoning and action.
As shown below, there are various types of useful reasoning traces, e.g., decomposing task goals to create action plans, injecting commonsense knowledge relevant to task solving, and so on.

Therefore, in order to implement ReAct, you need:
- An environment where a text action is chosen from various options based on the environment's internal state and then generates a text observation in response.
- An output parser framework that stops text generation after producing a valid action, executes it in the environment, and returns the observation by appending it to the generated text so far and prompting the LLM.
- Human-generated examples of intermixed thoughts, actions, and observations in the environment to use for few-shot learning.
Langchain provides a mechanism to implement ReAct through framework like Agents and Tools. We will cover these in details in upcoming editions where I’ll demonstrate these concepts in action through developing LLM powered applications.
Although there are other prompting techniques like TreeOfThought (ToT), Self-consistency, and Automatic Prompt Engineer (APE), the above method lays a foundational ground for building more complex LLM applications.



## References

RAG:
> https://mindfulmatrix.substack.com/p/build-a-simple-llm-application-with

> https://mindfulmatrix.substack.com/p/prompting-in-the-age-of-llms

> https://mindfulmatrix.substack.com/p/unveiling-the-revolutionary-architecture

> https://jalammar.github.io/illustrated-transformer/

> https://www.linkedin.com/posts/sagarg55_what-are-some-good-starting-points-for-diving-activity-7180054059981164544-2qq-/?utm_source=share&utm_medium=member_desktop

## LLMs interview prep

### LLM based application
Besides just building our LLM application, we’re also going to be focused on scaling and serving it in production. Unlike traditional machine learning, or even supervised deep learning, scale is a bottleneck for LLM applications from the very beginning. Large datasets, models, compute intensive workloads, serving requirements, etc. We’ll develop our application to be able to handle any scale as the world around us continues to grow. We’re also going to be focused on evaluation and performance. Our application involves many moving pieces: embedding models, chunking logic, the LLM itself, etc. and so it's important that we experiment with different configurations to optimize for the best quality responses. However, it's non-trivial to evaluate and quantitatively compare different configurations for a generative task. We’re going to break down evaluation of individual parts of our application (retrieval given query, generation given source), also assess the overall performance (end-to-end generation) and share findings towards an optimized configuration.
With large data sources, models and application serving needs, scale is a day-1 priority for LLM applications. We want to build our applications in such a way that they can scale as our needs grow without us having to change our code later.

### evaluating Large language models
#### Evaluator
We're going to start by determining our evaluator. Given a response to a query and relevant context, our evaluator should be a trusted way to score/assess the quality of the response. But before we can determine our evaluator, we need a dataset of questions and the source where the answer comes from. We can use this dataset to ask our different evaluators to provide an answer and then rate their answer (ex. score between 1-5). We can then inspect this dataset to determine if our evaluator is unbiased and has sound reasoning for the scores that are assigned.

We’re evaluating the ability of our LLM to generate a response given the relevant context. This is a component-level evaluation (quality_score (LLM)) because we aren’t using retrieval to fetch the relevant context.

We'll start by manually creating our dataset (keep reading if you can’t manually create a dataset). We have a list of user queries and the ideal source to answer the query datasets/eval-dataset-v1.jsonl. We will use our LLM app above to generate reference answers for each query/source pair using gpt-4.

Each data point has a question and the labeled source that has the precise context with the answer to the question.
We can extract the text from this context and pass it to our LLM to generate a response to the question. We’re also going to ask it to score the quality of its response for the query.

We can now create a dataset with question, source, answer, score and reasoning. We can inspect this to determine if our evaluator is of high quality.
- question:"I’m struggling a bit with Ray Data type conversions when I do map_batches.
Any advice?"
- source:"https://docs.ray.io/en/master/data/transforming-data.html#configuring-batch-format"
- answer:"You can configure the batch type in Ray Data by specifying the 'batch_format' in the 'map_batches()' function. If you're working with NumPy ndarrays, your function should return a dict of ndarrays. If you're working with pandas DataFrames, your function should return a DataFrame. Make sure your function is returning the correct type based on your specified 'batch_format'."
- score:5
- reasoning:"The context provides clear instructions on how to configure the batch type in Ray Data and how to use the 'map_batches()' function. It also provides examples for both NumPy and pandas, which directly answers the query."

We found that gpt-4 was a high quality evaluator based on the scores and reasonings it provided. We performed the same evaluation with other LLMs (ex. Llama-2-70b) and we found that they lacked the appropriate reasoning and were very generous with responses from themselves.

#### Cold Start
We may not always have `a prepared dataset of questions and the best source to answer that question readily` available. To address this cold start problem, we could use an LLM to look at our `text chunks` and `generate questions that the specific chunk would answer`. This provides us with `quality questions` and `the exact source the answer is in`. However, this dataset generation method could be a bit noisy. `The generated questions may not always have high alignment to what our users may ask`. And `the specific chunk we say is the best source may also have that exact information in other chunks`. Nonetheless, this is a great way to start our development process while we `collect + manually label` a high quality dataset.



#### Evaluation
Our evaluation workflow will use our evaluator to assess the end-to-end quality (quality_score (overall)) of our application since the response depends on the retrieved context and the LLM. But we’ll also include a retrieval_score to measure the quality of our retrieval process (chunking + embedding). Our logic for determining the retrieval_score registers a success if the best source is anywhere in our retrieved num_chunks sources. We don't account for order, exact page section, etc. but we could add those constraints to have a more conservative retrieval score.

Regardless of what configuration(s) we want to evaluate, we’ll need to first generate responses using that configuration and then evaluate those responses using our evaluator.
- Context: without-context vs. with-context
- Chunk size
- Number of chunks
- Embedding models
  - gte-base
  - gte-large
  - bge-large-en
  - text-embedding-ada-002
- OSS vs. closed LLMs
Open-Source LLM vs Closed Source LLM
  - llms = ["gpt-3.5-turbo",
        "gpt-4",
        "gpt-4-1106-preview",
        "meta-llama/Llama-2-7b-chat-hf",
        "meta-llama/Llama-2-13b-chat-hf",
        "meta-llama/Llama-2-70b-chat-hf",
        "codellama/CodeLlama-34b-Instruct-hf",
        "mistralai/Mistral-7B-Instruct-v0.1",
        "mistralai/Mixtral-8x7B-Instruct-v0.1"]
- MoEs without context
Curious how well these mixture of experts (MoE) fare without any context.


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

#### Fine-tuning
Everything we have explored so far involves optimizing for how our data is preprocessed and using our models (embedding, LLM, etc.) as is. However, it's also worth exploring fine-tuning our models with data unique to our use case. This could help us better represent our data and ultimately increase our retrieval and quality scores. In this section, we're going to fine-tune our embedding model. The intuition here is that it may be worth it to learn a more contextual representation of our tokens than the default embedding models can. This can especially be impactful if we have a lot of:
- new tokens that the default tokenization process creates subtokens out of that lose the significance of the token
- existing tokens that have contextually different meanings in our use case
When it comes to fine-tuning our embedding model, we will exploring two approaches:
- full parameter: including the embedding layer and all subsequent encoder layers (transformer blocks)
- embedding layer: to better represent our unique subtokens and avoid overfitting (version of linear adapter)

`Synthetic dataset`
Our first step will be to create a dataset to fine-tune our embedding model on. Our current embedding models have been trained via self-supervised learning (word2vec, GloVe, next/masked token prediction, etc.) and so we will continue fine-tuning with a self-supervised workflow. We're going to reuse a very similar approach as our cold start QA dataset section earlier so that we can map sections in our data to questions. The fine-tuning task here will be for the model to determine which sections in our dataset maps best to the input query. This optimization task will allow our embedding model to learn better representations of tokens in our dataset.

Note: While we could create a dataset mapping section titles with section text, we are creating a synthetic Q&A dataset because it will be most representative of the types of data we want to learn how to embed.

Our prompt is going to be a bit different because we want to generate a variety of different questions and we're going to use llama-70b here so that we can scale this QA generation process (and avoid any rate limits). To be thorough, we're going to generate one question from every section in our dataset so that we can try to capture as many unique tokens as possible.

`Validation`
While our dataset may have multiple valid sections for a particular query, we will treat all other sections besides the one used to generate the query, as negative samples. This isn't an ideal scenario but the noise introduced is minimal, especially since we are using this to tune a representation layer (and not for a classification task).

We'll be using MultipleNegativesRankingLoss as our loss function. It will use the data points (InputExample(texts=[query, source_text]) in our training data as positive pairs and all other combinations as negative pairs. And the objective will be to increase the cosine similarity (default similarity_fct) for our positive pair and decrease it for the other pairs.

`Resize tokenizer`
While our tokenizer can represent new subtokens that are part of the vocabulary, it might be very helpful to explicitly add new tokens to our base model (BertModel) in our cast to our transformer. And then we can use resize_token_embeddings to adjust the model's embedding layer prior to fine-tuning. This can be very useful for contextual use cases, especially if many tokens are new or existing tokens have a very different meaning in our context.

`Optimization techniques for fine-tuning`
For fine-tuning, the combination of appropriate optimizations and an orchestrator lays the foundation for constructing large language models for production.
- Parameter-efficient fine-tuning: Parameter-efficient fine-tuning, or PEFT, focuses on fine-tuning only a small subset of additional model parameters, resulting in substantial reductions in both computational and storage costs. Remarkably, these techniques achieve performance levels that are comparable to full fine-tuning approaches. A widely used PEFT technique is Low Rank Adaptation, or LoRA. LoRA is an approach that trims down model size and computational needs by approximating large matrices through low-rank decomposition.
- Quantization: Quantization is the process of reducing the precision of numerical data so it consumes less memory and increases processing speed. One library that may be of interest to fine-tuners is the bitsandbytes library, which uses 8-bit optimizers to significantly reduce the memory footprint during model training.
- Zero-redundancy optimization: Zero Redundancy Optimizer, commonly known as ZeRO, harnesses the collective computational and memory capabilities of data parallelism. This approach minimizes the memory and computational demands on each device (GPU) utilized during model training. ZeRO accomplishes this by distributing the model training states (weights, gradients and optimizer states) across the available devices (GPUs and CPUs) within the distributed training hardware, thereby decreasing the memory consumption of each GPU.


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

#### Lexical search
We're going to now supplement our vector embedding based search with traditional lexical search, which searches for exact token matches between our query and document chunks. Our intuition here is that lexical search can help identify chunks with exact keyword matches where semantic representation may fail to capture. Especially for tokens that are out-of-vocabulary (and so represented via subtokens) with our embedding model. But our embeddings based approach is still very advantageous for capturing implicit meaning, and so we're going to combine several retrieval chunks from both vector embeddings based search and lexical search.

#### Reranking
So far with all of our approaches, we've used an embedding model (+ lexical search) to identify the top k relevant chunks in our dataset. The number of chunks (k) has been a small number because we found that adding too many chunks did not help and our LLMs have restricted context lengths. However, this was all under the assumption that the top k retrieved chunks were truly the most relevant chunks and that their order was correct as well. What if increasing the number of chunks didn't help because some relevant chunks were much lower in the ordered list. And, semantic representations, while very rich, were not trained for this specific task.

In this section, we implement reranking so that we can use our semantic and lexical search methods to cast a much wider net over our dataset (retrieve many chunks) and then rerank the order based on the user's query. The intuition here is that we can account for gaps in our semantic representations with ranking specific to our use case. We'll train a supervised model that predicts which part of our documentation is most relevant for a given user's query. We'll use this prediction to then rerank the relevant chunks so that chunks from this part of our documentation are moved to the top of the list.

Note: we didn't omnisciently know to create these unique preprocessing functions! This is all a result of methodical iteration. We train a model → view incorrect data points → view how the data was represented (ex. subtokenization) → update preprocessing → iterate ↺

Now we’re going to train a simple logistic regression model that will predict the tag given the input text.
Note: we also trained a BERT classifier and while performance was better than our logistic classifier, these large networks suffer from overconfidence and we can't use a threshold based approach as we do below. And without the threshold approach (where we only rerank when the reranker is truly confident), then the quality score of our application does not improve.

- Reranking experiments
Now we're ready to apply our reranking model post retrieval using these steps:
 - Increase the retrieved context (can experiment with this) so that we can apply reranking to yield a smaller subset (num_chunks). The intuition here is that we'll use semantic and lexical search to retrieve N chunks (N > k) and then we'll use reranking to reorder the retrieved results (top k).
 - If the predicted tag is above the threshold, then we will move all retrieved sources from that tag to the top. If the predicted tag is below the threshold, then no reranking will be performed. The intuition here is that, unless we are confident about which parts of our documentation a specific query pertains to (or if it happens to involve multiple parts), then we will not incorrectly rerank the results.
 - Perform generation using the top k retrieved chunks.

### Cost analysis
Besides just performance, we also want to evaluate the cost of our configurations (especially given the high price points of larger LLMs). We’re going to break this down into prompt and sampled pricing. The prompt size is the number of characters in our system, assistant and user contents (which includes the retrieved contexts). And the sampled size is the number of characters the LLM generated in its response.

### Routing
It seems that the most performant LLM, gpt-4-turbo, is also very expensive. While our OSS LLM (mixtral-8x7b-instruct-v0.1) is very close in quality but ~25X more cost-effective. However, we want to be able to serve the most performant and cost-effective solution. We can close this gap in performance between open source and proprietary models by routing queries to the right LLM according to the complexity or topic of the query. For example, in our application, open source models perform really well on simple queries where the answer can be easily inferred from the retrieved context. However, the OSS models fall short for queries that involve reasoning, numbers or code examples. To identify the appropriate LLM to use, we can train a classifier that takes the query and routes it to the best LLM.

In order to implement this, we hand-annotated a dataset of 1.8k queries according to which model (gpt-4 (label=0) or OSS LLM (label=1)) would be appropriate -- by default we route to OSS LLM and only if the query needs more advanced capabilities do we send the query to gpt-4. We then evaluate the performance of the model on a test dataset that has been scored with an evaluator.

Note: For our dataset, a small logistic regression model is good enough to perform the routing. But if your use case is more complex, consider training a more complex model, like a BERT-based classifier to perform the classification. These models are still small enough that wouldn’t introduce too much latency. Be sure to check out this guide if you want to learn how to train and deploy supervised deep learning models.

### Impact
`Products and productivity`
Building an LLM application like this has had a tremendous impact on our products and company. There were expected 1st order impacts in overall developer and user adoption for our products. The capability to interact and solve problems that our users experience in a self-serve and immediate manner is the type of feature that would improve the experience of any product. It makes it significantly easier for people to succeed and it elevated the perception around LLM applications from a nice-to-have to a must-have.

`Foundational agents`
However, there were also some 2nd order impacts that we didn’t immediately realize. For example, when we further inspected user queries that yielded poor scores, often the issue existed because of a gap in our documentation. When we made the fix (ex. added the appropriate section to our docs), this improved our product and the LLM application itself — creating a very valuable feedback flywheel. Furthermore, when internal teams learned of the capabilities of our LLM application, this generated the development of highly valuable LLM applications that depend on this Ray docs LLM application as one of its foundational agents that it uses to perform its tasks.

## References

RAG:
*** > https://www.anyscale.com/blog/a-comprehensive-guide-for-building-rag-based-llm-applications-part-1#response-generation

> https://mindfulmatrix.substack.com/p/build-a-simple-llm-application-with

> https://mindfulmatrix.substack.com/p/prompting-in-the-age-of-llms

> https://mindfulmatrix.substack.com/p/unveiling-the-revolutionary-architecture

> https://jalammar.github.io/illustrated-transformer/

> https://www.linkedin.com/posts/sagarg55_what-are-some-good-starting-points-for-diving-activity-7180054059981164544-2qq-/?utm_source=share&utm_medium=member_desktop

> https://www.anyscale.com/blog/end-to-end-llm-workflows-guide?__hstc=218704582.00f159e343060f6b070803af47ca3180.1723166370722.1723166370722.1723166370722.1&__hssc=218704582.3.1723166370722&__hsfp=4274120786

> https://www.union.ai/blog-post/large-language-models-in-production

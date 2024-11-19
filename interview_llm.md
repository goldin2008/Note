## LLMs interview prep
### LLMOps
We will implement a `continuous integration and continuous deployment (CI/CD)` pipeline to test the integrity of our code and automate the deployment process, a `continuous training (CT)` pipeline to automate our training, and a monitoring pipeline to track all our prompts and generated answers. This is a natural progression in any ML project, regardless of whether you use LLMs.

 We will implement a `CI/CD pipeline using GitHub Actions`, a `CT and alerting pipeline using ZenML`, and a `monitoring pipeline using Opik from Comet ML`.

let’s look over the core flow of running a pipeline in the cloud that we will learn to implement, presented in Figure 11.5:
- Build a Docker image that contains all the system dependencies, the project dependencies, and the LLM Twin application.
- Push the Docker image to ECR, where SageMaker can access it.
- Now, we can trigger any pipeline implemented during this book either from the CLI of our local machine or ZenML’s dashboard.
- Each step from ZenML’s pipeline will be mapped to a SageMaker job that runs on an AWS EC2 virtual machine (VM). Based on the dependencies between the directed acyclic graph (DAG) steps, some will run in parallel and others sequentially.
- When running a step, SageMaker pulls the Docker image from ECR, defined in step 2. Based on the pulled image, it creates a Docker container that executes the pipeline step.
- As the job is executed, it can access the S3 artifact storage, MongoDB, and Qdrant vector DB to query or push data. The ZenML dashboard is a key tool, providing real-time updates on the pipeline’s progress and ensuring a clear view of the process.

### Evaluate LLM System
`Model evaluation`
  - `General-purpose LLM evaluations`: We can broadly categorize general-purpose evaluations in three phases: during pre-training, after pre-training, and after fine-tuning.
  - `Domain-specific LLM evaluations`
  - `Task-specific LLM evaluations`:
  For example, a summarization task can leverage the
  `Recall-Oriented Understudy for Gisting Evaluation (ROUGE)` metric, which measures the overlap between the generated text and reference text using n-grams.
  Likewise, classification tasks also benefit from it and use the following classic metrics, among others:
  `Accuracy`: Accuracy refers to the proportion of correctly predicted instances compared to the total instances. It’s particularly useful for tasks with categorical outputs or where there is a clear distinction between right and wrong answers, such as named entity recognition (NER).
  `Precision`: The ratio of true positive predictions to the total positive predictions made by the model.
  `Recall`: The ratio of true positive predictions to the total actual positive instances.
  `F1 Score`: The harmonic mean of precision and recall, used to balance both metrics. These are particularly useful in tasks such as classification or entity extraction.

`RAG evaluation`

The evaluation of RAG systems goes beyond assessing a standalone LLM. It requires examining the entire system’s performance, including:
  - Retrieval accuracy: How well does the system fetch relevant information?
  - Integration quality: How effectively is the retrieved information incorporated into the generated response?
  - Factuality and relevance: Does the final output address the query appropriately while seamlessly blending retrieved and generated content?

- `Ragas`: `Retrieval-Augmented Generation Assessment (Ragas)`
  - `Faithfulness`: This metric measures the factual consistency of the generated answer against the given context. It works by breaking down the answer into individual claims and verifying if each claim can be inferred from the provided context. The faithfulness score is calculated as the ratio of verifiable claims to the total number of claims in the answer.
  - `Answer relevancy`: This metric evaluates how pertinent the generated answer is to the given prompt. It uses an innovative approach where an LLM is prompted to generate multiple questions based on the answer and then calculates the mean cosine similarity between these generated questions and the original question. This method helps identify answers that may be factually correct but off-topic or incomplete.
  - `Context precision`: This metric evaluates whether all the ground-truth relevant items present in the contexts are ranked appropriately. It considers the position of relevant information within the retrieved context, rewarding systems that place the most pertinent information at the top.
  - `Context recall`: This metric measures the extent to which the retrieved context aligns with the annotated answer (ground truth). It analyzes each claim in the ground truth answer to determine whether it can be attributed to the retrieved context, providing insights into the completeness of the retrieved information.
- `ARES`:
  `ARES (an automated evaluation framework for RAG systems)` is a comprehensive tool designed to evaluate RAG systems. It offers an automated process that combines synthetic data generation with fine-tuned classifiers to assess various aspects of RAG performance, including `context relevance`, `answer faithfulness`, and `answer relevance`.
  The ARES framework operates in three main stages: `synthetic data generation`, `classifier training`, and `RAG evaluation`. Each stage is configurable, allowing users to tailor the evaluation process to their specific needs and datasets.


### Large-Language Foundation Models
Some models may use slight variations of the original Transformer architecture to optimize for specific language tasks. This may cause issues if you try to swap out models during development, so it’s important to conduct enough research before you begin development to prevent this from happening.

Fear of missing out (FOMO) may tempt you to swap out a newer generative model before completing your evaluation of the current model. Try to avoid this temptation and complete your testing with a single model—or set of models—before chasing the latest and greatest leaderboard winner.
- Tokenizers
- Embedding Vectors
- Transformer Architecture
  - Inputs and Context Window
  - Embedding Layer
  - Encoder
  - Self-Attention
  - Decoder
  - Softmax Output

Types of Transformer-Based Foundation Models
- `Encoder-only models, or autoencoders`, are pretrained using a technique called masked language modeling (MLM), which randomly mask input tokens and try to predict the masked tokens. This is sometimes called a denoising objective. Autoencoding models use bidirectional representations of the input to better understand the full context of a token—not just the previous tokens in the sequence.
Encoder-only models are best suited for language tasks that utilize the embeddings generated by the encoder, such as `text classification`. They are not particularly useful for generative tasks that continue to generate more text. A well-known encoder-only model is `BERT`.
- `Decoder-only models, or autoregressive models`, are pretrained using unidirectional causal language modeling (CLM), which predicts the next token using only the previous tokens—every other token is masked.
Decoder-only, autoregressive models use millions of text examples to learn a statistical language representation by continuously predicting the next token from the previous tokens. These models are the standard for generative tasks, including `question-answer`. The families of `GPT-3, Falcon, and LLaMA models` are well-known autoregressive models.
- `Encoder-decoder models, often called sequence-to-sequence models`, use both the Transformer encoder and decoder. While the pretraining objectives vary from model to model, the popular T5 foundation model (e.g., FLAN-T5) was pretrained using consecutive multitoken masking called span corruption. The decoder then attempts to reconstruct the masked sequence of tokens.
Sequence-to-sequence models, originally designed for `translation`, are also very useful for `text-summarization` tasks. `T5 and its fine-tuned sibling, FLAN-T5`, are well-known encoder-decoder, sequence-to-sequence models used across a wide number of generative language tasks.

#### Pretraining-LLM

#### RAG overflow
`naive RAG`
- Retrieve: The user query is used to retrieve relevant context from an external knowledge source. For this, the user query is embedded with an embedding model into the same vector space as the additional context in the vector database. This allows to perform a similarity search, and the top k closest data objects from the vector database are returned.
- Augment: The user query and the retrieved additional context are stuffed into a prompt template.
- Generate: Finally, the retrieval-augmented prompt is fed to the LLM.

`Implementing Naive RAG with LlamaIndex and Weaviate`
Step 1: Define the embedding model and LLM
- Embedding model: used to generate vector embeddings for the document chunks and the query.
- LLM: used to generate an answer based on the user query and the relevant context.
Step 2: Load data
Step 3: Chunk documents into nodes
Step 4: Build index
Step 5: Setup query engine
Step 6: Run a naive RAG query on your data
Step 7: Preparing the Evaluation Data
Step 8: Evaluating the RAG application

`Implementing Advanced RAG with LlamaIndex`
In this section, we will cover some simple adjustments you can make to turn the above naive RAG pipeline into an advanced one. This walkthrough will cover the following selection of advanced RAG techniques:
- Pre-retrieval optimization: Sentence window retrieval
It separates the document into single sentences, which will be embedded.
For each sentence, it creates a context window. If you specify a window_size = 3, the resulting window will be three sentences long, starting at the previous sentence of the embedded sentence and spanning the sentence after. The window will be stored as metadata.
During retrieval, the sentence that most closely matches the query is returned. After retrieval, you need to replace the sentence with the entire window from the metadata.
- Retrieval optimization: Hybrid search
- Post-retrieval optimization: Re-ranking

#### Query Translation
Query transformations are a set of approaches focused on re-writing and / or modifying questions for retrieval.
https://github.com/langchain-ai/rag-from-scratch/blob/main/rag_from_scratch_5_to_9.ipynb
- `Multi Query`
Distance-based vector database retrieval embeds (represents) queries in high-dimensional space and finds similar embedded documents based on "distance". But, retrieval may produce different results with subtle changes in query wording or if the embeddings do not capture the semantics of the data well. Prompt engineering / tuning is sometimes done to manually address these problems, but can be tedious. The MultiQueryRetriever automates the process of `prompt tuning by using an LLM to generate multiple queries from different perspectives for a given user input query`. For each query, it retrieves a set of relevant documents and takes the unique union across all queries to get a larger set of potentially relevant documents. By generating multiple perspectives on the same question, the MultiQueryRetriever might be able to overcome some of the limitations of the distance-based retrieval and get a richer set of results.
https://python.langchain.com/v0.1/docs/modules/data_connection/retrievers/MultiQueryRetriever/
- `RAG-Fusion`
RAG-Fusion, a search methodology that aims to bridge the gap between traditional search paradigms and the multifaceted dimensions of human queries. Inspired by the capabilities of Retrieval Augmented Generation (RAG), this project goes a step further by employing multiple query generation and Reciprocal Rank Fusion to re-rank search results.
https://github.com/langchain-ai/langchain/blob/master/cookbook/rag_fusion.ipynb?ref=blog.langchain.dev
- `Decomposition`
  - `Answer recursively`
  - `Answer individually`
- `Step Back`
Sometimes search quality and model generations can be tripped up by the specifics of a question. One way to handle this is to first generate a more abstract, "step back" question and to query based on both the original and step back question.
For example, if we ask a question of the form "Why does my LangGraph agent astream_events return {LONG_TRACE} instead of {DESIRED_OUTPUT}" we will likely retrieve more relevant documents if we search with the more generic question "How does astream_events work with a LangGraph agent" than if we search with the specific user question.
https://python.langchain.com/v0.1/docs/use_cases/query_analysis/techniques/step_back/
- `HyDE`
At a high level, HyDE is an embedding technique that takes queries, generates a hypothetical answer, and then embeds that generated document and uses that as the final example.
In order to use HyDE, we therefore need to provide a base embedding model, as well as an LLMChain that can be used to generate those documents. By default, the HyDE class comes with some default prompts to use (see the paper for more details on them), but we can also create our own.
https://github.com/langchain-ai/langchain/blob/master/cookbook/hypothetical_document_embeddings.ipynb

#### Retrieval
retriever = db.as_retriever(search_type="mmr", search_kwargs={'k': 4, 'fetch_k': 20})
- `Pre-retrieval`: Auto-Retrieval (Metadata filtering), `Sentence window retrieval`
One technique we will implement in this article is sentence window retrieval, which embeds single sentences for retrieval and replaces them with a larger text window at inference time.
`Pre-retrieval optimizations` focus on `data indexing optimizations` as well as `query optimizations`. Data indexing optimization techniques aim to store the data in a way that helps you improve retrieval efficiency, such as [1]:
  - `Sliding window` uses an overlap between chunks and is one of the simplest techniques.
  - `Enhancing data granularity` applies data cleaning techniques, such as `removing irrelevant information`, `confirming factual accuracy`, `updating outdated information`, etc.
  - `Adding metadata`, such as dates, purposes, or chapters, for filtering purposes.
  - `Sub-Queries`: There are different query strategies such as tree queries or sequential querying of chunks that can be used for different scenarios. LlamaIndex offers a sub question query engine that allows a query to be broken down into several questions that use different relevant data sources.
  - `Hypothetical Document Embeddings`: HyDE generates a hypothetical answer to a query, embeds it, and uses it to retrieve documents similar to the hypothetical answer as opposed to using the query directly.
  - Optimizing index structures involves different strategies to index data, such as adjusting the chunk sizes or using multi-indexing strategies. One technique we will implement in this article is sentence window retrieval, which embeds single sentences for retrieval and replaces them with a larger text window at inference time.
Additionally, `pre-retrieval techniques aren’t limited to data indexing and can cover techniques at inference time`, such as `query routing`, `query rewriting`, and `query expansion`.

- `Retrieval`: Hybrid Search (Semantic and Lexical Search)
  - `Fine-tuning embedding models` customizes embedding models to domain-specific contexts, especially for domains with evolving or rare terms. For example, `BAAI/bge-small-en` is a high-performance embedding model that can be fine-tuned.
  - `Dynamic Embedding` adapts to the context in which words are used, unlike static embedding, which uses a single vector for each word. For example, `OpenAI’s embeddings-ada-02` is a sophisticated dynamic embedding model that captures contextual understanding.
  - `Hybrid Search Exploration`: This approach leverages a combination of search techniques like keyword-based search and semantic search to retrieve relevant and context-rich information; this is useful when dealing with different query types and information needs.
  - `Recursive Retrieval and Query Engine`: Involves a recursive retrieval process that might start with small semantic chunks and subsequently retrieve larger chunks that enrich the context; this is useful to balance efficiency and context-rich information.
  - `StepBack-prompt`: A prompting technique that enables LLMs to perform abstraction that produces concepts and principles that guide reasoning; this leads to better-grounded responses when adopted to a RAG framework because the LLM moves away from specific instances and is allowed to reason more broadly if needed.
  - `Iterative retrieval` enables the model to perform multiple retrieval cycles to enhance the depth and relevance of information. Notable approaches that leverage this method include RETRO and GAR-meets-RAG.
  - `Recursive retrieval` recursively iterates on the output of one retrieval step as the input to another retrieval step; this enables delving deeper into relevant information for complex and multi-step queries (e.g., academic research and legal case analysis). Notable approaches that leverage this method include IRCoT and Tree of Clarifications.
  - `Adaptive retrieval` tailors the retrieval process to specific demands by determining optimal moments and content for retrieval. Notable approaches that leverage this method include FLARE and Self-RAG.

- `Post-retrieval` techniques: Reranking, Few-Shot prompt engineering
Additional processing of the retrieved context can help address issues such as exceeding the context window limit or introducing noise, thus hindering the focus on crucial information. Post-retrieval optimization techniques summarized in the RAG survey [1] are:
  - `Prompt compression` reduces the overall prompt length by removing irrelevant and highlighting important context.
  - `Re-ranking` uses machine learning models to recalculate the relevance scores of the retrieved contexts.

`Ensemble Retriever`
is a sophisticated retrieval algorithm designed to enhance the performance of information retrieval by combining the strengths of multiple individual retrievers. This approach, known as "ensemble retrieval," uses a method called Reciprocal Rank Fusion to rerank and merge the results from different retrievers, thereby providing more accurate and relevant results than any single retriever alone.
The Ensemble Retriever is particularly effective in scenarios where different types of retrievers can complement each other. For instance, it can combine a sparse retriever, such as BM25 (which is adept at keyword-based searches), with a dense retriever that uses embedding similarity (which excels at finding semantically similar documents). This hybrid approach leverages the precise keyword matching of the sparse retriever and the broader semantic understanding of the dense retriever, resulting in a more robust retrieval system.
- `Maximal Marginal Relevance (MMR)` is a method used in information retrieval to select documents that are both relevant to the query and diverse with respect to the previously selected documents. This approach helps in reducing redundancy and increasing the coverage of different aspects of the query in the selected documents.
- `BM25`, or Okapi BM25, is a ranking function used in information retrieval to estimate the relevance of documents to a given search query. It is an enhancement of the traditional TF-IDF method, which considers the frequency of terms within a document (term frequency) and the rarity of terms across all documents (inverse document frequency) to compute relevance scores.
  `Key Features of BM25`
  - Relevance Scoring: BM25 improves upon TF-IDF by introducing a term saturation component, which accounts for the diminishing returns of term frequency. This means that after a certain point, additional occurrences of a term in a document contribute less to the document's relevance score. This is controlled by parameters k1 and b, which can be tuned based on empirical observations.
  - Document Length Normalization: One of BM25's significant advantages is its ability to normalize document length. This prevents longer documents from being unfairly penalized or favored simply due to their length. The parameter b controls the degree of normalization.
  - Flexibility and Precision: BM25 is particularly effective in handling diverse datasets, including those with noisy or sparse data. It provides more accurate relevance scoring for longer documents compared to traditional TF-IDF.
  `Practical Applications`
  - Web Search Engines: BM25 is widely used in search engines to rank web pages based on their relevance to the search query.
  - Document Retrieval Systems: It is applied in various document retrieval systems where precise relevance scoring is crucial.
  - Legal Case Retrieval: BM25 serves as a strong baseline for retrieving relevant legal documents due to its robust handling of term frequencies and document length.
  `Advantages in RAG Framework`
  - Handling Diverse Queries: BM25's robust handling of term frequencies and document length normalization ensures that it can handle a variety of queries efficiently, providing a good starting point for further processing by generative models.
  - Scalability: BM25 is lightweight and scalable, making it suitable for large-scale retrieval tasks common in RAG frameworks.
  By integrating BM25 within a RAG framework, systems can leverage efficient retrieval mechanisms alongside powerful generative models to provide more accurate and contextually relevant responses.


`Fusion retrieval or hybrid search`
This concept, though not entirely new, involves integrating the strengths of two distinct search methods: traditional keyword-based search, which employs sparse retrieval algorithms such as tf-idf or the search industry standard BM25, and contemporary semantic or vector search.
The challenge lies in effectively merging the results obtained from these different similarity scoring methods. This issue is typically addressed using the Reciprocal Rank Fusion (RRF) algorithm, which re-ranks the retrieved results to produce the final output.
In LangChain this is implemented in the Ensemble Retriever class, combining a list of retrievers you define, for example a Faiss vector index and a BM25 based retriever and using RRF for reranking.
As vector database, we'll use FAISS, a library developed by Facebook AI. FAISS specializes in the efficient similarity search and clustering of dense vectors, which suits our needs perfectly. Currently, FAISS is among the top libraries for conducting Nearest Neighbor (NN) search in large datasets.

#### `Prompt`
A prompt may contain the following:
1. `Instruction`: Task or instruction for the model (eg: classify, summarize, …)
2. `Input`: Input statement or question for the model to generate a response.
3. `Context`: Additional relevant information to guide the model’s response (eg: examples to help the model better understand the task.)
4. `Output Format`: Specific type or format of the output generated by the model.

`General tips for designing prompt`
1. Be clear and concise - Avoid ambigous language.
2. Format prompts properly : Separate the input, instruction, context, and output directions. Prompts with the format tends to achieve better results than prompts with random formatting.
3. Focus on what the model needs to do - Try not to focus on what model should not do. Positive instructions are more effective.
4. Provide examples to articulate the desired output format
5. Control the length of output - Explicitly requesting the output length in the prompt helps in faster inference and cost effective as most services charges per token generated.

`Type of Prompting Techniques`
- `Zero-shot Prompting`
- `Few-shot Prompting`
- `Chain-of-Thought Prompting`
Chain-of-Thought (CoT) prompting is technique that breaks down complex tasks through intermediate reasoning steps. This allows LLMs to overcome difficulties with some reasoning tasks that require logical thinking and multiple steps to solve, such as arithmetic or commonsense reasoning questions.
This encourages model to explain it’s reasoning process by decomposing the solution into a series of steps, mimicking human-like conversation flow. This behaviour can be facilitated through various strategies (Zero shot, few short, etc).
- `ReAct Prompting`
CoT aims to imitate how humans think about problems, but it lack access to the external world or inability to update its knowledge which lead to issues like fact hallucination and error propagation, which is where ReAct Prompting is useful.
ReAct allows language models to generate verbal reasoning traces and text actions concurrently.
Actions receive feedback from the external environment ("Env"), while reasoning traces update the model's internal state by reasoning over the context and incorporating useful information for future reasoning and action.

Therefore, in order to implement ReAct, you need:
1. An environment where a text action is chosen from various options based on the environment's internal state and then generates a text observation in response.
2. An output parser framework that stops text generation after producing a valid action, executes it in the environment, and returns the observation by appending it to the generated text so far and prompting the LLM.
3. Human-generated examples of intermixed thoughts, actions, and observations in the environment to use for few-shot learning.


#### `Generation`
The generator in a RAG system is responsible for converting retrieved information into a coherent text that will form the final output of the model. This process involves diverse input data which sometimes require efforts to refine the adaptation of the language model to the input data derived from queries and documents. This can be addressed using post-retrieval process and fine-tuning:
- `Post-retrieval with Frozen LLM`: Post-retrieval processing leaves the LLM untouched and instead focuses on enhancing the quality of retrieval results through operations like information compression and result reranking. Information compression helps with reducing noise, addressing an LLM's context length restrictions, and enhancing generation effects. Reranking aims at reordering documents to prioritize the most relevant items at the top.
- `Fine-tuning LLM for RAG`: To improve the RAG system, the generator can be further optimized or fine-tuned to ensure that the generated text is natural and effectively leverages the retrieved documents.

#### `Evaluating RAG Applications with RAGAs`
building a proof of concept for a Retrieval-Augmented Generation (RAG) application is easy, but making it production-ready is very difficult. Getting the RAG pipeline's performance to a satisfying state is especially difficult because of the different components in a RAG pipeline:
- Retriever component: retrieves additional context from an external database for the LLM to answer the query.
- Generator component: generates an answer based on a prompt augmented with the retrieved information.
When evaluating a RAG pipeline, you must evaluate both components separately and together to understand if and where the RAG pipeline still needs improvement. Additionally, to understand whether your RAG application’s performance is improving, you must evaluate it quantitatively. For this, you will need two ingredients: An evaluation metric and an evaluation dataset.

`What is RAGAs`
RAGAs (Retrieval-Augmented Generation Assessment) is a framework (GitHub, Docs) that provides you with the necessary ingredients to help you evaluate your RAG pipeline on a component level.
To evaluate the RAG pipeline, RAGAs expects the following information:
- `question`: The user query that is the input of the RAG pipeline. The input.
- `answer`: The generated answer from the RAG pipeline. The output.
- `contexts`: The contexts retrieved from the external knowledge source used to answer the question.
- `ground_truths`: The `ground truth answer` to the `question`. This is the only human-annotated information. This information is only required for the metric `context_recall` (see Evaluation Metrics).

Note that the framework has expanded to provide metrics and paradigms that require ground truth labels (e.g., `context_recall` and `answer_correctness`, see Evaluation Metrics).

`Evaluation Metrics`
RAGAs provide you with a few metrics to evaluate a RAG pipeline `component-wise` as well as `end-to-end`.
On a component level, RAGAs provides you with metrics to evaluate the `retrieval component` (`context_relevancy` and `context_recall`) and the `generative component` (`faithfulness` and `answer_relevancy`) separately [2]:
- `Context precision` measures the signal-to-noise ratio of the retrieved context. This metric is computed using the `question` and the `contexts`.
- `Context recall` measures if all the relevant information required to answer the question was retrieved. This metric is computed based on the `ground_truth` (this is the only metric in the framework that relies on human-annotated ground truth labels) and the `contexts`.
- `Faithfulness` measures the factual accuracy of the generated answer. The number of correct statements from the given contexts is divided by the total number of statements in the generated answer. This metric uses the `question`, `contexts` and the `answer`.
- `Answer relevancy` measures how relevant the generated answer is to the question. This metric is computed using the `question` and the `answer`. For example, the answer “France is in western Europe.” to the question “Where is France and what is it’s capital?” would achieve a low answer relevancy because it only answers half of the question.
All metrics are scaled to the `range [0, 1]`, with higher values indicating a better performance.

RAGAs also provides you with metrics to evaluate the RAG pipeline end-to-end, such as `answer semantic similarity` and `answer correctness`. This article focuses on the component-level metrics.

We can make the following observations:
- `context_relevancy` (signal-to-noise ratio of the retrieved context): While the LLM judges all of the context as relevant for the last question, it also judges that most of the retrieved context for the second question is irrelevant. Depending on this metric, you could experiment with different numbers of retrieved contexts to reduce the noise.
- `context_recall` (if all the relevant information required to answer the question was retrieved): The LLMs evaluate that the retrieved contexts contain the relevant information required to answer the questions correctly.
- `faithfulness` (factual accuracy of the generated answer): While the LLM judges that the first and last questions are answered correctly, the answer to the second question, which wrongly states that the president did not mention Intel’s CEO, is judged with a faithfulness of 0.5.
- `answer_relevancy` (how relevant is the generated answer to the question): All of the generated answers are judged as fairly relevant to the questions.

- `answer semantic similarity` The concept of Answer Semantic Similarity pertains to the assessment of the semantic resemblance between the generated answer and the ground truth. This evaluation is based on the ground truth and the answer. Measuring the semantic similarity between answers can offer valuable insights into the quality of the generated response. This evaluation utilizes a cross-encoder model to calculate the semantic similarity score.
- `Answer Correctness` The assessment of Answer Correctness involves gauging the accuracy of the generated answer when compared to the ground truth. This evaluation relies on the ground truth and the answer. Answer correctness encompasses two critical aspects: semantic similarity between the generated answer and the ground truth, as well as factual similarity. These aspects are combined using a weighted scheme to formulate the answer correctness score. Users also have the option to employ a ‘threshold’ value to round the resulting score to binary, if desired.

`Labeled generated metrics`:
- `answer_correctness` - Is the response correct, based on the ground_truth response.
`Reference-free generator metrics`:
- `faithfulness` - Proportion of claims in the response that are grounded in the retrieved context (entailment-based).
`Reference-free retriever metrics`:
- `context_relevancy` - Proportion of retrieved sentences that are "relevant" to the user question.
`Labeled retriever metrics`:
- `context_recall` - Proportion of the ground truth answer that can be attributed to the docs.
- `context_precision` - Are the relevant docs (according to the ground truth) ranked higher? Works by scoring each document as useful in deducing the ground truth, computing precision @ K using that score for each K, then averaging over the total number of useful docs.

In reality, you likely won't need to apply all of these metrics at the same time, but each metric can shed a bit of light on the different aspects of your retriever and generator setup.

`Generating a Testset`: Ideally, you would use your own product's logs to evaluate using Ragas, but you may want to test out different RAG optimizations prior to your product going live. One option for experimenting in this way is by generating our own testset using language models. Specifically, Ragas offers a way to generate our own testset via language model.
`Calculating the Metrics`: In the following section, we will very briefly demonstrate how to actually calculate the Ragas metrics. You'll find that they are very easily to generate from a coding perspective!
`Explaining the Metrics`: After we have derived the metrics via code, we will do a much deeper dive into what each of these metrics are and how they are scored behind the scenes.

#### `A Guide on 12 Tuning Strategies for Production-Ready RAG Applications`
Data Science is an experimental science. It starts with the “No Free Lunch Theorem,” which states that there is `no one-size-fits-all algorithm` that works best for every problem. And it results in data scientists using experiment tracking systems to help them tune the hyperparameters of their Machine Learning (ML) projects to achieve the best performance.
This article covers the following “hyperparameters” sorted by their relevant stage.

In the ingestion stage of a RAG pipeline, you can achieve performance improvements by:
- `Data cleaning`
- `Chunking`
One important step is choosing the right chunking strategy which depends on the content you are dealing with and the application you are generating responses for. Different models also display different strengths on varying block sizes. Sentence transformers will perform better on single sentences but text-embedding-ada-002 will perform better with blocks containing 256 or 512 tokens. Other aspects to consider include the length of user questions, application, and token limits but it's common to experiment with different chunking strategies to help optimize retrieval in your RAG system.
- `Embedding models`
Massive Text Embedding Benchmark (MTEB) Leaderboard, fine-tune your embedding model
- `Metadata`
When you store vector embeddings in a vector database, some vector databases let you store them together with metadata (or data that is not vectorized). Annotating vector embeddings with metadata can be helpful for additional post-processing of the search results, such as metadata filtering [1, 3, 8, 9]. For example, you could add metadata, such as the date, chapter, or subchapter reference.
- `Multi-indexing`
If the metadata is not sufficient enough to provide additional information to separate different types of context logically, you may want to experiment with multiple indexes [1, 9]. For example, you can use different indexes for different types of documents. Note that you will have to incorporate some index routing at retrieval time [1, 9]. If you are interested in a deeper dive into metadata and separate collections, you might want to learn more about the concept of native multi-tenancy.
- `Indexing algorithms`
To enable lightning-fast similarity search at scale, vector databases and vector indexing libraries use an Approximate Nearest Neighbor (ANN) search instead of a k-nearest neighbor (kNN) search. As the name suggests, ANN algorithms approximate the nearest neighbors and thus can be less precise than a kNN algorithm.

And in the inferencing stage (retrieval and generation), you can tune:
- `Query transformations`
Since the search query to retrieve additional context in a RAG pipeline is also embedded into the vector space, its phrasing can also impact the search results. Thus, if your search query doesn’t result in satisfactory search results, you can experiment with various query transformation techniques [5, 8, 9], such as:
  - `Rephrasing`: Use an LLM to rephrase the query and try again.
  - `Hypothetical Document Embeddings (HyDE)`: Use an LLM to generate a hypothetical response to the search query and use both for retrieval.
  - `Sub-queries`: Break down longer queries into multiple shorter queries.
  - `Query Rewriting`: Focuses on rewriting queries using a variety of techniques such as Query2Doc, ITER-RETGEN, and HyDE.
  - `Embedding Transformation`: Optimizes the representation of query embeddings and align them to a latent space that is more closely aligned with a task.

- `Retrieval parameters`
The retrieval is an essential component of the RAG pipeline. The first consideration is whether `semantic search` will be sufficient for your use case or if you want to experiment with `hybrid search`.
In the latter case, you need to experiment with weighting the aggregation of sparse and dense retrieval methods in hybrid search [1, 4, 9]. Thus, tuning the parameter alpha, which controls the weighting between semantic (alpha = 1) and keyword-based search (alpha = 0), will become necessary.
Also, the `number of search results to retrieve` will play an essential role. The number of retrieved contexts will impact the length of the used context window (see Prompt Engineering). Also, if you are using a re-ranking model, you need to consider how many contexts to input to the model (see Re-ranking models).

- `Advanced retrieval strategies`
The underlying idea of this section is that the chunks for `retrieval shouldn’t necessarily be the same chunks used for the generation`. Ideally, you would embed smaller chunks for retrieval (see Chunking) but retrieve bigger contexts. [7]
  - `Sentence-window retrieval`: Do not just retrieve the relevant sentence, but the window of appropriate sentences before and after the retrieved one.
  - `Auto-merging retrieval`: The documents are organized in a tree-like structure. At query time, separate but related, smaller chunks can be consolidated into a larger context.

- `Re-ranking models`
While semantic search retrieves context based on its semantic similarity to the search query, `“most similar” doesn’t necessarily mean “most relevant”`. Re-ranking models, such as Cohere’s Rerank model, can help eliminate irrelevant search results by computing a score for the relevance of the query for each retrieved context [1, 9].
If you are using a re-ranker model, you may need to re-tune the `number of search results for the input of the re-ranker` and `how many of the reranked results you want to feed into the LLM`.
As with the embedding models, you may want to experiment with `fine-tuning the re-ranker` to your specific use case.

- `LLMs`
The LLM is the core component for generating the response. Similarly to the embedding models, there is a wide range of LLMs you can choose from depending on your requirements, such as open vs. proprietary models, inferencing costs, context length, etc. [1]
As with the embedding models or re-ranking models, you may want to experiment with fine-tuning the LLM to your specific use case to incorporate specific wording or tone of voice.

- `Prompt engineering`
How you phrase or engineer your prompt will significantly impact the LLM’s completion [1, 8, 9].
Additionally, using few-shot examples in your prompt can improve the quality of the completions.
As mentioned in Retrieval parameters, the number of contexts fed into the prompt is a parameter you should experiment with [1]. While the performance of your RAG pipeline can improve with increasing relevant context, you can also run into a `“Lost in the Middle”` [6] effect where relevant context is not recognized as such by the LLM if it is placed in the middle of many contexts.

This article covered the following strategies in the ingestion stage:
- `Data cleaning`: Ensure data is clean and correct.
- `Chunking`: Choice of chunking technique, chunk size (chunk_size) and chunk overlap (overlap).
- `Embedding models`: Choice of the embedding model, incl. dimensionality, and whether to fine-tune it.
- `Metadata`: Whether to use metadata and choice of metadata.
- `Multi-indexing`: Decide whether to use multiple indexes for different data collections.
- `Indexing algorithms`: Choice and tuning of ANN and vector compression algorithms can be tuned but are usually not tuned by practitioners.
And the following strategies in the inferencing stage (retrieval and generation):
- `Query transformations`: Experiment with rephrasing, HyDE, or sub-queries.
- `Retrieval parameters`: Choice of search technique (alpha if you have hybrid search enabled) and the number of retrieved search results.
- `Advanced retrieval strategies`: Whether to use advanced retrieval strategies, such as sentence-window or auto-merging retrieval.
- `Re-ranking models`: Whether to use a re-ranking model, choice of re-ranking model, number of search results to input into the re-ranking model, and whether to fine-tune the re-ranking model.
- `LLMs`: Choice of LLM and whether to fine-tune it.
- `Prompt engineering`: Experiment with different phrasing and few-shot examples.

#### engineering
This shows you how effective an LLM can be after we add just a handful of articles. here’s a quick recap on what is happening here:
- `PromptTemplate Creation`: We initiated the process by creating a PromptTemplate. This template requires two inputs: a context and a question. The context provides background information relevant to the question, while the question is what we want our LLM to answer.
- `Chain Creation`: Next, we created a chain. This chain is a sequence of operations that allows us to invoke a query.
- `RunnablePassthrough Usage`: The query is then passed along using RunnablePassthrough(). This function is a part of LangChain’s API and is used to pass the query to the next step in the chain.
- `Retriever Invocation`: The query is also passed into the retriever. The retriever queries our FAISS index, a database designed for efficient similarity search and clustering of dense vectors, and retrieves the relevant context.
- `Context Integration`: The retrieved context is then integrated into our prompt. This step is crucial as it provides the necessary background information that aids the LLM in generating a more accurate and context-aware response.
- `LLM Invocation`: Finally, the enriched prompt is passed into the LLM. In this demonstration, we used a quantized Mistral-7B model, which is a powerful language model capable of generating high-quality text.

`RAG agent`
- `Routing: Adaptive RAG` (paper). Route questions to different retrieval approaches
- `Fallback: Corrective RAG` (paper). Fallback to web search if docs are not relevant to query
- `Self-correction: Self-RAG` (paper). Fix answers w/ hallucinations or don’t address question



### LLM based application
Besides just building our LLM application, we’re also going to be focused on scaling and serving it in production. Unlike traditional machine learning, or even supervised deep learning, scale is a bottleneck for LLM applications from the very beginning. Large datasets, models, compute intensive workloads, serving requirements, etc. We’ll develop our application to be able to handle any scale as the world around us continues to grow. We’re also going to be focused on evaluation and performance. Our application involves many moving pieces: embedding models, chunking logic, the LLM itself, etc. and so it's important that we experiment with different configurations to optimize for the best quality responses. However, it's non-trivial to evaluate and quantitatively compare different configurations for a generative task. We’re going to break down evaluation of individual parts of our application (retrieval given query, generation given source), also assess the overall performance (end-to-end generation) and share findings towards an optimized configuration.
With large data sources, models and application serving needs, scale is a day-1 priority for LLM applications. We want to build our applications in such a way that they can scale as our needs grow without us having to change our code later.

### RAG
Retrieval-Augmented Generation (RAG) is a widely used application pattern for Large Language Models (LLMs). It uses information retrieval systems to give LLMs extra context, which aids in answering user queries not covered in the LLM's training data and helps to prevent hallucinations.

In a RAG application, the goal is to enhance the quality of responses generated by an LLM by supplementing its parametric knowledge with context retrieved from an external knowledge base. To build the knowledge base, large reference documents are broken up into smaller chunks, and each chunk is stored in a database along with its vector embedding generated using an embedding model.
Given a user query, it is first embedded using the same embedding model, and the most relevant chunks are retrieved based on the similarity between the query and chunk vectors. An LLM then uses the user’s question, prompt, and the retrieved documents to generate an answer to the question.

There are many challenges when working with LLMs such as domain knowledge gaps, factuality issues, and hallucination. Retrieval Augmented Generation (RAG) provides a solution to mitigate some of these issues by augmenting LLMs with external knowledge such as databases. RAG is particularly useful in knowledge-intensive scenarios or domain-specific applications that require knowledge that's continually updating. A key advantage of RAG over other approaches is that the LLM doesn't need to be retrained for task-specific applications. RAG has been popularized recently with its application in conversational agents.
In particular, we focus on the existing approaches, state-of-the-art RAG, evaluation, applications and technologies surrounding the different components that make up a RAG system (retrieval, generation, and augmentation techniques).

RAG takes input and retrieves a set of relevant/supporting documents given a source (e.g., Wikipedia). The documents are concatenated as context with the original input prompt and fed to the text generator which produces the final output. This makes RAG adaptive for situations where facts could evolve over time. This is very useful as LLMs's parametric knowledge is static. RAG allows language models to bypass retraining, enabling access to the latest information for generating reliable outputs via retrieval-based generation.
In short, the retrieved evidence obtained in RAG can serve as a way to enhance the accuracy, controllability, and relevancy of the LLM's response. This is why RAG can help reduce issues of hallucination or performance when addressing problems in a highly evolving environment.
While RAG has also involved the optimization of pre-training methods, current approaches have largely shifted to combining the strengths of RAG and powerful fine-tuned models like ChatGPT and Mixtral.

`How to evaluate a RAG application`
The main elements to evaluate in a RAG application are as follows:
- Retrieval: This involves experimenting with different data processing strategies, embedding models, etc., and evaluating how they impact retrieval.
- Generation: Once you decide on the best settings for the retriever, this step involves experimenting with different LLMs to find the best completion model for the task.
In this tutorial, we will evaluate different embedding models for retrieval, different completion models for generation, and the system as a whole with the best-performing models.

`Advanced RAG`
Advanced RAG helps deal with issues present in Naive RAG such as improving retrieval quality that could involve optimizing the pre-retrieval, retrieval, and post-retrieval processes.
- The `pre-retrieval` process involves optimizing data indexing which aims to enhance the quality of the data being indexed through five stages: enhancing data granularity, optimizing index structures, adding metadata, alignment optimization, and mixed retrieval.
- The `retrieval` stage can be further improved by optimizing the embedding model itself which directly impacts the quality of the chunks that make up the context. This can be done by fine-tuning the embedding to optimize retrieval relevance or employing dynamic embeddings that better capture contextual understanding (e.g., OpenAI’s embeddings-ada-02 model).
- Optimizing `post-retrieval` focuses on avoiding context window limits and dealing with noisy or potentially distracting information. A common approach to address these issues is re-ranking which could involve approaches such as relocation of relevant context to the edges of the prompt or recalculating the semantic similarity between the query and relevant text chunks. Prompt compression may also help in dealing with these issues.

`Modular RAG`
As the name implies, Modular RAG enhances functional modules such as incorporating a search module for similarity retrieval and applying fine-tuning in the retriever. Both Naive RAG and Advanced RAG are special cases of Modular RAG and are made up of fixed modules. Extended RAG modules include search, memory, fusion, routing, predict, and task adapter which solve different problems. These modules can be rearranged to suit specific problem contexts. Therefore, Modular RAG benefits from greater diversity and flexibility in that you can add or replace modules or adjust the flow between modules based on task requirements.
Given the increased flexibility in building RAG systems, other important optimization techniques have been proposed to optimize RAG pipelines including:
- Hybrid Search Exploration: This approach leverages a combination of search techniques like keyword-based search and semantic search to retrieve relevant and context-rich information; this is useful when dealing with different query types and information needs.
- Recursive Retrieval and Query Engine: Involves a recursive retrieval process that might start with small semantic chunks and subsequently retrieve larger chunks that enrich the context; this is useful to balance efficiency and context-rich information.
- StepBack-prompt: A prompting technique that enables LLMs to perform abstraction that produces concepts and principles that guide reasoning; this leads to better-grounded responses when adopted to a RAG framework because the LLM moves away from specific instances and is allowed to reason more broadly if needed.
- Sub-Queries: There are different query strategies such as tree queries or sequential querying of chunks that can be used for different scenarios. LlamaIndex offers a sub question query engine that allows a query to be broken down into several questions that use different relevant data sources.
- Hypothetical Document Embeddings: HyDE generates a hypothetical answer to a query, embeds it, and uses it to retrieve documents similar to the hypothetical answer as opposed to using the query directly.

In this section, we summarize the key developments of the components of a RAG system, which include Retrieval, Generation, and Augmentation.

`Retrieval`
Retrieval is the component of RAG that deals with retrieving highly relevant context from a retriever. A retriever can be enhanced in many ways, including:
- Enhancing Semantic Representations
This process involves directly improving the semantic representations that power the retriever. Here are a few considerations:
  - Chunking: One important step is choosing the right chunking strategy which depends on the content you are dealing with and the application you are generating responses for. Different models also display different strengths on varying block sizes. Sentence transformers will perform better on single sentences but text-embedding-ada-002 will perform better with blocks containing 256 or 512 tokens. Other aspects to consider include the length of user questions, application, and token limits but it's common to experiment with different chunking strategies to help optimize retrieval in your RAG system.
  - Fine-tuned Embedding Models: Once you have determined an effective chunking strategy, it may be required to fine-tune the embedding model if you are working with a specialized domain. Otherwise, it's possible that the user queries will be completely misunderstood in your application. You can fine-tune on broad domain knowledge (i.e., domain knowledge fine-tuning) and for specific downstream tasks. BGE-large-EN developed BAAI is a notable embedding model that can be fine-tuned to optimize retrieval relevance.
- Aligning Queries and Documents
This process deals with aligning user's queries to those of documents in the semantic space. This may be needed when a user's query may lack semantic information or contain imprecise phrasing. Here are some approaches:
  - Query Rewriting: Focuses on rewriting queries using a variety of techniques such as Query2Doc, ITER-RETGEN, and HyDE.
  - Embedding Transformation: Optimizes the representation of query embeddings and align them to a latent space that is more closely aligned with a task.
- Aligning Retriever and LLM
This process deals with aligning the retriever outputs with the preferences of the LLMs.
  - Fine-tuning Retrievers: Uses an LLM's feedback signals to refine the retrieval models. Examples include augmentation adapted retriever (AAR), REPLUG, and UPRISE, to name a few.
  - Adapters: Incorporates external adapters to help with the alignment process. Examples include PRCA, RECOMP, and PKG.

- `Metadata filtering`
Incorporating these models into your RAG systems, especially when combined with NLP techniques, allows for the extraction of rich metadata from documents. This includes elements like the sentiment expressed in text, the structure or summarization of a document, or the data encapsulated in a table. Most modern vector databases supports storing metadata alongside text embeddings, as well as using metadata filtering during retrieval, which can significantly enhance the retrieval accuracy.

`Generation`
The generator in a RAG system is responsible for converting retrieved information into a coherent text that will form the final output of the model. This process involves diverse input data which sometimes require efforts to refine the adaptation of the language model to the input data derived from queries and documents. This can be addressed using post-retrieval process and fine-tuning:
- Post-retrieval with Frozen LLM: Post-retrieval processing leaves the LLM untouched and instead focuses on enhancing the quality of retrieval results through operations like information compression and result reranking.
  - Information compression helps with reducing noise, addressing an LLM's context length restrictions, and enhancing generation effects.
  - Reranking aims at reordering documents to prioritize the most relevant items at the top.
- Fine-tuning LLM for RAG: To improve the RAG system, the generator can be further optimized or fine-tuned to ensure that the generated text is natural and effectively leverages the retrieved documents.

- `Reranking models`
While embedding models are a powerful tool for initial retrieval in RAG systems, they can sometimes return a large number of documents that might be generally relevant, but not necessarily the most precise answers to a user's query. This is where reranking models come into play.
Reranking models introduce a two-step retrieval process that significantly improves precision:
  - Initial retrieval: An embedding model acts as a first filter, scanning the entire database and identifying a pool of potentially relevant documents. This initial retrieval is fast and efficient.
  - Reranking: The reranking model then takes over, examining the shortlisted documents from the first stage. It analyzes each document's content in more detail, considering its specific relevance to the user's query. Based on this analysis, the reranking model reorders the documents, placing the most relevant ones at the top (sometimes at both ends of the context window for maximum relevance).


`Augmentation`
Augmentation involves the process of effectively integrating context from retrieved passages with the current generation task.
Retrieval augmentation can be applied in many different stages such as pre-training, fine-tuning, and inference.
- Augmentation Stages: RETRO is an example of a system that leverages retrieval augmentation for large-scale pre-training from scratch; it uses an additional encoder built on top of external knowledge. Fine-tuning can also be combined with RAG to help develop and improve the effectiveness of RAG systems. At the inference stage, many techniques are applied to effectively incorporate retrieved content to meet specific task demands and further refine the RAG process.
- Augmentation Source: A RAG model's effectiveness is heavily impacted by the choice of augmentation data source. Data can be categorized into unstructured, structured, and LLM-generated data.
- Augmentation Process: For many problems (e.g., multi-step reasoning), a single retrieval isn't enough so a few methods have been proposed:
  - `Iterative retrieval` enables the model to perform multiple retrieval cycles to enhance the depth and relevance of information. Notable approaches that leverage this method include RETRO and GAR-meets-RAG.
  - `Recursive retrieval` recursively iterates on the output of one retrieval step as the input to another retrieval step; this enables delving deeper into relevant information for complex and multi-step queries (e.g., academic research and legal case analysis). Notable approaches that leverage this method include IRCoT and Tree of Clarifications.
  - `Adaptive retrieval` tailors the retrieval process to specific demands by determining optimal moments and content for retrieval. Notable approaches that leverage this method include FLARE and Self-RAG.

- `Context-aware chunking`
Most simple RAG systems rely on fixed-size chunking, dividing documents into equal segments with some overlap to ensure continuity. This method, while straightforward, can sometimes strip away the rich context embedded in the data.
By contrast, context-aware chunking breaks down text data into more meaningful pieces, considering the actual content and its structure. Instead of splitting text at fixed intervals (like word count), it identifies logical breaks in the text using NLP techniques. These breaks can occur at the end of sentences, paragraphs, or when topics shift. This ensures each chunk captures a complete thought or idea, and makes it possible to add additional metadata to each chunk, for implementing metadata filtering or Small-to-Big retrieval.
As your RAG system can understand the overall flow and ideas within a document with context-aware chunking, it is capable of creating chunks that capture not just isolated sentences but also the broader context they belong to.


`RAG Evaluation`
Evaluating a RAG framework focuses on three primary quality scores and four abilities.
`Quality scores` include:
- measuring context relevance (i.e., the precision and specificity of retrieved context)
- answer faithfulness (i.e., the faithfulness of answers to the retrieved context)
- answer relevance (i.e., the relevance of answers to posed questions).
In addition, there are `four abilities` that help measure the adaptability and efficiency of a RAG system:
- noise robustness
- negative rejection
- information integration
- counterfactual robustness

To evaluate our agent using RAGAS, we need a `dataset` containing `questions`, `ideal contexts`, and the `ground truth answers` to those questions. RAGAS does provide utilities for automatically generating these, but these are out of the scope of this article. Nonetheless, we will be using a prebuilt evaluation dataset created using RAGAS.

`Retrieval Metrics`
Retrieval is the first step in every RAG pipeline, so we will focus on metrics that assess retrieval first. We primarily want to focus on context_recall and context_precision, but we must understand what they measure before diving into these metrics.

Actual vs. Predicted
When evaluating the performance of retrieval systems, we tend to compare the actual (ground truth) to predicted results. We define these as:
- Actual condition is the true label of every context in the dataset. These are positive (p) if the context is relevant to our query or negative (n) if the context is irrelevant to our query.
- Predicted condition is the predicted label determined by our retrieval system. Every context our pipeline returns is a predicted positive, i.e., ^p. If our pipeline does not return a context, it is a predicted negative, i.e., ^n.
Given these conditions, we can say the following:
- `p ^p` is a true positive, meaning a relevant result has been returned.
- `n ^n` is a true negative, meaning an irrelevant result was not returned.
- `n ^p` is a false positive, meaning an irrelevant result has been returned.
- `p ^n` is a false negative, meaning a relevant result has not been returned.
Let's see how these apply to our metrics in RAGAS.
- `Context Recall`
Context recall (or just recall) measures how many relevant records in a dataset have been retrieved by the pipeline. We calculate it as follows:

`Recall@K= p ^p / (p ^p + n ^n) = Relevant contexts retrieved / Total number of relevant contexts`
​
RAGAS calculates context recall using Recall@K, where the @K represents the number of contexts returned. If we increase the @K value, the recall scores will improve (as the capture size of the retrieval step increases). At its extreme, we could set @K equal to the dataset size to guarantee perfect recall — although this negates the point of RAG in the first place.
By default, RAGAS uses a @K value of 5.

The recall is a useful metric but easily fooled by simply returning more records, i.e., increasing the @K value. Because of that, it is typically paired with precision.

- `Context Precision`
Context precision (or just precision) is another popular retrieval metric. We typically see both recall and precision paired together when evaluating retrieval systems.

As with recall, the actual metric here is called Precision@K, where @K represents the number of contexts returned. However, unlike recall, precision focuses on the number of relevant results returned compared to the total results returned, whether relevant or not — this is equal to our chosen @K value.

`Precision@K= p ^p / (p ^p + p ^n) = Relevant contexts retrieved / Number of contexts retrieved`


`Generation Metrics`
- `Faithfulness`
The faithfulness metric measures (from 0 to 1) the factual consistency of an answer when compared to the retrieved context. A score of 1 means we can find all answer claims in the context. A score of 0 would indicate that we find no answer claims in the context.
We calculate the faithfulness like so:
`Faithfulness = Number of claims in answer also found in context / Number of claims in answer`

When calculating faithfulness, RAGAS uses OpenAI LLMs to decide which claims are in the answer and whether they exist in the context. Because of this approach's "generative" nature, we won't always get accurate scores.
We can see that we get perfect scores for all but our fourth result, which scores 0.0. However, we can see some related claims. Nonetheless, the fourth answer is less grounded in the truth of our context than other responses, indicating justification behind this low score.

- `Answer Relevancy`
Answer relevancy is our final metric. It focuses on the generation component and is similar to our "context precision" metric as it measures how much of the returned information is relevant to our original question.
We return a low answer relevancy score when:
Answers are incomplete.
Answers contain redundant information.
A high answer relevancy score indicates that an answer is concise and does not contain "fluff" (i.e., irrelevant information).
The score is calculated by asking an LLM to generate multiple questions for a generated answer and then calculating the cosine similarity between the original and generated questions. Naturally, if we have a concise answer that answers a specific question, we should find that the generated question will have a high cosine similarity to the original question.


#### General Techniques for Building Production-Grade RAG
- `Decoupling Chunks Used for Retrieval vs. Chunks Used for Synthesis`
A key technique for better retrieval is to decouple chunks used for retrieval with those that are used for synthesis.

Motivation#
The optimal chunk representation for retrieval might be different than the optimal consideration used for synthesis. For instance, a raw text chunk may contain needed details for the LLM to synthesize a more detailed answer given a query. However, it may contain filler words/info that may bias the embedding representation, or it may lack global context and not be retrieved at all when a relevant query comes in.

Key Techniques#
There’s two main ways to take advantage of this idea:
1. Embed a document summary, which links to chunks associated with the document.
This can help retrieve relevant documents at a high-level before retrieving chunks vs. retrieving chunks directly (that might be in irrelevant documents).

2. Embed a sentence, which then links to a window around the sentence.
This allows for finer-grained retrieval of relevant context (embedding giant chunks leads to “lost in the middle” problems), but also ensures enough context for LLM synthesis.

- `Structured Retrieval for Larger Document Sets`
Motivation#
A big issue with the standard RAG stack (top-k retrieval + basic text splitting) is that it doesn’t do well as the number of documents scales up - e.g. if you have 100 different PDFs. In this setting, given a query you may want to use structured information to help with more precise retrieval; for instance, if you ask a question that's only relevant to two PDFs, using structured information to ensure those two PDFs get returned beyond raw embedding similarity with chunks.

Key Techniques#
There’s a few ways of performing more structured tagging/retrieval for production-quality RAG systems, each with their own pros/cons.
1. Metadata Filters + Auto Retrieval Tag each document with metadata and then store in a vector database. During inference time, use the LLM to infer the right metadata filters to query the vector db in addition to the semantic query string.

Pros ✅: Supported in major vector dbs. Can filter document via multiple dimensions.
Cons 🚫: Can be hard to define the right tags. Tags may not contain enough relevant information for more precise retrieval. Also tags represent keyword search at the document-level, doesn’t allow for semantic lookups.

2. Store Document Hierarchies (summaries -> raw chunks) + Recursive Retrieval Embed document summaries and map to chunks per document. Fetch at the document-level first before chunk level.

Pros ✅: Allows for semantic lookups at the document level.
Cons 🚫: Doesn’t allow for keyword lookups by structured tags (can be more precise than semantic search). Also autogenerating summaries can be expensive.

- `Dynamically Retrieve Chunks Depending on your Task`
Motivation#
RAG isn't just about question-answering about specific facts, which top-k similarity is optimized for. There can be a broad range of queries that a user might ask. Queries that are handled by naive RAG stacks include ones that ask about specific facts e.g. "Tell me about the D&I initiatives for this company in 2023" or "What did the narrator do during his time at Google". But queries can also include summarization e.g. "Can you give me a high-level overview of this document", or comparisons "Can you compare/contrast X and Y". All of these use cases may require different retrieval techniques.

Key Techniques#
LlamaIndex provides some core abstractions to help you do task-specific retrieval. This includes our router module as well as our data agent module. This also includes some advanced query engine modules. This also include other modules that join structured and unstructured data.
You can use these modules to do joint question-answering and summarization, or even combine structured queries with unstructured queries.

`Basic Strategies`
There are many easy things to try, when you need to quickly squeeze out extra performance and optimize your RAG workflow.
- Prompt Engineering
- Embeddings
- Chunk Sizes
- Hybrid Search
Hybrid search is a common term for retrieval that involves combining results from both semantic search (i.e. embedding similarity) and keyword search. Embeddings are not perfect, and may fail to return text chunks with matching keywords in the retrieval step.
  - semantic search (i.e. embedding similarity)
  - lexical search (keyword search)
- Metadata Filters
Before throwing your documents into a vector index, it can be useful to attach metadata to them. While this metadata can be used later on to help track the sources to answers from the response object, it can also be used at query time to filter data before performing the top-k similarity search. Metadata filters can be set manually, so that only nodes with the matching metadata are returned.
- `*** Multi-Tenancy RAG`
Multi-Tenancy in RAG systems is crucial for ensuring data security. It enables users to access exclusively their indexed documents, thereby preventing unauthorized sharing and safeguarding data privacy. Search operations are confined to the user's own data, protecting sensitive information. Implementation can be achieved with VectorStoreIndex and VectorDB providers through Metadata Filters.

`Advanced Retrieval Strategies`
- Reranking
- Recursive retrieval
- Embedded tables
- Small-to-big retrieval

`Query Transformations (Query Decomposition)`
Multi-step query transformations are a generalization on top of existing single-step query transformation approaches.
Given an initial, complex query, the query is transformed and executed against an index. The response is retrieved from the query. Given the response (along with prior responses) and the query, follow-up questions may be asked against the index as well. This technique allows a query to be run against a single knowledge source until that query has satisfied all questions.


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
Before we begin, it is important to distinguish LLM model evaluation from LLM application evaluation. Evaluating LLM models involves measuring the performance of a given model across different tasks, whereas LLM application evaluation is about evaluating different components of an LLM application such as prompts, retrievers, etc., and the system as a whole. In this tutorial, we will focus on evaluating LLM applications.

As with any software, you will want to evaluate each component separately and the system as a whole. In RAG systems, for example, you will want to evaluate the retrieval and generation to ensure that you are retrieving the right context and generating suitable answers, whereas in tool-calling agents, you will want to validate the intermediate responses from each of the tools. You will also want to evaluate the overall system for correctness, typically done by comparing the final answer to the ground truth answer.
Finally, think about how you will collect feedback from your users, incorporate it into your evaluation pipeline, and track the performance of your application over time.

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

BentoML is optimized for building such serving systems, streamlining both the workflow from development to deployment and the serving architecture itself. Developers can encapsulate the entire RAG logic within a single Python application, referencing each component (like OCR, reranker, text embedding, and large language models) as a straightforward Python function call. The framework eliminates the need to build and manage distributed services, optimizing resource efficiency and scalability for each component. BentoML also manages the entire pipeline, packaging the necessary code and models into a single versioned unit (a "Bento"). This consistency across different application lifecycle stages drastically simplifies the deployment and evaluation process.

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

`RAG`:

*** > https://www.anyscale.com/blog/a-comprehensive-guide-for-building-rag-based-llm-applications-part-1#response-generation

*** > https://www.promptingguide.ai/research/rag

*** > https://www.bentoml.com/blog/building-rag-with-open-source-and-custom-ai-models

*** > https://www.pinecone.io/learn/series/rag/rerankers/

*** > https://github.com/langchain-ai/rag-from-scratch

*** > https://medium.com/@mohammed97ashraf/building-a-retrieval-augmented-generation-rag-model-with-gemma-and-langchain-a-step-by-step-f917fc6f753f



*** > https://towardsdatascience.com/retrieval-augmented-generation-rag-from-theory-to-langchain-implementation-4e9bd5f6a4f2

*** > https://towardsdatascience.com/advanced-retrieval-augmented-generation-from-theory-to-llamaindex-implementation-4de1464a9930

*** > https://towardsdatascience.com/evaluating-rag-applications-with-ragas-81d67b0ee31a

*** > https://towardsdatascience.com/a-guide-on-12-tuning-strategies-for-production-ready-rag-applications-7ca646833439



*** > https://www.kaggle.com/code/gpreda/rag-using-llama-2-langchain-and-chromadb
*** > https://towardsdatascience.com/local-rag-from-scratch-3afc6d3dea08



> https://mindfulmatrix.substack.com/p/build-a-simple-llm-application-with

> https://mindfulmatrix.substack.com/p/prompting-in-the-age-of-llms

> https://mindfulmatrix.substack.com/p/unveiling-the-revolutionary-architecture

> https://jalammar.github.io/illustrated-transformer/

> https://www.linkedin.com/posts/sagarg55_what-are-some-good-starting-points-for-diving-activity-7180054059981164544-2qq-/?utm_source=share&utm_medium=member_desktop

> https://www.anyscale.com/blog/end-to-end-llm-workflows-guide?__hstc=218704582.00f159e343060f6b070803af47ca3180.1723166370722.1723166370722.1723166370722.1&__hssc=218704582.3.1723166370722&__hsfp=4274120786

> https://www.union.ai/blog-post/large-language-models-in-production

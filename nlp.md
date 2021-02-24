## Natural Language Processing
#### NLP Pipeline #### 
This step-by-step processing of text is known as a pipeline. Note that, in the real world, the process may not always be linear as it’s shown in the pipeline in Figure 2-1; it often involves going back and forth between individual steps (e.g., between feature extraction and modeling, modeling and evaluation, and so on). Also, there are loops in between, most commonly going from evaluation to pre-processing, feature engineering, modeling, and back to evaluation. There is also an overall loop that goes from monitoring to data acquisition, but this loop happens at the project level.

![Diagram of rsz_system_monitoring.](pic/pnlp_0201.png)

***Data Acquisition***
- Use a public dataset
- Scrape data
    - Scrape the data from there and get it labeled by human annotators.
- Product intervention
- Data augmentation
- Synonym replacement
- Back translation
    - Say we have a sentence, S1, in English. We use a machine-translation library like Google Translate to translate it into some other language—say, German. Let the corresponding sentence in German be S2. Now, we’ll use the machine-translation library again to translate back to English. Let the output sentence be S3. We’ll find that S1 and S3 are very similar in meaning but are slight variations of each other. Now we can add S3 to our dataset. This trick works beautifully for text classification.
- Replacing entities
- Adding noise to data
    - In many NLP applications, the incoming data contains spelling mistakes. This is primarily due to characteristics of the platform where the data is being generated (for example, Twitter). In such cases, we can add a bit of noise to data to train robust models. 
- Advanced techniques
    - Snorkel
    - Active learning

***Text Extraction and Cleanup***
- HTML Parsing and Cleanup
- Unicode Normalization
- Spelling Correction
    - In the world of fast typing and fat-finger typing [6], incoming text data often has spelling errors. shorthand text messages in social microblogs often hinder language processing and context understanding.
- System-Specific Error Correction
    - The pipeline in this case starts with extraction of plain text from PDF documents. However, different PDF documents are encoded differently, and sometimes, we may not be able to extract the full text, or the structure of the text may get messed up. Text extraction from scanned documents is typically done through optical character recognition (OCR), using libraries such as Tesseract [25, 26].

***Pre-Processing***
However, all NLP software typically works at the sentence level and expects a separation of words at the minimum. So, we need some way to split a text into words and sentences before proceeding further in a processing pipeline. Sometimes, we need to remove special characters and digits, and sometimes, we don’t care whether a word is in upper or lowercase and want everything in lowercase. Many more decisions like this are made while processing text. Such decisions are addressed during the pre-processing step of the NLP pipeline. Here are some common pre-processing steps used in NLP software:
![Diagram of rsz_system_monitoring.](pic/pnlp_0211.png)

- Preliminaries
    - Sentence segmentation and word tokenization.
- Frequent steps
    - Stop word removal, stemming and lemmatization, removing digits/punctuation, lowercasing, etc.
    - Stemming refers to the process of removing suffixes and reducing a word to some base form such that all different variants of that word can be represented by the same form (e.g., “car” and “cars” are both reduced to “car”).
    - Lemmatization is the process of mapping all the different forms of a word to its base word, or lemma. While this seems close to the definition of stemming, they are, in fact, different. For example, the adjective “better,” when stemmed, remains the same. However, upon lemmatization, this should become “good,”

![Diagram of rsz_system_monitoring.](pic/pnlp_0207.png)

- Other steps
    - Normalization, language detection, code mixing, transliteration, etc.
- Advanced processing
    - POS tagging, parsing, coreference resolution, etc.

![Diagram of rsz_system_monitoring.](pic/pnlp_0210.png)

Remember that not all of these steps are always necessary, and not all of them are performed in the order in which they’re discussed here. For example, if we were to remove digits and punctuation, what is removed first may not matter much. However, we typically lowercase the text before stemming. We also don’t remove tokens or lowercase the text before doing lemmatization because we have to know the part of speech of the word to get its lemma, and that requires all tokens in the sentence to be intact. A good practice to follow is to prepare a sequential list of pre-processing tasks to be done after having a clear understanding of how to process our data.

For example, POS tagging cannot be preceded by stop word removal, lowercasing, etc., as such processing affects POS tagger output by changing the grammatical structure of the sentence. How a particular pre-processing step is helping a given NLP problem is another question that is specific to the application, and it can only be answered with a lot of experimentation. We’ll discuss more specific pre-processing required for different NLP applications in upcoming chapters.

***Feature engineering***
When we use ML methods to perform our modeling step later, we’ll still need a way to feed this pre-processed text into an ML algorithm. Feature engineering refers to the set of methods that will accomplish this task. It’s also referred to as feature extraction. The goal of feature engineering is to capture the characteristics of the text into a numeric vector that can be understood by the ML algorithms. 

It’s very hard to explain a DL model’s prediction, which is a disadvantage in a business-driven use case. For example, when identifying an email as ham or spam, it might be worth knowing which word or phrases played the significant role in making the email ham or spam. While this is easy to do with handcrafted features, it’s not easy in the case of DL models.

***Modeling***
We may have to do many iterations of the model-building process to “build THE model” that gives good performance and is also production-ready. We cover some of the approaches to address this issue here:
- Ensemble and stacking
    - There are two ways of doing this: we can feed one model’s output as input for another model, thus sequentially going from one model to another and obtaining a final output. This is called `model stacking`.i Alternatively, we can also pool predictions from multiple models and make a final prediction. This is called `model ensembling`.
- Better feature engineering
- Transfer learning
    - Transfer learning provides a better initialization, which helps in the downstream tasks, especially when the dataset for the downstream task is smaller. In these cases, transfer learning yields better results than just initializing a downstream model from scratch with random initialization. As an example, for email spam classification, we can use BERT to fine-tune the email dataset.
- Reapplying heuristics

![Diagram of rsz_system_monitoring.](pic/pnlp_0212.png)

![Diagram of rsz_system_monitoring.](pic/pnlp_0403.png)

***Evaluation***
Also, evaluations are of two types: `intrinsic` and `extrinsic`. Intrinsic focuses on intermediary objectives, while extrinsic focuses on evaluating performance on the final objective. For example, consider a spam-classification system. The ML metric will be precision and recall, while the business metric will be “the amount of time users spent on a spam email.” `Intrinsic evaluation` will focus on measuring the system performance using precision and recall. `Extrinsic evaluation` will focus on measuring the time a user wasted because a spam email went to their inbox or a genuine email went to their spam folder.

Ranking tasks like information search and retrieval mostly uses ranking-based metrics, such as MRR and MAP, but usual classification metrics can be used, too. In the case of retrieval, we care mainly about recall, so recall at various ranks is calculated. For example, for information retrieval, a common metric is “Recall at rank K”; it looks for the presence of ground truth in top K retrieved results. If present, it’s a success.

***Post-Modeling Phases***
`Deployment`

`Monitoring and model updating`

***Text Representation***
- One-Hot Encoding
    - However, it suffers from a few shortcomings:
    - The size of a one-hot vector is directly proportional to size of the vocabulary, and most real-world corpora have large vocabularies.
    - This representation does not give a fixed-length representation for text
    - It treats words as atomic units and has no notion of (dis)similarity between words.
    - This is known as the out of vocabulary (OOV) problem.
- Bag of Words
    - The key idea behind it is as follows: represent the text under consideration as a bag (collection) of words while ignoring the order and context. The basic intuition behind it is that it assumes that the text belonging to a given class in the dataset is characterized by a unique set of words. If two text pieces have nearly the same words, then they belong to the same bag (class). Thus, by analyzing the words present in a piece of text, one can identify the class (bag) it belongs to.
- Bag of N-Grams
    - It still provides no way to address the OOV problem.
- TF-IDF
    - term frequency–inverse document frequency
    - However, despite the fact that TF-IDF is better than the vectorization methods we saw earlier in terms of capturing similarities between words, it still suffers from the curse of high dimensionality.
    - They’re discrete representations—i.e., they treat language units (words, n-grams, etc.) as atomic units.
    - The feature vectors are sparse and high-dimensional representations.
    - They cannot handle OOV words.

`Distributed Representations`: the vectors in distributional representation are very high dimensional and sparse. This makes them computationally inefficient and hampers learning.
`Embedding`: embedding is a mapping between vector space coming from distributional representation to vector space coming from distributed representation.
- Word Embeddings
    - The Word2vec model is in many ways the dawn of modern-day NLP.
    - Word2vec ensures that the learned word representations are low dimensional (vectors of dimensions 50–500, instead of several thousands, as with previously studied representations in this chapter) and dense (that is, most values in these vectors are non-zero). 
    - To “derive” the meaning of the word, Word2vec uses distributional similarity and distributional hypothesis. That is, it derives the meaning of a word from its context: words that appear in its neighborhood in the text. So, if two different words (often) occur in similar context, then it’s highly likely that their meanings are also similar. Word2vec operationalizes this by projecting the meaning of the words in a vector space where words with similar meanings will tend to cluster together, and words with very different meanings are far from one another.
    - Conceptually, Word2vec takes a large corpus of text as input and “learns” to represent the words in a common vector space based on the contexts in which they appear in the corpus.
- PRE-TRAINED WORD EMBEDDINGS
    - Training your own word embeddings is a pretty expensive process (in terms of both time and computing). Thankfully, for many scenarios, it’s not necessary to train your own embeddings, and using pre-trained word embeddings often suffices.
    - Such embeddings can be thought of as a large collection of key-value pairs, where keys are the words in the vocabulary and values are their corresponding word vectors.
    - various dimensions like d = 25, 50, 100, 200, 300, 600.
    - The higher the score, the more similar the word is to the query word:
    - gensim, also supports training and loading GloVe pre-trained models.
- TRAINING OUR OWN EMBEDDINGS
    - we construct a shallow net (it’s shallow since it has a single hidden layer)
    - One of the most commonly used implementations is gensim [15].
- Going Beyond Words
    - A simple approach is to break the text into constituent words, take the embeddings for individual words, and combine them to form the representation for the text. There are various ways to combine them, the most popular being sum, average, etc.
    - A simple approach that often works is to exclude those words from the feature extraction process so we don’t have to worry about how to get their representations. 
    - Another way to deal with the OOV problem for word embeddings is to create vectors that are initialized randomly, where each component is between –0.25 to +0.25, and continue to use these vectors throughout the application we’re building
    - There are also other approaches that handle the OOV problem by modifying the training process by bringing in characters and other subword-level linguistic components.
    - fastText learns embeddings for words and character n-grams together and views a word’s embedding vector as an aggregation of its constituent character n-grams. This makes it possible to generate embeddings even for words that are not present in the vocabulary.
- Distributed Representations Beyond Words and Characters
    - Word2vec learned representations for words, and we aggregated them to form text representations. fastText learned representations for character n-grams, which were aggregated to form word representations and then text representations.
    - Doc2vec is based on the paragraph vectors framework [21] and is implemented in gensim. This is similar to Word2vec in terms of its general architecture, except that, in addition to the word vectors, it also learns a “paragraph vector” that learns a representation for the full text (i.e., with words in context).
    - Doc2vec was perhaps the first widely accessible implementation for getting an embedding representation for the full text instead of using a combination of individual word vectors.
- Universal Text Representations
    - Neural architectures such as recurrent neural networks (RNNs) and transformers were used to develop large-scale models of language (ELMo [24], BERT [25]), which can be used as pre-trained models to get text representations. The key idea is to leverage “transfer learning”—that is, to learn embeddings on a generic task (like language modeling) on a massive corpus and then fine-tune learnings on task-specific data.
    - However, based on our experience, here are a few important aspects to keep in mind while using them in your project:
    - All text representations are inherently biased based on what they saw in training data.
    - Unlike the basic vectorization approaches, pre-trained embeddings are generally large-sized files (several gigabytes), which may pose problems in certain deployment scenarios.
    - Modeling language for a real-world application is more than capturing the information via word and sentence embeddings. 
    - As we speak, neural text representation is an evolving area in NLP, with rapidly changing state of the art.
- Handcrafted Feature Representations
    - However, in many cases, we do have some domain-specific knowledge about the given NLP problem, which we would like to incorporate into the model we’re building. In such cases, we resort to handcrafted features.
    - These are all examples of commonly used tools where we often need custom features to incorporate domain knowledge.

 For some applications, such as text classification, it’s more common to see vectorization approaches and embeddings as the go-to feature representations for text. For some other applications, such as information extraction, or in the examples we saw in the previous section, it’s more common to look for handcrafted, domain-specific features. Quite often, a hybrid approach that combines both kinds of features are used in practice. 

 #### Text Classification #### 


#### NER #### 
However, in real-world scenarios, using the trained model by itself won’t be sufficient, as the data keeps changing and new entities keep getting added, and there will also be some domain-specific entities or patterns that were not seen in generic training datasets. Hence, most NER systems deployed in real-world scenarios use a combination of ML models, gazetteers, and some pattern matching–based heuristics to improve their performance.


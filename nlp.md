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

***Evaluation***
Also, evaluations are of two types: `intrinsic` and `extrinsic`. Intrinsic focuses on intermediary objectives, while extrinsic focuses on evaluating performance on the final objective. For example, consider a spam-classification system. The ML metric will be precision and recall, while the business metric will be “the amount of time users spent on a spam email.” `Intrinsic evaluation` will focus on measuring the system performance using precision and recall. `Extrinsic evaluation` will focus on measuring the time a user wasted because a spam email went to their inbox or a genuine email went to their spam folder.

Ranking tasks like information search and retrieval mostly uses ranking-based metrics, such as MRR and MAP, but usual classification metrics can be used, too. In the case of retrieval, we care mainly about recall, so recall at various ranks is calculated. For example, for information retrieval, a common metric is “Recall at rank K”; it looks for the presence of ground truth in top K retrieved results. If present, it’s a success.


***Post-Modeling Phases***
`Deployment`

`Monitoring and model updating`
# Presentation and Note

Digitized documents have become an omnipresent medium of information. A plethora of scholarly documents on the web is excessively being increased. Most of the scientific literature is stored in Portable Document Format (PDF). PDF documents hold a complex structure due to which their comprehension and extraction of useful information from them is a challenging task. In this regard, research community has been proposing different rule based and machine learning based techniques in the past several years. We believe that accurate and efficient information extraction form the PDF files is an important issue as major portion of scholarly literature is stored in PDF.

To help a soil science team from the United States Department of Agriculture (USDA) build a queryable journal paper system, we used web crawler with Python to download journal papers on soil science from the digital library to provide users with papers they are interested in. To extract useful information including authors, journal, publish date, abstract, DOI, journal type, experiment location and key words in papers and highlight the paper characteristics in data system, we applied named entity recognition to extract authors and location of experiments, table analysis to extract tables in the paper. The named entity recognition technique is used to extract authors and experiment location. And the table analysis is used to store the tables from the journal paper in a computer queryable form. Text analysis is applied to figure out the parts of interest, and stored them in the database to save time. We used traditional machine learning techniques including logistic regression, support vector machine, decision tree, naive bayes, k-nearest neighbors, random forest, ensemble modeling, and neural networks in text analysis and compare the advantages of these approaches in the end.

In an age of rapidly increasing numbers of published scientific articles, it is surprising that most systematic literature reviews and extraction of information from tables are still conducted by manually processing articles individually \cite{fut1}. Systematic literature reviews aim to find and collect relevant information concerning a specific research question and are an essential step in virtually every area of research, e.g., for the preparation of review articles, project proposals, and experimental designs. While machine learning tools are available for literature searches and screens \cite{context}, they require a large number of manually evaluated articles for the training of the tool. They are often restricted to filtering articles by study design or choosing topics from a limited set of terms, and are generally limited to the evaluation of article titles and abstracts.

To extract information from journals automatically and easily, a soil science team from the United States Department of Agriculture (USDA) want to build a queryable journal paper data system, where users can easily identify journal papers of interest to them. To satisfy their requirements, the system needs information including authors, journal, publish date, abstract, DOI, journal type, experiment location and key words in papers to highlight the paper characteristics. This information will help users to figure out if the paper is of interest to them and locate it quickly if needed. The important initial factor is data, which is journal papers in the system. We used web crawler with Python to download journal papers on soil science from the digital library to provide users with papers which is of interest to them. To extract useful information from journal papers and store them in data system as indexing and abstract, we applied name entity recognition to extract authors and location of experiments, table analysis to extract tables in the paper and store the them in a computer queryable form.

To make system recommend journal papers to users automatically, we built machine learning and deep learning models to identify users' interests. Text analysis is applied on the text data to figure out what parts of paper the user are interested in, and stored them in the database to save users' search time. During this part, I fed the text data including sections, paragraphs to many types of machine learning algorithms and used the trained models to classify unseen data in order to help user distinguish if the new pieces of text in journal paper is useful. I used traditional machine learning techniques including logistic regression, support vector machine, decision tree, naive bayes, k-nearest neighbors, random forest, ensemble modeling, and neural networks in text analysis and compare the advantages of these approaches in the end.

My contributions consist of five parts: Web harvesting, Text Classification, Table Analysis, Named Entity Recognition and Database System Building. Finally all of them can populate a relational database with information automatically extracted from journal papers collected from internet resources, and send users proper recommendations. The reason we used a web crawler to download papers is we need collect papers to build database and the papers are also the basis of the following tasks. Text classification can help identify the section or paragraph in a paper that may be of interest to users based on their own search interest. Named Entity Recognition can extract author and experiment location from paper to store them in data system, and database system will make the future query more efficiently.

The contributions of this thesis are:
1. Web harvesting: We downloaded 38,444 papers with size of 29.53 GB from Digital Library at University of Nebraska Lincoln.
2. Text Classification: We built a machine learning-based system to identify the sections or paragraphs in the papers that may be of interest to users based on their own search interest. The model we built can catch all positives and 83\% negatives. This means there is 1 paper of interest to users for every 2.89 suggested papers.
3. Table Analysis: After manually creating different kinds of tables in the journal papers, we used Seth et al.'s approach and found the program could process about 90\% of all tables, which are well-formed tables. For the other 10\% not well-formed tables, the program can not extract correct information.
4. Named Entity Recognition: We used Stanford's Named Entity Recognition to extract author and experiment location from paper and store them in data system which will make the future query more efficiently. The accuracy can reach about 83\%.
5. Database System Building: We stored the journal paper related information including Title, Publication Date, Abstract, Journal, DOI and Type, authors, city and state extracted from papers by Stanford NER, the count of the occurrences of terms of interest to soil scientists, and infromation contained in the well-formed table converted by the algorithm of Seth et al. \cite{t1} in the Microsoft Access Database.



> https://www.datainnovation.org/2020/07/5-qs-for-priscilla-alexander-vice-president-of-engineering-at-arthurai/

> https://www.arthur.ai/blog/2020/4/8/fairness-in-machine-learning-is-tricky


>AWS Account:
```
udacitystudylei@gmail.com
nigama7@gmail.com
```

>Project
```
1. Install env
2. Install packages
3. Create requirements.txt 
```

Project Command 
>Install env
```
python3 -m venv env
source env/bin/activate
pip list
pip freeze > requirements.txt
cat requirements.txt
```

>Install packages
```
pip install jupyterlab pandas sklearn matplotlib seaborn flake8 pycodestyle_magic pylint
```

## TODO
> OCR

https://www.kaggle.com/ahoo1260/ocr-post-correction-using-nlp-bert

https://www.kaggle.com/zacchaeus/rl-ocr-pipeline

https://www.kaggle.com/dmitryyemelyanov/receipt-ocr-part-1-image-segmentation-by-opencv

https://www.kaggle.com/deshwalmahesh/image-processing-1-basic-ocr-feature-pooling-conv

https://www.kaggle.com/samfc10/handwriting-recognition-using-crnn-in-keras

https://www.kaggle.com/blagoyh/identifying-handwriting-with-ai-99-6

https://www.kaggle.com/rrishabhporwal/handwriting-recognisation-on-mnistNLP

> NLP

https://www.kaggle.com/arthurtok/spooky-nlp-and-topic-modelling-tutorial

https://www.kaggle.com/itratrahman/nlp-tutorial-using-python

https://www.kaggle.com/shahules/basic-eda-cleaning-and-glove

https://www.kaggle.com/dijorajsenroy/different-ways-to-use-bert-ner-sent-analysis

https://www.kaggle.com/johoshua/word-embedding-teach-machine-to-learn-words

https://www.kaggle.com/hoonkeng/deep-eda-word-embeddings-sentiment-analysis

https://www.kaggle.com/ankur561999/enron-email-classification-using-word-embeddings

https://www.kaggle.com/jannesklaas/17-nlp-and-word-embeddings

https://www.kaggle.com/tkrsh09/nlp-starter-complete-tpu-bert-guide-keras

https://www.kaggle.com/datafan07/disaster-tweets-nlp-eda-bert-with-transformers

https://www.kaggle.com/lapidshay/bilstm-for-text-classification

https://www.kaggle.com/urbanbricks/keras-lstm-for-document-classification

https://www.kaggle.com/kawiswara/malicious-web-detection-with-1d-cnn

https://www.kaggle.com/muonneutrino/sentiment-analysis-with-amazon-reviews

https://www.kaggle.com/zuhaalfaraj/customer-behavior-prediction-auc-85

https://www.kaggle.com/shival16/2020-kaggle-ml-ds-survey-generation-behavior

https://www.kaggle.com/tuli09/customer-behavior-prediction-model

> NLP 2

https://www.kaggle.com/vbmokin/nlp-eda-bag-of-words-tf-idf-glove-bert

https://machinelearningmastery.com/stacking-ensemble-for-deep-learning-neural-networks/

https://machinelearningmastery.com/stacking-ensemble-machine-learning-with-python/

https://machinelearningmastery.com/blending-ensemble-machine-learning-with-python/

https://machinelearningmastery.com/combine-predictions-for-ensemble-learning/

https://machinelearningmastery.com/ensemble-machine-learning-algorithms-python-scikit-learn/

https://www.datacamp.com/community/tutorials/ensemble-learning-python

https://www.analyticsvidhya.com/blog/2018/06/comprehensive-guide-for-ensemble-models/

https://stackabuse.com/ensemble-voting-classification-in-python-with-scikit-learn/

https://www.geeksforgeeks.org/ensemble-methods-in-python/

#### Part 1

https://www.kaggle.com/abhishek/approaching-almost-any-nlp-problem-on-kaggle

https://www.kaggle.com/arthurtok/introduction-to-ensembling-stacking-in-python

https://www.kaggle.com/sarikakv1221/human-dream-anlaysis-ner-sentiment-analysis-lda#Sentiment-Analysis

https://www.kaggle.com/jatinmittal0001/ner-bi-lstm-dealing-with-oov-words

https://www.kaggle.com/chopeen/custom-ner-to-recognize-risk-factor-names

https://www.kaggle.com/gabrielmv/ner-transformer

https://www.kaggle.com/bhagone/bi-lstm-for-ner

https://www.kaggle.com/shashaalam/ner-using-lstm-with-keras

https://www.kaggle.com/aiswaryaramachandran/ner-using-lstm-s-and-keras

#### Part 2

https://www.kaggle.com/stoicstatic/twitter-sentiment-analysis-using-word2vec-bilstm/

https://www.kaggle.com/alexcherniuk/imdb-review-word2vec-bilstm-99-acc

https://www.kaggle.com/rizdelhi/bilstm-model-for-sentence-classification

https://www.kaggle.com/prithiviraj/beginner-friendly-fastext-bilstmcnn-top-1

https://www.kaggle.com/xusiyang/sentimental-analysis-bilstm

https://www.kaggle.com/sumantindurkhya/movie-review-sentiment-bilstm-with-attention

https://www.kaggle.com/ujjwalsharma26/nlp-ml-tfidf-svc-and-dl-glove-bilstm-approach

https://www.kaggle.com/namanj27/bilstms-for-ner-liveplotloss

https://radimrehurek.com/gensim/auto_examples/tutorials/run_word2vec.html

https://www.analyticsvidhya.com/blog/2017/06/word-embeddings-count-word2veec/

https://www.kaggle.com/anilkrsah/name-entity-recognition

https://www.kaggle.com/aditya310794/name-entity-recognition

https://www.kaggle.com/navya098/bi-lstm-for-ner

https://www.kaggle.com/akshay235/bert-implementation-on-ner-corpus

https://www.kaggle.com/nikkisharma536/ner-with-bilstm-and-crf

https://www.kaggle.com/alouiamine/ner-using-bidirectional-lstm

https://www.kaggle.com/vishakha10/ner-using-bert-model

https://www.kaggle.com/ananysharma/ner-with-bi-lstm

https://www.kaggle.com/balraj98/ner-coreference-resolution-using-spacy

https://www.kaggle.com/dijorajsenroy/different-ways-to-use-bert-ner-sent-analysis

https://www.kaggle.com/ab971631/ner-with-bi-lstm-crf

https://www.kaggle.com/amarsharma768/custom-ner-using-spacy

https://www.kaggle.com/slavaz/spacy-ner-ensemble

https://www.kaggle.com/namanj27/bi-lstm-for-ner-with-liveplotloss

https://www.kaggle.com/rrishabhporwal/ner-detection

https://www.kaggle.com/rahulkumarpatro/ner-using-spacy

https://www.kaggle.com/farsanas/nlp-spacy-custom-named-entity-recognition-ner

https://www.kaggle.com/ashwinik/starter-basic-eda-and-ner-tagging-using-spacy

https://www.kaggle.com/haoxliu/ner-with-spacy

https://www.kaggle.com/kunduruanil/spacy-ner-model

https://www.kaggle.com/niyamatalmass/task-1-training-ner-model

https://www.kaggle.com/nishantbhadauria/hyderabad-zomato-nlp-t-sne-lda-eda-ner-pos

https://www.kaggle.com/foolishboi/spacy-ner

https://www.kaggle.com/nicolalandro/study-ner-named-entity-recognition-and-evaluation

https://www.kaggle.com/swapnilagashe/kernel-ner-tweet-support-sentence-extraction

https://www.kaggle.com/nanar69m/preprocessing-ner-srl-bert

https://www.kaggle.com/sunnyrain/nerual-network-with-keras

https://www.kaggle.com/mathurinache/ner-using-random-forest-and-crf

https://www.kaggle.com/yasash/custom-ner#Predicting-on-NEW-data

https://www.kaggle.com/ajithvajrala/ner-using-lstm

https://www.kaggle.com/rahulsattar/eda-and-ner-model

https://www.kaggle.com/revs96/exploring-spacy-tokenizer-phraser-ner#3.-Named-Entity-Recognizer

https://www.kaggle.com/ivanl1/training-spacy-ner-with-early-stopping

https://www.kaggle.com/eggwhites2705/transformers-ner

https://www.kaggle.com/shiki777/bert-ner-chinese

https://www.kaggle.com/tanyadayanand/tweet-sentiment-extraction-ner

https://www.kaggle.com/alewicka/mnist-digit-recognizer-cnn-in-keras-99-63

https://www.kaggle.com/dwarika/analysis-and-manual-cross-validation-with-knn

https://www.kaggle.com/hirazawahiroshi/visualization-tuning-ridge-lasso-xgboost

https://www.kaggle.com/kawiswara/malicious-web-detection-with-1d-cnn

https://www.kaggle.com/urbanbricks/keras-lstm-for-document-classification

https://www.kaggle.com/vbmokin/nlp-eda-bag-of-words-tf-idf-glove-bert

https://www.kaggle.com/lapidshay/bilstm-for-text-classification

https://www.kaggle.com/datafan07/disaster-tweets-nlp-eda-bert-with-transformers

https://www.kaggle.com/tkrsh09/nlp-starter-complete-tpu-bert-guide-keras

https://www.kaggle.com/jannesklaas/17-nlp-and-word-embeddings

https://www.kaggle.com/ankur561999/enron-email-classification-using-word-embeddings/?select=preprocessed.csv



> OCR

https://www.kaggle.com/ahoo1260/ocr-post-correction-using-nlp-bert

https://www.kaggle.com/zacchaeus/rl-ocr-pipeline

https://www.kaggle.com/dmitryyemelyanov/receipt-ocr-part-1-image-segmentation-by-opencv

https://www.kaggle.com/deshwalmahesh/image-processing-1-basic-ocr-feature-pooling-conv

https://www.kaggle.com/samfc10/handwriting-recognition-using-crnn-in-keras

https://www.kaggle.com/blagoyh/identifying-handwriting-with-ai-99-6

https://www.kaggle.com/rrishabhporwal/handwriting-recognisation-on-mnist

https://filingdb.com/b/pdf-text-extraction

https://docs.microsoft.com/en-us/azure/cognitive-services/bing-spell-check/quickstarts/python

https://github.com/pyenchant/pyenchant

https://github.com/KBNLresearch/ochre

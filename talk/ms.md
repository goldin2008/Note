## Presentation and Note
### Motivation
To extract information from journals automatically and easily, a soil science team from the United States Department of Agriculture (USDA) want to build a queryable journal paper data system, where users can easily identify journal papers of interest to them. 

### Introduction
To make system recommend journal papers to users automatically, we built machine learning and deep learning models to identify users' interests. Text analysis is applied on the text data to figure out what parts of paper the user are interested in, and stored them in the database to save users' search time.

We followed Prof. Seth's well formed table requirement and create tables in CSV format manually and used his program to store the table in a queryable machine readable format. The users can query and search key words or highlight some section or paragraph in the paper, then the system will provide the relevant information or recommend a paper which is of interest to users. This system will make future queries more efficient.

### Background
Embedding layer:
The Embedding layer is defined as the first hidden layer of a network.
An embedding is a relatively low-dimensional space into which you can translate high-dimensional vectors. Embeddings make it easier to do machine learning on large inputs like sparse vectors representing words.

1D-CNN:
To process an entire sequence of words, these kernels will slide down a list of word embeddings, in sequence. This is called a 1D convolution because the kernel is moving in only one dimension: time. A single kernel will move one-by-one down a list of input embeddings, looking at the first word embedding (and a small window of next-word embeddings) then the next word embedding, and the next, and so on. The resultant output will be a feature vector.

Multi-Channel CNN:
Just like in a typical convolutional neural network, one convolutional kernel is not enough to detect all the different kinds of features that will be useful for a classification task. To set up a network so that it is capable of learning a variety of different relationships between words, you’ll need many filters of different heights.

The diagonal of a ROC graph can be interpreted as random guessing and classification models that fall below the diagonal are considered as worse than random guessing. A perfect classifier would fall into the top left corner of the graph with a True Positive Rate of $1$ and a False Positive Rate of $0$. Based on the ROC curve, the so-called Area Under the Curve (AUC) can be used to calculate the performance of a classification model. The bigger AUC value, the better classification model.

`ROC curves are appropriate when the observations are balanced between each class, whereas precision-recall curves are appropriate for imbalanced datasets. In both cases the area under the curve (AUC) can be used as a summary of the model performance.`

### Web Scraping


### Data Statistical Description


### Text Classification
We need to first convert PDF to text format, since the text can not be read directly from PDF format. PDF conversion is a big challenge in our work. many PDF Text converters handle single column text well but fail when presented with a typical multiple-column layout by interlacing the multiple columns. For these journal papers, we need to clean the text, since after conversion from PDF format the text would get scrambled, with pieces of left column being mixed with the right one. Some papers have three columns, making the problem more serious. Another common problem is that the position of splitting is not fixed. Part of content in the first paragraph may be split to the second, or even third paragraph. These would make data cleaning tough.

1. Clean Data: We first clean numbers, punctuation marks, and other non letter characters in the text data, since they do not contain much useful semantic information in our project.
2. Tokenization: Tokenization is the process of breaking down a text corpus into individual elements that serve as input for various natural language processing algorithms. Usually, tokenization is accompanied by other optional processing steps, such as the removal of stop words and punctuation characters, stemming or lemmatizing, and the construction of n-grams.
3. Stop Words: We remove the stop words, since they are pretty common in all kinds of texts and do not contain much useful information for document classification. NLTK library has a set of 127 English stop words. And we could use it to remove stop words in the text.
4. Lowercase: Then we convert the text into lowercase characters, since the semantic information does not depend on whether the word is at the start of the sentence or not.
5. Stemming and Lemmatization: Stemming describes the process of transforming a word into its root form. In contrast to stemming, lemmatization aims to obtain the canonical (grammatically correct) forms of the words, the so-called lemmas. Lemmatization is computationally more difficult and expensive than stemming.
6. N-Grams: a token can be defined as a sequence of n items. The simplest case is the so-called unigram (1-gram) where each token consists of exactly one word, letter, or symbol. Choosing the optimal number n depends on the language as well as the particular application. In our work, we chose range $1$ to $3$ as n-gram grid search search to balance train time and performance due to compute resource limit.

`Deep Learning`
We can see LSTM achieved the best performance and it shows us that users will get 1 paper which they are interested in given every 2.89 recommendations.

To build a robust model, we need to catch all true positives and reduce false positives. we search the optimum cutoff to achieve this goal. The top two plots are for Percentage, while the bottom two are for Counts. They give us a clear tracking during the search. We search twice, the first search window is $0$ to $1$ which are probabilities of class 1 (interest). Then we narrow the search window and get a preciser cutoff, since a tiny cutoff change can change the model performance a lot.

CM shows we catch all positives and 195 (83\%) negatives. This means every 2.89 suggested papers, users can get 1 which they are interested. 2.89 is calculated on (103+195)/103. Because the data is imbalanced, accuracy is not a good metric for model evaluation. Our goal is to make sure all true positives can be identified since we hope the model does not miss any piece of text which users are interested in, while reduce the false positives since they are undesirable informaiton to users. To achieve this purpose, we built a custom metric which can catch all true positives and reduce false positives as many as it could.

### Named Entity Recognition
Named entities are definite noun phrases that refer to specific types of individuals, such as organizations, persons, locations, geo-political entities, date, percent etc. the purpose of NER is to identify all named entities. We used Stanford NER, which is a Java implementation of a Named Entity Recognizer, to identify persons and locations contained in the journal. 

### Table Analysis
`In Seth et al.'s algorithm, critical cells (CC1, CC2, CC3, CC4) delineate regions. In a WFT every critical cell must appear in the grid. CC1 and CC2 demarcate the StubHeader and CC3 and CC4 demarcate the Data region. Furthermore, in combination with one another, these critical cells also demarcate both the ColHeader and RowHeader regions. Letting row \textit{$r_i$} and column \textit{$c_i$} be the coordinates of critical cell CCi, a WFT satisfies the following constraints: $r_1 \leq r_2 < r_3 \leq r_4$ and $c_1 \leq c_2 < c_3 \leq c_4$. These constraints guarantee that the ColHeader and RowHeader regions properly align with the Data region and that the Data region is not degenerate. A single row or column of data is acceptable, provided both row and column headers exist.`

`In a well-formed table (WFT), every data cell is uniquely indexed by its row and column header paths, which are respectively left of and above the data region. A hierarchical (row or column) header may index one or more categories. A single-category header path consists of the root-to-leaf path of the corresponding category tree. A multi-category header path consists of concatenated category paths.`

`They do not deal with composite tables, nested tables (tables whose data cells may themselves be tables), tables containing graphic data.`

Their program could transform well-formed tables to a new canonical table format via: segmenting table regions by algorithmic data cell indexing, factoring header paths into categories by algorithmic header analysis, and generating queryable canonical relational tables.


We created 1006 tables for 207 journal papers in Comma-Separated Values (CSV) format manually. Then we ran the algorithm of Seth et al. to extract data from CSV and store them in a machine-readable format. 
There are 1006 tables in the 207 papers. Each table would cost 20-30 minutes, we test 50\% of them, so the total time spent on preparing and checking these 500 tables is about 280 hours.

The program can output two kinds of tables. One is a classification table. This table is in a five-column format, with a row entry (after the header row) for each cell of its source table. The first column is a unique cell identifier with the file name of the CSV table and the cell coordinates. The second and third rows give the numerical cell coordinates separately for ease of handling. The fourth column is the content of the cell in the original table, and the last column is its assigned class.\\

The other table is a category table which is a relational table where each row comprises the indexing header paths and the corresponding indexed data value. Therefore the number of rows in the category table equals the number of data cells in the original table (plus one for the relational table’s field names in a header row). The number of columns is one for the Cell$\_$ID, plus one for DATA, plus the sum of the heights of the category trees (which, usually, equals the sum of the column width of the row header and row height of the column header). In the category table, Cell$\_$ID is a key field and each cell label in the original header paths becomes a key field value in the composite key comprising all the category fields.

### Database System
We used Stanford NER to extract city and state from papers, wrote code to extract first five authors, Title, Publication Date, Abstract, Journal, DOI and Type from papers, and count if keywords defined by soil scientist appear in the paper. Then we used the algorithm of Seth et al. to convert the well-formed table (manually created by myself) to tables. Finally, we inserted all information mentioned above into Microsoft Access Database.

keywords are defined by soil scientist and they are used to count the occurrences of terms that soil scientists are interested in, including Conservation, No Tillage, Ridge Tillage, Mulch Tillage, Strip Tillage, Reduced Till etc. in Keyword 1 list and Germanium, Gold, Hafnium, Hassium etc. in Keyword 2 list. 

### Conclusion
The contributions of this thesis are:
1. Web harvesting: We downloaded 38,444 papers with size of 29.53 GB from Digital Library at University of Nebraska Lincoln.
2. Text Classification: We built a machine learning-based system to identify the sections or paragraphs in the papers that may be of interest to users based on their own search interest. The model we built can catch all positives and 83\% negatives. This means there is 1 paper of interest to users for every 2.89 suggested papers.
3. Table Analysis: After manually creating different kinds of tables in the journal papers, we used Seth et al.'s approach and found the program could process about 90\% of all tables, which are well-formed tables. For the other 10\% not well-formed tables, the program can not extract correct information.
4. Named Entity Recognition: We used Stanford's Named Entity Recognition to extract author and experiment location from paper and store them in data system which will make the future query more efficiently. The accuracy can reach about 83\%.
5. Database System Building: We stored the journal paper related information including Title, Publication Date, Abstract, Journal, DOI and Type, authors, city and state extracted from papers by Stanford NER, the count of the occurrences of terms of interest to soil scientists, and infromation contained in the well-formed table converted by the algorithm of Seth et al. \cite{t1} in the Microsoft Access Database.


Committee: \\
Prof. Stephen D. Scott \\
Prof. Vinodchandran Variyam \\
Prof. Ashok Samal \\

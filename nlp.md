## Natural Language Processing
#### NLP Pipeline #### 
This step-by-step processing of text is known as a pipeline. Note that, in the real world, the process may not always be linear as it’s shown in the pipeline in Figure 2-1; it often involves going back and forth between individual steps (e.g., between feature extraction and modeling, modeling and evaluation, and so on). Also, there are loops in between, most commonly going from evaluation to pre-processing, feature engineering, modeling, and back to evaluation. There is also an overall loop that goes from monitoring to data acquisition, but this loop happens at the project level.

***Data Acquisition***
- Use a public dataset
- Scrape data
    - Scrape the data from there and get it labeled by human annotators.
- Product intervention
- Data augmentation
- Synonym replacement
- Back translation
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

***Pre-processing***

***Feature engineering***

***Modeling***

***Evaluation***

***Deployment***

***Monitoring and model updating***
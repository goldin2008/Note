```mermaid
  graph TD;
      A-->B;
      A-->C;
      B-->D;
      C-->D;
```

```mermaid
graph TD
    A[User Interface] --> B[API Gateway];
    B --> C["AWS Lambda (RAG Function)"];
    C --> D["Amazon Kendra / Knowledge Bases for Amazon Bedrock"];
    D --> E["Amazon S3 (Data Sources)"];
    C --> F["Amazon Bedrock (LLM)"];
    F --> C;
    C --> G["Amazon DynamoDB (Chat History/State)"];
    G --> C;
    C --> B;
    B --> A;
```


Overview: This interview will be mostly conversational but may include some design drawing utilizing Excalidraw. This interview will walk through a realistic use-case for generative language models at Datadog. You will be asked to talk through how you would solve the problem, including framing the initial approach, evaluating, dealing with the practicalities of productionizing the solution, and possible optimizations. Familiarity with modern prompting and LLM techniques will be helpful. We will not go deep into Transformer architecture. You will be asked to design a LLM/NLP system similar to those we’ve built at Datadog which help translate natural language queries into a specialized query language used by our log management platform. We will look to see how you evaluate the performance of the translation system, how you consider cost and latency issues, how you would productionize this system, deploy it, and reduce memory load.

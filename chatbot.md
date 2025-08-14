``mermaid
graph TD
    A[User Interface] --> B[API Gateway];
    B --> C[AWS Lambda (RAG Function)];
    C --> D[Amazon Kendra / Knowledge Bases for Amazon Bedrock];
    D --> E[Amazon S3 (Data Sources)];
    C --> F[Amazon Bedrock (LLM)];
    F --> C;
    C --> G[Amazon DynamoDB (Chat History/State)];
    G --> C;
    C --> B;
    B --> A;
``

## AWS

### Non-relational Stores
- `Key Value Databases`
  - `Key-value databases` are a type of non-relational database that offer a simple yet powerful data model, enabling efficient storage and retrieval of data based on unique keys using distributed hash tables. This design principle, which revolves around mapping keys to their corresponding values, provides a highly scalable and flexible approach to data management. In this section, we will delve into the architecture and design considerations of key-value stores, uncovering the inner workings of these streamlined databases.
  - Open-source key-value databases provide developers with flexible and scalable solutions for managing data in a distributed and highly available manner. One popular open-source key-value store, Dynamo, has gained significant attention and adoption.
  `Dynamo` is a highly available and scalable key-value store developed by Amazon. It was designed to handle the demanding requirements of Amazon’s shopping cart service. While Dynamo itself is not open-source, its principles have influenced the development of various open-source implementations such as Riak, Voldemort, and Dynomite.
- `Document Databases`
  - `Document databases` are a type of non-relational database that are specifically designed for storing, retrieving, and managing semi-structured data in the form of documents. They provide a flexible and schema-less approach to data storage, making them ideal for applications with dynamic and evolving data structures. In this section, we will explore the architecture and design considerations of document stores, shedding light on their key features and benefits.
  - `MongoDB` is a widely adopted open-source document database known for its scalability, performance, and developer-friendly features. It uses a flexible JSON-like document model, allowing developers to store and retrieve data in a schema-less manner. MongoDB supports dynamic schemas, which means that each document in a collection can have its own unique structure.
- `Columnar Databases`
  - `Columnar databases` or column-family databases, also known as Wide column stores, are a type of non-relational database that offer a unique architecture optimized for handling vast amounts of structured and semi-structured data. These databases excel at managing large-scale distributed systems, analytics, and use cases requiring fast read and write performance. In this section, we will explore the architecture and design considerations of wide column stores, unveiling their key features and advantages.
  - `Apache Cassandra` is a highly scalable and distributed open-source columnar database known for its ability to handle massive amounts of structured and semi-structured data across multiple commodity servers. It offers a robust architecture and a range of features that make it suitable for high-performance and fault-tolerant applications. Let’s delve into Apache Cassandra and explore its key features.
- `Graph Databases`
  - `Graph databases` are a specialized type of non-relational database designed to handle highly interconnected data and complex relationships. They excel at storing, querying, and traversing graph-like structures, making them ideal for scenarios involving social networks, recommendation systems, fraud detection, and knowledge graphs. In this section, we will explore the architecture and design considerations of graph stores, uncovering their key features and advantages.
  - `Neo4j` is a leading open-source graph database known for its powerful graph processing capabilities and intuitive query language. Neo4j is designed to efficiently store, manage, and traverse highly connected data, making it ideal for applications that heavily rely on complex relationships and interconnections.

### Communication Networks and Protocols
`Communication Types`
- `Pull Mechanism: HTTP Polling`
- `Push Mechanism: WebSockets`
WebSockets represent a bi-directional persistent connection (full-duplex communication on a single TCP connection) over HTTP where clients and servers communicate with each other.
- `Push Mechanism: Server Sent Events`
The SSE can be a feasible approach in this case as the server is responsible for updating the order status and there is no as such input required from the client’s end.
The SSE is implemented over a long lived HTTP connection to consume any updates or notifications from the server in text format.
We mentioned that responses in case of async architectures can be delivered via websockets or SSE.

### AWS Network Services
AWS networking services such as Amazon VPC, Amazon Route 53, Amazon Elastic Load Balancer (ELB), Amazon API Gateway.
- Complete separation of applications, meaning every application is launched in a new AWS account.
- Separation of AWS accounts based on business type. All applications related to a single business will operate in a single account.
- Separation of AWS accounts based on software domains—for example, having separate accounts for networking, monitoring, storage, and security and auditing.

Further, there are some global services such as Amazon S3 or AWS Identity and Access Management (AWS IAM) service where region selection is not a requirement.
- `AWS Availability Zones`
You can think of a single region as a cluster of data centers and each individual (or combination of) data center is an availability zone.
AZ are classified with suffix to region names—for example, us-east-1a or us-east-1b are AZs within the us-east-1 region.
- `AWS Edge Locations`
Edge Locations help improve the performance of content delivery by acting as caching and content delivery endpoints for Amazon Cloudfront, thus reducing latency and improving data transfer speeds.
You can think of AWS Edge locations as data centers which are connected with AWS regions to support fast upload and download of data.
- `Amazon VPC`
We can think of Amazon VPC as your personal data center located inside AWS Cloud.
Amazon VPC enables you to securely launch resources like Amazon EC2 instances, Amazon RDS, and Amazon Elastic Load Balancers within a logically isolated section of the AWS cloud.
- `Subnets`
Each subnet is associated with an availability zone (AZ) within an AWS region.
The subnet can be a public subnet or private subnet depending on its connectivity to the internet.
The key point is that the direct route to the internet gateway is the only differentiating factor between public and private subnets. A subnet with resources having a public IPv4 address but no direct route to the internet gateway is referred to as a private subnet.
When setting up your VPCs and subnets inside your AWS account, consider these following best practices:
  - Use multiple subnets: Create multiple subnets within different availability zones to achieve fault tolerance and high availability.
  - Isolate resources: Use separate subnets for different types of resources to improve security and network segmentation.
  - Public and private subnets: Place resources with public access in public subnets and sensitive resources in private subnets.

`Internet Connectivity`
The routing of traffic and securing of resources is achieved via components such as route tables, internet gateway, security groups
- `Route Tables`
Route Tables direct network traffic in and out of a subnet but it doesn’t apply any security filters on this traffic. AWS provides software firewalls, Security Groups(SGs) and Network Access Control Lists(NACLs) to implement traffic filters which are useful in controlling the network traffic permissions.
- `Security Groups`
Let’s understand how SGs can help to control the traffic we want to essentially filter out or disallow any unwanted traffic. SGs are created at the VPC level and assigned at an instance level, controlling inbound and outbound traffic at an instance level based on protocols, ports and IP addresses. Your EC2 instance can have one or more SGs. There will always be one SG associated to an instance, and, if not created, a default SG will be associated, which is created at time of VPC creation.
- `Network Access Control Lists`
You may think of NACLs as an additional layer of security on top of SGs which ensure to block the traffic if SGs are too flexible.
Route Tables, SGs and NACLs help to configure the routes and configure network security.

`Amazon VPC To Internet Connectivity`
- `Internet Gateway`
Internet Gateway (IGW) is a horizontally scalable and highly available AWS managed VPC software component that provides connection between your VPC and the internet.
The private subnet to public internet connectivity is achieved via a NAT Gateway.
- `NAT Gateway`
You may think of NAT gateway as a bridge between internet gateway and private instances.
NAT Gateways (Network Address Translation Gateways) are AWS-managed network devices that allow resources within private subnets in a VPC to initiate outbound internet connections while preventing direct inbound access from the internet by hiding their private IP addresses.
it converts private IP address to NAT device public IP address and is mapped back to private IP address on return of response from internet.
NAT gateway provides public(default) and private connectivity.

`Amazon VPC to Amazon VPC Connectivity`
- `AWS Transit Gateways`
Transit Gateway is a scalable solution to establish connectivity between multiple VPCs, on-premise networks and other AWS services.

- `Amazon Route 53`
Route 53 is a scalable and highly available Domain Name System(DNS) available in the AWS ecosystem which helps in domain registration, DNS routing and health checking.
- `Amazon Elastic Load Balancer`
Load Balancers help improve the availability, scalability, and fault tolerance of applications by distributing traffic across healthy targets. Load balancers can automatically scale based on traffic patterns and health checks, ensuring optimal performance.
AWS ELB is available as Application Load Balancer (ALB), Network Load Balancer (NLB), Classic Load Balancer(CLB) and Gateway Load Balancer(GWLB).
- `Amazon API Gateway`
API Gateway is a fully managed AWS service that helps in creating, publishing, maintaining, monitoring and securing REST, HTTP and WebSocket APIs.
- `Amazon CloudFront`
Another cost effective solution is to cache the content near the customer’s location via a Content Delivery Network (CDN), as discussed in Chapter 4. Amazon CloudFront is CDN, a world-wide network of data centers called edge locations which helps to achieve low latency for serving both static and dynamic content in a secure way via AWS Shield, IAM, WAF and TLS certificates.
In short, Amazon CloudFront allows us to cache the content near our application users and serve the user queries faster.

### AWS Storage Services

### AWS Compute Services

### AWS Orchestration Services

### Big Data, Analytics and Machine Learning Services

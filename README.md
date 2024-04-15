# DE-project
# Overview
The goal of this project is to apply data engineering (DE) concepts to orchestrate a real time pipeline to ingest data from a financial API to Amazon Cloud Platform and perform simple transformation and visualization with dashboards. The project uses an "extract-transform-load" (ETL) philosophy, where data is sent into AWS by kenisis producer and then subsequently transformed and loaded by Lambda function into DynamoDB in AWS.<br>
The data was ingested using websocket method and Finnhub Stock API (https://finnhub.io/). <br>
A data dictionary for specific API can be found at Finnhub website.<br>
I've presented a small overview of some of the data analysis in a dashboard where you can get a general idea about what it has done.<br>

# Pipeline Technologies
The pipeline was built to get real time Finnhub, and use Amazon components to store data and make real-time analysis dashboard. <br>

Amazon Kinesis is a scalable and durable real-time data streaming service provided by AWS. It enables continuous collection and analysis of large streams of data records. With Kinesis, you can ingest real-time data such as video, audio, application logs, website clickstreams, and IoT telemetry data for machine learning, analytics, and other applications. Kinesis can handle high throughput and scale with ease, allowing you to process and analyze data as it arrives and respond in real-time. <br>

Finnhub API is a comprehensive financial data API that provides real-time market data, financial statements, SEC filings, stock fundamentals, and historical market data. It’s designed for investors, traders, and developers looking to integrate financial data into their applications, websites, or algorithms. Finnhub offers a wide array of financial information including news, analysis, forex, and cryptocurrency data, making it a versatile tool for financial analysis.  <br>

AWS Lambda is a serverless compute service offered by Amazon Web Services, which automatically manages the computing infrastructure required to run code in response to events. Lambda enables you to run code without provisioning or managing servers, and you're only charged for the compute time you consume. With Lambda, you can execute code for virtually any type of application or backend service with zero administration. Just upload your code, and Lambda takes care of everything required to run and scale your code with high availability. <br>



# Data Ingestion
Data is ingested in Kafka-like methods using the python script. Data for each category (stock) is extrated immediately through Finnhub API, formatted to json, uploaded to Amazon in an automatical way. <br>



# Transformations
Then lamdba functions were used to do the transformation.



# Data Warehouse
We use DynamoDB as our data warehouse. <br>
Amazon DynamoDB is a fully-managed NoSQL database service provided by AWS. It delivers reliable performance at any scale, making it a go-to solution for mobile, web, gaming, ad tech, IoT, and many other applications that require low-latency data access. DynamoDB supports both document and key-value data models, and it offers features such as ACID transactions, in-memory caching with DynamoDB Accelerator (DAX), and built-in security, backup, restore, and in-place data modification capabilities. <br>


# Dashboard/Visualization


# Reproducing this repo
1.Prepare Python3 and AWS service accounts with appropriate permissions for Kenisis and DynamoDB. <br>
2. Configure the Lambda Function.


# Future Improvement
1.Improve project documentation. <br>
2.Make more transformation methods.

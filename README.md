# DE-project
# Overview
The goal of this project is to apply data engineering (DE) concepts to orchestrate a real time pipeline to ingest data from a financial API to Amazon Cloud Platform and perform simple transformation and visualization with dashboards. The project uses an "extract-transform-load" (ETL) philosophy, where data is sent into AWS by kenisis producer and then subsequently transformed and loaded by Lambda function into DynamoDB in AWS.<br>
The data was ingested using websocket method and Finnhub Stock API (https://finnhub.io/). <br>
A data dictionary for specific API can be found at Finnhub website.<br>
I've presented a small overview of some of the data analysis in a dashboard where you can get a general idea about what it has done.<br>

# Pipeline Technologies
The pipeline was built to get real time data from Finnhub using websocket API, and use Amazon components to store data in DynamoDB. Then we use middleware called Rockset and PowerBI to make real-time analysis dashboard. <br>

![alt text](https://github.com/XiaoLirui/DE-project/blob/main/other%20files/pipeline.png)

Amazon Kinesis is a scalable and durable real-time data streaming service provided by AWS. It enables continuous collection and analysis of large streams of data records. With Kinesis, you can ingest real-time data such as video, audio, application logs, website clickstreams, and IoT telemetry data for machine learning, analytics, and other applications. Kinesis can handle high throughput and scale with ease, allowing you to process and analyze data as it arrives and respond in real-time. <br>

Finnhub API is a comprehensive financial data API that provides real-time market data, financial statements, SEC filings, stock fundamentals, and historical market data. It’s designed for investors, traders, and developers looking to integrate financial data into their applications, websites, or algorithms. Finnhub offers a wide array of financial information including news, analysis, forex, and cryptocurrency data, making it a versatile tool for financial analysis.  <br>

AWS Lambda is a serverless compute service offered by Amazon Web Services, which automatically manages the computing infrastructure required to run code in response to events. Lambda enables you to run code without provisioning or managing servers, and you're only charged for the compute time you consume. With Lambda, you can execute code for virtually any type of application or backend service with zero administration. Just upload your code, and Lambda takes care of everything required to run and scale your code with high availability. <br>



# Data Ingestion
Data is continuously ingested using Kafka-like methods through a Python script. This script automatically extracts real-time data for each category (such as individual stocks) directly from the Finnhub API. After extraction, the data is formatted into JSON and automatically uploaded to Amazon cloud services. Simultaneously, the Kethesis data stream consistently captures and processes data streams from remote topic subscriptions provided by the Python script, ensuring seamless real-time data integration and accessibility. This system enables efficient and scalable handling of large volumes of financial data, optimizing data flow and storage for enhanced analytical processing.<br>



# Transformations
AWS Lambda functions are triggered by an upstream event from the Kethesis data stream. This trigger is activated continuously as data flows into the Kethesis data stream, ensuring that the Lambda functions are invoked in real-time upon data arrival. These functions are responsible for performing ETL (Extract, Transform, Load) processes on the incoming streaming data. After transformation, the processed data is efficiently routed to Amazon DynamoDB for persistent storage. This automated pipeline facilitates real-time data processing and storage, enabling rapid access and retrieval of transformed data for further analysis and application use.



# Data Warehouse
We use DynamoDB as our data warehouse. <br>
Amazon DynamoDB is a fully-managed NoSQL database service provided by AWS. It delivers reliable performance at any scale, making it a go-to solution for mobile, web, gaming, ad tech, IoT, and many other applications that require low-latency data access. DynamoDB supports both document and key-value data models, and it offers features such as ACID transactions, in-memory caching with DynamoDB Accelerator (DAX), and built-in security, backup, restore, and in-place data modification capabilities. <br>


# Dashboard/Visualization
We employ Power BI as our primary tool for data visualization. Power BI is a robust business analytics service provided by Microsoft that enables users to create interactive reports and dashboards. It offers comprehensive capabilities for data aggregation, visualization, and sharing, allowing us to gain deep insights into our data through rich visualizations and customized reports.

Additionally, we utilize Rockset, a real-time indexing database service designed for rapid, low-latency queries at scale. Rockset is particularly advantageous due to its excellent integration with DynamoDB. This integration allows us to execute complex queries directly on our DynamoDB data without the need for manual data extraction and transformation, thus enhancing our data processing workflows.

![alt text](https://github.com/XiaoLirui/DE-project/blob/main/other%20files/Rockset.png)

The reason we use Rockset stems from its seamless connectivity with DynamoDB, enabling efficient real-time data operations. In this setup, we utilize the Rockset Python SDK to create a Query Lambda. This Query Lambda acts as a powerful intermediary, allowing us to run SQL-like queries over our DynamoDB data, which is especially useful for integrating with external data visualization tools like Power BI.

To configure Rockset with Power BI, we leverage the Power BI Python SDK. This integration involves preparing a Python script within Power BI that uses the Rockset Python SDK. The script executes the Query Lambda, and the results are then used as input data for Power BI’s visualizations. This approach allows us to dynamically visualize and interact with our data in Power BI, using the latest updates processed by Rockset in near-real-time. This method provides a streamlined, efficient pipeline for visual analytics, enhancing our decision-making processes with up-to-date insights derived directly from our operational database.

![alt text](https://github.com/XiaoLirui/DE-project/blob/main/other%20files/Dashboard.png)

# Reproducing this repo
1.Prepare Python3 and AWS service accounts with appropriate permissions(IAM) for Kenisis and DynamoDB. <br>
2. Configure the Lambda Function.


# Future Improvement
1.Improve project documentation. <br>
2.Make more transformation methods.

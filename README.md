# DE-project
# Overview
The goal of this project is to apply data engineering (DE) concepts to orchestrate a real time pipeline to ingest data from a financial API to Amazon Cloud Platform and perform simple transformation and visualization with dashboards. The project uses an "extract-transform-load" (ETL) philosophy, where data is sent into AWS by kenisis producer and then subsequently transformed and loaded by Lambda function into DynamoDB in AWS.

The data was ingested using websocket method and Finnhub Stock API (https://finnhub.io/). 

A data dictionary for specific API can be found at Finnhub website.

I've presented a small overview of some of the data analysis in a dashboard where you can get a general idea about what it has done.

# Pipeline Technologies
The pipeline was built to get real time Finnhub, and use Amazone components to store data dating back to 1999, as well as team injury data (back to 2009).

Apache Airflow is used to orchestrate batch data ingestion into the Google Cloud Storage (GCS) data lake and Google BigQuery (BQ) data warehouse. dbt is used to perform transformations within BQ where core metrics for game-by-game performance of NFL wide receivers are calculated and used as a final 'data mart' layer for Tableau. All infrastracture for GCP is deployed with Terraform. Airflow is deployed on a Docker image using docker-compose.

# Data Ingestion




# Transformations




# Data Warehouse


# Dashboard/Visualization


# Reproducing this repo
1.Prepare Python3 and AWS service accounts with appropriate permissions for Ken and BQ
Set up a VM on Google Cloud with docker, docker-compose, and git.
Clone this repo to the VM
Set up appropriate GCP credentials on the VM (including installing google cloud SDK and granting appropriate permissions)
Change user-specific attributes in code:
In Terraform variables.tf change project id, region, and name of the GCS bucket to your GCS bucket
In docker-compose.yaml change the environment variables for google cloud authentication, your GCP project ID, and the GCP bucket you're using
Build image using docker build in /airflow/, and run airflow using docker-compose up
Forward port 8080 and connect to it on your local machine. Unpause the DAGs - they should catch up to the current year
Grant dbt cloud the appropriate permissions for GCP and connect it to your DWH


# Future Improvement
Improve project documentation

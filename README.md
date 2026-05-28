# Real-Time Retail Data Pipeline

A real-time retail data engineering project built with Python, Kafka, Spark, and layered data architecture principles.

This project simulates a retail company's streaming order pipeline using intentionally messy and imperfect data to practice real-world data engineering scenarios including:

* Streaming ingestion with Kafka
* Producer/Consumer workflows
* Bronze/Silver/Gold architecture
* Dirty data handling
* Data cleaning and transformation
* Schema standardization
* Data quality validation

The pipeline generates realistic retail activity including customers, products, suppliers, employees, and streaming orders with simulated inconsistencies such as:

* Missing values
* Invalid foreign keys
* Duplicate records
* Incorrect date formats
* Future timestamps
* Negative quantities
* Corrupted business records

The goal of the project is to build hands-on experience with modern data engineering workflows and realistic ETL challenges.

Powered by caffeine, Kafka, and vampire working hours.




## Architecture

The project follows a layered data architecture approach:

* **Bronze Layer** → Raw ingested streaming and generated data
* **Silver Layer** → Cleaned and standardized datasets
* **Gold Layer** → Final analytical datasets and reporting-ready outputs

This structure simulates real-world ETL and modern data engineering workflows.

## Technologies Used

* Python
* Apache Kafka
* PySpark
* Pandas
* Docker
* CSV-based storage layers

## Project Structure

```bash
KafkaLearning/
│
├── bronze/
├── silver/
├── gold/
│
├── generators/
│   ├── generate_customers.py
│   ├── employees_csv.py
│   ├── products_csv.py
│   └── suppliers_csv.py
│
├── streaming/
│   ├── streaming_orders_producer.py
│   └── streaming_orders_consumer.py
│
├── transformations/
│   └── silver_transform.py
│
├── docker-compose.yml
├── requirements.txt
├── README.md
└── .gitignore
```

## Pipeline Flow

1. Generate retail datasets (customers, employees, suppliers, products)
2. Stream order events through Kafka producer
3. Consume streaming events into Bronze layer storage
4. Simulate dirty and inconsistent real-world data
5. Clean and standardize records in the Silver layer
6. Prepare future analytical datasets in the Gold layer

## Dirty Data Simulation

The project intentionally generates problematic records to simulate realistic business data challenges, including:

* Missing values
* Invalid customer IDs
* Duplicate order IDs
* Future dates
* Incorrect date formats
* Negative quantities
* Inconsistent text formatting
* Corrupted business logic

## Future Improvements

Planned future improvements include:

* Automated data quality checks
* Spark streaming transformations
* Alerting and monitoring systems
* Power BI dashboards
* Data warehouse integration
* Pipeline orchestration
* Real-time business triggers

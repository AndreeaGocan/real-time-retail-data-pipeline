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

The Medallion Architecture (Bronze, Silver, and Gold layers) was implemented in Azure Databricks and organized using Unity Catalog schemas.

Powered by caffeine, Kafka, and vampire working hours.

## Highlights
* Built a Medallion Architecture (Bronze, Silver, Gold).
* Implemented dimensional modeling using a star-schema analytical layer built with views.
* Developed analytical summary views for reporting.
* Integrated Azure Data Lake Storage and Azure Databricks.
* Created Power BI dashboards for customer, product, and sales analytics.
* Simulated real-world data quality issues and remediation workflows.
* Designed a streaming ingestion pipeline using Apache Kafka.


## Architecture

The project follows a layered data architecture approach:

* **Bronze Layer** → Raw ingested streaming and generated data
* **Silver Layer** → Cleaned and standardized datasets
* **Gold Layer** → Final analytical datasets and reporting-ready outputs

This structure simulates real-world ETL and modern data engineering workflows.

## Current Project Status

### Completed

* ✅ Synthetic retail data generation
* ✅ Kafka Producer for streaming retail sales and order details
* ✅ Multiple Kafka Consumers for Bronze layer ingestion
* ✅ Bronze Layer implementation
* ✅ Orders Silver Layer implementation
* ✅ Data quality validation framework
* ✅ Customer Silver Layer implementation
* ✅ Product Silver Layer implementation
* ✅ Supplier Silver Layer implementation
* ✅ Employee Silver Layer implementation
* ✅ Order Details Kafka Stream
* ✅ Order Details Silver Layer implementation
* ✅ Gold Layer implementation
* ✅ Customer Summary analytical view
* ✅ Product Summary analytical view
* ✅ Sales Summary analytical view
* ✅ Azure Data Lake Storage integration
* ✅ Azure Databricks implementation
* ✅ Gold dimensional model
* ✅ Fact table implementation
* ✅ Power BI dashboards

## Orders Silver Layer Features

The Orders Silver Layer performs data cleaning and validation before data is passed to downstream layers.

## Customer Silver Layer Features

The Customer Silver Layer standardizes and validates customer records before they are passed to downstream analytical layers.

## Product Silver Layer Features

The Product Silver Layer standardizes and validates product records before they are passed to downstream analytical layers.

## Supplier Silver Layer Features

The Supplier Silver Layer performs data quality validation on supplier records before they are used by downstream analytical processes.

## Employee Silver Layer Features

The Employee Silver Layer standardizes and validates employee records before they are used by downstream analytical processes.

## Order Details Silver Layer Features

The Order Details Silver Layer validates transactional order metadata before it is passed to downstream analytical layers.

## Gold Layer Features

The Gold Layer transforms cleaned Silver datasets into business-ready analytical models using dimensional modeling principles.

Implemented components include:

## Dimension Views

* Customer dimension containing demographic and geographic customer attributes
* Product dimension containing product and category information
* Employee dimension containing employee and management hierarchy information
* Order dimension containing order metadata and transactional attributes

## Fact Table

* Centralized sales fact view
* Foreign key relationships to business dimensions
* Transaction-level sales metrics
* Optimized structure for analytical reporting and dashboard consumption

## Analytical Summary Views

## Customer Summary

Provides customer-level performance metrics including:

* Total sales by customer
* Customer lifetime value metrics
* Purchase behavior analysis
* Customer segmentation
* Recency and lifecycle measurements

## Product Summary

Provides product-level analytical metrics including:

* Product sales performance
* Category rankings
* Customer reach metrics
* Product lifecycle analysis
* Revenue and sales velocity measurements

## Sales Summary

Provides daily sales trend analysis including:

* Daily revenue tracking
* Day-over-day growth analysis
* Previous-day sales comparisons
* Rolling 7-day sales metrics
* Business performance trend monitoring

The project includes three interactive Power BI dashboards built on top of the Gold analytical layer.

## Power BI Dashboards

### Sales Dashboard

![Sales Dashboard](dashboards/Sales_Performance_dashboard.png)

### Products Dashboard

![Product Dashboard](dashboards/Product_performance_dashboard.png)

### Customers Dashboard

![Customer Dashboard](dashboards/Customer_analytics_dashboard.png)



### Project Roadmap

| Phase                                         | Status         |
| --------------------------------------------- | -------------- |
| Data Generation                               | ✅ Completed    |
| Kafka Streaming                               | ✅ Completed    |
| Bronze Layer                                  | ✅ Completed    |
| Orders Silver Layer                           | ✅ Completed    |
| Customer Silver Layer                         | ✅ Completed    |
| Product Silver Layer                          | ✅ Completed    |     
| Supplier Silver Layer                         | ✅ Completed    |
| Employee Silver Layer                         | ✅ Completed    |
| Order Details Silver Layer                    | ✅ Completed    |
| Gold Layer                                    | ✅ Completed    |
| Power BI Dashboard                            | ✅ Completed    |
| Lakehouse Expansion (Databricks + Delta Lake) | ✅ Completed    |
| Pipeline Automation                           | 🔄 In Progress  |
| Pipeline Health Monitoring                    | ⏳ Planned |





## Technologies Used

* Python
* Apache Kafka
* PySpark
* Pandas
* Docker
* CSV-based storage layers
* Azure Storage Account
* Azure Data Lake Storage Gen2
* Azure Databricks
* Databricks SQL
* Unity Catalog
* Power BI
* Git
* GitHub

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
│   ├──  streaming_orders_consumer.py
│   └── streaming_order_details_consumer.py
│
├── transformations/
│   ├── silver_orders_transform.py
│   ├── silver_customers_transform.py
│   ├── silver_products_transform.py
│   ├── silver_suppliers_transform.py
│   ├── silver_employees_transform.py
│   └── silver_order_details_transform.py
│
├── dimensions/
│   ├── dim_customers.sql
│   ├── dim_products.sql
│   ├── dim_employees.sql
│   └── dim_orders.sql
│
├── facts/
│   └── fact_sales.sql
│
├──  summaries/
│    ├── customer_summary.sql
│    ├── product_summary.sql
│    └── sales_summary.sql
│
├── dashboards/
│   ├── sales_dashboard.png
│   ├── product_performance_dashboard.png
│   ├── customer_analytics_dashboard.png
│   └── retail_analytics.pbix
│
├── docker-compose.yml
├── requirements.txt
├── README.md
└── .gitignore
```

## Architecture Diagram

```text
Data Generators
        ↓
Apache Kafka
        ↓
Azure Data Lake Storage
        ↓
Databricks Bronze
        ↓
Databricks Silver
        ↓
Databricks Gold
        ↓
Power BI Dashboards
```

## Pipeline Flow

1. Generate retail datasets (customers, employees, suppliers, products)
2. Stream order events through Kafka producer
3. Consume streaming events into Bronze layer storage
4. Simulate dirty and inconsistent real-world data
5. Clean and standardize records in the Silver layer
6. Build dimensional models and fact views in the Gold layer
7. Create analytical summary views for business reporting
8. Prepare datasets for dashboarding and BI consumption

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

## Next Steps

* Star and Snowflake schema modeling
* Automated data quality monitoring and validation reporting
* Pipeline health and execution monitoring
* Business alerting and anomaly detection

## Planned Monitoring Features

* Automated alerts when sales drop below historical averages
* Notifications for unusual spikes or declines in product demand
* Pipeline status monitoring for ingestion and transformation jobs
* Data quality reports highlighting failed validation checks
* Dashboard refresh and data pipeline execution tracking
* Exception reporting for missing, invalid, or inconsistent records




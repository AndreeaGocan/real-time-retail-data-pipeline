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

## Orders Silver Layer Features

The Orders Silver Layer performs data cleaning and validation before data is passed to downstream layers.

Implemented checks include:

* Standardized mixed date formats into a consistent DateType format
* Removed future order dates
* Removed duplicate order records
* Removed invalid customer IDs
* Removed invalid product IDs
* Removed invalid supplier IDs
* Removed missing foreign keys
* Removed negative quantities
* Validated sales calculations against quantity × unit price
* Removed invalid sales values

## Customer Silver Layer Features

The Customer Silver Layer standardizes and validates customer records before they are passed to downstream analytical layers.

Implemented checks include:

* Standardized customer first names
* Standardized customer last names
* Handled missing country values
* Calculated customer age from birthdate
* Validated customer age against business rules (16–100 years old)
* Identified future birthdates
* Quarantined invalid customer records for investigation
* Separated valid and rejected customer datasets

## Product Silver Layer Features

The Product Silver Layer standardizes and validates product records before they are passed to downstream analytical layers.

Implemented checks include:

* Standardized product names
* Standardized product categories
* Preserved original brand values
* Identified products with missing unit prices
* Identified products with negative stock quantities
* Validated supplier references against the supplier dataset
* Quarantined invalid product records for investigation
* Separated valid and rejected product datasets

## Supplier Silver Layer Features

The Supplier Silver Layer performs data quality validation on supplier records before they are used by downstream analytical processes.

Implemented checks include:

* Missing supplier ID validation
* Supplier ID uniqueness validation
* Missing supplier name validation
* Missing email validation
* Lead time validation
* Reliability score validation (0-100 range)
* Supplier quality audit reporting

## Employee Silver Layer Features

The Employee Silver Layer standardizes and validates employee records before they are used by downstream analytical processes.

Implemented checks include:

* Standardized department names
* Preserved IT department abbreviation
* Standardized country values
* Converted manager IDs to the correct integer data type
* Validated manager references against existing employee records
* Allowed null manager IDs for top-level management positions
* Performed employee-manager integrity validation
* Validated employee salary values
* Removed employees with missing or invalid salaries

## Order Details Silver Layer Features

The Order Details Silver Layer validates transactional order metadata before it is passed to downstream analytical layers.

Implemented checks include:

* Order ID validation
* Order ID uniqueness validation
* Customer ID validation
* Order status validation
* Payment method validation
* Sales channel validation
* Discount code validation
* Future order date validation
* Order details quality audit reporting

## Gold Layer Features

The Gold Layer transforms cleaned Silver datasets into business-ready analytical models using dimensional modeling principles.

Implemented components include:

## Dimension Views

* Customer dimension containing demographic and geographic customer attributes
* Product dimension containing product and category information
* Employee dimension containing employee and management hierarchy information
* Order dimension containing order metadata and transactional attributes

## Fact Table

* Centralized sales fact table
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

Implemented dashboards include:

• Sales Dashboard
  - Revenue trends
  - Order performance
  - Rolling 7-day metrics
  - Growth analysis

• Product Dashboard
  - Product performance analysis
  - Category contribution
  - Demand monitoring
  - Revenue rankings

• Customer Dashboard
  - Customer segmentation
  - Revenue contribution analysis
  - Customer demographics
  - Activity monitoring



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
| Pipeline Automation                           | 🔄 In Progress  |
| Pipeline Health Monitoring                    | ⏳ Planned |
| Lakehouse Expansion (Databricks + Delta Lake) | ⏳ Planned |




## Technologies Used

* Python
* Apache Kafka
* PySpark
* Pandas
* Docker
* CSV-based storage layers
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

## Pipeline Flow

1. Generate retail datasets (customers, employees, suppliers, products)
2. Stream order events through Kafka producer
3. Consume streaming events into Bronze layer storage
4. Simulate dirty and inconsistent real-world data
5. Clean and standardize records in the Silver layer
6. Build dimensional models and fact tables in the Gold layer
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

## Future Enhancements

* Azure Blob Storage / Azure Data Lake integration
* Databricks implementation with Delta Lake
* Lakehouse architecture using the Medallion (Bronze, Silver, Gold) approach
* Star and Snowflake schema modeling
* PostgreSQL Data Warehouse implementation
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




/*
====================================================================================
View: gold.fact_sales
====================================================================================
Description:
    Sales fact table containing transactional sales records and measurable
    business metrics.

Business Purpose:
    Serves as the central fact table for sales analytics, enabling reporting
    on revenue, product performance, customer behavior, employee performance,
    and sales trends over time.

Grain:
    One row per sales transaction.

Primary Key:
    order_id

Foreign Keys:
    - customer_id
    - product_id
    - employee_id

Measures:
    - quantity
    - unit_price
    - sales

Attributes:
    - Order date

Source Tables:
    - silver.sales
====================================================================================
*/

CREATE VIEW gold.fact_sales AS

SELECT
    order_id,
    customer_id,
    product_id,
    employee_id,
    quantity,
    unit_price,
    sales,
    order_date
FROM silver.sales;


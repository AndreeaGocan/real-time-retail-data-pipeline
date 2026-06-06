/*
====================================================================================
View: gold.dim_customers
====================================================================================
Description:
    Customer dimension containing demographic and descriptive customer attributes.

Business Purpose:
    Supports customer-based analysis and reporting by providing a centralized
    customer dimension for analytical models and dashboards.

Grain:
    One row per customer.

Primary Key:
    customer_id

Source Tables:
    - silver.customers
====================================================================================
*/

CREATE VIEW gold.dim_customers AS

--==================================================================================
-- Base Query
--==================================================================================

WITH customer_base AS (
    SELECT
        customer_id,
        customer_full_name,
        country,
        birthdate,
        EXTRACT(YEAR FROM AGE(CURRENT_DATE, birthdate))::INT AS customer_age
    FROM silver.customers
)

--==================================================================================
-- Final Query
--==================================================================================

SELECT
    customer_id,
	customer_full_name,
	country,
	birthdate,
	customer_age,
    CASE
        WHEN customer_age < 20 THEN 'Under 20'
        WHEN customer_age BETWEEN 20 AND 29 THEN '20-29'
        WHEN customer_age BETWEEN 30 AND 39 THEN '30-39'
        WHEN customer_age BETWEEN 40 AND 49 THEN '40-49'
        ELSE '50 and Above'
    END AS age_group
FROM customer_base;
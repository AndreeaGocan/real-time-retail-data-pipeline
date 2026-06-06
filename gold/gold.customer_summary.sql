/*
====================================================================================
View: gold.customers_summary
====================================================================================
Description:
    This view provides customer-level analytical metrics and behavioral insights
    including purchasing activity, spending behavior, customer lifecycle,
    purchase frequency, recency, and customer segmentation.

Business Purpose:
    Supports customer analytics, customer segmentation, retention analysis,
    purchasing behavior analysis, and business intelligence reporting.

Grain:
    One row per customer.

Primary Key:
    customer_id

Key Metrics:
    - Total orders
    - Total products purchased
    - Total sales
    - Average order value
    - Average monthly spend
    - Yearly purchase frequency
    - Customer lifespan
    - Customer recency

Derived Attributes:
    - Age group
    - Customer segment (VIP, Regular, New)
    - Activity status (Active, Inactive)
    - Purchase frequency segment

Source Tables:
    - silver.sales
    - silver.customers

Business Rules:
    - Customer age is calculated from birthdate.
    - Recency is calculated as the difference between the latest order date
      in the dataset and the customer's most recent purchase date.
    - Lifespan is calculated as the difference between the first and last
      purchase dates.
    - Customer segmentation is based on lifespan and total sales.
    - Purchase frequency is calculated as total orders per active year.
====================================================================================
*/

CREATE VIEW gold.customers_summary AS
--========================================================
-- Base Layer
--========================================================
WITH customers_base AS 

(SELECT
	s.order_id,
	s.product_id,
	s.quantity,
	s.sales,
	s.order_date,
	c.customer_id,
	c.customer_full_name,
	c.country,
	c.birthdate
FROM silver.sales AS s
LEFT JOIN silver.customers AS c
ON s.customer_id = c.customer_id
WHERE order_date IS NOT NULL),
--========================================================
-- Aggregations Layer
--========================================================
customer_aggregations AS

(SELECT
	customer_id,
	customer_full_name,
	country,
	EXTRACT(YEAR FROM AGE(CURRENT_DATE, birthdate))::INT AS customer_age,
	COUNT(DISTINCT order_id) AS total_orders,
	SUM(quantity) AS total_products,
	SUM(sales) AS total_sales,
	MIN(order_date) AS first_order_date,
	MAX(order_date) AS last_order_date,
	(MAX(order_date) - MIN(order_date)) AS lifespan,
	(
		SELECT 
			MAX(order_date)
		FROM customers_base
	) - MAX(order_date) AS recency,
	ROUND(
		SUM(sales) / 
		NULLIF(COUNT(DISTINCT DATE_TRUNC('month', order_date)),0)
		,2) AS avg_monthly_spend
FROM customers_base
GROUP BY 
	customer_id,
	birthdate,
	customer_full_name,
	country),

--========================================================
-- Customer Metrics
--========================================================
customer_metrics AS

(SELECT
	customer_id,
	customer_full_name,
	customer_age,
	country,
	CASE
		WHEN customer_age < 20 THEN 'Under 20'
		WHEN customer_age BETWEEN 20 AND 29 THEN '20-29'
		WHEN customer_age BETWEEN 30 AND 39 THEN '30-39'
		WHEN customer_age BETWEEN 40 AND 49 THEN '40-49'
		ELSE '50 and Above'
	END AS age_group,
	lifespan,
	CASE 
		WHEN lifespan >= 365 AND total_sales >= 10000
			THEN 'VIP'
		WHEN lifespan >= 90 AND total_sales >= 5000
			THEN 'REGULAR'
		ELSE 'NEW'
	END AS customer_segment,
	recency,
	CASE
		WHEN recency > 365 THEN 'INACTIVE'
		ELSE 'ACTIVE'
	END AS activity_status,
	CASE 
		WHEN total_orders = 0 THEN 0
		ELSE ROUND((total_sales/total_orders)::numeric, 2)
	END AS avg_order_value,
	avg_monthly_spend,
	ROUND(
   		total_orders /
   		NULLIF(lifespan/365.0, 0),2) 
	AS yearly_purchase_frequency,
	total_orders,
	total_products,
	total_sales,
	first_order_date,
	last_order_date
FROM customer_aggregations)

--========================================================
--Final Layer
--========================================================

SELECT 
	customer_id,
	customer_full_name,
	country,
	customer_age,
	age_group,
	lifespan,
	customer_segment,
	recency,
	activity_status,
	avg_order_value,
	avg_monthly_spend,
	yearly_purchase_frequency,
	CASE
	    WHEN lifespan = 0 THEN 'Not Enough Lifespan'
    	WHEN yearly_purchase_frequency >= 12 THEN 'Frequent Buyer'
    	WHEN yearly_purchase_frequency >= 4 THEN 'Regular Buyer'
    	ELSE 'Occasional Buyer'
	END AS purchase_frequency_segment,
	total_orders,
	total_products,
	total_sales,
	first_order_date,
	last_order_date
FROM customer_metrics
	
	
	
	
	
	
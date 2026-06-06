/*
====================================================================================
View: gold.sales_summary
====================================================================================
Description:
    This view provides daily sales performance metrics and trend analysis
    for the retail business. It aggregates sales activity at the daily level
    and calculates key performance indicators used for operational monitoring
    and business reporting.

Business Purpose:
    Supports sales performance tracking, trend analysis, revenue monitoring,
    and business intelligence reporting by providing a daily view of sales
    activity and short-term performance trends.

Key Metrics:
    - Total sales revenue
    - Total orders
    - Total customers
    - Total unique products sold
    - Total quantity sold
    - Average order revenue
    - Previous day sales comparison
    - Day-over-day sales growth percentage
    - Sales trend classification
    - Rolling 7-day sales total

Sales Trend Categories:
    - Growth
    - Decline
    - No-Change
    - Not-Available

Source Tables:
    - silver.sales

Notes:
    - One record represents one business day.
    - Day-over-day growth is calculated using the previous available sales day.
    - Rolling 7-day sales totals are calculated using a window function.
====================================================================================
*/

CREATE VIEW gold.sales_summary AS

--======================================================================
-- Base Layer
--======================================================================
WITH sales_base AS

(SELECT
	order_id,
	customer_id,
	product_id,
	quantity,
	sales,
	order_date
FROM silver.sales 
),

--======================================================================
-- Aggregations Layer
--======================================================================
sales_aggregations AS

(SELECT
	COUNT(DISTINCT order_id) AS total_orders,
	COUNT(DISTINCT customer_id) AS total_customers,
	COUNT(DISTINCT product_id) AS total_unique_products,
	SUM(quantity) AS total_quantity,
	SUM(sales) AS total_sales,
	order_date
FROM sales_base
GROUP BY 
	order_date
),

--======================================================================
-- Benchmarks Layer
--======================================================================
sales_benchmarks AS

(SELECT
	total_orders,
	total_customers,
	total_unique_products,
	total_quantity,
	total_sales,
	LAG(total_sales) OVER (ORDER BY order_date) AS previous_day_sales,
	SUM(total_sales) OVER (ORDER BY order_date ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS rolling_7day_sales,
	order_date
FROM sales_aggregations
)

--======================================================================
-- Final Layer
--======================================================================

SELECT
	order_date,
	total_orders,
	CASE
		WHEN total_orders = 0 THEN 0
		ELSE ROUND(total_sales * 1.0 / NULLIF(total_orders, 0), 2)
	END AS avg_order_revenue,
	total_customers,
	total_unique_products,
	total_quantity,
	total_sales,
	previous_day_sales,
	ROUND(
		(
		(total_sales - previous_day_sales) * 100
		/ NULLIF(previous_day_sales, 0)
		)::numeric,
		2) AS day_over_day_growth_percentage,
		CASE
			WHEN previous_day_sales IS NULL
				THEN 'Not-Available'
			WHEN total_sales > previous_day_sales
				THEN 'Growth'
			WHEN total_sales < previous_day_sales
				THEN 'Decline'
			ELSE 'No-Change'
		END AS sales_trend,
	rolling_7day_sales
FROM sales_benchmarks
	
	





	

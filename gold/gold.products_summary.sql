/*
View: gold.products_summary

Description:
This view provides product-level analytical metrics including sales
performance, customer reach, inventory utilization, product lifecycle
behavior, and category-level ranking insights.

Business Purpose:
Supports product performance analysis, sales trend monitoring, product
segmentation, lifecycle tracking, and strategic decision-making for
analytics and business intelligence reporting.

Key Metrics:
- Total sales revenue and quantity sold
- Total orders and customers per product
- Average revenue per order
- Average quantity per order
- Sales-to-stock ratio
- Product sales ranking within category
- Product lifecycle and recency metrics
- Product performance segmentation
- Product lifecycle stage classification

Source Tables:
- silver.sales
- silver.products
=================

*/


CREATE VIEW gold.products_summary AS

--=============================================================================
-- Base Layer
--=============================================================================
WITH products_base AS

(SELECT
	s.order_id,
	s.customer_id,
	s.quantity,
	s.sales,
	s.order_date,
	p.product_id,
	p.product_name,
	p.category,
	p.brand,
	p.stock
FROM silver.sales AS s
LEFT JOIN silver.products AS p
ON s.product_id = p.product_id),

--=============================================================================
-- Aggregations Layer
--=============================================================================
products_aggregations AS

(SELECT
	product_id,
	product_name,
	category,
	brand,
	stock,
	COUNT(DISTINCT order_id) AS total_orders,
	COUNT(DISTINCT customer_id) AS total_customers,
	SUM(quantity) AS total_products_sold,
	SUM(sales) AS total_sales,
	MIN(order_date) AS first_order_date,
	MAX(order_date) AS last_order_date,
	(MAX(order_date) - MIN(order_date)) AS lifespan,
	(
		SELECT
			MAX(order_date)
		FROM products_base 
	) - MAX(order_date) AS recency
FROM products_base
GROUP BY 
	product_id,
	product_name,
	category,
	brand,
	stock)

--=============================================================================
-- Final Layer
--=============================================================================

SELECT
	product_id,
	product_name,
	category,
	RANK() OVER (PARTITION BY category ORDER BY total_sales DESC) AS rank_by_category,
	brand,
	total_orders,
	CASE
		WHEN total_orders = 0 THEN 0
		ELSE ROUND(
		(total_sales * 1.0 / total_orders)::numeric,
		2
		)
	END AS avg_order_revenue,
	ROUND(
		(total_products_sold * 1.0 / NULLIF(total_orders,0))::numeric,
		2
	) AS avg_quantity_per_order,
	total_customers,
	total_products_sold,
	stock,
	ROUND(
		total_products_sold * 1.0 / NULLIF(stock,0),
		2
	) AS sales_stock_ratio,
	total_sales,
	CASE
		WHEN total_sales > 30000
			THEN 'High-Performer'
		WHEN total_sales >= 20000
			THEN 'Mid-Range'
		ELSE 'Low-Performer'
	END AS product_segment,
	first_order_date,
	last_order_date,
	lifespan,
	CASE
		WHEN lifespan > 365 THEN 'Mature'
		WHEN lifespan >= 180 THEN 'Growing'
		ELSE 'Early-Stage'
	END AS product_lifecycle_stage,
	CASE
		WHEN lifespan = 0 THEN total_sales
		ELSE ROUND(
			(total_sales * 1.0 / lifespan)::numeric,
			2
		)
	END AS avg_daily_revenue,
	recency
FROM products_aggregations 
	
/*
====================================================================================
View: gold.dim_products
====================================================================================
Description:
    Product dimension containing descriptive product attributes and inventory
    information.

Business Purpose:
    Supports product analytics, inventory reporting, sales analysis, and
    dashboarding by providing a centralized product dimension.

Grain:
    One row per product.

Primary Key:
    product_id

Attributes:
    - Product name
    - Category
    - Brand
    - Unit price
    - Stock quantity

Source Tables:
    - silver.products
====================================================================================
*/

CREATE VIEW gold.dim_products AS 

SELECT
	product_id,
	product_name,
	category,
	brand,
	unit_price,
	stock,
	CASE
    	WHEN stock = 0 THEN 'Out of Stock'
    	WHEN stock < 20 THEN 'Low Stock'
    	ELSE 'In Stock'
	END AS stock_status
FROM silver.products
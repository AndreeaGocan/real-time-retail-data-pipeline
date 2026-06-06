/*
====================================================================================
View: gold.dim_orders
====================================================================================
Description:
    Order dimension containing descriptive order attributes and transaction
    information.

Business Purpose:
    Supports order analysis, sales reporting, customer behavior analysis,
    and dashboarding by providing a centralized order dimension.

Grain:
    One row per order.

Primary Key:
    order_id

Attributes:
    - Customer identifier
    - Order date
    - Order status
    - Payment method
    - Sales channel

Source Tables:
    - silver.order_details
====================================================================================
*/

CREATE VIEW gold.dim_orders AS

SELECT
    order_id,
    customer_id,
    order_date,
    order_status,
    payment_method,
    channel
FROM silver.order_details;


CREATE VIEW gold.dim_orders AS

SELECT
	order_id,
	customer_id,
	order_date,
	order_status,
	payment_method,
	channel
FROM silver.order_details

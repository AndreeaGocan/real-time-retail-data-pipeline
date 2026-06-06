/*
====================================================================================
View: gold.dim_employees
====================================================================================
Description:
    Employee dimension containing descriptive employee attributes, organizational
    information, reporting structure, and tenure-related classifications.

Business Purpose:
    Supports workforce analytics, organizational reporting, employee analysis,
    and dashboarding by providing a centralized employee dimension.

Grain:
    One row per employee.

Primary Key:
    employee_id

Attributes:
    - Employee name
    - Country
    - Department
    - Job title
    - Salary
    - Manager relationship
    - Hire date
    - Years at company
    - Employee type
    - Tenure group

Derived Attributes:
    - Employee Type (Manager / Employee)
    - Years at Company
    - Tenure Group

Source Tables:
    - silver.employees

Business Rules:
    - Years at Company is calculated from the employee hire date.
    - Employees with a NULL manager_id are classified as Managers.
    - Tenure Group classifications:
        * New Hire (< 1 year)
        * Junior Tenure (1-4 years)
        * Experienced (5-9 years)
        * Veteran (10+ years)
====================================================================================
*/

CREATE VIEW gold.dim_employees AS

--============================================================================
-- Base Query
--============================================================================
WITH employees_base AS 

(SELECT
	employee_id,
	employee_full_name,
	country,
	department,
	job_title,
	salary,
	manager_id,
	hire_date,
	EXTRACT(YEAR FROM AGE(CURRENT_DATE, hire_date))::INT
    	AS years_at_company
FROM silver.employees)

--============================================================================
-- Final Query
--============================================================================

SELECT
	employee_id,
	employee_full_name,
	country,
	department,
	job_title,
	salary,
	manager_id,
	CASE
    	WHEN manager_id IS NULL THEN 'Manager'
    	ELSE 'Employee'
	END AS employee_type,
	hire_date,
	years_at_company,
	CASE
    	WHEN years_at_company < 1 THEN 'New Hire'
    	WHEN years_at_company < 5 THEN 'Junior Tenure'
    	WHEN years_at_company < 10 THEN 'Experienced'
    	ELSE 'Veteran'
	END AS tenure_group
FROM employees_base
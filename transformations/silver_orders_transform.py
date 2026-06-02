import os
from pyspark.sql import SparkSession

base_path = os.path.dirname(
    os.path.abspath(__file__)
)

bronze_path = os.path.join(
    base_path,
    '..',
    'bronze',
    'bronze_orders.csv'
)

spark = SparkSession.builder\
    .appName('Silver_Orders_Cleaning')\
    .getOrCreate()

df = spark.read.csv(
    bronze_path,
    header=True,
    inferSchema=True
)

df.show()
df.printSchema()

from pyspark.sql.functions import col

#==========================================================
# Quality Check - Negative Quantities
#==========================================================

df.filter(
    col("quantity") < 0
).show()

#==========================================================
# Remove Invalid Quantities
#==========================================================

clean_df = df.filter(
    col('quantity') > 0
)
clean_df.show()

#==========================================================
# Quality Check: Missing Quantity
#==========================================================

clean_df.filter(
    col('quantity').isNull()
).show()

#==========================================================
# Remove Missing Quantity
#==========================================================

clean_df = clean_df.filter(
    col('quantity').isNotNull()
)

clean_df.show()

#==========================================================
# Convert Dates to Date Type
#==========================================================

from pyspark.sql.functions import(
    col,
    when,
    to_date
)

clean_df = clean_df.withColumn(
    'order_date',
    when(
        col('order_date').contains('/'),
        to_date(
            col('order_date'),
            'dd/MM/yyyy'
        )
    ).otherwise(
        to_date(
            col('order_date'),
            'yyyy-MM-dd'
        )
    )
)

#==========================================================
# Convert Dates that did not pass convention to Nulls
# =========================================================

clean_df.filter(
    col('order_date').isNull()
).show()

#==========================================================
# Quality Check: Future Dates
#==========================================================

from pyspark.sql.functions import current_date

clean_df.filter(
    col('order_date') > current_date()
).show()

#==========================================================
# Store invalid Dates Separately for Further Investigation
#==========================================================

future_dates_df = clean_df.filter(
    col('order_date') > current_date()
)

future_dates_df.show()

#============================================================
# Remove Future Dates
#============================================================

clean_df = clean_df.filter(
    col('order_date') <= current_date()
)

clean_df.show()

#============================================================
# Quality Check: Missing Dates
#============================================================

clean_df.filter(
    col('order_date').isNull()
).show()

#============================================================
# Store missing dates for Further Investigation
#============================================================

missing_dates = clean_df.filter(
    col('order_date').isNull()
)

missing_dates.show()

#============================================================
# Remove Missing Dates
#============================================================

clean_df = clean_df.filter(
    col('order_date').isNotNull()
)

clean_df.show()

#=============================================================
# Quality Check: Very Old Orders
#=============================================================

clean_df.filter(
    col('order_date') < '2020-01-01'
).show()

#=============================================================
# Store Old Orders for Further Investigation
#=============================================================

old_orders_df = clean_df.filter(
    col('order_date') < '2020-01-01'
)

old_orders_df.show()

#=============================================================
# Remove Old Orders
#=============================================================

clean_df = clean_df.filter(
    col('order_date') >= '2020-01-01'
)

clean_df.show()

#=============================================================
# Quality Check: Duplicate IDs
#=============================================================

clean_df.groupBy('order_id')\
    .count()\
    .filter(col('count') > 1)\
    .show()

#===========================================================
# Remove Duplicates
#===========================================================

clean_df = clean_df.dropDuplicates(
    ['order_id']
)

clean_df.show()

#===========================================================
# Quality Check: Invalid Customer IDs
#===========================================================

clean_df.filter(
    col('customer_id') == 999999
).show()

#================================================================
# Store invalid Customer IDs Separately for Further Investigation
#================================================================

invalid_customer_ids = clean_df.filter(
    col('customer_id') == 999999
)

invalid_customer_ids.show()

#===============================================================
# Remove invalid IDs
#===============================================================

clean_df = clean_df.filter(
    col('customer_id') != 999999
)

clean_df.show()

#================================================================
# Quality Check: Missing Employee Id
#================================================================

clean_df.filter(
    col('employee_id').isNull()
).show()

#================================================================
# Store Missing Employee IDs Separately for Further Investigation
#================================================================

missing_employee_ids = clean_df.filter(
    col('employee_id').isNull()
)

missing_employee_ids.show()

#================================================================
# Remove Invalid Employee IDs
#================================================================

clean_df = clean_df.filter(
    col('employee_id').isNotNull()
)

clean_df.show()

#================================================================
# Quality Check: Invalid Product IDs
#================================================================

clean_df.filter(
    col('product_id') <= 0
).show()

#=================================================================
# Store Invalid Product IDs for Further Investigation
#=================================================================

invalid_product_ids = clean_df.filter(
    col('product_id') <=0
)

invalid_product_ids.show()

#=================================================================
# Remove Invalid Product IDs
#=================================================================

clean_df = clean_df.filter(
    col('product_id') > 0
)

clean_df.show()

#==================================================================
# Quality Check: Missing Product IDs
#==================================================================

clean_df.filter(
    col('product_id').isNull()
).show()

#===================================================================
# Store Missing Product IDs for Further Investigation
#===================================================================

missing_product_ids_df = clean_df.filter(
    col('product_id').isNull()
)

missing_product_ids_df.show()

#===================================================================
# Remove Missing Product IDs 
#===================================================================

clean_df = clean_df.filter(
    col('product_id').isNotNull()
)

clean_df.show()

#===================================================================
# Quality Check: Invalid Supplier IDs
#===================================================================

clean_df.filter(
    col('supplier_id') <= 0
).show()

#===================================================================
# Store Invalid Supplier IDs for Further Investigation
#===================================================================

invalid_supplier_ids_df = clean_df.filter(
    col('supplier_id') <= 0
)

invalid_supplier_ids_df.show()

#===================================================================
# Remove Invalid Supplier IDs
#===================================================================

clean_df = clean_df.filter(
    col('supplier_id') > 0
)
clean_df.show()

#===================================================================
# Quality Check: Missing Supplier IDs
#===================================================================

clean_df.filter(
    col('supplier_id').isNull()
).show()

#===================================================================
# Store Missing Supplier IDs for Further Investigation
#===================================================================

missing_supplier_ids_df = clean_df.filter(
     col('supplier_id').isNull()
)

missing_supplier_ids_df.show()

#===================================================================
# Remove Missing Supplier IDs 
#===================================================================

clean_df = clean_df.filter(
    col('supplier_id').isNotNull()
)

clean_df.show()

#===================================================================
# Quality Check: Invalid Prices
#===================================================================

clean_df.filter(
    col('unit_price') <= 0
).show()

#===================================================================
# Store Invalid Prices for Further Investigation
#===================================================================

invalid_prices_df = clean_df.filter(
    col('unit_price') <= 0
)

invalid_prices_df.show()

#===================================================================
# Remove Invalid Prices
#===================================================================

clean_df = clean_df.filter(
    col('unit_price') > 0
)

clean_df.show()

#===================================================================
# Quality Check: Missing Prices
#===================================================================

clean_df.filter(
    col('unit_price').isNull()
).show()

#===================================================================
# Store Missing Prices for Further Investigation
#===================================================================

missing_prices_df = clean_df.filter(
    col('unit_price').isNull()
)

missing_prices_df.show()

#===================================================================
# Remove Missing Prices
#===================================================================

clean_df = clean_df.filter(
    col('unit_price').isNotNull()
)

clean_df.show()

#===========================================================
# Quality Check: Zero or Negative Sales
#===========================================================

clean_df.filter(
    col('sales') <= 0
).show()

#===================================================================
# Quality Check: Missing Sales
#===================================================================

clean_df.filter(
    col('sales').isNull()
).show()

#===================================================================
# Retrieve Missing Sales
#===================================================================

from pyspark.sql.functions import col, when

clean_df = clean_df.withColumn(
    'sales',
    when(
        col('sales').isNull(),
        col('quantity') * col('unit_price')
    ).otherwise(
        col('sales')
    )
)

clean_df.show()

#===================================================================
# Quality Check: Final
#===================================================================

print("Final Silver Count:")
print(clean_df.count())

clean_df.groupBy('order_id') \
    .count() \
    .filter(col('count') > 1) \
    .show()

clean_df.filter(
    col('customer_id') == 999999
).show()

clean_df.filter(
    col('quantity') <= 0
).show()

clean_df.filter(
    col('order_date') > current_date()
).show()

#====================================================================
# Saving Results
#====================================================================

silver_path = os.path.join(
    base_path,
    '..',
    'silver',
    'silver_orders'
)

test_path = os.path.join(
    base_path,
    '..',
    'silver',
    'test_orders'
)

silver_path = os.path.join(
    base_path,
    '..',
    'silver',
    'silver_orders.csv'
)

clean_df.toPandas().to_csv(
    silver_path,
    index=False
)

print(
    f'Silver Orders saved to: {silver_path}'
)

print(
    f'Bronze rows: {df.count()}'
)

print(
    f'Silver rows: {clean_df.count()}'
)
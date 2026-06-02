import os
from pyspark.sql import SparkSession

base_path = os.path.dirname(
    os.path.abspath(__file__)
)

bronze_path = os.path.join(
    base_path,
    '..',
    'bronze',
    'bronze_order_details.csv'
)

spark = SparkSession.builder\
    .appName('Silver_Order_Details_Cleaning')\
    .getOrCreate()

df = spark.read.csv(
    bronze_path,
    header=True,
    inferSchema=True
)

valid_statuses = [
    'Completed',
    'Pending',
    'Returned',
    'Cancelled'
]

valid_payment_methods = [
    'Credit Card',
    'Debit Card',
    'PayPal',
    'Bank Transfer'
]

valid_channels = [
    'Online',
    'Mobile App',
    'Store'
]

df.show()
df.printSchema()

clean_df = df

#==============================================================
# Convert Order-Date to Date
#==============================================================

from pyspark.sql.functions import(
    col,
    to_date,
    current_date
)

clean_df = clean_df.withColumn(
    'order_date',
    to_date(col('order_date'), 'yyyy-MM-dd')
)

#==============================================================
# Quality Check: Invalid Order-Dates
#==============================================================

clean_df.filter(
    col('order_date') > current_date()
).show()

#==============================================================
# Quality Check: Missing Order-IDs
#==============================================================

clean_df.filter(
    col('order_id').isNull()
).show()

#=============================================================
# Quality Check: Duplicate IDs
#=============================================================

clean_df.groupBy('order_id')\
    .count()\
    .filter(col('count') > 1)\
    .show()

#=============================================================
# Quality Check: Missing Customer-IDs
#=============================================================

clean_df.filter(
    col('customer_id').isNull()
).show()

#=============================================================
# Quality Check: Invalid Order Status
#=============================================================

invalid_order_status = clean_df.filter(
    ~col('order_status').isin(valid_statuses)
)

invalid_order_status.show()

#=============================================================
# Keep only Valid Order Statuses
#=============================================================

clean_df = clean_df.filter(
    col('order_status').isin(valid_statuses)
)

#=============================================================
# Quality Check: Invalid Payment Methods
#=============================================================

invalid_payment_status = clean_df.filter(
    ~col('payment_method').isin(valid_payment_methods)
)

invalid_payment_status.show()

#=============================================================
# Keep only Valid Payment Methods
#=============================================================

clean_df = clean_df.filter(
    col('payment_method').isin(valid_payment_methods)
)

#=============================================================
# Quality Check: Invalid channels
#=============================================================

invalid_channel_status = clean_df.filter(
    ~col('channel').isin(valid_channels)
)

invalid_channel_status.show()

#=============================================================
# Keep only Valid Payment Methods
#=============================================================

clean_df = clean_df.filter(
    col('channel').isin(valid_channels)
)

#=============================================================
# Keep only Valid Discount Codes
#=============================================================

clean_df = clean_df.filter(
    col('discount_code').isNull() |
    col('discount_code').isin(
        'WELCOME5',
        'SUMMER10',
        'VIP15'
    )
)


silver_path = os.path.join(
    base_path,
    '..',
    'silver',
    'silver_order_details.csv'
)

clean_df.toPandas().to_csv(
    silver_path,
    index=False
)

print(
    f'Invalid statuses: {invalid_order_status.count()}'
)

print(
    f'Invalid payment methods: {invalid_payment_status.count()}'
)

print(
    f'Invalid channels: {invalid_channel_status.count()}'
)

print(
    f'Bronze rows: {df.count()}'
)

print(
    f'Silver rows: {clean_df.count()}'
)
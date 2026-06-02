import os
from pyspark.sql import SparkSession

base_path = os.path.dirname(
    os.path.abspath(__file__)
)

bronze_path = os.path.join(
    base_path,
    '..',
    'bronze',
    'bronze_suppliers.csv'
)

spark = SparkSession.builder\
    .appName('Silver_Suppliers_Cleaning')\
    .getOrCreate()

df = spark.read.csv(
    bronze_path,
    header=True,
    inferSchema=True
)

df.show()
df.printSchema()

clean_df = df

#================================================================
# Quality Check: Missing Supplier-IDs
#================================================================
from pyspark.sql.functions import col

clean_df.filter(
    col('supplier_id').isNull()
).show()

#================================================================
# Quality Check: Supplier-IDs Uniqueness
#================================================================

clean_df.groupBy('supplier_id')\
            .count()\
            .filter(col('count') > 1)\
            .show()

#================================================================
# Quality Check: Missing Supplier Name
#================================================================

clean_df.filter(
    col('supplier_name').isNull()
).show()

#================================================================
# Quality Check: Missing email
#================================================================

clean_df.filter(
    col('contact_email').isNull()
).show()

#================================================================
# Quality Check: Invalid Lead-Time-Days
#================================================================

clean_df.filter(
    col('lead_time_days') < 0
).show()

#================================================================
# Quality Check: Reliability Score Between 0 - 100
#================================================================

clean_df.filter(
    (col('reliability_score') < 0) |
    (col('reliability_score') > 100)
).show()

print(
    f'Bronze rows: {df.count()}'
)

print(
    'Supplier quality checks completed.'
)
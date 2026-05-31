import os
from pyspark.sql import SparkSession

base_path = os.path.dirname(
    os.path.abspath(__file__)
)

bronze_path = os.path.join(
    base_path,
    '..',
    'bronze',
    'bronze_products.csv'
)

suppliers_path = os.path.join(
    base_path,
    '..',
    'bronze',
    'bronze_suppliers.csv'
)

spark = SparkSession.builder\
    .appName('Silver_Products_Cleaning')\
    .getOrCreate()

df = spark.read.csv(
    bronze_path,
    header=True,
    inferSchema=True
)

df.show()
df.printSchema()

clean_df = df

suppliers = spark.read.csv(
    suppliers_path,
    header=True,
    inferSchema=True
).select('supplier_id')

#==============================================================
# Standardizing Product Names
#==============================================================

from pyspark.sql.functions import (
    col,
    lower,
    initcap,
    trim
)

clean_df = clean_df.withColumn(
    'product_name',
    trim(
        initcap(
            lower(
                col('product_name')
            )
        )
    )
)

#==============================================================
# Standardizing Category
#==============================================================

clean_df = clean_df.withColumn(
    'category',
    trim(
        initcap(
            lower(
                col('category')
            )
        )
    )
)

#==============================================================
# Quarantine Missing Unit-Prices
#==============================================================

missing_price = clean_df.filter(
    col('unit_price').isNull()
)

#==============================================================
# Keep only Valid Unit-Prices
#==============================================================

clean_df = clean_df.filter(
    col('unit_price').isNotNull()
)

#==============================================================
# Quarantine Invalid Stock
#==============================================================

invalid_stock = clean_df.filter(
    col('stock') < 0
)

#==============================================================
# Keep only Valid Stock
#==============================================================

clean_df = clean_df.filter(
    col('stock') >= 0
)

#==============================================================
# Check Supplier-IDs Integrity
#==============================================================

invalid_products = clean_df.join(
    suppliers,
    'supplier_id',
    'left_anti'
)

#==============================================================
# Keep Only Valid Products
#==============================================================

valid_products = clean_df.join(
    suppliers,
    'supplier_id',
    'inner'
)

clean_df = valid_products

from pyspark.sql import DataFrame

#==============================================================
# Creating Quarantine File
#==============================================================

quarantine_df = (
    missing_price
    .unionByName(invalid_stock)
    .unionByName(invalid_products)
    .dropDuplicates()
)

#==============================================================
# Saving Results
#==============================================================

silver_path = os.path.join(
    base_path,
    '..',
    'silver',
    'silver_products.csv'
)

clean_df.toPandas().to_csv(
    silver_path,
    index=False
)

quarantine_path = os.path.join(
    base_path,
    '..',
    'silver',
    'quarantined_products.csv'
)

quarantine_df.toPandas().to_csv(
    quarantine_path,
    index=False
)

print(
    f'Invalid stock rows: {invalid_stock.count()}'
)

print(
    f'Missing price rows: {missing_price.count()}'
)

print(
    f'Invalid supplier rows: {invalid_products.count()}'
)

print(
    f'Silver Products saved to: {silver_path}'
)

print(
    f'Bronze rows: {df.count()}'
)

print(
    f'Silver rows: {clean_df.count()}'
)
import os
from pyspark.sql import SparkSession

base_path = os.path.dirname(
    os.path.abspath(__file__)
)

bronze_path = os.path.join(
    base_path,
    '..',
    'bronze',
    'bronze_customers.csv'
)

spark = SparkSession.builder\
    .appName('Silver_Customers_Cleaning')\
    .getOrCreate()

df = spark.read.csv(
    bronze_path,
    header=True,
    inferSchema=True
)

df.show()
df.printSchema()

clean_df = df

#==============================================================
# Standardizing Customers First Names
#==============================================================

from pyspark.sql.functions import (
    col,
    lower,
    initcap,
    when,
    current_date,
    add_months,
    floor,
    months_between
)

clean_df = clean_df.withColumn(
    'first_name',
    initcap(
        lower(
            col('first_name')
        )
    )

)

#==============================================================
# Standardizing Customers Last Names
#==============================================================

clean_df = clean_df.withColumn(
    'last_name',
    initcap(
        lower(
            col('last_name')
        )
    )
)

#==============================================================
# Handling Missing Countries
#==============================================================

clean_df = clean_df.withColumn(
    'country',
    when(
        col('country').isNull() |
        (col('country') == ''),
        'Unknown'
    ).otherwise(
        col('country')
    )
)

#==============================================================
# Calculating Customers Age
#==============================================================

age_df = clean_df.withColumn(
    'age',
    floor(
        months_between(
            current_date(),
            col('birthdate')
        ) / 12
    )
)

#==============================================================
# Handling Invalid Birthdates: Keep only customers between
# 16 and 100 years old
#==============================================================

valid_customers = age_df.filter(
    (col('age') >= 16)&
    (col('age') <= 100)
)

#==============================================================
# Quarantine Impossible Birth-Dates for Further Investigation
#==============================================================

invalid_customers = age_df.filter(
    (col('age') < 16) |
    (col('age') > 100)
)

clean_df = valid_customers.drop('age')

#==============================================================
# Saving Results
#==============================================================

silver_path = os.path.join(
    base_path,
    '..',
    'silver',
    'silver_customers.csv'
)

clean_df.toPandas().to_csv(
    silver_path,
    index=False
)

rejected_path = os.path.join(
    base_path,
    '..',
    'silver',
    'rejected_customers.csv'
)

invalid_customers.toPandas().to_csv(
    rejected_path,
    index=False
)

print(
    f'Rejected rows: {invalid_customers.count()}'
)

print(
    f'Rejected Customers saved to: {rejected_path}'
)

print(
    f'Silver Customers saved to: {silver_path}'
)

print(
    f'Bronze rows: {df.count()}'
)

print(
    f'Silver rows: {clean_df.count()}'
)
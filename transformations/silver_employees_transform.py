import os
from pyspark.sql import SparkSession

base_path = os.path.dirname(
    os.path.abspath(__file__)
)

employees_path = os.path.join(
    base_path,
    '..',
    'bronze',
    'bronze_employees.csv'
)

spark = SparkSession.builder\
    .appName('Silver_Employees_Cleaning')\
    .getOrCreate()

df = spark.read.csv(
    employees_path,
    header=True,
    inferSchema=True
)

df.show()
df.printSchema()

clean_df = df

#==============================================================
# Standardizing Department Names
#==============================================================

from pyspark.sql.functions import (
    col,
    lower,
    initcap,
    trim,
    when
)

clean_df = clean_df.withColumn(
    'department',
    when(
        lower(trim(col('department'))) == 'it',
        'IT'
    ).otherwise(
        trim(
            initcap(
                lower(
                    col('department')
                )
            )
        )
    )
)

#==============================================================
# Standardizing Country Names
#==============================================================

clean_df = clean_df.withColumn(
    'country',
    when(
        lower(trim(col('country'))) == 'usa',
        'United States'
    )
    .when(
        lower(trim(col('country'))) == 'uk',
        'United Kingdom'
    )
    .otherwise(
        trim(
            initcap(
                lower(
                    col('country')
                )
            )
        )
    )
)

#==============================================================
# Convert Manager-IDs to the Correct Data-Type 
#==============================================================

clean_df = clean_df.withColumn(
    'manager_id',
    col('manager_id').cast('int')
)


#==============================================================
# Quality Check: Manager-IDs Integrity
#==============================================================

valid_managers = clean_df.select(
    col("employee_id").alias("valid_manager_id")
)

invalid_managers = (
    clean_df.join(
        valid_managers,
        clean_df.manager_id == valid_managers.valid_manager_id,
        "left"
    )
    .filter(
        col("manager_id").isNotNull() &
        col("valid_manager_id").isNull()
    )
)

invalid_count = invalid_managers.count()

if invalid_count > 0:
    print(
        f"WARNING: {invalid_count} invalid manager IDs found."
    )
else:
    print(
        "Manager ID integrity check passed."
    )

#================================================================
# Quality Check: Invalid Salaries
#================================================================

invalid_salary = clean_df.filter(
    col('salary').isNull() |
    (col('salary') <= 0)
)

#=================================================================
# Remove Invalid Salaries
#=================================================================

clean_df = clean_df.filter(
    col('salary').isNotNull() &
    (col('salary') > 0)
)

clean_df.printSchema()

clean_df.show()

silver_path = os.path.join(
    base_path,
    '..',
    'silver',
    'silver_employees.csv'
)

clean_df.toPandas().to_csv(
    silver_path,
    index=False
)

print(
    f"Rows in Silver Employees: {clean_df.count()}"
)

print(
    f'Silver Employees saved to: {silver_path}'
)

print(
    f'Invalid salaries: {invalid_salary.count()}'
)

spark.stop()
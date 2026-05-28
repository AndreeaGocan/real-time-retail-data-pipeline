#employees_csv
import pandas as pd
import os
import random
from datetime import datetime, timedelta

base_path = os.path.dirname(
    os.path.abspath(__file__)
)

bronze_folder = os.path.join(
    base_path,
    'bronze'
)

os.makedirs(
    bronze_folder,
    exist_ok=True
)

employees_path = os.path.join(
    bronze_folder,
    'bronze_employees.csv'
)


first_names = [
    'John', 'Sarah', 'Michael', 'Emma', 'David',
    'Sophia', 'Daniel', 'Olivia', 'James', 'Emily'
]

last_names = [
    'Smith', 'Johnson', 'Brown', 'Wilson',
    'Taylor', 'Miller', 'Davis', 'Moore'
]

hire_dates = []

start_hire = datetime(2018, 1, 1)
end_hire = datetime(2025, 1, 1)

for i in range(18):

    hire_date = start_hire + timedelta(
        days=random.randint(
            0,
            (end_hire - start_hire).days
        )
    )

    hire_dates.append(
        hire_date.strftime('%Y-%m-%d')
    )

employee_names = []


while len(employee_names) < 18:

    full_name = (
        random.choice(first_names)
        + ' ' +
        random.choice(last_names)
    )

    if full_name not in employee_names:
        employee_names.append(full_name)

employees = pd.DataFrame({

    'employee_id': list(range(1, 19)),

    'department': ['sales', 'sales', 'sales', 'sales',
                   'operations', 'operations', 'operations', 'operations',
                   'operations', 'support', 'support', 'support',
                   'support', 'management', 'management', 'IT',
                   'IT', 'IT' ],

    'country': ['Germany', 'UK', 'USA', 'Spain', 'Greece',
                'Greece', 'UK', 'UK', 'USA', 'Spain',
                'Italy', 'Italy', 'Germany', 'UK', 'Germany',
                'UK', 'USA', 'Greece'],

    'salary': [1200, 1000, 1000, 1100,
               950, 970, 1000, 1000, 950,
               1300, 1250, 1170, 1350,
               2050, 2100,
               1900, 1850, 2000],

    'employee_name': employee_names,

    'manager_id': [14, 14, 14, 14,
                   15, 15, 15, 15, 15,
                   14, 14, 14, 14, 
                   None, None, None,
                   16, 16],

    'job_title': ['Sales Rep','Sales Rep','Sales Rep','Sales Rep',
                  'Operations Analyst','Operations Analyst',
                  'Operations Analyst','Operations Analyst',
                  'Operations Analyst',
                  'Support Specialist','Support Specialist',
                  'Support Specialist','Support Specialist',
                  'Sales Manager',
                  'Operations Manager',
                  'IT Manager','IT Engineer','IT Engineer'],

    'hire_date': hire_dates,

    'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    })

employees.loc[3, 'department'] = 'Sales '

employees.loc[7, 'salary'] = None


employees.to_csv(
    employees_path,
    index=False
    )

print('Employees CSV created successfully')
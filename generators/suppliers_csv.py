#suppliers_csv
import pandas as pd
import os

base_path = os.path.dirname(
    os.path.abspath(__file__)
)

bronze_folder = os.path.join(
    base_path,
    'bronze'
)

suppliers_path = os.path.join(
    base_path,
    'bronze',
    'bronze_suppliers.csv'
)

suppliers = pd.DataFrame({

    'supplier_id': [1, 2, 3, 4],

    'supplier_name': [
        'Tech Distribution Ltd',
        'Global Electronics Supply',
        'Premium Mobile Partners',
        'Accessory Hub International'
    ],

    'country': [
        'Germany',
        'Netherlands',
        'USA',
        'China'
    ],

    'contact_email': [
        'contact@techdistribution.com',
        'sales@globalelectronics.com',
        'support@premiummobile.com',
        'orders@accessoryhub.com'
    ],

    'lead_time_days': [
        5,
        7,
        10,
        4
    ],

    'reliability_score': [
        96,
        92,
        98,
        90
    ]
})

os.makedirs(
    bronze_folder,
    exist_ok=True
)

suppliers.to_csv(
    suppliers_path,
    index=False
    )

print('Suppliers CSV created successfully')
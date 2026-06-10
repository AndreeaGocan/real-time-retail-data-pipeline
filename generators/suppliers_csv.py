# suppliers_csv.py

import pandas as pd
import os

base_path = os.path.dirname(
    os.path.abspath(__file__)
)

bronze_folder = os.path.join(
    base_path,
    '..',
    'bronze'
)

os.makedirs(
    bronze_folder,
    exist_ok=True
)

suppliers_path = os.path.join(
    bronze_folder,
    'bronze_suppliers.csv'
)

suppliers = pd.DataFrame({

    'supplier_id': list(range(1, 11)),

    'supplier_name': [

        'Tech Distribution Ltd',
        'Global Electronics Supply',
        'Premium Mobile Partners',
        'Accessory Hub International',
        'AudioTech Wholesale',
        'Network Solutions Europe',
        'Storage Systems Group',
        'Gaming Gear Distribution',
        'Digital Hardware Group',
        'Smart Device Logistics'
    ],

    'country': [

        'Germany',
        'Netherlands',
        'USA',
        'China',
        'Japan',
        'Germany',
        'Singapore',
        'Taiwan',
        'UK',
        'South Korea'
    ],

    'contact_email': [

        'contact@techdistribution.com',
        'sales@globalelectronics.com',
        'support@premiummobile.com',
        'orders@accessoryhub.com',
        'sales@audiotech.com',
        'contact@networksolutions.com',
        'support@storagesystems.com',
        'orders@gaminggear.com',
        'sales@digitalhardware.com',
        'contact@smartdevices.com'
    ],

    'lead_time_days': [

        5,
        7,
        10,
        4,
        8,
        6,
        9,
        7,
        5,
        8
    ],

    'reliability_score': [

        96,
        92,
        98,
        90,
        94,
        95,
        91,
        93,
        97,
        92
    ]
})

suppliers.to_csv(
    suppliers_path,
    index=False
)

print(
    'Suppliers CSV created successfully'
)

print(
    f'Saved to: {suppliers_path}'
)
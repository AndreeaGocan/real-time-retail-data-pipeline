import pandas as pd
import os
import random
from datetime import datetime

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

products_path = os.path.join(
    bronze_folder,
    'bronze_products.csv'
)

catalog = {

    'Electronics': [

        ('Laptop Pro X', 'Dell', 1500),
        ('Laptop Air', 'HP', 1100),
        ('BusinessBook 14', 'Lenovo', 1200),
        ('Gaming Beast G9', 'ASUS', 1800),
        ('Workstation Elite', 'Dell', 2200),
        ('Desktop Tower X', 'Lenovo', 1300),
        ('Business Desktop', 'HP', 1000),
        ('Monitor HD 24', 'LG', 250),
        ('Monitor UltraWide', 'Samsung', 550),
        ('Monitor 4K Pro', 'Dell', 700)

    ],

    'Mobile Devices': [

        ('Smartphone Ultra', 'Samsung', 950),
        ('Smartphone Lite', 'Google', 650),
        ('Smartphone Max', 'Apple', 1200),
        ('Foldable Phone X', 'Samsung', 1600),
        ('Tablet Air', 'Apple', 750),
        ('Tablet Pro', 'Samsung', 950),
        ('Smartwatch Active', 'Apple', 350),
        ('Smartwatch Elite', 'Samsung', 450)

    ],

    'Accessories': [

        ('Mechanical Keyboard', 'Logitech', 120),
        ('Wireless Keyboard', 'Logitech', 90),
        ('Compact Keyboard', 'HP', 60),
        ('Wireless Mouse', 'Logitech', 45),
        ('Gaming Mouse Pro', 'Razer', 80),
        ('Travel Mouse', 'Dell', 35),
        ('Webcam HD', 'Logitech', 70),
        ('USB-C Dock', 'Dell', 140)

    ],

    'Audio': [

        ('Wireless Headphones', 'Sony', 180),
        ('Noise Cancelling Headphones', 'Bose', 300),
        ('Wireless Earbuds', 'Sony', 150),
        ('Studio Headphones', 'Bose', 250),
        ('Gaming Headset Elite', 'Razer', 140),
        ('Bluetooth Speaker Mini', 'JBL', 90),
        ('Bluetooth Speaker Pro', 'JBL', 180),
        ('USB Microphone', 'Sony', 130)

    ],

    'Gaming': [

        ('Gaming Keyboard RGB', 'Corsair', 160),
        ('Gaming Mouse RGB', 'Razer', 90),
        ('Gaming Headset RGB', 'Razer', 160),
        ('Gaming Controller Pro', 'MSI', 80),
        ('Streaming Camera Pro', 'Logitech', 120),
        ('Capture Card X', 'MSI', 180),
        ('Gaming Microphone', 'Corsair', 150),
        ('RGB Mouse Pad', 'Corsair', 35)

    ],

    'Networking': [

        ('Router AX1800', 'TP-Link', 120),
        ('Router AX3000', 'Netgear', 180),
        ('Mesh WiFi System', 'TP-Link', 300),
        ('Network Switch 8-Port', 'Netgear', 110),
        ('Network Switch 16-Port', 'Netgear', 180),
        ('WiFi Adapter USB', 'TP-Link', 45),
        ('Range Extender Pro', 'TP-Link', 80),
        ('Access Point Business', 'Netgear', 220)

    ],

    'Storage': [

        ('SSD 512GB', 'Kingston', 60),
        ('SSD 1TB', 'Samsung', 90),
        ('SSD 2TB', 'WD', 180),
        ('External SSD 1TB', 'Samsung', 140),
        ('External HDD 4TB', 'Seagate', 160),
        ('USB Drive 128GB', 'Kingston', 20),
        ('USB Drive 256GB', 'Kingston', 35),
        ('NAS Storage Drive', 'WD', 220)

    ]
}

products = []

product_id = 1

for category, items in catalog.items():

    for product_name, brand, price in items:

        product = {

            'product_id': product_id,

            'product_name': product_name,

            'category': category,

            'brand': brand,

            'supplier_id': random.randint(1, 10),

            'unit_price': price,

            'stock': random.randint(20, 150),

            'created_at': datetime.now().strftime(
                '%Y-%m-%d %H:%M:%S'
            )
        }

        products.append(product)

        product_id += 1

products = pd.DataFrame(products)

products.loc[4, 'category'] = 'electronics'

products.loc[12, 'category'] = ' Accessories '

products.loc[55, 'unit_price'] = None

products.loc[57, 'supplier_id'] = 999

products.to_csv(
    products_path,
    index=False
)

print(
    f'Products CSV created successfully: {products_path}'
)

print(
    f'Total products generated: {len(products)}'
)
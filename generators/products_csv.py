#products_csv
import pandas as pd
import os
from datetime import datetime

products = pd.DataFrame({

    'product_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],

    'product_name': [
        'Laptop Pro X',
        'Laptop Air',
        'Gaming Laptop G7',

        'Smartphone X',
        'Smartphone Mini',
        'Smartphone Ultra',

        'Mechanical Keyboard',
        'Gaming Keyboard RGB',
        'Compact Keyboard',

        'Wireless Mouse',
        'Gaming Mouse Pro',
        'Travel Mouse',

        'Monitor HD 24',
        'Monitor UltraWide',
        'Gaming Monitor 27'
    ],

    'category': [
        'Electronics', 'Electronics', 'Electronics',
        'Electronics', 'Electronics', 'Electronics',
        'Accessories', 'Accessories', 'Accessories',
        'Accessories', 'Accessories', 'Accessories',
        'Electronics', 'Electronics', 'Electronics'
    ],

    'brand': [
        'Dell', 'HP', 'Lenovo',
        'Samsung', 'Apple', 'Google',
        'Logitech', 'Razer', 'HP',
        'Logitech', 'Razer', 'Dell',
        'LG', 'Samsung', 'ASUS'
    ],

    'supplier_id': [
        1,1,2,
        2,3,2,
        4,4,4,
        4,4,1,
        1,2,2
    ],

    'unit_price': [
        1500,1100,1800,
        800,950,1000,
        80,120,45,
        35,70,25,
        300,550,450
    ],

    'stock': [
        15,20,10,
        25,18,12,
        40,30,50,
        60,35,55,
        25,15,20
    ],

    'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')

})

products.loc[4, 'category'] = 'electronics'

products.loc[8, 'category'] = ' Accessories '

products.loc[11, 'unit_price'] = None

products.loc[14, 'product_name'] = 'Laptop Pro X'

products.loc[13, 'stock'] = -5


os.makedirs(
    'bronze',
    exist_ok=True
)

products.to_csv(
    'bronze/bronze_products.csv',
    index=False
)

print('Products CSV created successfully')

# orders_producer.py

from kafka import KafkaProducer
import json
import random
import time
from datetime import datetime, timedelta
import pandas as pd
import os

base_path = os.path.dirname(
    os.path.abspath(__file__)
)

products_path = os.path.join(
    base_path,
    '..',
    'bronze',
    'bronze_products.csv'
)

customers_path = os.path.join(
    base_path,
    '..',
    'bronze',
    'bronze_customers.csv'
)


producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

customer_ids = list(range(1000,11000))

start_date = datetime.now() - timedelta(days=730)

current_day = start_date

country_preferences = {

    'Cyprus': [
        'Accessories',
        'Networking',
        'Mobile Devices'
    ],

    'UK': [
        'Electronics',
        'Mobile Devices',
        'Gaming'
    ],

    'Greece': [
        'Mobile Devices',
        'Audio',
        'Accessories'
    ],

    'Germany': [
        'Electronics',
        'Gaming',
        'Networking'
    ],

    'Spain': [
        'Audio',
        'Mobile Devices',
        'Accessories'
    ]
}

payment_methods = [
   'Credit Card',
   'Debit Card',
   'PayPal',
   'Bank Transfer'
]

channels = [
   'Online',
   'Mobile App',
   'Store'
]

discount_codes = [
   None,
   'WELCOME5',
   'SUMMER10',
   'VIP15'
]

customer_df = pd.read_csv(
    customers_path
)

products_df = pd.read_csv(
    products_path
)

valid_products = products_df[
    (products_df['unit_price'].notna()) &
    (products_df['supplier_id'].between(1, 10))
].copy()

customer_lookup = dict(
    zip(
        customer_df['customer_id'],
        customer_df['country']
    )
)

order_id = 5000


while True:

    orders_today = random.randint(4,10)

    for i in range(orders_today):

        selected_customer = random.choice(customer_ids)

        customer_country = customer_lookup[
            selected_customer
        ]

        if customer_country not in country_preferences:
           continue
    
        selected_category = random.choice(
            country_preferences[
         customer_country
         ]
        )

        available_products = valid_products[
            valid_products['category']
            .str.strip()
            .str.title()
            == selected_category
        ]

        selected_product = available_products.sample(
            1
        ).iloc[0]

        product_id = int(
            selected_product['product_id']
        )

        unit_price = float(
            selected_product['unit_price']
        )

        supplier_id = int(
            selected_product['supplier_id']
        )

        print(
         f'Category: {selected_category} | '
         f'Product: {product_id}'
        )

        quantity = 1

        status = random.choices(
            ['Completed', 'Pending', 'Returned', 'Cancelled'],
            weights=[85, 5, 7, 3]
        )[0]

        sales_amount = round(
            quantity * unit_price,
            2
        )

        if status == 'Cancelled':
            sales_amount = 0

        elif status == 'Returned':
            sales_amount = -sales_amount

        employee_id = random.randint(1, 18)

        order = {

            'order_id': order_id,

            'customer_id': selected_customer,

            'product_id': product_id,

            'employee_id': employee_id,

            'supplier_id': supplier_id,

            'quantity': quantity,

            'unit_price': unit_price,

            'sales': sales_amount,

            'order_date': current_day.strftime('%Y-%m-%d')
        }

        order_details = {

            'order_id': order_id,

            'customer_id': selected_customer,

            'order_date': current_day.strftime('%Y-%m-%d'),

            'order_status': status,

            'payment_method': random.choice(
                 payment_methods
            ),

            'channel': random.choice(
                channels
            ),

            'discount_code': random.choice(
                 discount_codes
            )
        }

     

        if random.random() < 0.01:
           order['order_id'] = order_id - 1

        if random.random() < 0.02:
           order['sales'] = order['sales'] + 100

        if random.random() < 0.01:
           order['customer_id'] = 999999

        if random.random() < 0.01:
           order['order_date'] = (
        datetime.now() + timedelta(days=30)
                ).strftime('%Y-%m-%d')
           
        if random.random() < 0.01:
           order['employee_id'] = None

        if random.random() < 0.01:
           order['order_date'] = current_day.strftime('%d/%m/%Y')

        

        producer.send(
            'orders',
            value=order
        )

        producer.send(
            'order_details',
             value=order_details
        )

        order_id += 1

        print('Sent:', order)

        print('Order Details:', order_details)

        time.sleep(1)

    current_day += timedelta(days=1)

    if current_day > datetime.now():
        current_day = start_date
from kafka import KafkaConsumer
import json
import csv
import os
from datetime import datetime

consumer = KafkaConsumer(
    "orders",
    bootstrap_servers='localhost:9092',
    auto_offset_reset='latest',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

file_exists = os.path.exists(
    "bronze/bronze_orders.csv"
)

with open(
    "bronze/bronze_orders.csv",
    "a",
    newline=""
) as file:

    writer = csv.writer(file)

    if not file_exists:

        writer.writerow([
            "order_id",
            "customer_id",
            "product_id",
            "employee_id",
            "supplier_id",
            "quantity",
            "unit_price",
            "sales",
            "order_date",
            "ingested_at"
        ])

    print("Listening and saving orders...\n")

    for message in consumer:

        try:

            order = message.value

            writer.writerow([

                order["order_id"],
                order["customer_id"],
                order["product_id"],
                order["employee_id"],
                order["supplier_id"],
                order["quantity"],
                order["unit_price"],
                order["sales"],
                order["order_date"],
                datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            ])

            file.flush()

            print(f"Saved: {order}")

        except Exception as e:
            print(f"error processing message: {e}")


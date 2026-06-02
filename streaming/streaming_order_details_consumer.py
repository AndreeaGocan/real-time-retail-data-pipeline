from kafka import KafkaConsumer
import json
import csv
import os
from datetime import datetime

consumer = KafkaConsumer(
    "order_details",
    bootstrap_servers='localhost:9092',
    auto_offset_reset='latest',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

base_path = os.path.dirname(
    os.path.abspath(__file__)
)

bronze_path = os.path.join(
    base_path,
    '..',
    'bronze',
    'bronze_order_details.csv'
)

file_exists = os.path.exists(
    bronze_path
)

with open(
    bronze_path,
    "a",
    newline=""
) as file:

    writer = csv.writer(file)

    if not file_exists:

        writer.writerow([
               "order_id",
               "customer_id",
               "order_date",
               "order_status",
               "payment_method",
               "channel",
               "discount_code",
               "ingested_at"
        ])

    print("Listening and saving orders...\n")

    for message in consumer:

        try:

            order_details = message.value

            writer.writerow([

                order_details["order_id"],
                order_details["customer_id"],
                order_details["order_date"],
                order_details["order_status"],
                order_details["payment_method"],
                order_details["channel"],
                order_details["discount_code"],
                datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            ])

            file.flush()

            print(f"Saved: {order_details}")

        except Exception as e:
            print(f"error processing message: {e}")


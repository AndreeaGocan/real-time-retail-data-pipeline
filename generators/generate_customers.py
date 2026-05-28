#generate_customers.py
import random
import pandas as pd
from datetime import datetime, timedelta

first_names = [
    'Maria','Anna','Baraa','Alex','John',
    'Chris','Elena','Daniel','Sophia','George',
    'Emma','Michael','David','Olivia',
    'Lucas','Mia','Noah','Sarah',
    'James','Emily'
]

last_names = [
    'Smith','Brown','Miller',
    'Wilson','Johnson',
    'Taylor','Anderson',
    'Thomas','Jackson',
    'White','Martin',
    'Walker','Lewis'
]

countries = [
    'Cyprus',
    'UK',
    'Greece',
    'Germany',
    'Spain'
]

weights = [
    5,
    30,
    10,
    35,
    20
]

customers = []

start_date = datetime(1960,1,1)

end_date = datetime(2005,12,31)


for customer_id in range(1000,11000):

    random_days = random.randint(
        0,
        (end_date - start_date).days
    )

    birthdate = (
        start_date+
        timedelta(days=random_days)
        ).strftime('%Y-%m-%d')
    
    customer = {
        'customer_id': customer_id,
        
        'first_name': random.choice(first_names),

        'last_name': random.choice(last_names),

        'country': random.choices(
            countries,
            weights=weights,
            k=1
            )[0],

        'birthdate': birthdate,

        'created at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }

    if random.random() < 0.01:
        customer['first_name'] = customer['first_name'].lower()

    if random.random() < 0.02:
        customer['country'] = None

    if random.random() < 0.005:
        customer['birthdate'] = '2035-01-01'

    if random.random() < 0.005:
        customer['birthdate'] = '1820-05-12'

    if random.random() < 0.01:
        customer['birthdate'] = '2020-07-15'   

    customers.append(customer)

df = pd.DataFrame(customers)

df.to_csv(
    'bronze/bronze_customers.csv',
    index=False
)

print("Customers created")
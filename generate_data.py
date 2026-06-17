# generate_data.py

import pandas as pd
import numpy as np
from faker import Faker

fake = Faker()

ROWS = 200000

data = []

for i in range(ROWS):

    # Normal transaction amount
    amount = round(max(100, np.random.normal(5000, 2500)), 2)

    txn_type = np.random.choice(
        ["credit", "debit", "transfer"],
        p=[0.4, 0.4, 0.2]
    )

    customer_segment = np.random.choice(
        ["Retail", "Corporate", "Premium"],
        p=[0.7, 0.2, 0.1]
    )

    region = np.random.choice(
        ["North", "South", "East", "West"]
    )

    channel = np.random.choice(
        ["Mobile", "Web", "ATM", "Branch"],
        p=[0.45, 0.30, 0.15, 0.10]
    )

    merchant_category = np.random.choice(
        [
            "Shopping",
            "Travel",
            "Utilities",
            "Food",
            "Healthcare",
            "Entertainment"
        ]
    )

    priority = np.random.choice(
        ["High", "Medium", "Low"],
        p=[0.1, 0.4, 0.5]
    )

    processing_ms = np.random.randint(100, 1500)

    sla_limit_ms = np.random.choice(
        [500, 700, 1000]
    )

    status = np.random.choice(
        ["SUCCESS", "FAILED", "PENDING"],
        p=[0.92, 0.05, 0.03]
    )

    # Fraud / Anomaly Injection
    is_fraud = False

    if np.random.rand() < 0.005:
        amount *= np.random.randint(10, 25)
        is_fraud = True

    # SLA Breach Injection
    if np.random.rand() < 0.04:
        processing_ms = np.random.randint(2000, 6000)

    # Failed Transaction Pattern
    if np.random.rand() < 0.02:
        status = "FAILED"
        processing_ms = np.random.randint(3000, 7000)

    timestamp = fake.date_time_between(
        start_date="-90d",
        end_date="now"
    )

    data.append([
        i + 1,
        round(amount, 2),
        txn_type,
        timestamp,
        status,
        processing_ms,
        sla_limit_ms,
        customer_segment,
        region,
        channel,
        merchant_category,
        priority,
        is_fraud
    ])

df = pd.DataFrame(
    data,
    columns=[
        "txn_id",
        "amount",
        "type",
        "timestamp",
        "status",
        "processing_ms",
        "sla_limit_ms",
        "customer_segment",
        "region",
        "channel",
        "merchant_category",
        "priority",
        "is_fraud"
    ]
)

df.to_csv(
    "data/transactions.csv",
    index=False
)

print(f"{ROWS:,} transactions generated successfully.")
print("Dataset saved to data/transactions.csv")
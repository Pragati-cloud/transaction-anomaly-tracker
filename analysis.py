# analysis.py

import pandas as pd
import os

# Create reports folder if not exists
os.makedirs("reports", exist_ok=True)

# Load data
df = pd.read_csv("data/transactions.csv")

# ---------------------------------
# Anomaly Detection (Z-Score)
# ---------------------------------

mean = df["amount"].mean()
std = df["amount"].std()

df["z_score"] = (df["amount"] - mean) / std

df["anomaly_flag"] = df["z_score"].abs() > 3

# ---------------------------------
# SLA Breach Detection
# ---------------------------------

df["sla_breach"] = (
    df["processing_ms"] > df["sla_limit_ms"]
)

# ---------------------------------
# Daily Report
# ---------------------------------

daily_report = (
    df.groupby(df["timestamp"].str[:10])
    .agg(
        transactions=("txn_id", "count"),
        anomalies=("anomaly_flag", "sum"),
        sla_breaches=("sla_breach", "sum"),
        failed_transactions=(
            "status",
            lambda x: (x == "FAILED").sum()
        )
    )
)

daily_report.to_csv(
    "reports/daily_report.csv"
)

# ---------------------------------
# Region Report
# ---------------------------------

region_report = (
    df.groupby("region")
    .agg(
        total_transactions=("txn_id", "count"),
        anomalies=("anomaly_flag", "sum"),
        sla_breaches=("sla_breach", "sum"),
        fraud_transactions=("is_fraud", "sum")
    )
)

region_report.to_csv(
    "reports/region_report.csv"
)

# ---------------------------------
# Channel Report
# ---------------------------------

channel_report = (
    df.groupby("channel")
    .agg(
        total_transactions=("txn_id", "count"),
        anomalies=("anomaly_flag", "sum"),
        sla_breaches=("sla_breach", "sum")
    )
)

channel_report.to_csv(
    "reports/channel_report.csv"
)

# ---------------------------------
# Merchant Category Report
# ---------------------------------

merchant_report = (
    df.groupby("merchant_category")
    .agg(
        total_transactions=("txn_id", "count"),
        failed_transactions=(
            "status",
            lambda x: (x == "FAILED").sum()
        ),
        fraud_transactions=("is_fraud", "sum")
    )
)

merchant_report.to_csv(
    "reports/merchant_report.csv"
)

# ---------------------------------
# Executive Summary Metrics
# ---------------------------------

total_txns = len(df)

total_anomalies = int(
    df["anomaly_flag"].sum()
)

total_breaches = int(
    df["sla_breach"].sum()
)

total_fraud = int(
    df["is_fraud"].sum()
)

error_rate = round(
    (
        (df["status"] == "FAILED").sum()
        / total_txns
    ) * 100,
    2
)

highest_breach_region = (
    df[df["sla_breach"]]["region"]
    .value_counts()
    .idxmax()
)

# ---------------------------------
# Executive Summary File
# ---------------------------------

with open(
    "reports/executive_summary.txt",
    "w"
) as f:

    f.write(
        "FINANCIAL TRANSACTION ANOMALY & SLA REPORT\n\n"
    )

    f.write(
        f"Total Transactions: {total_txns:,}\n"
    )

    f.write(
        f"Anomalies Detected: {total_anomalies:,}\n"
    )

    f.write(
        f"SLA Breaches: {total_breaches:,}\n"
    )

    f.write(
        f"Fraud Transactions: {total_fraud:,}\n"
    )

    f.write(
        f"Error Rate: {error_rate}%\n"
    )

    f.write(
        f"Highest Breach Region: {highest_breach_region}\n\n"
    )

    f.write(
        "Recommendations:\n"
    )

    f.write(
        "- Investigate high breach regions.\n"
    )

    f.write(
        "- Review slow processing channels.\n"
    )

    f.write(
        "- Monitor high-value anomalous transactions.\n"
    )

# ---------------------------------
# Save Processed Dataset
# ---------------------------------

df.to_csv(
    "reports/processed_transactions.csv",
    index=False
)

print("Analysis completed successfully.")
print("Reports generated in reports/ folder")
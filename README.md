# 💳 Financial Transaction Anomaly & SLA Tracker

A data analytics project that simulates and monitors **200,000+ financial transactions** to identify anomalies, track SLA breaches, detect fraud patterns, and generate operational insights using **Python, SQL, SQLite, and Power BI**.

---

## 📌 Project Overview

Financial institutions process millions of transactions daily. Monitoring transaction performance, identifying anomalies, and tracking SLA violations are critical for reducing operational risk and ensuring service reliability.

This project builds an end-to-end analytics pipeline that:

* Generates realistic financial transaction data
* Detects anomalous transactions using Z-Score analysis
* Tracks SLA breaches
* Identifies fraud patterns
* Produces automated reports
* Visualizes operational KPIs in Power BI

---

## 🛠 Tech Stack

* Python
* Pandas
* NumPy
* Faker
* SQLite
* SQL
* Power BI
* Excel

---

## 📂 Project Structure

```text
transaction-anomaly-tracker/
│
├── data/
│   └── transactions.csv
│
├── reports/
│   ├── daily_report.csv
│   ├── region_report.csv
│   ├── channel_report.csv
│   ├── merchant_report.csv
│   ├── processed_transactions.csv
│   └── executive_summary.txt
│
├── sql/
│   ├── schema.sql
│   └── queries.sql
│
├── generate_data.py
├── load_to_sqlite.py
├── analysis.py
├── transactions.db
└── README.md
```

---

## 📊 Dataset

Generated using the Faker library with realistic banking transaction behavior.

### Total Records

* 200,000 Transactions

### Features

| Column            | Description                   |
| ----------------- | ----------------------------- |
| txn_id            | Unique Transaction ID         |
| amount            | Transaction Amount            |
| type              | Credit / Debit / Transfer     |
| timestamp         | Transaction Date & Time       |
| status            | SUCCESS / FAILED / PENDING    |
| processing_ms     | Processing Time               |
| sla_limit_ms      | SLA Threshold                 |
| customer_segment  | Retail / Corporate / Premium  |
| region            | North / South / East / West   |
| channel           | Mobile / Web / ATM / Branch   |
| merchant_category | Shopping / Travel / Food etc. |
| priority          | High / Medium / Low           |
| is_fraud          | Fraud Indicator               |

---

## 🔍 Business Problems Solved

### 1. Transaction Monitoring

Track daily transaction throughput and processing performance.

### 2. SLA Monitoring

Identify transactions exceeding agreed processing limits.

### 3. Fraud Detection

Flag suspicious high-value transactions.

### 4. Operational Reporting

Generate automated reports for management review.

### 5. Customer & Channel Analytics

Analyze transaction patterns across channels and customer segments.

---

## ⚙️ Anomaly Detection Logic

Z-Score based anomaly detection:

```python
z_score = (amount - mean) / std
```

Transaction is flagged as anomalous when:

```python
abs(z_score) > 3
```

---

## 🚨 SLA Breach Logic

A transaction is considered a breach when:

```python
processing_ms > sla_limit_ms
```

---

## 📈 SQL Analytics

Implemented analytical SQL queries including:

### Daily Transaction Volume

```sql
SELECT DATE(timestamp),
COUNT(*)
FROM transactions
GROUP BY DATE(timestamp);
```

### SLA Breach Count

```sql
SELECT COUNT(*)
FROM transactions
WHERE processing_ms > sla_limit_ms;
```

### Error Rate

```sql
SELECT
100.0 *
SUM(CASE WHEN status='FAILED' THEN 1 ELSE 0 END)
/ COUNT(*)
FROM transactions;
```

### Top Breach Categories

```sql
SELECT type,
COUNT(*)
FROM transactions
WHERE processing_ms > sla_limit_ms
GROUP BY type;
```

### Weekly Transaction Trends

```sql
SELECT
strftime('%Y-%W', timestamp),
COUNT(*)
FROM transactions
GROUP BY 1;
```

---

## 📊 Power BI Dashboard

### Executive KPIs

* Total Transactions
* Total Transaction Value
* SLA Breach %
* Fraud Count
* Error Rate %
* Average Processing Time

### Dashboard Pages

#### Operations Overview

* Transaction Volume Trend
* SLA Breach Trend
* Throughput KPIs

#### Risk & Fraud Analysis

* Fraud by Merchant Category
* Fraud by Region
* High Risk Transactions

#### Customer & Channel Analytics

* Customer Segment Analysis
* Channel Performance
* Regional Performance

---

## 📑 Generated Reports

The analysis pipeline automatically creates:

```text
daily_report.csv
region_report.csv
channel_report.csv
merchant_report.csv
executive_summary.txt
processed_transactions.csv
```

---

## 🎯 Key Insights

* Detected anomalous transactions using statistical analysis.
* Monitored SLA compliance across transaction channels.
* Identified fraud-prone merchant categories.
* Analyzed operational performance by region and customer segment.
* Generated executive-ready business reports.

---

## 🚀 How to Run

### Install Dependencies

```bash
pip install pandas numpy faker matplotlib
```

### Generate Data

```bash
python generate_data.py
```

### Load Data into SQLite

```bash
python load_to_sqlite.py
```

### Run Analysis

```bash
python analysis.py
```

---

## 📸 Dashboard Preview

Add screenshots here:

```text
images/dashboard_overview.png
images/fraud_analysis.png
images/customer_segments.png
```

---

## 📌 Resume Highlights

* Developed a Financial Transaction Anomaly & SLA Tracker processing 200,000+ simulated transactions using Python, SQL, SQLite, and Power BI.
* Implemented Z-Score based anomaly detection and automated SLA monitoring to identify operational risks and fraud patterns.
* Built executive dashboards and automated reporting workflows for transaction analytics and performance monitoring.

---

## 👨‍💻 Author

Pragati Mishra

B.Tech Computer Science Engineering (2026)

Skills: Python, SQL, Power BI, Data Analytics, Business Intelligence, Machine Learning

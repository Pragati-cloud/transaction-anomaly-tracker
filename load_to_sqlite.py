import sqlite3 
import pandas as pd

conn = sqlite3.connect("transactions.db")

df = pd.read_csv("data/transactions.csv")

df.to_sql(
    "transactions",
    conn,
    if_exists="replace",
    index=False
)

print("Loaded to SQLite")
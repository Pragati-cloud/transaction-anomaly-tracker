-- sql/schema.sql

CREATE TABLE transactions (

txn_id INTEGER PRIMARY KEY,

amount REAL,

type TEXT,

timestamp TEXT,

status TEXT,

processing_ms INTEGER,

sla_limit_ms INTEGER

);
Daily Volume
SELECT
DATE(timestamp) AS day,
COUNT(*) AS total_transactions
FROM transactions
GROUP BY day
ORDER BY day;

SLA Breach Count
SELECT
COUNT(*) AS breach_count
FROM transactions
WHERE processing_ms > sla_limit_ms;

Error Rate
SELECT

ROUND(
100.0 *
SUM(
CASE WHEN status='FAILED'
THEN 1 ELSE 0 END
)
/ COUNT(*),
2
) AS error_rate

FROM transactions;

Top Breach Categories
SELECT
type,
COUNT(*) AS breaches
FROM transactions
WHERE processing_ms > sla_limit_ms
GROUP BY type
ORDER BY breaches DESC;

Weekly Trend
SELECT

strftime('%Y-%W',timestamp) AS week,

COUNT(*) AS total

FROM transactions

GROUP BY week

ORDER BY week;
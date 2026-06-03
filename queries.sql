-- 1. Top 5 funds by AUM
SELECT amfi_code, SUM(aum_value) as total_aum 
FROM fact_aum 
GROUP BY amfi_code 
ORDER BY total_aum DESC LIMIT 5;

-- 2. Average NAV per month for a specific year
SELECT strftime('%Y-%m', date) as month, AVG(nav_value) as avg_nav
FROM fact_nav
GROUP BY month
ORDER BY month;

-- 3. SIP Year-over-Year (YoY) Growth Volume
SELECT strftime('%Y', transaction_date) as year, SUM(amount) as total_sip_volume
FROM fact_transactions
WHERE transaction_type = 'SIP'
GROUP BY year
ORDER BY year;

-- 4. Total transaction volume by State
SELECT state, SUM(amount) as total_investment
FROM fact_transactions
WHERE transaction_type IN ('SIP', 'LUMPSUM')
GROUP BY state
ORDER BY total_investment DESC;

-- 5. Funds with expense_ratio < 1%
SELECT amfi_code, expense_ratio 
FROM fact_performance 
WHERE expense_ratio < 1.0;

-- 6. Total Redemption volume vs Lumpsum Volume
SELECT transaction_type, SUM(amount) as total_amount
FROM fact_transactions
GROUP BY transaction_type;

-- 7. Highest performing funds (1Y Return) excluding anomalies
SELECT amfi_code, 1y_return
FROM fact_performance
WHERE anomaly_flag = 0
ORDER BY 1y_return DESC LIMIT 10;

-- 8. Daily NAV Volatility (Max NAV - Min NAV) per fund
SELECT amfi_code, (MAX(nav_value) - MIN(nav_value)) as nav_volatility
FROM fact_nav
GROUP BY amfi_code
ORDER BY nav_volatility DESC;

-- 9. Count of active transactions by KYC Status
SELECT kyc_status, COUNT(transaction_id) as txn_count
FROM fact_transactions
GROUP BY kyc_status;

-- 10. Top 3 states with highest Redemption rates
SELECT state, SUM(amount) as total_redemption
FROM fact_transactions
WHERE transaction_type = 'REDEMPTION'
GROUP BY state
ORDER BY total_redemption DESC LIMIT 3;
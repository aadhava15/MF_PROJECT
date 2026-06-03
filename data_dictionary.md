# Data Dictionary: Mutual Fund Data Warehouse

## 1. fact_nav (Cleaned NAV History)
| Column Name | Data Type | Description / Business Definition | Source |
| :--- | :--- | :--- | :--- |
| `amfi_code` | TEXT | Unique AMFI identifier for the mutual fund scheme. | nav_history.csv |
| `date` | DATE | Date of the NAV record. | nav_history.csv |
| `nav_value` | REAL | Net Asset Value (Must be > 0). Missing weekends are ffilled. | nav_history.csv |

## 2. fact_transactions (Cleaned Investor Transactions)
| Column Name | Data Type | Description / Business Definition | Source |
| :--- | :--- | :--- | :--- |
| `transaction_id`| TEXT | Unique identifier for the transaction. | investor_transactions.csv|
| `amfi_code` | TEXT | Linked mutual fund scheme code. | investor_transactions.csv|
| `transaction_type`| TEXT | Type of txn (SIP, LUMPSUM, REDEMPTION). | investor_transactions.csv|
| `amount` | REAL | Transaction amount (Must be > 0). | investor_transactions.csv|
| `kyc_status` | TEXT | Investor KYC (VERIFIED, PENDING, REJECTED). | investor_transactions.csv|

## 3. fact_performance (Cleaned Scheme Performance)
| Column Name | Data Type | Description / Business Definition | Source |
| :--- | :--- | :--- | :--- |
| `amfi_code` | TEXT | Linked mutual fund scheme code. | scheme_performance.csv |
| `1y_return` | REAL | 1-Year trailing return percentage. | scheme_performance.csv |
| `expense_ratio` | REAL | Annual operating fee percentage (0.1% to 2.5%).| scheme_performance.csv |
| `anomaly_flag` | INTEGER| 1 if returns are unrealistic (>100% or <-99%), else 0.| Computed |
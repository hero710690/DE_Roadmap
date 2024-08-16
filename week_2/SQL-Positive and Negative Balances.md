### Problem Overview

You might be given a table that tracks transactions for various accounts. Your task is to analyze the balance of each account and determine whether it is positive or negative. Depending on the specific question, you may also need to identify accounts that have had both positive and negative balances over time.

### Example Table Structure

Let’s assume you have a table named `Transactions` with the following structure:

```sql
CREATE TABLE Transactions (
    account_id INT,
    transaction_date DATE,
    amount DECIMAL(10, 2)
);
```

### Sample Data

Here’s what some sample data might look like:

| account_id | transaction_date | amount  |
|------------|------------------|---------|
| 1          | 2024-08-01       | 100.00  |
| 1          | 2024-08-02       | -150.00 |
| 1          | 2024-08-03       | 200.00  |
| 2          | 2024-08-01       | -50.00  |
| 2          | 2024-08-02       | -20.00  |
| 2          | 2024-08-03       | 30.00   |
| 3          | 2024-08-01       | 100.00  |
| 3          | 2024-08-02       | 50.00   |
| 3          | 2024-08-03       | 25.00   |

### Problem Statement

1. **Determine the current balance of each account and categorize it as positive or negative.**
2. **Identify accounts that have had both positive and negative balances over time.**

### Solution Approach

#### 1. **Determine Current Balance and Categorize**

First, to determine whether an account's current balance is positive or negative, you need to sum up all the transactions for each account.

### SQL Query:

```sql
SELECT
    account_id,
    SUM(amount) AS balance,
    CASE 
        WHEN SUM(amount) > 0 THEN 'Positive'
        WHEN SUM(amount) < 0 THEN 'Negative'
        ELSE 'Zero'
    END AS balance_status
FROM
    Transactions
GROUP BY
    account_id;
```

#### Explanation:

- **SUM(amount)**: Calculates the total balance for each account.
- **CASE Statement**: Categorizes the balance as 'Positive', 'Negative', or 'Zero' based on the sum of transactions.
- **GROUP BY account_id**: Aggregates the data by each account.

**Result for Sample Data**:

Given the sample data:

| account_id | transaction_date | amount  |
|------------|------------------|---------|
| 1          | 2024-08-01       | 100.00  |
| 1          | 2024-08-02       | -150.00 |
| 1          | 2024-08-03       | 200.00  |
| 2          | 2024-08-01       | -50.00  |
| 2          | 2024-08-02       | -20.00  |
| 2          | 2024-08-03       | 30.00   |
| 3          | 2024-08-01       | 100.00  |
| 3          | 2024-08-02       | 50.00   |
| 3          | 2024-08-03       | 25.00   |

The query will return:

| account_id | balance | balance_status |
|------------|---------|----------------|
| 1          | 150.00  | Positive       |
| 2          | -40.00  | Negative       |
| 3          | 175.00  | Positive       |

#### 2. **Identify Accounts with Both Positive and Negative Balances Over Time**

To find accounts that have fluctuated between positive and negative balances, you would need to track the running balance over time and check if it has ever crossed zero.

### SQL Query:

```sql
WITH RunningBalance AS (
    SELECT
        account_id,
        transaction_date,
        SUM(amount) OVER (PARTITION BY account_id ORDER BY transaction_date) AS running_balance
    FROM
        Transactions
),
BalanceStatus AS (
    SELECT
        account_id,
        MAX(CASE WHEN running_balance > 0 THEN 1 ELSE 0 END) AS has_positive,
        MAX(CASE WHEN running_balance < 0 THEN 1 ELSE 0 END) AS has_negative
    FROM
        RunningBalance
    GROUP BY
        account_id
)
SELECT
    account_id
FROM
    BalanceStatus
WHERE
    has_positive = 1 AND has_negative = 1;
```

#### Explanation:

- **RunningBalance CTE**:
  - **SUM(amount) OVER (PARTITION BY account_id ORDER BY transaction_date)**: Computes the running balance for each account.
- **BalanceStatus CTE**:
  - Uses conditional aggregation to determine if an account has ever had a positive (`has_positive`) or negative (`has_negative`) balance.
- **Final Select**:
  - Selects only those accounts that have both positive and negative balances.

**Result for Sample Data**:

Given the sample data, the query will return:

| account_id |
|------------|
| 1          |
| 2          |

This output indicates that accounts 1 and 2 have both experienced positive and negative balances over time.

### Additional Considerations:

- **Handling Edge Cases**: Consider how to handle accounts with a balance that never crosses zero or those with only one transaction.
- **Performance**: For large datasets, ensure indexes on `account_id` and `transaction_date` are in place to optimize performance.

### Real-world Application:

- **Banking Systems**: This type of analysis is crucial in banking for identifying accounts that frequently go into overdraft or analyzing customer behavior based on their account balances.
- **Financial Audits**: In audits, it's important to track accounts that fluctuate between positive and negative balances to identify risky accounts or accounts that may require intervention.

This approach gives you a comprehensive way to analyze account balances, categorizing them and identifying patterns of fluctuation, which can be critical for financial analysis and reporting.
### Problem Overview

You're typically provided with a table containing transaction data for various accounts. Your task is to determine the specific days on which an account balance went negative (i.e., overdraft occurred).

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
| 1          | 2024-08-04       | -300.00 |
| 2          | 2024-08-01       | 50.00   |
| 2          | 2024-08-02       | -20.00  |
| 2          | 2024-08-03       | -40.00  |
| 2          | 2024-08-04       | -10.00  |

### Problem Statement

Find the specific dates for each account where the balance drops below zero (indicating an overdraft). 

### Solution Approach

1. **Calculate Running Balance**: First, calculate the running balance for each account based on the transaction data.
2. **Identify Overdraft Days**: Identify the days on which the running balance is less than zero.

### SQL Query

Here's how you can write the SQL query to solve this problem:

```sql
WITH RunningBalance AS (
    SELECT 
        account_id,
        transaction_date,
        SUM(amount) OVER (PARTITION BY account_id ORDER BY transaction_date) AS running_balance
    FROM 
        Transactions
)
SELECT 
    account_id,
    transaction_date
FROM 
    RunningBalance
WHERE 
    running_balance < 0;
```

### Explanation:

1. **RunningBalance CTE**:
   - **`SUM(amount) OVER (PARTITION BY account_id ORDER BY transaction_date)`**: This window function computes the running total of the `amount` column for each account. The `PARTITION BY account_id` ensures the balance is calculated separately for each account, and the `ORDER BY transaction_date` ensures that transactions are summed in chronological order.
   
2. **Final Select**:
   - The main query selects the `account_id` and `transaction_date` from the `RunningBalance` CTE where the `running_balance` is less than zero, indicating an overdraft.

### Example Result:

Given the sample data:

| account_id | transaction_date | amount  |
|------------|------------------|---------|
| 1          | 2024-08-01       | 100.00  |
| 1          | 2024-08-02       | -150.00 |
| 1          | 2024-08-03       | 200.00  |
| 1          | 2024-08-04       | -300.00 |
| 2          | 2024-08-01       | 50.00   |
| 2          | 2024-08-02       | -20.00  |
| 2          | 2024-08-03       | -40.00  |
| 2          | 2024-08-04       | -10.00  |

The query will return:

| account_id | transaction_date |
|------------|------------------|
| 1          | 2024-08-02       |
| 1          | 2024-08-04       |
| 2          | 2024-08-03       |

### Additional Considerations:

- **Multiple Transactions per Day**: If there are multiple transactions per day, the `SUM` function in the window query will naturally aggregate these, maintaining accuracy.
- **Performance**: The performance can be improved by indexing the `account_id` and `transaction_date` columns, especially if the table is large.

### Real-world Application:
- **Banking Systems**: This type of query is common in banking systems, where it is crucial to track and notify customers about overdrafts to avoid fees.
- **Financial Reporting**: Identifying overdrafts is also useful in financial reporting, especially for ensuring that accounts maintain adequate balances.

By breaking down the problem and using window functions, this query effectively identifies the days when an overdraft occurred for each account, providing a clear and efficient solution.
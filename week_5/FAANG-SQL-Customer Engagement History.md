### Problem Overview

You might be given tables that record customer activities, such as logins, purchases, support interactions, or other forms of engagement. Your task could involve creating a detailed engagement history for each customer, summarizing their interactions, or identifying patterns over time.

### Example Table Structure

Let’s assume you have two tables: `Customers` and `Engagements`.

1. **Customers Table**:
    - Contains basic information about each customer.
    - Structure:
      ```sql
      CREATE TABLE Customers (
          customer_id INT PRIMARY KEY,
          customer_name VARCHAR(255),
          email VARCHAR(255),
          join_date DATE
      );
      ```

2. **Engagements Table**:
    - Contains records of customer interactions with the platform.
    - Structure:
      ```sql
      CREATE TABLE Engagements (
          engagement_id INT PRIMARY KEY,
          customer_id INT,
          engagement_type VARCHAR(50),  -- e.g., 'login', 'purchase', 'support'
          engagement_date DATE,
          details TEXT
      );
      ```

### Sample Data

Here’s what some sample data might look like:

**Customers Table**:
| customer_id | customer_name | email                 | join_date  |
|-------------|---------------|-----------------------|------------|
| 1           | John Doe      | john@example.com      | 2023-01-15 |
| 2           | Jane Smith    | jane@example.com      | 2023-02-20 |
| 3           | Mike Johnson  | mike@example.com      | 2023-03-10 |

**Engagements Table**:
| engagement_id | customer_id | engagement_type | engagement_date | details              |
|---------------|-------------|-----------------|-----------------|----------------------|
| 1             | 1           | login           | 2023-02-01      | "Logged in from web" |
| 2             | 1           | purchase        | 2023-02-05      | "Bought Product A"   |
| 3             | 1           | support         | 2023-02-07      | "Issue with Product A"|
| 4             | 2           | login           | 2023-03-01      | "Logged in from mobile"|
| 5             | 2           | purchase        | 2023-03-10      | "Bought Product B"   |
| 6             | 3           | login           | 2023-03-11      | "Logged in from web" |
| 7             | 1           | login           | 2023-03-15      | "Logged in from mobile"|

### Problem Statement

1. **Summarize Customer Engagement History**: For each customer, provide a summary of their engagements, such as the total number of logins, purchases, and support interactions.
2. **Detailed Engagement History**: Generate a detailed engagement history for each customer, listing all their engagements in chronological order.
3. **Identify Active Customers**: Identify customers who have engaged with the platform within a specific time frame, such as the last 30 days.

### Solution Approach

Let's explore how to solve these problems using SQL.

#### 1. **Summarize Customer Engagement History**

To summarize customer engagement history, you need to group the engagements by customer and engagement type, then count the number of each type of engagement.

### SQL Query:

```sql
SELECT
    e.customer_id,
    c.customer_name,
    c.email,
    e.engagement_type,
    COUNT(e.engagement_id) AS engagement_count
FROM
    Engagements e
JOIN
    Customers c ON e.customer_id = c.customer_id
GROUP BY
    e.customer_id, c.customer_name, c.email, e.engagement_type
ORDER BY
    e.customer_id, e.engagement_type;
```

#### Explanation:

- **JOIN Engagements e ON Customers c**: Joins the `Engagements` table with the `Customers` table to access customer details.
- **COUNT(e.engagement_id)**: Counts the number of engagements of each type for each customer.
- **GROUP BY**: Groups the results by customer ID, customer name, email, and engagement type.
- **ORDER BY**: Orders the results by customer ID and engagement type.

**Result for Sample Data**:

| customer_id | customer_name | email             | engagement_type | engagement_count |
|-------------|---------------|-------------------|-----------------|------------------|
| 1           | John Doe      | john@example.com  | login           | 2                |
| 1           | John Doe      | john@example.com  | purchase        | 1                |
| 1           | John Doe      | john@example.com  | support         | 1                |
| 2           | Jane Smith    | jane@example.com  | login           | 1                |
| 2           | Jane Smith    | jane@example.com  | purchase        | 1                |
| 3           | Mike Johnson  | mike@example.com  | login           | 1                |

This output shows the number of each type of engagement for each customer.

#### 2. **Detailed Engagement History**

To generate a detailed engagement history for each customer, you can simply select all engagements and order them by customer and engagement date.

### SQL Query:

```sql
SELECT
    c.customer_id,
    c.customer_name,
    e.engagement_type,
    e.engagement_date,
    e.details
FROM
    Engagements e
JOIN
    Customers c ON e.customer_id = c.customer_id
ORDER BY
    c.customer_id, e.engagement_date;
```

#### Explanation:

- **JOIN Engagements e ON Customers c**: Joins the `Engagements` table with the `Customers` table to get customer information.
- **ORDER BY c.customer_id, e.engagement_date**: Orders the results by customer ID and engagement date to show a chronological history of each customer's engagements.

**Result for Sample Data**:

| customer_id | customer_name | engagement_type | engagement_date | details               |
|-------------|---------------|-----------------|-----------------|-----------------------|
| 1           | John Doe      | login           | 2023-02-01      | "Logged in from web"  |
| 1           | John Doe      | purchase        | 2023-02-05      | "Bought Product A"    |
| 1           | John Doe      | support         | 2023-02-07      | "Issue with Product A"|
| 1           | John Doe      | login           | 2023-03-15      | "Logged in from mobile"|
| 2           | Jane Smith    | login           | 2023-03-01      | "Logged in from mobile"|
| 2           | Jane Smith    | purchase        | 2023-03-10      | "Bought Product B"    |
| 3           | Mike Johnson  | login           | 2023-03-11      | "Logged in from web"  |

This result provides a detailed log of each customer's engagement history.

#### 3. **Identify Active Customers**

To identify customers who have engaged with the platform within a specific time frame (e.g., the last 30 days), you can filter the results using the `WHERE` clause.

### SQL Query:

```sql
SELECT DISTINCT
    c.customer_id,
    c.customer_name,
    c.email
FROM
    Engagements e
JOIN
    Customers c ON e.customer_id = c.customer_id
WHERE
    e.engagement_date >= DATE_SUB(CURDATE(), INTERVAL 30 DAY)
ORDER BY
    c.customer_id;
```

#### Explanation:

- **DATE_SUB(CURDATE(), INTERVAL 30 DAY)**: Calculates the date 30 days before the current date.
- **WHERE e.engagement_date >= ...**: Filters engagements to include only those within the last 30 days.
- **DISTINCT**: Ensures each customer is listed only once, even if they have multiple engagements in the time frame.

**Result for Sample Data**:

| customer_id | customer_name | email             |
|-------------|---------------|-------------------|
| 1           | John Doe      | john@example.com  |
| 2           | Jane Smith    | jane@example.com  |
| 3           | Mike Johnson  | mike@example.com  |

This output lists all customers who have engaged with the platform within the last 30 days.

### Additional Considerations:

- **Handling NULL Values**: Ensure that NULL values in columns like `details` or `engagement_date` are handled appropriately, depending on your specific needs.
- **Performance**: For large datasets, ensure that appropriate indexes are in place, especially on columns like `customer_id` and `engagement_date`, to optimize query performance.
- **Time Zones**: If engagements are logged in different time zones, consider normalizing times to a standard time zone before analysis.

### Real-world Application:

- **Customer Relationship Management (CRM)**: Tracking customer engagement history helps businesses understand customer behavior, identify high-value customers, and tailor marketing strategies.
- **Customer Support**: Detailed engagement history can help customer support teams understand a customer's journey and provide better service.
- **User Experience Design**: Analyzing engagement patterns can inform UX design decisions to improve user satisfaction and retention.

This approach provides a comprehensive way to analyze and understand customer engagement history using SQL, offering valuable
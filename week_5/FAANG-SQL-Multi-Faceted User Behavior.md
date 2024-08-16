### Problem Overview

You might be given tables that record different types of user interactions or behaviors, such as logins, purchases, page views, or other activities. Your task could involve creating a comprehensive profile of user behavior by aggregating and analyzing these different types of activities.

### Example Table Structure

Let’s assume you have three tables: `Users`, `UserActions`, and `UserPurchases`.

1. **Users Table**:
    - Contains basic information about each user.
    - Structure:
      ```sql
      CREATE TABLE Users (
          user_id INT PRIMARY KEY,
          user_name VARCHAR(255),
          join_date DATE
      );
      ```

2. **UserActions Table**:
    - Contains records of different user actions on the platform (e.g., logins, page views).
    - Structure:
      ```sql
      CREATE TABLE UserActions (
          action_id INT PRIMARY KEY,
          user_id INT,
          action_type VARCHAR(50),  -- e.g., 'login', 'page_view', 'click'
          action_date DATE
      );
      ```

3. **UserPurchases Table**:
    - Contains records of purchases made by users.
    - Structure:
      ```sql
      CREATE TABLE UserPurchases (
          purchase_id INT PRIMARY KEY,
          user_id INT,
          purchase_amount DECIMAL(10, 2),
          purchase_date DATE
      );
      ```

### Sample Data

Here’s what some sample data might look like:

**Users Table**:
| user_id | user_name  | join_date  |
|---------|------------|------------|
| 1       | Alice      | 2023-01-15 |
| 2       | Bob        | 2023-02-20 |
| 3       | Charlie    | 2023-03-10 |

**UserActions Table**:
| action_id | user_id | action_type | action_date  |
|-----------|---------|-------------|--------------|
| 1         | 1       | login       | 2023-02-01   |
| 2         | 1       | page_view   | 2023-02-01   |
| 3         | 1       | click       | 2023-02-05   |
| 4         | 2       | login       | 2023-03-01   |
| 5         | 2       | page_view   | 2023-03-10   |
| 6         | 3       | login       | 2023-03-11   |
| 7         | 3       | page_view   | 2023-03-15   |

**UserPurchases Table**:
| purchase_id | user_id | purchase_amount | purchase_date |
|-------------|---------|-----------------|---------------|
| 1           | 1       | 50.00           | 2023-02-05    |
| 2           | 2       | 75.00           | 2023-03-10    |
| 3           | 3       | 100.00          | 2023-03-15    |

### Problem Statement

1. **Summarize Multi-Faceted User Behavior**: For each user, provide a summary that includes the number of logins, page views, clicks, and total purchase amount.
2. **Detailed Behavioral Analysis**: Generate a detailed report of user activities, combining different facets of behavior such as actions and purchases.
3. **Identify Users with Specific Behavior Patterns**: Identify users who meet certain behavioral criteria, such as those who have made a purchase but have low engagement in other activities.

### Solution Approach

Let's explore how to solve these problems using SQL.

#### 1. **Summarize Multi-Faceted User Behavior**

To summarize multi-faceted user behavior, you need to aggregate the different types of user actions and their purchase behavior.

### SQL Query:

```sql
SELECT
    u.user_id,
    u.user_name,
    SUM(CASE WHEN ua.action_type = 'login' THEN 1 ELSE 0 END) AS login_count,
    SUM(CASE WHEN ua.action_type = 'page_view' THEN 1 ELSE 0 END) AS page_view_count,
    SUM(CASE WHEN ua.action_type = 'click' THEN 1 ELSE 0 END) AS click_count,
    SUM(up.purchase_amount) AS total_purchase_amount
FROM
    Users u
LEFT JOIN
    UserActions ua ON u.user_id = ua.user_id
LEFT JOIN
    UserPurchases up ON u.user_id = up.user_id
GROUP BY
    u.user_id, u.user_name
ORDER BY
    u.user_id;
```

#### Explanation:

- **LEFT JOIN**: Joins the `Users` table with `UserActions` and `UserPurchases` to gather all relevant data.
- **SUM(CASE WHEN ... THEN 1 ELSE 0 END)**: Counts the number of each type of action by using conditional aggregation.
- **SUM(up.purchase_amount)**: Sums up the total purchase amount for each user.
- **GROUP BY u.user_id, u.user_name**: Groups the results by user to summarize their behavior.

**Result for Sample Data**:

| user_id | user_name | login_count | page_view_count | click_count | total_purchase_amount |
|---------|-----------|-------------|-----------------|-------------|-----------------------|
| 1       | Alice     | 1           | 1               | 1           | 50.00                 |
| 2       | Bob       | 1           | 1               | 0           | 75.00                 |
| 3       | Charlie   | 1           | 1               | 0           | 100.00                |

This output shows a summary of each user's activities, including the number of logins, page views, clicks, and total purchase amount.

#### 2. **Detailed Behavioral Analysis**

To generate a detailed report of user activities, you can combine user actions and purchases in a single query.

### SQL Query:

```sql
SELECT
    u.user_id,
    u.user_name,
    ua.action_type AS activity_type,
    ua.action_date AS activity_date,
    up.purchase_amount,
    up.purchase_date
FROM
    Users u
LEFT JOIN
    UserActions ua ON u.user_id = ua.user_id
LEFT JOIN
    UserPurchases up ON u.user_id = up.user_id
ORDER BY
    u.user_id, ua.action_date, up.purchase_date;
```

#### Explanation:

- **LEFT JOIN**: Joins the `Users`, `UserActions`, and `UserPurchases` tables.
- **ORDER BY u.user_id, ua.action_date, up.purchase_date**: Orders the results by user, then by the date of actions and purchases to create a chronological view of user behavior.

**Result for Sample Data**:

| user_id | user_name | activity_type | activity_date | purchase_amount | purchase_date |
|---------|-----------|---------------|---------------|-----------------|---------------|
| 1       | Alice     | login         | 2023-02-01    | NULL            | NULL          |
| 1       | Alice     | page_view     | 2023-02-01    | NULL            | NULL          |
| 1       | Alice     | click         | 2023-02-05    | 50.00           | 2023-02-05    |
| 2       | Bob       | login         | 2023-03-01    | NULL            | NULL          |
| 2       | Bob       | page_view     | 2023-03-10    | 75.00           | 2023-03-10    |
| 3       | Charlie   | login         | 2023-03-11    | NULL            | NULL          |
| 3       | Charlie   | page_view     | 2023-03-15    | 100.00          | 2023-03-15    |

This result provides a detailed log of each user's activities, including actions and purchases.

#### 3. **Identify Users with Specific Behavior Patterns**

To identify users who have made a purchase but have low engagement in other activities (e.g., fewer than 2 logins), you can use a `HAVING` clause.

### SQL Query:

```sql
SELECT
    u.user_id,
    u.user_name,
    SUM(CASE WHEN ua.action_type = 'login' THEN 1 ELSE 0 END) AS login_count,
    SUM(up.purchase_amount) AS total_purchase_amount
FROM
    Users u
LEFT JOIN
    UserActions ua ON u.user_id = ua.user_id
LEFT JOIN
    UserPurchases up ON u.user_id = up.user_id
GROUP BY
    u.user_id, u.user_name
HAVING
    total_purchase_amount > 0 AND login_count < 2
ORDER BY
    total_purchase_amount DESC;
```

#### Explanation:

- **HAVING total_purchase_amount > 0 AND login_count < 2**: Filters users who have made a purchase but have fewer than 2 logins.
- **ORDER BY total_purchase_amount DESC**: Orders the results by total purchase amount.

**Result for Sample Data**:

Given the sample data, none of the users would satisfy this condition, but if there were a user who made a purchase and had fewer
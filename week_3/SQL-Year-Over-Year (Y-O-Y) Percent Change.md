The SQL question titled "Year-Over-Year (Y-O-Y) Percent Change" typically involves calculating the percentage change in a particular metric (such as revenue, sales, or user sign-ups) from one year to the next. This kind of analysis is crucial for understanding growth trends and performance over time.

### Problem Overview

You might be given a table that tracks yearly data for a specific metric, and your task is to calculate the Year-Over-Year percent change for each year compared to the previous year.

### Example Table Structure

Let’s assume you have a table named `AnnualMetrics` with the following structure:

```sql
CREATE TABLE AnnualMetrics (
    year INT,
    metric_value DECIMAL(15, 2)
);
```

### Sample Data

Here’s what some sample data might look like:

| year | metric_value |
|------|--------------|
| 2021 | 10000.00     |
| 2022 | 12000.00     |
| 2023 | 9000.00      |
| 2024 | 15000.00     |

### Problem Statement

1. **Calculate the Year-Over-Year percent change for each year compared to the previous year.**
2. **Handle cases where there is no previous year to compare (e.g., for the first year in the dataset).**

### Solution Approach

#### 1. **Calculate the Year-Over-Year Percent Change**

To calculate the Year-Over-Year percent change, you need to:
- Compare each year’s `metric_value` with the previous year’s `metric_value`.
- Compute the percentage change using the formula:

\[
\text{Percent Change} = \frac{(\text{Current Year Value} - \text{Previous Year Value})}{\text{Previous Year Value}} \times 100
\]

### SQL Query:

```sql
WITH YearlyComparison AS (
    SELECT
        year,
        metric_value,
        LAG(metric_value) OVER (ORDER BY year) AS previous_year_value
    FROM
        AnnualMetrics
)
SELECT
    year,
    metric_value,
    previous_year_value,
    CASE
        WHEN previous_year_value IS NULL THEN NULL
        ELSE ((metric_value - previous_year_value) / previous_year_value) * 100
    END AS yoy_percent_change
FROM
    YearlyComparison;
```

#### Explanation:

- **LAG(metric_value) OVER (ORDER BY year)**: The `LAG` window function is used to access the metric value of the previous year for each row. It creates a new column `previous_year_value` that contains the metric value from the previous year.
- **CASE Statement**: Handles the case where there is no previous year to compare (i.e., the first year in the dataset), returning `NULL` for that year.
- **Percent Change Calculation**: The percent change is calculated using the formula provided, and the result is multiplied by 100 to convert it to a percentage.

**Result for Sample Data**:

Given the sample data, the query will return:

| year | metric_value | previous_year_value | yoy_percent_change |
|------|--------------|---------------------|--------------------|
| 2021 | 10000.00     | NULL                | NULL               |
| 2022 | 12000.00     | 10000.00            | 20.00              |
| 2023 | 9000.00      | 12000.00            | -25.00             |
| 2024 | 15000.00     | 9000.00             | 66.67              |

### Additional Considerations:

- **Handling Missing Years**: If there are gaps in the years (e.g., no data for 2022), the query as written will still calculate the percent change relative to the last available year. If you need to account for missing years differently (e.g., by assuming no change), you might need additional logic.
- **Performance**: Ensure that your table has an index on the `year` column to optimize the `ORDER BY` operation within the window function.

### Real-world Application:

- **Financial Analysis**: This type of calculation is common in financial analysis, where companies track metrics like revenue, profit, or expenses over time to understand growth trends.
- **Business Reporting**: Y-O-Y percent change is a standard KPI in business reports to compare performance over time and identify growth or decline patterns.

This approach provides a clear and efficient way to calculate Year-Over-Year percent changes using SQL, offering valuable insights into how a particular metric evolves over time.
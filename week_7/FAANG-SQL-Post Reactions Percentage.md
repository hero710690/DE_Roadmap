### Problem Overview

You might be given tables that track posts and the reactions to those posts. Your task could involve calculating the percentage of each reaction type for each post, identifying which posts have the most positive or negative reactions, or analyzing reaction trends over time.

### Example Table Structure

Let’s assume you have two tables: `Posts` and `Reactions`.

1. **Posts Table**:
    - Contains information about each post.
    - Structure:
      ```sql
      CREATE TABLE Posts (
          post_id INT PRIMARY KEY,
          post_content TEXT,
          post_date DATE
      );
      ```

2. **Reactions Table**:
    - Contains records of reactions to each post.
    - Structure:
      ```sql
      CREATE TABLE Reactions (
          reaction_id INT PRIMARY KEY,
          post_id INT,
          user_id INT,
          reaction_type VARCHAR(50),  -- e.g., 'like', 'love', 'angry', 'sad'
          reaction_date DATE
      );
      ```

### Sample Data

Here’s what some sample data might look like:

**Posts Table**:
| post_id | post_content          | post_date  |
|---------|-----------------------|------------|
| 1       | "First post!"          | 2024-08-01 |
| 2       | "Check out this photo" | 2024-08-02 |
| 3       | "Important announcement" | 2024-08-03 |

**Reactions Table**:
| reaction_id | post_id | user_id | reaction_type | reaction_date |
|-------------|---------|---------|---------------|---------------|
| 1           | 1       | 101     | 'like'        | 2024-08-01    |
| 2           | 1       | 102     | 'love'        | 2024-08-01    |
| 3           | 1       | 103     | 'like'        | 2024-08-02    |
| 4           | 2       | 104     | 'angry'       | 2024-08-02    |
| 5           | 2       | 105     | 'sad'         | 2024-08-02    |
| 6           | 2       | 106     | 'like'        | 2024-08-03    |
| 7           | 3       | 107     | 'love'        | 2024-08-03    |
| 8           | 3       | 108     | 'like'        | 2024-08-04    |

### Problem Statement

1. **Calculate the Percentage of Each Reaction Type for Each Post**: Determine what percentage of the total reactions to a post are of each type (like, love, angry, sad, etc.).
2. **Identify the Most Common Reaction per Post**: Determine which reaction type is most common for each post.
3. **Compare Reaction Distribution Across Multiple Posts**: Compare how reactions are distributed across different posts to identify patterns or trends.

### Solution Approach

Let’s explore how to solve these problems using SQL.

#### 1. **Calculate the Percentage of Each Reaction Type for Each Post**

To calculate the percentage of each reaction type for each post, you need to count the total reactions and then determine what percentage each type contributes.

### SQL Query:

```sql
SELECT
    r.post_id,
    r.reaction_type,
    COUNT(r.reaction_id) * 100.0 / (
        SELECT COUNT(*)
        FROM Reactions r2
        WHERE r2.post_id = r.post_id
    ) AS reaction_percentage
FROM
    Reactions r
GROUP BY
    r.post_id, r.reaction_type
ORDER BY
    r.post_id, reaction_percentage DESC;
```

#### Explanation:

- **COUNT(r.reaction_id) * 100.0 / (...) AS reaction_percentage**: Calculates the percentage of each reaction type by dividing the count of a specific reaction by the total number of reactions for that post, multiplied by 100 to get a percentage.
- **GROUP BY r.post_id, r.reaction_type**: Groups the results by post ID and reaction type to calculate the percentage for each type.
- **ORDER BY r.post_id, reaction_percentage DESC**: Orders the results by post and then by the percentage in descending order to show the most common reactions first.

**Result for Sample Data**:

For the sample data, the query might return:

| post_id | reaction_type | reaction_percentage |
|---------|---------------|---------------------|
| 1       | 'like'        | 66.67%              |
| 1       | 'love'        | 33.33%              |
| 2       | 'like'        | 33.33%              |
| 2       | 'angry'       | 33.33%              |
| 2       | 'sad'         | 33.33%              |
| 3       | 'love'        | 50.00%              |
| 3       | 'like'        | 50.00%              |

This output shows the percentage distribution of each reaction type for each post.

#### 2. **Identify the Most Common Reaction per Post**

To find the most common reaction type for each post, you can build on the previous query by selecting only the top result per post.

### SQL Query:

```sql
WITH ReactionCounts AS (
    SELECT
        r.post_id,
        r.reaction_type,
        COUNT(r.reaction_id) AS reaction_count,
        RANK() OVER (PARTITION BY r.post_id ORDER BY COUNT(r.reaction_id) DESC) AS rank
    FROM
        Reactions r
    GROUP BY
        r.post_id, r.reaction_type
)
SELECT
    post_id,
    reaction_type,
    reaction_count
FROM
    ReactionCounts
WHERE
    rank = 1
ORDER BY
    post_id;
```

#### Explanation:

- **RANK() OVER (PARTITION BY r.post_id ORDER BY COUNT(r.reaction_id) DESC)**: Assigns a rank to each reaction type per post, based on the number of reactions, with the most common reaction type being ranked 1.
- **WHERE rank = 1**: Filters to include only the most common reaction per post.
- **ORDER BY post_id**: Orders the results by post ID for clarity.

**Result for Sample Data**:

For the sample data, this query might return:

| post_id | reaction_type | reaction_count |
|---------|---------------|----------------|
| 1       | 'like'        | 2              |
| 2       | 'like'        | 1              |
| 3       | 'love'        | 1              |

This output shows the most common reaction type for each post.

#### 3. **Compare Reaction Distribution Across Multiple Posts**

To compare reaction distributions across posts, you can use a query similar to the first one but aggregate the data across multiple posts.

### SQL Query:

```sql
SELECT
    r.post_id,
    r.reaction_type,
    COUNT(r.reaction_id) * 100.0 / (
        SELECT COUNT(*)
        FROM Reactions r2
        WHERE r2.post_id = r.post_id
    ) AS reaction_percentage
FROM
    Reactions r
GROUP BY
    r.post_id, r.reaction_type
ORDER BY
    post_id, reaction_percentage DESC;
```

#### Explanation:

- **This query is similar to the first one** but can be used to generate a comparative analysis by running it for multiple posts or filtering specific posts.

**Result for Sample Data**:

The result will allow you to compare the percentage distribution of reactions across different posts.

### Additional Considerations

- **Handling Zero Reactions**: If a post has no reactions, ensure that the query handles this scenario gracefully (e.g., by returning a percentage of 0% for all types).
- **Scalability**: Ensure that your queries are optimized for performance, especially if dealing with a large dataset with millions of reactions.
- **Data Integrity**: If reactions can be deleted or modified, consider how this might affect your calculations and whether you need to account for historical data or use snapshots.

### Real-world Application

- **Content Analysis**: Understanding which reactions are most common for a post can help content creators gauge the sentiment and engagement of their audience.
- **User Engagement**: Analyzing reactions can provide insights into how users interact with different types of content, which can inform future content strategy and platform development.
- **Marketing and Strategy**: By identifying trends in user reactions, companies can tailor their marketing and content strategies to better align with user preferences and emotions.

This approach provides a comprehensive way to analyze user reactions on posts using SQL, offering valuable insights into user engagement and sentiment.
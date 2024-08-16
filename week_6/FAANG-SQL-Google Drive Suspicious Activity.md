### Problem Overview

You might be given tables that record various activities on files, such as access, edits, or shares, and your task could involve identifying patterns that suggest suspicious behavior, such as multiple accesses from different locations, unusually high access frequency, or unexpected file deletions or shares.

### Example Table Structure

Let’s assume you have two tables: `Files` and `FileActivities`.

1. **Files Table**:
    - Contains information about each file stored in Google Drive.
    - Structure:
      ```sql
      CREATE TABLE Files (
          file_id INT PRIMARY KEY,
          file_name VARCHAR(255),
          owner_id INT,
          created_date DATE
      );
      ```

2. **FileActivities Table**:
    - Records activities performed on files, such as access, edits, and shares.
    - Structure:
      ```sql
      CREATE TABLE FileActivities (
          activity_id INT PRIMARY KEY,
          file_id INT,
          user_id INT,
          activity_type VARCHAR(50),  -- e.g., 'access', 'edit', 'share', 'delete'
          activity_date TIMESTAMP,
          location VARCHAR(255)  -- Optional: Record of the IP location
      );
      ```

### Sample Data

Here’s what some sample data might look like:

**Files Table**:
| file_id | file_name        | owner_id | created_date |
|---------|------------------|----------|--------------|
| 1       | ProjectPlan.docx  | 101      | 2024-01-15   |
| 2       | Financials.xlsx   | 102      | 2024-02-20   |
| 3       | Presentation.pptx | 103      | 2024-03-10   |

**FileActivities Table**:
| activity_id | file_id | user_id | activity_type | activity_date        | location       |
|-------------|---------|---------|---------------|----------------------|----------------|
| 1           | 1       | 101     | access        | 2024-08-01 10:00:00  | New York, USA  |
| 2           | 1       | 104     | edit          | 2024-08-01 11:00:00  | San Francisco, USA |
| 3           | 1       | 101     | access        | 2024-08-01 11:05:00  | London, UK     |
| 4           | 2       | 102     | delete        | 2024-08-01 12:00:00  | New York, USA  |
| 5           | 3       | 105     | share         | 2024-08-02 09:00:00  | Chicago, USA   |
| 6           | 1       | 106     | access        | 2024-08-02 09:15:00  | New York, USA  |
| 7           | 1       | 101     | access        | 2024-08-02 10:00:00  | Sydney, Australia |

### Problem Statement

1. **Identify Multiple Accesses from Different Locations**: Detect instances where the same file was accessed by the same user from different locations within a short time frame, which could indicate suspicious activity.
2. **Detect Unusual File Deletions**: Identify cases where a file was deleted by a user who is not the owner of the file.
3. **Find Unusual Sharing Patterns**: Look for files that have been shared multiple times within a short period, which could indicate a security risk.

### Solution Approach

Let’s explore how to solve these problems using SQL.

#### 1. **Identify Multiple Accesses from Different Locations**

To detect instances where the same file was accessed by the same user from different locations within a short time frame, you can compare consecutive access records for the same user and file.

### SQL Query:

```sql
SELECT
    fa1.file_id,
    fa1.user_id,
    fa1.activity_date AS access_time_1,
    fa1.location AS location_1,
    fa2.activity_date AS access_time_2,
    fa2.location AS location_2
FROM
    FileActivities fa1
JOIN
    FileActivities fa2 ON fa1.file_id = fa2.file_id
                       AND fa1.user_id = fa2.user_id
                       AND fa1.activity_type = 'access'
                       AND fa2.activity_type = 'access'
                       AND fa1.activity_date < fa2.activity_date
                       AND TIMESTAMPDIFF(MINUTE, fa1.activity_date, fa2.activity_date) < 60
                       AND fa1.location <> fa2.location
ORDER BY
    fa1.file_id, fa1.user_id, fa1.activity_date;
```

#### Explanation:

- **Self-Join on FileActivities**: The table is joined with itself to compare each access event with subsequent access events for the same user and file.
- **TIMESTAMPDIFF(MINUTE, fa1.activity_date, fa2.activity_date) < 60**: Filters to find access events that occurred within 60 minutes of each other.
- **fa1.location <> fa2.location**: Ensures that the accesses occurred from different locations.
- **ORDER BY**: Orders the results by file ID, user ID, and access time for easier analysis.

**Result for Sample Data**:

For the sample data, this query would identify that user 101 accessed the file "ProjectPlan.docx" from both New York and London within a short time frame, which could be suspicious.

#### 2. **Detect Unusual File Deletions**

To identify cases where a file was deleted by a user who is not the owner, you can filter the `FileActivities` table for delete actions and check against the `Files` table to ensure the user is not the owner.

### SQL Query:

```sql
SELECT
    fa.file_id,
    fa.user_id,
    fa.activity_date,
    f.owner_id
FROM
    FileActivities fa
JOIN
    Files f ON fa.file_id = f.file_id
WHERE
    fa.activity_type = 'delete'
    AND fa.user_id <> f.owner_id
ORDER BY
    fa.activity_date DESC;
```

#### Explanation:

- **JOIN with Files**: Joins the `FileActivities` table with the `Files` table to compare the user who deleted the file with the file owner.
- **fa.user_id <> f.owner_id**: Ensures the user who deleted the file is not the owner.
- **ORDER BY fa.activity_date DESC**: Orders the results by the most recent deletions.

**Result for Sample Data**:

For the sample data, the query would show that user 102 deleted the file "Financials.xlsx," which they do own, so it wouldn't be flagged. If there were a deletion by a non-owner, it would appear here.

#### 3. **Find Unusual Sharing Patterns**

To identify files that have been shared multiple times within a short period, you can count the number of share activities for each file within a certain time frame.

### SQL Query:

```sql
SELECT
    file_id,
    COUNT(*) AS share_count,
    MIN(activity_date) AS first_share_time,
    MAX(activity_date) AS last_share_time
FROM
    FileActivities
WHERE
    activity_type = 'share'
GROUP BY
    file_id
HAVING
    share_count > 3  -- Example threshold
    AND TIMESTAMPDIFF(MINUTE, MIN(activity_date), MAX(activity_date)) < 60
ORDER BY
    share_count DESC;
```

#### Explanation:

- **COUNT(*) AS share_count**: Counts the number of share activities for each file.
- **TIMESTAMPDIFF(MINUTE, MIN(activity_date), MAX(activity_date)) < 60**: Ensures all sharing activities happened within a 60-minute window.
- **HAVING share_count > 3**: Filters to include only files that were shared more than three times in the time frame.

**Result for Sample Data**:

Given the sample data, if any file was shared multiple times within an hour, it would be listed as potentially suspicious.

### Additional Considerations:

- **Time Frame Flexibility**: Depending on the sensitivity of the system, you may want to adjust the time frames (e.g., from 60 minutes to 30 minutes or 24 hours) to capture more or fewer activities.
- **Location Accuracy**: Location data might not always be accurate, so consider cross-referencing with other data (e.g., IP addresses) if available.
- **Performance**: Ensure that indexes are used on key columns like `file_id`, `user_id`, `activity_date`, and `location` to optimize performance, especially with large datasets.

### Real-world Application:

- **Security Monitoring**: Identifying suspicious activities in cloud storage systems is critical for preventing data breaches, unauthorized access, and ensuring compliance with security policies.
- **Anomaly Detection**: These queries can be part of a broader anomaly detection system that continuously monitors user behavior for potential security threats.
- **Incident Response**: If suspicious activity is detected, it can trigger alerts for further investigation, helping to mitigate potential risks before they escalate.

This approach provides a structured way to detect and analyze suspicious activities in Google Drive (or any similar cloud storage system) using SQL, enhancing the security and integrity of the platform.
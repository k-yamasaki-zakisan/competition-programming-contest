-- https://leetcode.com/problems/user-activity-for-the-past-30-days-i/
-- Runtime: 1223 ms, faster than 5.01% of MySQL online submissions for User Activity for the Past 30 Days I.
-- Memory Usage: 0B, less than 100.00% of MySQL online submissions for User Activity for the Past 30 Days I.

-- Write your MySQL query statement below
SELECT
    activity_date as day,
    count(DISTINCT user_id) as active_users
FROM Activity
WHERE DATE_FORMAT("2019-06-28", '%Y-%m-%d') <= activity_date and activity_date <= DATE_FORMAT("2019-07-27", '%Y-%m-%d')
GROUP BY activity_date;
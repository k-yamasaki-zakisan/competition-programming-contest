-- https://leetcode.com/problems/duplicate-emails/
-- Runtime: 323 ms, faster than 46.63% of MySQL online submissions for Duplicate Emails.
-- Memory Usage: 0B, less than 100.00% of MySQL online submissions for Duplicate Emails.

SELECT Email
FROM Person
GROUP BY Email
HAVING 1<count(Email);
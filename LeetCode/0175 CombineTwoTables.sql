-- https://leetcode.com/problems/combine-two-tables/
-- Runtime: 321 ms, faster than 46.90% of MySQL online submissions for Combine Two Tables.
-- Memory Usage: 0B, less than 100.00% of MySQL online submissions for Combine Two Tables.

SELECT p.FirstName, p.LastName, a.City, a.State
From Person AS p
LEFT JOIN Address AS a
ON p.PersonId = a.PersonId;
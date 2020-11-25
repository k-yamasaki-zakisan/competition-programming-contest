-- https://leetcode.com/problems/second-highest-salary/
-- Runtime: 155 ms, faster than 99.00% of MySQL online submissions for Second Highest Salary.
-- Memory Usage: 0B, less than 100.00% of MySQL online submissions for Second Highest Salary.

SELECT MAX( Salary ) AS SecondHighestSalary
FROM Employee
WHERE Salary < ( SELECT MAX( Salary ) FROM Employee );
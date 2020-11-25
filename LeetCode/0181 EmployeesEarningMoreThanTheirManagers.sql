-- https://leetcode.com/problems/employees-earning-more-than-their-managers/
-- Runtime: 317 ms, faster than 69.91% of MySQL online submissions for Employees Earning More Than Their Managers.
-- Memory Usage: 0B, less than 100.00% of MySQL online submissions for Employees Earning More Than Their Managers.

SELECT b.Name AS 'Employee'
FROM Employee AS a, Employee AS b
WHERE a.Id = b.ManagerId and a.Salary < b.Salary;
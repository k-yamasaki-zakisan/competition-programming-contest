-- https://leetcode.com/problems/customers-who-never-order/
-- Runtime: 483 ms, faster than 34.59% of MySQL online submissions for Customers Who Never Order.
-- Memory Usage: 0B, less than 100.00% of MySQL online submissions for Customers Who Never Order.

SELECT c.Name AS 'Customers'
FROM Customers AS c
LEFT JOIN Orders AS o
ON c.ID = o.CustomerId
WHERE o.CustomerId IS null;
-- https://leetcode.com/problems/big-countries/
-- Runtime: 237 ms, faster than 58.38% of MySQL online submissions for Big Countries.
-- Memory Usage: 0B, less than 100.00% of MySQL online submissions for Big Countries.

SELECT name, population, area
FROM World
WHERE population>25000000 OR area>3000000;
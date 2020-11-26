-- https://leetcode.com/problems/rising-temperature/
-- Runtime: 271 ms, faster than 98.19% of MySQL online submissions for Rising Temperature.
-- Memory Usage: 0B, less than 100.00% of MySQL online submissions for Rising Temperature.

SELECT w1.Id As 'id' 
FROM Weather AS w1
INNER JOIN Weather w2 
ON w1.recordDate = DATE_ADD(w2.recordDate, INTERVAL 1 DAY)
AND w1.Temperature > w2.Temperature;
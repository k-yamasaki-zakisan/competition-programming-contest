-- https://leetcode.com/problems/rank-scores/
-- Runtime: 219 ms, faster than 92.54% of MySQL online submissions for Rank Scores.
-- Memory Usage: 0B, less than 100.00% of MySQL online submissions for Rank Scores.

SELECT SCORE, DENSE_RANK() OVER (ORDER BY SCORE DESC) 'Rank'
FROM SCORES
ORDER BY SCORE DESC;
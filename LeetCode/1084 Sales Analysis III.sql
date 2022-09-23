-- https://leetcode.com/problems/sales-analysis-iii/
-- Runtime: 1823 ms, faster than 22.40% of MySQL online submissions for Sales Analysis III.
-- Memory Usage: 0B, less than 100.00% of MySQL online submissions for Sales Analysis III.

-- Write your MySQL query statement below
SELECT P.product_id, P.product_name
FROM Product as P
    LEFT JOIN Sales AS S ON P.product_id = S.product_id
WHERE '2019-01-01' <= S.sale_date and S.sale_date <= '2019-03-31' and P.product_id NOT IN(
    SELECT product_id
    FROM Sales
    WHERE sale_date < '2019-01-01' or '2019-03-31' < sale_date
)
GROUP BY P.product_id;
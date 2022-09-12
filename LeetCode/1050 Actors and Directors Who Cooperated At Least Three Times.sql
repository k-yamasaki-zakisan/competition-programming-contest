-- https://leetcode.com/problems/actors-and-directors-who-cooperated-at-least-three-times/
-- Runtime: 457 ms, faster than 50.12% of MySQL online submissions for Actors and Directors Who Cooperated At Least Three Times.
-- Memory Usage: 0B, less than 100.00% of MySQL online submissions for Actors and Directors Who Cooperated At Least Three Times.

-- Write your MySQL query statement below
SELECT actor_id, director_id
FROM ActorDirector
GROUP BY actor_id, director_id
HAVING 3 <= count(actor_id);
# https://leetcode.com/problems/possible-bipartition/
# Runtime: 668 ms, faster than 97.31% of Python3 online submissions for Possible Bipartition.
# Memory Usage: 19.2 MB, less than 99.30% of Python3 online submissions for Possible Bipartition.

class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        g = [[] for _ in range(N+1)]
        color = [1] + [-1]*N
        for u, v in dislikes:
            g[u].append(v)
            g[v].append(u)

        def bfs(node):
            color[node] = 0
            q = collections.deque([node])

            while q:
                cur = q.popleft()
                for neighbor in g[cur]:
                    if color[neighbor] == -1:
                        color[neighbor] = 1 - color[cur]
                        q.append(neighbor)
                    elif color[neighbor] == color[cur]:
                        return False
            return True
        return all(bfs(node) for node in range(1, N+1) if color[node] == -1)

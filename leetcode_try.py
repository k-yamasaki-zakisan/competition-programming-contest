from typing import List, Optional
from collections import defaultdict, deque

# from collections import Counter
# from collections import defaultdict
# from bisect import bisect_right
# from copy import copy
# from collections import deque


class Solution:
    def isEscapePossible(
        self, blocked: List[List[int]], source: List[int], target: List[int]
    ) -> bool:
        from collections import deque

        blocks = set([(a, b) for a, b in blocked])
        max_num = 10**6

        def bfs(sh, sw, gh, gs):
            pos = deque([[sh, sw]])
            visited = set([(sh, sw)])
            cnt = 0
            while pos and cnt < 200:
                nowh, noww = pos.popleft()
                if nowh == gh and noww == gs:
                    return True
                for nexth, nextw in [
                    [nowh + 1, noww],
                    [nowh - 1, noww],
                    [nowh, noww + 1],
                    [nowh, noww - 1],
                ]:
                    if (
                        0 <= nexth < max_num
                        and 0 <= nextw < max_num
                        and (nexth, nextw) not in blocks
                        and (nexth, nextw) not in visited
                    ):
                        visited.add((nexth, nextw))
                        pos.append((nexth, nextw))
                cnt += 1
                if len(pos) == 0:
                    return False
            return True

        return bfs(source[0], source[1], target[0], target[1]) and bfs(
            target[0], target[1], source[0], source[1]
        )


S = Solution()
blocked = []
source = [0, 0]
target = [999999, 999999]
print(S.isEscapePossible(blocked, source, target))

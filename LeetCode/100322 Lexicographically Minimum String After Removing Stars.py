class Solution:
    def clearStars(self, s: str) -> str:
        from heapq import heapify, heappop, heappush
        from collections import defaultdict

        char_memo = []
        char_point = defaultdict(list)
        remove_memo = set()
        n = len(s)
        for i in range(n):
            if s[i] != "*":
                heappush(char_memo, s[i])
                char_point[s[i]].append(i)
            if s[i] == "*" and len(char_memo):
                c = heappop(char_memo)
                target_i = char_point[c].pop()
                remove_memo.add(target_i)
        ans = ""
        for i in range(n):
            if s[i] != "*" and i not in remove_memo:
                ans += s[i]
        return ans

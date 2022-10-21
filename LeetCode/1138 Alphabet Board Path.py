# https://leetcode.com/problems/alphabet-board-path/
# Runtime: 179 ms, faster than 5.19% of Python3 online submissions for Alphabet Board Path.
# Memory Usage: 13.9 MB, less than 36.31% of Python3 online submissions for Alphabet Board Path.


class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        from collections import deque

        alph_num = {chr(ord("a") + i): i for i in range(26)}
        board = [
            list("abcde"),
            list("fghij"),
            list("klmno"),
            list("pqrst"),
            list("uvwxy"),
            ["z"],
        ]
        memo = [[-1] * 26 for _ in range(26)]

        for h in range(6):
            for w in range(5):
                if h == 5 and 0 < w:
                    continue
                start = alph_num[board[h][w]]
                memo[start][start] = ""
                stack = deque([[h, w]])
                visit = [[False] * 5 for _ in range(5)]
                visit.append([False])
                visit[h][w] = True
                while len(stack):
                    now_h, now_w = stack.popleft()
                    ex_code = memo[start][alph_num[board[now_h][now_w]]]
                    if now_h == 4 and now_w == 0 and not visit[now_h + 1][now_w]:
                        visit[now_h + 1][now_w] = True
                        t = alph_num[board[now_h + 1][now_w]]
                        memo[start][t] = ex_code + "D"
                        stack.append((now_h + 1, now_w))
                    if (
                        0 <= now_h + 1 < 5
                        and 0 <= now_w < 5
                        and not visit[now_h + 1][now_w]
                    ):
                        visit[now_h + 1][now_w] = True
                        t = alph_num[board[now_h + 1][now_w]]
                        memo[start][t] = ex_code + "D"
                        stack.append((now_h + 1, now_w))
                    if (
                        0 <= now_h - 1 < 5
                        and 0 <= now_w < 5
                        and not visit[now_h - 1][now_w]
                    ):
                        visit[now_h - 1][now_w] = True
                        t = alph_num[board[now_h - 1][now_w]]
                        memo[start][t] = ex_code + "U"
                        stack.append((now_h - 1, now_w))
                    if (
                        0 <= now_h < 5
                        and 0 <= now_w + 1 < 5
                        and not visit[now_h][now_w + 1]
                    ):
                        visit[now_h][now_w + 1] = True
                        t = alph_num[board[now_h][now_w + 1]]
                        memo[start][t] = ex_code + "R"
                        stack.append((now_h, now_w + 1))
                    if (
                        0 <= now_h < 5
                        and 0 <= now_w - 1 < 5
                        and not visit[now_h][now_w - 1]
                    ):
                        visit[now_h][now_w - 1] = True
                        t = alph_num[board[now_h][now_w - 1]]
                        memo[start][t] = ex_code + "L"
                        stack.append((now_h, now_w - 1))
        ans = ""
        now = "a"
        for i, t in enumerate(target):
            if 0 < i:
                ans += "!"
            ans += memo[alph_num[now]][alph_num[t]]
            now = t
        return ans + "!"

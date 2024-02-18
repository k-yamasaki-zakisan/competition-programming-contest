from typing import List
import math


class Solution:
    def mostFrequentPrime(self, mat: List[List[int]]) -> int:
        from collections import defaultdict

        def is_prime(n):
            if n == 1:
                return False

            for k in range(2, int(math.sqrt(n)) + 1):
                if n % k == 0:
                    return False

            return True

        cnt_memo = defaultdict(int)
        not_prime_list = set()
        m, n = len(mat), len(mat[0])
        for i in range(m):
            for j in range(n):
                for next_add_h, next_add_w in [
                    [1, 1],
                    [1, 0],
                    [1, -1],
                    [0, 1],
                    [0, -1],
                    [-1, 1],
                    [-1, 0],
                    [-1, -1],
                ]:
                    now_h, now_w = i, j
                    tmp = str(mat[now_h][now_w])
                    while 0 <= now_h + next_add_h < m and 0 <= now_w + next_add_w < n:
                        now_h += next_add_h
                        now_w += next_add_w
                        tmp += str(mat[now_h][now_w])
                        if tmp in cnt_memo:
                            cnt_memo[tmp] += 1
                        elif tmp in not_prime_list:
                            continue
                        else:
                            if is_prime(int(tmp)):
                                cnt_memo[tmp] += 1
                            else:
                                not_prime_list.add(tmp)
                        # print(cnt_memo, i, j, now_h, now_w, next_add_h, next_add_w)
        max_val = -1
        for key, val in cnt_memo.items():
            max_val = max(max_val, val)
        max_key = 0
        for key, val in cnt_memo.items():
            if max_val == val:
                max_key = max(int(max_key), int(key))
        return max_key if max_val != -1 else -1

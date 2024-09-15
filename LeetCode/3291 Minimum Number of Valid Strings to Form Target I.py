from collections import deque
from typing import List


class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        words.sort()
        new_words = []
        for i in range(len(words)):
            flag = True
            for j in range(i + 1, len(words)):
                if words[i] == words[j][: len(words[i])]:
                    flag = False
                    break
            if flag:
                new_words.append(words[i])

        n = len(target)
        distance_cnt = [-1] * (n + 1)
        distance_cnt[0] = 0
        stack = deque([0])
        while len(stack):
            now = stack.popleft()
            for word in new_words:
                plus = 0
                j = 0
                while (
                    now + plus < n
                    and j + plus < len(word)
                    and word[j + plus] == target[now + plus]
                ):
                    if distance_cnt[now + plus + 1] == -1:
                        distance_cnt[now + plus + 1] = distance_cnt[now] + 1
                        stack.append(now + plus + 1)
                        if now + plus + 1 == n:
                            return distance_cnt[now + plus + 1]
                    plus += 1
        return -1

from typing import List

# from collections import Counter
# from collections import defaultdict
# from bisect import bisect_right
# from copy import copy
# from collections import deque


def deckRevealedIncreasing(deck: List[int]) -> str:
    from collections import deque

    N = len(deck)
    index = deque(range(N))
    ans = [None] * N

    for card in sorted(deck):
        ans[index.popleft()] = card
        if index:
            index.append(index.popleft())

    return ans


deck = [17, 13, 11, 2, 3, 5, 7]
print(deckRevealedIncreasing(deck))

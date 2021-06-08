# https://atcoder.jp/contests/typical90/tasks/typical90_bi

from collections import deque

Q = int(input())
TX = [list(map(int, input().split())) for _ in range(Q)]
cards = deque([])
for t, x in TX:
    if t == 1:
        cards.appendleft(x)
    elif t == 2:
        cards.append(x)
    else:
        print(cards[x-1])

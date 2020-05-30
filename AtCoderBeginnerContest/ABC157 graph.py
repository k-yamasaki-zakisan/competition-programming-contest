#https://atcoder.jp/contests/abc157/tasks/abc157_d

import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
friends_table = [[] for i in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    friends_table[a-1] += [b-1]
    friends_table[b-1] += [a-1]

group_list = [i for i in range(N)]
friends_candidate = [[] for i in range(N)]

for i in range(N):
    # すでにDFS済み
    if i != group_list[i]:
        continue
    next_stack = [i]
    friend = [i]
    while next_stack:
        u = next_stack.pop(-1)
        for v in friends_table[u]:
            # 訪問済み
            if i == group_list[v]:
                continue
            friend += [v]
            group_list[v] = i
            next_stack += [v]
    for f in friend:
        friends_candidate[f] = friend

blocks_table = [[] for i in range(N)]
for _ in range(K):
    a, b = map(int, input().split())
    if group_list[a-1] == group_list[b-1]:
        blocks_table[a-1] += [b-1]
        blocks_table[b-1] += [a-1]

for i in range(N):
    print(len(friends_candidate[i]) - len(friends_table[i]) - len(blocks_table[i])-1)

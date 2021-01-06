# https://atcoder.jp/contests/arc011/tasks/arc011_3

from collections import deque

first, last = map(str, input().split())

N = int(input())
S = [first]+[input() for _ in range(N)]+[last]

if first == last:
    print(0)
    print(first)
    print(last)
    exit()

graph = [[] for _ in range(N+2)]
for i in range(N+1):
    for j in range(i+1, N+2):
        tmp = 0
        for k in range(len(first)):
            if S[i][k] != S[j][k]:
                tmp += 1
        if tmp == 1:
            graph[i].append(j)
            graph[j].append(i)

visited = [-1] * (N+2)
visited[0] = [0]

stack = deque([0])

while len(stack):
    p = stack.popleft()
    for i in graph[p]:
        if visited[i] == -1:
            visited[i] = visited[p]+[i]
            stack.append(i)

if visited[-1] != -1:
    print(len(visited[-1])-2)
    for i in visited[-1]:
        print(S[i].strip())
else:
    print(-1)

# https://atcoder.jp/contests/typical90/tasks/typical90_c

from collections import deque
N = int(input())
AB = [list(map(int, input().split())) for _ in range(N-1)]
root = [[] for i in range(N)]
for a, b in AB:
    a, b = a-1, b-1
    root[a].append(b)
    root[b].append(a)


def getDistances(start: int) -> list:
    distances = [-1]*N
    distances[start] = 0
    stack = deque([start])
    while len(stack) > 0:
        v = stack.popleft()
        for i in root[v]:
            if distances[i] == -1:
                distances[i] = distances[v]+1
                stack.append(i)
    return distances


tmp_distances = getDistances(0)
max_distance_point = tmp_distances.index(max(tmp_distances))
distances = getDistances(max_distance_point)
print(max(distances)+1)

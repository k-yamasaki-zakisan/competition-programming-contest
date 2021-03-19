# https://atcoder.jp/contests/arc028/tasks/arc028_2

from heapq import heappop, heapify, heappush
N, K = map(int, input().split())
X = list(map(int, input().split()))

conversion_table = {}
for i, x in enumerate(X):
    conversion_table[x] = i+1

tmp_X = [-x for x in X[:K]]
heapify(tmp_X)
x = -tmp_X[0]
print(conversion_table[x])

for i in range(K, N):
    heappush(tmp_X, -X[i])
    heappop(tmp_X)
    print(conversion_table[-tmp_X[0]])

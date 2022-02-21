# 一個だけ数字
n = int(input())

# 文字列のインプット
s = input()

# 個数がわかっている場合
x, y = map(int, input().split())
print(x, y)
# =>x y

# n個の文字列のインプット
# 1 2 3 4 5 ... n
t = input().split()
["1", "2", "3", ..., "n"]

# 1 2 3 4 5 ... n
t = list(map(int, input().split()))
[1, 2, 3, 4, 5, ..., n]

# 一重配列
dp = [0 for j in range(10)]

# 二重配列
dp = [[0 for i in range(10)] for j in range(10)]

# 二重配列でデータの取り込み
h, n = (int(x) for x in input().split())
ab = []
for _ in range(n):
    a, b = (int(x) for x in input().split())
    ab.append([a, b])

# 二重配列でデータの取り込み
N = int(input())
a = [int(i) for i in input().split()]

# モッド
mod = 1000000007


# ループ文
for i in range(5):
    print(i)
0
1
2
3
4

# for文の中断、スキップ（break、continue）

# インデックス
for ix, val in enumerate(["りんご", "ゴリラ", "ライオン"]):
    print("インデックスは{},要素は{}".format(ix, val))

# インデックスは0,要素はりんご
# インデックスは1,要素はゴリラ
# インデックスは2,要素はライオン

# ソート
# org_list.sort()

# ゼロ埋め・幅寄せ
print(str(29).rjust(10, "0"))  # 10桁ゼロ埋め
# 0000000029

# 配列一列表示
print(" ".join(map(str, dp)))

# 配列の要素を追加
l = list(range(3))
print(l)
# =>[0, 1, 2]
l.append(100)
print(l)
# =>[0, 1, 2, 100]

# アルファベット作成
print([chr(ord("a") + i) for i in range(26)])
# => ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


root = [[] for i in range(n)]

pi = 3.141592
# 今回は引数に数値を代入した変数を渡します。
print("{:.1f}".format(pi))  # 小数点以下1位
print("{:.2f}".format(pi))  # 小数点以下2位
print("{:.3f}".format(pi))  # 小数点以下3位

# ナップサック問題(Atcoder 153 E)
h, n = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]
dp = [0] * (h + 1)
for i in range(0, h + 1):
    if i == 0:
        dp[i] = 0
    else:
        dp[i] = min(dp[i - a] + b for a, b in ab)
print(dp[h])

# ナップサック問題
h, n = (int(x) for x in input().split())
dp = [[0 for i in range(n + 1)] for j in range(h + 1)]
for i in range(h):
    a, b = (int(x) for x in input().split())
    for j in range(n + 1):
        if j < b:
            dp[i + 1][j] = dp[i][j]
        else:
            dp[i + 1][j] = max([dp[i][j], dp[i][j - b] + a])
print(max(list(itertools.chain.from_iterable(dp))))

# 二重配列の平坦化
l_2d = [[0, 1], [2, 3]]
print(list(itertools.chain.from_iterable(l_2d)))
# [0, 1, 2, 3]


# 最小公倍数(3.8var)
import math
from functools import reduce


def lcm_base(x, y):
    return (x * y) // math.gcd(x, y)


def lcm(*numbers):
    return reduce(lcm_base, numbers, 1)


def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)


print(lcm(27, 9, 3))
# 27
print(lcm_list([27, 9, 3]))
# 27

# 最大公約数
import math
from functools import reduce


def gcd(*numbers):
    return reduce(math.gcd, numbers)


def gcd_list(numbers):
    return reduce(math.gcd, numbers)


print(gcd(27, 18, 9, 3))
# 3
print(gcd_list([27, 18, 9, 3]))
# 3


# ダイグスラスト法
# 最小公倍数(3.4var)
def lcm(a):
    from fractions import gcd

    x = a[0]
    for i in range(1, len(a)):
        x = (x * a[i]) // gcd(x, a[i])
    return x


a = [3, 4, 6]
print(lcm(a))  # 実行結果: 12

# 最大公約数(3.4var)
from fractions import gcd

a = [27, 18, 9, 3]
x = a[0]
for i in range(1, len(a)):
    x = gcd(x, a[i])

print(x)
# 3


n, m, t = map(int, input().split())
A = list(map(int, input().split()))
abc = [list(map(int, input().split())) for _ in range(m)]

import heapq


def dij(cost, start):
    d = [float("inf")] * n  # 最短距離
    d[start] = 0

    q = [(d[start], start)]  # min-heap, (距離, 頂点)
    heapq.heapify(q)
    while q:
        # print(q)
        du, u = heapq.heappop(q)  # 最短距離とその頂点
        if d[u] < du:
            continue
        for v, weight in cost[u]:
            if du + weight < d[v]:
                d[v] = du + weight
                heapq.heappush(q, (d[v], v))
    return d


# コストテーブルの作成
cost1 = [[] for _ in range(n)]
for i, j, k in abc:
    cost1[i - 1].append((j - 1, k))
cost2 = [[] for _ in range(n)]
for i, j, k in abc:
    cost2[j - 1].append((i - 1, k))


d1 = dij(cost1, 0)
d2 = dij(cost2, 0)

ans = 0
for i in range(n):
    d = d1[i] + d2[i]
    ans = max(ans, (t - d) * A[i])

print(ans)

# ループインデックス
for i, name in enumerate(l, 42):
    print(i, name)
# 42 Alice
# 43 Bob
# 44 Charlie

# 二次元ソート
# 5
# 2 4
# 1 9
# 1 8
# 4 9
# 3 12
n = int(input())
ab = []
for _ in range(n):
    a, b = (int(x) for x in input().split())
    ab.append([a, b])
ab = sorted(ab, key=lambda x: x[1])
print(ab)
[[2, 4], [1, 8], [1, 9], [4, 9], [3, 12]]

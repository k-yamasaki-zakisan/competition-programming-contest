# https://atcoder.jp/contests/abc251/tasks/abc251_e

"""
問題文
高橋君と N 匹の動物がいます。 N 匹の動物はそれぞれ動物 1 、動物 2 、… 、動物 N と呼ばれます。
高橋君は下記の N 種類の行動をそれぞれ好きな回数だけ（ 0 回でも良い）行います。
A 1 円払い、動物 1 と動物 2 に餌をあげる。
A 2 円払い、動物 2 と動物 3 に餌をあげる。
...
A N−1 円払い、動物 (N−1) と動物 N に餌をあげる。
A N 円払い、動物 N と動物 1 に餌をあげる。

上記の N 種類目の行動では、「動物 N と動物 1 に」餌をあげることに注意してください。

すべての動物にそれぞれ 1 回以上餌をあげるまでにかかる費用の合計として考えられる最小値を出力してください。

制約
2 ≤ N ≤ 3×10^5
1≤ Ai ≤10^9
入力はすべて整数
"""

INF = float("inf")

N = int(input())
A = list(map(int, input().split()))

dp1 = 0
dp2 = INF
for i in range(N):
    a = A[i]
    dp1, dp2 = dp2, min(dp1, dp2) + a

ans = min(dp1, dp2)

dp1 = INF
dp2 = A[-1]
for i in range(N - 1):
    a = A[i]
    dp1, dp2 = dp2, min(dp1, dp2) + a

ans = min(ans, dp1, dp2)

print(ans)

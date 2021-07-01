# https://atcoder.jp/contests/typical90/tasks/typical90_cc

N, K = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]
HW = [[0]*5011 for _ in range(5011)]
S = [[0]*5011 for _ in range(5011)]
for a, b in AB:
    HW[a][b] += 1

for h in range(5010):
    for w in range(5010):
        S[h][w] = S[h][w-1] + S[h-1][w] - S[h-1][w-1] + HW[h][w]

ans = 0
for h in range(1, 5005-K):
    for w in range(1, 5005-K):
        tmp = S[h+K][w+K]+S[h-1][w-1]-S[h-1][w+K]-S[h+K][w-1]
        ans = max(ans, tmp)
print(ans)

# https://atcoder.jp/contests/typical90/tasks/typical90_f

N, K = map(int, input().split())
S = input()

S_number = [ord(s)-97 for i, s in enumerate(S)]
nex = [[N]*26 for _ in range(100009)]

# 前計算
for i in range(N-1, -1, -1):
    for j in range(26):
        if S_number[i] == j:
            nex[i][j] = i
        else:
            nex[i][j] = nex[i + 1][j]

# 一文字ずつ貪欲に決める
ans = ""
CurrentPos = 0
for i in range(1, K+1):
    for j in range(26):
        NexPos = nex[CurrentPos][j]
        MaxPossibleLength = (N - NexPos - 1) + i
        if K <= MaxPossibleLength:
            ans += (chr(ord('a')+j))
            CurrentPos = NexPos + 1
            break
print(ans)

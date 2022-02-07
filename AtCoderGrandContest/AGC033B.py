# https://atcoder.jp/contests/agc033/tasks/agc033_b

H, W, N = [int(i) for i in input().split()]
sr, sc = [int(i) for i in input().split()]
S = input()
T = input()

l = sc
r = sc
u = sr
d = sr

flag = True
for i in range(N):
    if S[i] == "R":
        r += 1
    if S[i] == "L":
        l -= 1
    if S[i] == "U":
        u -= 1
    if S[i] == "D":
        d += 1
    if l == 0 or r == W+1 or u == 0 or d == H+1:
        flag = False
        break
    if T[i] == "R" and l != W:
        l += 1
    if T[i] == "L" and r != 1:
        r -= 1
    if T[i] == "U" and d != 1:
        d -= 1
    if T[i] == "D" and u != H:
        u += 1

if flag:
    print("YES")
else:
    print("NO")

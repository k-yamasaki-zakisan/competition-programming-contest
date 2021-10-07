# https://atcoder.jp/contests/arc125/tasks/arc125_a

N, M = map(int, input().split())
S = list(map(int, input().split()))
T = list(map(int, input().split()))
set_s = set(S)
set_t = set(T)
for t in set_t:
    if t not in set_s:
        print(-1)
        exit()
if len(set_t) == 1:
    p = 10**10
    for i in range(N):
        if T[0] == S[i]:
            p = min(i, p)
            break
    for i in range(N):
        if T[0] == S[-1-i]:
            p = min(p, i+1)
    print(p+M)
else:
    p = 10**10
    for i in range(N-1):
        if S[i+1] != S[i]:
            p = min(i, p)
            break
    for i in range(N-1):
        if S[-1-i] != S[-i]:
            p = min(p, i)
    ans = 0
    if T[0] == S[p]:
        ans += p+1
    else:
        ans += p+2
    for i in range(1, M):
        if T[i] == T[i-1]:
            ans += 1
        else:
            ans += 2
    print(ans)

#https://atcoder.jp/contests/arc104/tasks/arc104_b

N,S = map(str,input().split())
N = int(N)
S = list(S)
ans = 0
for i in range(N-1):
    AT = [0,0]
    CG = [0,0]
    for j in range(i,N):
        if S[j] == 'A':
            AT[0] += 1
        elif S[j] == 'T':
            AT[1] += 1
        if S[j] == 'C':
            CG[0] += 1
        if S[j] == 'G':
            CG[1] += 1
        if AT[0] == AT[1] and CG[0] == CG[1]:
            ans += 1
print(ans)

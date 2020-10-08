#https://atcoder.jp/contests/yahoo-procon2017-qual/tasks/yahoo_procon2017_qual_c

N,K = map(int,input().split())
A = list(map(int,input().split()))
aa = [0 for i in range(N)]
for i in range(K):
    aa[A[i]-1] = 1
#検索対象
S = []
#検索対象外
T = []
for i in range(N):
    if aa[i] == 1:
        S.append(input())
    else:
        T.append(input())

kk = float('inf')
for i in range(len(S)):
    l = 0
    for j in range(min(len(S[0]), len(S[i]))):
        if S[0][j] == S[i][j]:
            l += 1
        else:
            break
    kk = min(kk, l)

ll = -1
for i in range(len(T)):
    l = 0
    for j in range(min(len(S[0]),len(T[i]))):
        if S[0][j] == T[i][j]:
            l += 1
        else:
            break
    ll = max(ll, l)

print(S[0][:ll+1] if kk>ll else -1)

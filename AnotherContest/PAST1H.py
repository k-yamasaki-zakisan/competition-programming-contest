# https://atcoder.jp/contests/past201912-open/tasks/past201912_h

N = int(input())
C = list(map(int,input().split()))
Q = int(input())
S = [list(map(int,input().split())) for _ in range(Q)]
total_min = min(C)
kisu_min = 10**10
for i in range(0,N,2):
    kisu_min = min(kisu_min, C[i])
ans = 0
kisu_dis = 0
total_dis = 0
dis_kisu = [0]*N
dis_total = [0]*N
for s in S:
    if s[0] == 1:
        s1,s2 = s[1]-1,s[2]
        if s1%2==0 and dis_kisu[s1] != kisu_dis:
            C[s1] -= kisu_dis-dis_kisu[s1]
            dis_kisu[s1] = kisu_dis
        if dis_total[s1] != total_dis:
            C[s1] -= total_dis-dis_total[s1]
            dis_total[s1] = total_dis
        if s2 <= C[s1]:
            C[s1] -= s2
            ans += s2
            total_min = min(total_min,C[s1])
            if s1%2 == 0:
                kisu_min = min(kisu_min,C[s1])
    elif s[0] == 2:
        if s[1] <= kisu_min:
            kisu_min -= s[1]
            total_min = min(total_min,kisu_min)
            ans += s[1]*(N//2+N%2)
            kisu_dis += s[1]
    else:
        if s[1] <= total_min:
            total_min -= s[1]
            kisu_min -= s[1]
            ans += s[1]*N
            total_dis += s[1]
print(ans)
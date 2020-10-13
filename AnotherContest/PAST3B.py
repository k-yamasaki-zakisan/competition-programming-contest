#https://atcoder.jp/contests/past202005-open/tasks/past202005_b

N,M,Q = map(int,input().split())
point = [N]*M
man_p = [[0]*M for _ in range(N)]
for i in range(Q):
    S = list(map(int,input().split()))
    if S[0] == 2:
        man, ans = S[1]-1, S[2]-1
        point[ans] -= 1
        man_p[man][ans] = point[ans]
    else:
        man = S[1]-1
        for j in range(M):
            if 0 < man_p[man][j]:
                man_p[man][j] = point[j]
        print(sum(man_p[man]))
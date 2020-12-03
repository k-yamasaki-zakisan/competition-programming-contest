# https://atcoder.jp/contests/arc040/tasks/arc040_c

N = int(input())
S = [list(input()) for _ in range(N)]
check = [[0]*N for _ in range(N)]
ans = 0
for h in range(N):
    for w in range(N-1,-1,-1):
        if S[h][w] == '.' and check[h][w] == 0:
            ans += 1
            nw = w
            nh = h
            while 0 <= nw:
                check[nh][nw] = 1
                nw -= 1
            nw = w
            nh = h+1
            if nh < N:
                while nw < N:
                    check[nh][nw] = 1
                    nw += 1
print(ans)
# https://atcoder.jp/contests/past202104-open/tasks/past202104_f

N, L, T, X = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]
load = 0
ans = 0
for a, b in AB:
    if L <= b and T < a:
        print('forever')
        exit()
    if b < L:
        ans += a
        load = 0
    elif L <= b:
        if T < load + a:
            ans += T-load+X+a
            load = a
            if a == T:
                ans += X
                load = 0
        elif T == load + a:
            ans += X+a
            load = 0
        else:
            ans += a
            load += a
print(ans)

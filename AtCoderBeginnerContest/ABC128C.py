#https://atcoder.jp/contests/abc128/tasks/abc128_c

N, M = map(int, input().split())
bulbs = []
for _ in range(M):
    b = tuple(map(int, input().split()))
    bulbs.append(b[1:])
P = list(map(int, input().split()))

ans = 0
for switch in range(2**N):
    check = [False] * M
    for i ,bulb in enumerate(bulbs):
        count = 0
        for b in bulb:
            if switch >> (b-1) & 1:
                count += 1
        if count % 2 ==P[i]:
            check[i] = True
        else:
            check[i] = False
    if all(check):
        ans += 1
print(ans)

# https://atcoder.jp/contests/past202104-open/tasks/past202104_j

N, C = map(int, input().split())
XY = [list(map(int, input().split())) for _ in range(N)]
# xの平均を算出
p = sum([x for x, y in XY])/N
ans = sum([(p-x)**2+(C-y)**2 for x, y in XY])
print(ans)

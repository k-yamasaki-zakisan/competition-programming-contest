# https://atcoder.jp/contests/arc118/tasks/arc118_c

N = int(input())
component = [6, 10, 15]
i = 1
ans = set()
while len(ans) <= N:
    for c in component:
        tmp_c = c*i
        if tmp_c <= 10000:
            ans.add(tmp_c)
    i += 1
ans = list(ans)
print(*ans[:N])

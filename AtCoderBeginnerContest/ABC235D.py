# https://atcoder.jp/contests/abc235/tasks/abc235_d

from collections import deque

A, N = map(int, input().split())
max_keta = len(str(N))
pool = set()
pool.add(1)
stack = deque([(1, 0)])
while len(stack):
    now, cnt = stack.popleft()
    if now == N:
        print(cnt)
        exit()
    now_a = now*A
    if now_a not in pool and len(str(now_a)) <= max_keta:
        pool.add(now_a)
        stack.append((now_a, cnt+1))
    if now % 10:
        str_now = str(now)
        n_now = int(str_now[-1]+str_now[:-1])
        if n_now not in pool and len(str(n_now)) <= max_keta:
            pool.add(n_now)
            stack.append((n_now, cnt+1))
    # print(pool, stack)
print(-1)

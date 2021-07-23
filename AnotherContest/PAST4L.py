# https://atcoder.jp/contests/past202010-open/tasks/past202010_l


from collections import defaultdict

N, Q = map(int, input().split())
H = list(map(int, input().split()))
Querys = [list(map(int, input().split())) for _ in range(Q)]
odd_diffs = defaultdict(int)
even_diffs = defaultdict(int)
for i in range(N-1):
    d = H[i+1]-H[i]
    if i % 2:
        even_diffs[d] += 1
    else:
        odd_diffs[d] += 1
g = 0
for q in Querys:
    if q[0] == 1:
        g += q[1]
    elif q[0] == 2:
        g -= q[1]
    else:
        u, v = q[1]-1, q[2]
        if u % 2:
            if u:
                odd_diffs[H[u] - H[u-1]] -= 1
            if u < N-1:
                even_diffs[H[u+1] - H[u]] -= 1
            H[u] += v
            if u:
                odd_diffs[H[u] - H[u-1]] += 1
            if u < N-1:
                even_diffs[H[u+1] - H[u]] += 1
        else:
            if u:
                even_diffs[H[u] - H[u-1]] -= 1
            if u < N-1:
                odd_diffs[H[u+1] - H[u]] -= 1
            H[u] += v
            if u:
                even_diffs[H[u] - H[u-1]] += 1
            if u < N-1:
                odd_diffs[H[u+1] - H[u]] += 1
    print(odd_diffs[g]+even_diffs[-g])

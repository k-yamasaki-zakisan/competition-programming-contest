# https://atcoder.jp/contests/abc195/tasks/abc195_d

N, M, Q = map(int, input().split())
WV = [list(map(int, input().split())) for _ in range(N)]
WV = sorted(WV, key=lambda x: -x[1])
X = list(map(int, input().split()))
Query = [list(map(int, input().split())) for _ in range(Q)]
for q in Query:
    l, r = q
    tmp_box = X[:(l-1)] + X[r:]
    tmp_box.sort()
    tmp_val = 0
    for w, v in WV:
        for i, x in enumerate(tmp_box):
            if w <= x:
                tmp_box.pop(i)
                tmp_val += v
                break
    print(tmp_val)

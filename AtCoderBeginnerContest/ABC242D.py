# https://atcoder.jp/contests/abc242/tasks/abc242_d

memo = [1]
for _ in range(63):
    memo.append(memo[-1] * 2)
alph = ["A", "B", "C"]
alph_2 = ["A", "C", "B"]

S = input()
Q = int(input())
TK = [list(map(int, input().split())) for _ in range(Q)]
for t, k in TK:
    if 63 <= t:
        cnt = 0
        tmp = 1
        while tmp <= k:
            cnt += 1
            tmp *= 2
        ex = t % 3
        botm = alph[(alph.index(S[0]) + ex) % 3]
        now = alph_2[(alph_2.index(botm) + cnt % 3) % 3]
    else:
        base = memo[t]
        i = k // base if k % base else k // base - 1
        k -= i * base
        cnt = t
        now = S[i]

    while cnt:
        if now == "A":
            ne1, ne2 = "B", "C"
        elif now == "B":
            ne1, ne2 = "C", "A"
        else:
            ne1, ne2 = "A", "B"

        if memo[cnt] // 2 < k:
            now = ne2
            k -= memo[cnt] // 2
        else:
            now = ne1
        cnt -= 1
    print(now)

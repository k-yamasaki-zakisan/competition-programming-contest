# https://atcoder.jp/contests/abc195/tasks/abc195_e

N = int(input())
S = input()
X = input()

X = X[::-1]
S = S[::-1]

E = {0}
for x, s in zip(X, S):
    F = E
    s = int(s)
    if x == "T":
        E = {a for a in range(7) if ((10 * a) % 7 in F) or ((10 * a + s) % 7 in F)}
    else:
        E = {a for a in range(7) if ((10 * a) % 7 in F) and ((10 * a + s) % 7 in F)}
print("Takahashi" if 0 in E else "Aoki")

# https://atcoder.jp/contests/typical90/tasks/typical90_bo

def Base_10_to_n(X: int, n) -> str:
    if (int(X//n)):
        return Base_10_to_n(int(X//n), n)+str(X % n)
    return str(X % n)


def Base_n_to_10(X: str, n) -> int:
    out = 0
    for i in range(1, len(str(X))+1):
        out += int(X[-i])*(n**(i-1))
    return out


N, K = map(int, input().split())
for _ in range(K):
    r1: int = Base_n_to_10(str(N), 8)
    r2: str = Base_10_to_n(r1, 9)
    r2 = r2.replace('8', '5')
    N = r2
print(N)

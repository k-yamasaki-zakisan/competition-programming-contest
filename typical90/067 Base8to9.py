# https://atcoder.jp/contests/typical90/tasks/typical90_bo

def Base_10_to_9(X: int):
    if X == 0:
        return "0"
    res = ""
    while 0 < X:
        res = str(X % 9) + res
        X //= 9
    return str(res)


N, K = map(int, input().split())
tmp = str(N)
for _ in range(K):
    tmp_10 = int(tmp, 8)
    tmp_9 = Base_10_to_9(int(tmp_10))
    num = ''
    for s in tmp_9:
        s = str(s)
        if s == '8':
            num += '5'
        else:
            num += s
    tmp = num
print(tmp)

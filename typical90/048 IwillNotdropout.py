# https://atcoder.jp/contests/typical90/tasks/typical90_av

N, K = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]
memo = []
for a, b in AB:
    memo.append(b)
    memo.append(a-b)
memo.sort(reverse=True)
print(sum(memo[:K]))

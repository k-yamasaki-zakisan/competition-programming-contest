# https://atcoder.jp/contests/typical90/tasks/typical90_bd

N, S = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]
memo = {}
for i in range(N):
    a, b = AB[i]
    if i == 0:
        memo[a] = 'A'
        memo[b] = 'B'
    else:
        tmp = {}
        for key, val in memo.items():
            if key+a <= S:
                tmp[key+a] = val+'A'
            if key+b <= S:
                tmp[key+b] = val+'B'
        memo = tmp
if S in memo and len(memo[S]) == N:
    print(memo[S])
else:
    print('Impossible')

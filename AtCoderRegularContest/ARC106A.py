# https://atcoder.jp/contests/arc106/tasks/arc106_a

N = int(input())

for i in range(1,1001):
    for j in range(1, 1001):
        if 3**i+5**j == N:
            print(i, j)
            exit()
print(-1)
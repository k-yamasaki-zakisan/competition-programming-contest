#https://atcoder.jp/contests/judge-update-202004/tasks/judge_update_202004_b

n=int(input())
red = []
blue = []
for _ in range(n):
    x, c = map(str,input().split())
    x = int(x)
    if c == 'R':
        red.append(x)
    else:
        blue.append(x)
red.sort()
blue.sort()

for num in red:
    print(num)
for num in blue:
    print(num)

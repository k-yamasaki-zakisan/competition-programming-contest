#https://atcoder.jp/contests/diverta2019-2/tasks/diverta2019_2_b

n=int(input())

if n == 1:
    print(1)
    exit()

ball_xy = []
for _ in range(n):
    x, y = (int(x) for x in input().split())
    ball_xy.append([x, y])

distance = {}

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if (ball_xy[i][0]-ball_xy[j][0], ball_xy[i][1]-ball_xy[j][1]) in distance:
            distance[(ball_xy[i][0]-ball_xy[j][0], ball_xy[i][1]-ball_xy[j][1])] += 1
        else:
            distance[(ball_xy[i][0]-ball_xy[j][0], ball_xy[i][1]-ball_xy[j][1])] = 1

cost_0 = max(distance.values())

print(n-cost_0)

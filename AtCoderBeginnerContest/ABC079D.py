#https://atcoder.jp/contests/abc079/tasks/abc079_d

def warshall_floyd(d):
    for k in range(10):
        for i in range(10):
            for j in range(10):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d
 
 
h, w = list(map(int, input().split())) 
 
power = [list(map(int, input().split())) for i in range(10)] 

power = warshall_floyd(power)

ans = 0
for i in range(h):
    wall = list(map(int, input().split()))  
    for key in wall:
        if key == -1:
            continue
        ans += power[key][1]
print(ans)

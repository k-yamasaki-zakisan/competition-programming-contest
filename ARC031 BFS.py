#https://atcoder.jp/contests/arc031/tasks/arc031_2

from collections import Counter
 
land = []
edge = ["x"]*(12)
okosu = 0
 
for _ in range(10):
    line = list(input())
    okosu += Counter(line)["o"]
    line = ["x"] + line + ["x"]
    land.append(line)
 
land = [edge] + land + [edge]
 
for sx in range(1 , 11):
    for sy in range(1 , 11):
        if land[sy][sx] == "x":
            tmp = land[sy][sx]
            land[sy][sx] = "o"
        else:
            continue
        stack = [[sx , sy]]
        visited = [[False]*12 for _ in range(12)]
        visited[sy][sx] = True
        okosu2 = 0
        while stack:
            x , y = stack.pop()
            if okosu == okosu2:
                print("YES")
                exit()
            hjkl = [[x-1 , y] , [x , y-1] , [x+1 , y] , [x , y+1]]
            for dx , dy in hjkl:
                if land[dy][dx] == "x" or visited[dy][dx] is True:
                    continue
                stack.append([dx , dy])
                visited[dy][dx] = True
                okosu2 += 1
        land[sy][sx] = tmp
        if okosu == okosu2:
            print("YES")
            exit()
 
print("NO")

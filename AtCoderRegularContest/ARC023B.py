#https://atcoder.jp/contests/arc023/tasks/arc023_2

from collections import deque
 
h,w,limit_step = (int(x) for x in input().split())

takoyaki_counter = []

for _ in range(h):
    a = list(map(int,input().split()))
    takoyaki_counter.append(a)

step_counter_memo = [[-1 for i in range(w)] for j in range(h)]

step_counter_memo[0][0] = 0

step = deque([[0, 0]])

if limit_step%2==0:
    ans = takoyaki_counter[0][0]
else:
    ans = 0
 
while len(step) > 0:
    y, x = step.popleft()
    
    if step_counter_memo[y][x] == limit_step:
        continue
    
    for dy, dx in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
        ny = y + dy
        nx = x + dx
        if -1 < ny < h and -1 < nx < w:
            if step_counter_memo[ny][nx] == -1:
                step_counter_memo[ny][nx] = step_counter_memo[y][x] + 1
                step.append([ny, nx])
                if (limit_step - step_counter_memo[ny][nx])%2==0:
                    ans = max(ans, takoyaki_counter[ny][nx])
                
print(ans)

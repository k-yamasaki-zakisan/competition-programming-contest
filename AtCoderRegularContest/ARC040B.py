#https://atcoder.jp/contests/arc040/tasks/arc040_b

from collections import deque

n,r = map(int,input().split())

s = list(input())

non_color_point = deque()

for i in range(n):
    if s[i] == '.':
        non_color_point.append(i)

takahashi_point = 0

color_jack_reach = 0

ans = 0

while len(non_color_point) > 0:
    if  non_color_point[-1]-non_color_point[0] < r:
        ans += max((non_color_point[-1]-(r-1))-takahashi_point,0)
        ans += 1
        break
    ans += non_color_point[0]-takahashi_point
    takahashi_point = non_color_point[0]
    color_jack_reach = takahashi_point+r-1
    ans += 1
    #print(non_color_point)
    while non_color_point[0] <= color_jack_reach:
        non_color_point.popleft()

print(ans)

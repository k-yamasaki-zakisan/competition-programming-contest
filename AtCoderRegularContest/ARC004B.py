#https://atcoder.jp/contests/arc004/tasks/arc004_2

n=int(input())
max_distance = 0
max_point = 0
 
for _ in range(n):
    a = int(input())
    max_distance += a
    max_point = max(max_point, a)
 
min_distance = max(0, max_point-(max_distance-max_point))
 
print(max_distance)
print(min_distance)

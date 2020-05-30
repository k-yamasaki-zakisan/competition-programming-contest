#https://atcoder.jp/contests/keyence2020/tasks/keyence2020_b


n=int(input())
ab = []
for _ in range(n):
    a, b = (int(x) for x in input().split())
    ab.append([a-b, a+b])
ab = sorted(ab, key=lambda x: x[1])

right_reach = ab[0][1]

count = 0

for i in range(1,n):
    if ab[i][0] < right_reach:
        count += 1
    else:
       right_reach =  ab[i][1]
print(n-count)

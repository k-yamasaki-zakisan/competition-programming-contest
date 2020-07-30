#https://atcoder.jp/contests/code-festival-2015-morning-middle/tasks/cf_2015_morning_easy_c

n,k,m,r = map(int,input().split())
stock_point = []
for _ in range(n-1):
    s=int(input())
    stock_point.append(s)

stock_point.sort(reverse=True)

tmp_point = sum(stock_point[:k-1])

last_exam_point = r*k-tmp_point

if n != k and last_exam_point <= stock_point[k-1]:
    print(0)
else:
    if m < last_exam_point:
        print(-1)
    else:
        print(last_exam_point)

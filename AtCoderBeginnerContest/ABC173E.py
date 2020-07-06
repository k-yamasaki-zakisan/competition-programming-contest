#https://atcoder.jp/contests/abc173/tasks/abc173_e

#オーバーフロ
from collections import deque

mod = 1000000007

n,k = map(int,input().split())

a = list(map(int,input().split()))

plus_1 = deque()
minus_1 = deque()
plus_2 = deque()
minus_2 = deque()

a.sort()

for i in a:
    if i > 0:
        plus_2.append(i)
    else:
        minus_1.append(i)

a.sort(reverse=True)

for i in a:
    if i > 0:
        plus_1.append(i)
    else:
        minus_2.append(i)

maxa = 1

mini = 1

i = 0

while i < k:
    if len(plus_1) > 1 and len(minus_1) > 1:
        if plus_1[0]*plus_1[1] < minus_1[0]*minus_1[1] and i+2<=k:
            maxa *= minus_1[0]*minus_1[1]
            minus_1.popleft()
            minus_1.popleft()
            i += 2
        else:
            maxa *= plus_1[0]
            plus_1.popleft()
            i += 1
    elif len(plus_1):
        maxa *= plus_1[0]
        plus_1.popleft()
        i += 1
    else:
        maxa *= minus_1[0]
        minus_1.popleft()
        i += 1

i = 0

while i < k:
    if len(plus_2) and len(minus_2):
        if plus_2[0] < abs(minus_2[0]):
            mini *= plus_2[0]
            plus_2.popleft()
        else:
            mini *= minus_2[0]
            minus_2.popleft()
    elif len(plus_2):
        mini *= plus_2[0]
        plus_2.popleft()
    else:
        mini *= minus_2[0]
        minus_2.popleft()
    i += 1

if maxa > 0:
    print(maxa%mod)
else:
    print(mini%mod)

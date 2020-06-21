#https://atcoder.jp/contests/indeednow-quala/tasks/indeednow_2015_quala_3

n=int(input())
ab = []
for _ in range(n):
    a = int(input())
    if a != 0:
        ab.append(a)
ab.sort(reverse=True)
#print(ab)
q=int(input())
for _ in range(q):
    k = int(input())
    try:
        print(ab[k]+1)
    except:
        print(0)

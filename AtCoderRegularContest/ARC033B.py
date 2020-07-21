#https://atcoder.jp/contests/arc033/tasks/arc033_2

x,y = map(int,input().split())

a = list(map(int,input().split()))

b = list(map(int,input().split()))

a_dec = {}

for aa in a:
    if aa in a_dec:
        a_dec[aa] += 1
    else:
        a_dec[aa] = 1

b_dec = {}

for bb in b:
    if bb in b_dec:
        b_dec[bb] += 1
    else:
        b_dec[bb] = 1

bunsi = 0

for key in a_dec.keys():
    if key in b_dec:
        bunsi += 1

print(bunsi/(x+y-bunsi))

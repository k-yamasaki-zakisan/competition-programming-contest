#https://atcoder.jp/contests/arc053/tasks/arc053_b

S = list(input())
hasi = {}
for s in S:
    if s in hasi:
        hasi[s] += 1
    else:
        hasi[s] = 1
#核となる1と２で割れるペアに分ける
kisu = 0
gusu = 0
for key, val in hasi.items():
    if val%2==1:
        hasi[key] -= 1
        kisu += 1
    gusu += hasi[key]
#回分になる最小分割回数を求めて分割後の最小回分を算出
if 0 <= kisu <= 1:
    print(kisu+gusu)
else:
    tmp = (gusu//2)//kisu
    print(tmp*2+1)
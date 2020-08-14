#https://atcoder.jp/contests/abc063/tasks/arc075_b

N,A,B = map(int,input().split())
H = []
for _ in range(N):
    h = int(input())
    H.append(h)

ok = 1000000000
ng = 0

while ok != ng+1:
    mid = (ok+ng)//2
    range_damage = mid*B
    attack_count = 0
    for value in H:
        if range_damage < value:
            if (value - range_damage)%(A-B)==0:
                attack_count += (value - range_damage)//(A-B)
            else:
                attack_count += 1+(value - range_damage)//(A-B)

    if attack_count <= mid:
        ok = mid
    else:
        ng = mid
print(ok)

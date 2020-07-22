#https://atcoder.jp/contests/arc030/tasks/arc030_1

n=int(input())

k=int(input())

katamari = n

bara = 0

while bara < k and 2 < katamari:
    if bara == 0 and katamari < 4:
        bara = 1
        katamari = 1
        break

    katamari -= 2
    
    if bara == 0 :
        bara += 2
        if katamari < 4:
            katamari = 1
    else:
        bara += 1
        if katamari < 4:
            katamari = 1
    #print(bara, katamari)
    
if k <= bara:
    print('YES')
else:
    print('NO')

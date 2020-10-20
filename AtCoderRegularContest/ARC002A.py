# https://atcoder.jp/contests/arc002/tasks/arc002_1

N = int(input())

if N%4 == 0:
    if N%100==0:
        if N%400==0:
            print('YES')
            exit()
        else:
            print('NO')
            exit()
    else:
        print('YES')
        exit()
else:
    print('NO')
    exit()

print('NO')
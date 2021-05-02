# https://atcoder.jp/contests/zone2021/tasks/zone2021_c

def check(border: int) -> bool:
    s = set()
    for abcde in ABCDE:
        flag = False
        ok_status = 0
        for i, num in enumerate(abcde):
            if border <= num:
                flag = True
                ok_status += 10**i
        if flag:
            s.add(str(ok_status).zfill(5))
    s = list(s)
    len_s = len(s)
    for x in range(len_s):
        for y in range(len_s):
            for z in range(len_s):
                a = int(s[x][0]) or int(s[y][0]) or int(s[z][0])
                b = int(s[x][1]) or int(s[y][1]) or int(s[z][1])
                c = int(s[x][2]) or int(s[y][2]) or int(s[z][2])
                d = int(s[x][3]) or int(s[y][3]) or int(s[z][3])
                e = int(s[x][4]) or int(s[y][4]) or int(s[z][4])
                if a and b and c and d and e:
                    return True
    return False


N = int(input())
ABCDE = [tuple(map(int, input().split())) for i in range(N)]
ok = 0
ng = 10**9 + 1
while 1 < ng-ok:
    mid = (ok+ng) // 2
    if check(mid):
        ok = mid
    else:
        ng = mid
print(ok)

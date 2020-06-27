#https://atcoder.jp/contests/abc161/tasks/abc161_d

from collections import deque

n=int(input())

if n < 10:
    print(n)
else:
    check_box = deque([1,2,3,4,5,6,7,8,9])
    check_num = 9
    while True:
        add_num = check_box.popleft()
        add_num = str(add_num)

        if int(add_num[-1]) - 1 >= 0:
            check_box.append(int(add_num + str(int(add_num[-1]) - 1)))
            check_num += 1
            if check_num == n:
                    print(add_num + str(int(add_num[-1]) - 1))
                    exit()

        check_num += 1
        check_box.append(int(add_num + add_num[-1]))
        if check_num == n:
                print(add_num + add_num[-1])
                exit()

        if int(add_num[-1]) + 1 <= 9:
            check_box.append(int(add_num + str(int(add_num[-1]) + 1)))
            check_num += 1
            if check_num == n:
                    print(add_num + str(int(add_num[-1]) + 1))
                    exit()
        

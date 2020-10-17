# https://atcoder.jp/contests/arc044/tasks/arc044_a

import math

def is_prime(n:int) -> bool:
    if n == 1: return False
 
    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False
 
    return True

N = input()

if int(N) == 1:
    print('Not Prime')
    exit()

if is_prime(int(N)):
    print('Prime')
    exit()

tmp = 0
for i in list(N):
    i = int(i)
    tmp += i
if int(N[-1])%2 == 1 and int(N[-1]) != 5 and tmp%3 != 0:
    print('Prime')
    exit()

print('Not Prime')
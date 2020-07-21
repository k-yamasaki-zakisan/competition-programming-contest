#https://atcoder.jp/contests/arc026/tasks/arc026_2

def divisor(p):
    sum_divisor = 1
    for i in range(2,(int(p**0.5)+1)):
        if p%i==0:
            sum_divisor += i
            if i != p//i:
                sum_divisor += p//i
                
    return sum_divisor

n=int(input())

if n == 1:
    print('Deficient')
    exit()

sum_divisor = divisor(n)

if sum_divisor == n:
    print('Perfect')
elif sum_divisor < n:
    print('Deficient')
else:
    print('Abundant')

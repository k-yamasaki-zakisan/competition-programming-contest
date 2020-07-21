#https://atcoder.jp/contests/arc056/tasks/arc056_a

a,b,k,l = map(int,input().split())

one_buy = a*k

set_buy = (k//l)*b+(k%l)*a

set_buy_over = (1+k//l)*b

print(min(one_buy,set_buy,set_buy_over))

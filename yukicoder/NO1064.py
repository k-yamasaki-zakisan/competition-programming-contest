#https://yukicoder.me/problems/no/1064

a,b,c,d = map(int,input().split())

x_1 = (-1*(a-c)+((a-c)**2-4*2*(b-d))**0.5)/4
x_2 = (-1*(a-c)-((a-c)**2-4*2*(b-d))**0.5)/4

if isinstance(x_1, complex):
    print('No')
elif x_1 == x_2:
    print('Yes')
else:
    y_1 = x_1**2 + a*x_1 + b
    y_2 = x_2**2 + a*x_2 + b
    p = (y_2-y_1)/(x_2-x_1)
    q = y_1-p*x_1
    print(p, q)

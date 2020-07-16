#https://atcoder.jp/contests/abc027/tasks/abc027_c

n=int(input())

if n == 1 or n == 2:
    print('Aoki')
    exit()

count = 0

tmp_point=1

while tmp_point < n:
    tmp_point = tmp_point*2+1
    count += 1

simulation = 1

if count%2==1:
    for i in range(n):
        if i%2==0:
            simulation = simulation*2
        else:
            simulation = simulation*2+1
        #print(simulation)
        if n < simulation:
            if i%2==0:
                print('Aoki')
                break
            else:
                print('Takahashi')
                break
else:
    for i in range(n):
        if i%2==1:
            simulation = simulation*2
        else:
            simulation = simulation*2+1
        #print(simulation)
        if n < simulation:
            if i%2==0:
                print('Aoki')
                break
            else:
                print('Takahashi')
                break

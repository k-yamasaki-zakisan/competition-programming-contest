#https://atcoder.jp/contests/abc175/tasks/abc175_d

N,K = map(int,input().split())

P = list(map(int,input().split()))

C = list(map(int,input().split()))

ans = -10000000000

if K <= N:
    for i in range(N):
        count = 0
        tmp_point = 0
        nv = i
        while count < K:
            nvv = P[nv]
            nvv -= 1
            tmp_point += C[nvv]
            count += 1
            nv = nvv
            ans = max(ans, tmp_point)
    print(ans)
else:
    loop = [0]*N
    for i in range(N):
        count = 0
        check = [False]*N
        tmp_point = 0
        nv = i
        while True:
            nvv = P[nv]
            nvv -= 1
            if check[nvv] == True:
                break
            check[nvv] = True
            tmp_point += C[nvv]
            count += 1
            nv = nvv
            ans = max(ans, tmp_point)
        loop[i] = [tmp_point, count, i]
    loop.sort(reverse=True)
    #print(loop)
    new_ans = -10000000
    for value, counter, key in loop:
        if value < 0:
            break
        shou = K//counter-1
        amari = K%counter+counter
        tmp_ans = value*shou
        new_ans = max(new_ans, tmp_ans)
        count = 0
        nv = key
        while count < amari:
            nvv = P[nv]
            nvv -= 1
            tmp_ans += C[nvv]
            count += 1
            nv = nvv
            new_ans = max(new_ans, tmp_ans)

        
    print(max(loop[0][0], ans, new_ans))


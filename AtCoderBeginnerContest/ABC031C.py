#https://atcoder.jp/contests/abc031/tasks/abc031_c

n=int(input())

a = list(map(int,input().split()))

ans = -100000000000

for i in range(n):
    aoki_point = []
    for j in range(n):
        if i == j:
            continue
        left, right = min(i,j), max(i,j)

        tmp_geme_histroy = a[left:right+1]
        tmp_takahashi_point = 0
        tmp_aoki_point = 0
        for k in range(len(tmp_geme_histroy)):
            if k%2==0:
                tmp_takahashi_point += tmp_geme_histroy[k]
            else:
                tmp_aoki_point += tmp_geme_histroy[k]
        aoki_point.append([tmp_aoki_point, tmp_takahashi_point])
    aoki_max_point = -1000000000000
    #print(aoki_point)
    for x in range(len(aoki_point)):
        if aoki_max_point < aoki_point[x][0]:
            aoki_max_point = aoki_point[x][0]
            aoki_max_point_index = x
    ans = max(ans, aoki_point[aoki_max_point_index][1])

print(ans)

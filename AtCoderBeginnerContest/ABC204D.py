# https://atcoder.jp/contests/abc204/tasks/abc204_d

N = int(input())
T = list(map(int, input().split()))
total_times = sum(T)
times = {}
for t in T:
    tmp_times = {t: 1}
    for key in times.keys():
        tmp_times[key] = 1
        tmp_times[key+t] = 1
    times = tmp_times
ans = 10**10
for key in times.keys():
    ans = min(ans, max(total_times-key, key))
print(ans)

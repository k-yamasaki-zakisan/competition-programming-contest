# https://atcoder.jp/contests/abc007/tasks/abc007_4

def nums_of_num_include_4_or_9(N):
    length = len(N)
    dp = [[[0]*2 for _ in range(2)] for _ in range(length+1)]
    dp[0][0][0] = 1

    for i in range(length):
        max_digit = int(N[i])
        for flag_less in range(2):
            for flag_four_or_nine in range(2):
                range_digit = 9 if flag_less else max_digit
                for d in range(range_digit+1):
                    flag_less_next = 0
                    flag_four_or_nine_next = 0   
                    if flag_less==1 or d < max_digit:
                        flag_less_next = 1
                    if flag_four_or_nine==1 or d ==4 or d==9:
                        flag_four_or_nine_next = 1
                    dp[i+1][flag_less_next][flag_four_or_nine_next] += dp[i][flag_less][flag_four_or_nine]
    return dp[length][0][1]+dp[length][1][1]

A,B = map(str,input().split())
A = str(int(A)-1)
ans = nums_of_num_include_4_or_9(B)-nums_of_num_include_4_or_9(A)
print(ans)
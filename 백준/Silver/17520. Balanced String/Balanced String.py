import sys
input = sys.stdin.readline

# diff = 0개수 - 1개수
n = int(input())
dp = [[0]*3 for _ in range(n+1)] # (n+1)*3. length*diff

# 문자열 길이 1일 때 초기값
dp[1][2] = 1
dp[1][0] = 1 

for length in range(1, n):
    for diff_idx in range(3): # 0, 1, 2
        cnt = dp[length][diff_idx]
        if cnt == 0:
            continue
        diff = diff_idx - 1 # -1, 0, 1

        # 다음 문자열로 0 추가
        new_diff = diff + 1
        if -1 <= new_diff <= 1:
            dp[length+1][new_diff+1] = (dp[length+1][new_diff+1] + cnt) % 16769023
        
        # 다음 문자열로 1 추가
        new_diff = diff - 1
        if -1 <= new_diff <= 1:
            dp[length+1][new_diff+1] = (dp[length+1][new_diff+1] + cnt) % 16769023

print(sum(dp[n])% 16769023)
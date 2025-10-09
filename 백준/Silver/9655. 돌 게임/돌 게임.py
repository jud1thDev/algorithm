import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (n + 1)

if n >= 1:
    dp[1] = 1  # SK
if n >= 2:
    dp[2] = 0  # CY

for i in range(3, n + 1):
    if dp[i - 1] == 0 or dp[i - 3] == 0:
        dp[i] = 1
    else:
        dp[i] = 0
        
print("SK" if dp[n] == 1 else "CY")

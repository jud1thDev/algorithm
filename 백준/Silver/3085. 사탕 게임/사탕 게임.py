import sys
input = sys.stdin.readline

n = int(input())
candies = [list(input().strip()) for _ in range(n)]
ans = 1

for i in range(n):
    for j in range(n):
        if j+1 < n and candies[i][j] != candies[i][j+1]:
            candies[i][j], candies[i][j+1] = candies[i][j+1], candies[i][j]
            for r in range(n):
                cnt = 1
                for c in range(1, n):
                    cnt = cnt + 1 if candies[r][c] == candies[r][c-1] else 1
                    if cnt > ans: ans = cnt
            for c in range(n):
                cnt = 1
                for r in range(1, n):
                    cnt = cnt + 1 if candies[r][c] == candies[r-1][c] else 1
                    if cnt > ans: ans = cnt
            candies[i][j], candies[i][j+1] = candies[i][j+1], candies[i][j]

        if i+1 < n and candies[i][j] != candies[i+1][j]:
            candies[i][j], candies[i+1][j] = candies[i+1][j], candies[i][j]
            for r in range(n):
                cnt = 1
                for c in range(1, n):
                    cnt = cnt + 1 if candies[r][c] == candies[r][c-1] else 1
                    if cnt > ans: ans = cnt
            for c in range(n):
                cnt = 1
                for r in range(1, n):
                    cnt = cnt + 1 if candies[r][c] == candies[r-1][c] else 1
                    if cnt > ans: ans = cnt
            candies[i][j], candies[i+1][j] = candies[i+1][j], candies[i][j]

print(ans)
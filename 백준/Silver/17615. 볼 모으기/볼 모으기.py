import sys
input = sys.stdin.readline

# 구하는 것: 최소 이동횟수
n = int(input())
balls = input().strip()

# 왼쪽 끝 R 제거
i = 0
while i < n and balls[i] == 'R':
    i += 1
cnt1 = balls[i:].count('R')

# 오른쪽 끝 R 제거
i = n - 1
while i >= 0 and balls[i] == 'R':
    i -= 1
cnt2 = balls[:i+1].count('R')

# 왼쪽 끝 B 제거
i = 0
while i < n and balls[i] == 'B':
    i += 1
cnt3 = balls[i:].count('B')

# 오른쪽 끝 B 제거
i = n - 1
while i >= 0 and balls[i] == 'B':
    i -= 1
cnt4 = balls[:i+1].count('B')

print(min(cnt1, cnt2, cnt3, cnt4))
import sys
input = sys.stdin.readline

# 구하는 것: 햄버거를 먹을 수 있는 최대 사람 수
n, k = map(int, input().split())
positions = list(input())
used = [False]*n
count = 0

for i in range(n):
    if positions[i] == 'P':
        left = i - k
        right = i + k
        for j in range(left, right + 1):
            if 0 <= j < n and positions[j] == 'H' and not used[j]:
                used[j] = True
                count += 1
                break

print(count)
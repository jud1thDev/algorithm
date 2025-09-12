import sys
input = sys.stdin.readline

from collections import defaultdict

# 구하는 것: 먹을 수 있는 초밥의 가짓수의 최댓값
n, d, k, c = map(int, input().split())
belt = [int(input()) for _ in range(n)]

count = defaultdict(int)
kind = 0
answer = 0

# 초기 윈도우 설정
for i in range(k):
    if count[belt[i]] == 0:
        kind += 1
    count[belt[i]] += 1

answer = kind + (0 if count[c] else 1)

for i in range(1, n):
    out = belt[i - 1]
    count[out] -= 1
    if count[out] == 0:
        kind -= 1

    inn = belt[(i + k - 1) % n]
    if count[inn] == 0:
        kind += 1
    count[inn] += 1

    now = kind + (0 if count[c] else 1)
    answer = max(answer, now)

print(answer)
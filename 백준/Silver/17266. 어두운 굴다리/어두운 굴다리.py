import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
streetlamps = list(map(int, input().split()))
streetlamps.sort()

# 첫 구간
max_dist = streetlamps[0]

# 중간 구간들
for i in range(1, M):
    dist = (streetlamps[i] - streetlamps[i - 1]) // 2
    if (streetlamps[i] - streetlamps[i - 1]) % 2:
        dist += 1
    max_dist = max(max_dist, dist)

# 마지막 구간
max_dist = max(max_dist, N - streetlamps[-1])

print(max_dist)
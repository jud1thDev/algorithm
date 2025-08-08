import sys
input = sys.stdin.readline

n = int(input())
lines = []
for _ in range(n):
    a, b = map(int, input().split())
    lines.append((a, b))

lines.sort(key=lambda x: x[0])
b_positions = [b for _, b in lines]

d = [1]*n

for i in range(n):
    for j in range(i):
        if b_positions[j] < b_positions[i]:
            d[i] = max(d[i], d[j] + 1)

print(n - max(d))
import sys
input = sys.stdin.readline

n = int(input())
given = list(map(int, input().split()))
m = int(input())

low = 0
high = max(given)

while low <= high:
    mid = (low + high) // 2
    total = 0

    for g in given:
        total += min(g, mid)

    if total <= m:
        low = mid + 1
    else:
        high = mid - 1

print(high)
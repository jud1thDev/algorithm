import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
trees = list(map(int, input().strip().split()))

lo = 0
hi = max(trees)
answer = 0

while lo <= hi:
    mid = (lo + hi) // 2
    cut = sum(t - mid for t in trees if t > mid)

    if cut >= M:
        answer = mid
        lo = mid + 1
    else:
        hi = mid - 1

print(answer)
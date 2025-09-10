import sys
input = sys.stdin.readline

import heapq

# 구하는 것: N번째 큰 수
n = int(input())
heap = []
numbers = []
for _ in range(n):
    line = list(map(int, input().split()))
    for i in line:
        heapq.heappush(heap, i)
        if len(heap) > n:
            heapq.heappop(heap)

print(heap[0])
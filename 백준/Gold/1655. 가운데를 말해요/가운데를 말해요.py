import sys
input = sys.stdin.readline
import heapq

# BOJ 1655 - 가운데를 말해요
n = int(input())
left = []  
right = [] 
result = []

for _ in range(n):
    num = int(input())

    heapq.heappush(left, -num)

    if right and -left[0] > right[0]:
        heapq.heappush(right, -heapq.heappop(left))
        heapq.heappush(left, -heapq.heappop(right))
    
    if len(left) > len(right) + 1:
        heapq.heappush(right, -heapq.heappop(left))
    elif len(right) > len(left):
        heapq.heappush(left, -heapq.heappop(right))
    
    result.append(-left[0])

print('\n'.join(map(str, result)))
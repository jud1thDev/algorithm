import sys 
input = sys.stdin.readline
from collections import deque

# 구하는 것: 인접한 두 통나무 간의 높이의 차의 최댓값이 가장 작도록
t = int(input())
for _ in range(t):
    n = int(input())
    woods = list(map(int, input().split()))
    woods.sort()
    
    arranged = deque()
    for i in range(n):
        if i % 2 == 0:
            arranged.appendleft(woods[i])
        else:
            arranged.append(woods[i])
    
    ans = 0
    for i in range(n):
        diff = abs(arranged[i] - arranged[(i+1)%n])
        ans = max(ans, diff)
    print(ans)
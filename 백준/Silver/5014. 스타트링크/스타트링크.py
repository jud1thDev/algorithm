import sys
input = sys.stdin.readline
from collections import deque

# 구하는 것: s에서 g까지 가는 최소 버튼 누르기 횟수
f, s, g, u, d = map(int, input().split())

visited = [0] * (f + 1)
q = deque() 
q.append((s, 0)) # (현재 층, 누른 횟수)

while q:
    floor, cnt = q.popleft()
    if floor == g:
        print(cnt)
        break

    for next_floor in (floor + u, floor - d):
        if 1 <= next_floor <= f and not visited[next_floor]:
            visited[next_floor] = 1
            q.append((next_floor, cnt + 1))
else:
    print("use the stairs")
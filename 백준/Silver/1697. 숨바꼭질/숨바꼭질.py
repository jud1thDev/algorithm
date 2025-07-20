from collections import deque
import sys 
input = sys.stdin.readline

n, k = map(int, input().split())
visited = [False]*100001

# bfs
def bfs():
    queue = deque()
    queue.append((n, 0)) # 시작위치, 시간 0
    visited[n] = True

    while queue:
        cx, t = queue.popleft()
        if cx == k:
            return t
        for nx in (cx-1, cx+1, cx*2):
            if 0 <= nx <= 100000 and not visited[nx]:
                visited[nx] = True
                queue.append((nx, t+1))

print(bfs())
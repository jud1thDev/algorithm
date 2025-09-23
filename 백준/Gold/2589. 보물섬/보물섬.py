import sys
input = sys.stdin.readline
from collections import deque

# BOJ 2589
# 맵, 최단거리 => bfs

h, w = map(int, input().split())
grid = [list(input().strip()) for _ in range(h)]

directions = [(1,0), (-1, 0), (0, 1), (0, -1)]

def bfs(x, y):
    queue = deque()
    queue.append((x, y, 0)) # x, y, distance
    visited = [[False]*w for _ in range(h)]
    visited[x][y] = True
    max_distance = 0
    
    while queue:
        x, y, distance = queue.popleft()
        max_distance = max(max_distance, distance)
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < h and 0 <= ny < w:
                if not visited[nx][ny] and grid[nx][ny] == 'L':
                    visited[nx][ny] = True
                    queue.append((nx, ny, distance + 1))
    return max_distance

distance = 0
for i in range(h):
    for j in range(w):
        if grid[i][j] == 'L':
            distance = max(distance, bfs(i, j))

print(distance)
from collections import deque
import sys 
input = sys.stdin.readline

n, m = map(int, input().split())

# 맵 정보 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

# 이동방향 정의
directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

# bfs
queue = deque()
# 아기상어위치를 큐에 넣기(출발점)
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append((i, j))

while queue: # 큐가 빌 때까지
    x, y = queue.popleft()
    for dx, dy in directions:
        nx = x + dx
        ny = y + dy
        # 종료: 범위 벗어남
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        # 이동 조건: 0인 칸
        if graph[nx][ny] == 0: 
            graph[nx][ny] = graph[x][y] +1
            queue.append((nx, ny))

# 구하는 것: 안전거리의 최댓값
ans = max(max(row) for row in graph)
print(ans-1)  # 상어 위치가 1부터 시작하므로
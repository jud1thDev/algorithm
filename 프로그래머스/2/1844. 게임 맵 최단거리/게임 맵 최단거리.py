from collections import deque

# 구하는 것: 상대 팀 진영에 도착하기 위해서 지나가야 하는 칸의 개수의 최솟값
def solution(maps):
    n, m = len(maps), len(maps[0])
    visited = [[False]*m for _ in range(n)]

    # 이동 방향 (상, 하, 좌, 우)
    directions = [(-1,0), (1,0), (0,-1), (0,1)]

    queue = deque()
    queue.append((0,0,1))  # 시작점, 거리 1
    visited[0][0] = True

    while queue:
        x, y, dist = queue.popleft()

        # 목표 지점 도착 시 거리 반환
        if x == n-1 and y == m-1:
            return dist

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and maps[nx][ny] == 1:
                    visited[nx][ny] = True
                    queue.append((nx, ny, dist + 1))

    return -1  # 도달 불가 시

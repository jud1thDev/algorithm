import sys
from collections import deque
input = sys.stdin.readline

R, C = map(int, input().split())
cave = [list(input().strip()) for _ in range(R)]
N = int(input())
heights = list(map(int, input().split()))

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(sr, sc, visited):
    q = deque([(sr, sc)])
    visited[sr][sc] = True
    cluster = [(sr, sc)]

    while q:
        r, c = q.popleft()
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C:
                if cave[nr][nc] == 'x' and not visited[nr][nc]:
                    visited[nr][nc] = True
                    q.append((nr, nc))
                    cluster.append((nr, nc))
    return cluster

def is_ground(cluster):
    for r, c in cluster:
        if r == R - 1:
            return True
    return False

for i in range(N):
    h = R - heights[i]

    hit = None
    if i % 2 == 0:
        for c in range(C):
            if cave[h][c] == 'x':
                cave[h][c] = '.'
                hit = (h, c)
                break
    else:
        for c in range(C - 1, -1, -1):
            if cave[h][c] == 'x':
                cave[h][c] = '.'
                hit = (h, c)
                break

    if not hit:
        continue

    visited = [[False]*C for _ in range(R)]

    for dr, dc in dirs:
        nr, nc = hit[0] + dr, hit[1] + dc
        if 0 <= nr < R and 0 <= nc < C and cave[nr][nc] == 'x' and not visited[nr][nc]:
            cluster = bfs(nr, nc, visited)

            if is_ground(cluster):
                continue

            # 클러스터 제거
            for r, c in cluster:
                cave[r][c] = '.'

            # 떨어질 수 있는 거리 계산
            drop = 0
            while True:
                for r, c in cluster:
                    nr = r + drop + 1
                    if nr == R or cave[nr][c] == 'x':
                        break
                else:
                    drop += 1
                    continue
                break

            # 클러스터 내리기
            for r, c in cluster:
                cave[r + drop][c] = 'x'
            break

for row in cave:
    print(''.join(row))

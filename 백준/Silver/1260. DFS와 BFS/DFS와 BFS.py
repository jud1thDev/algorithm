from collections import deque
import sys
input = sys.stdin.readline

N, M, V = map(int, input().split())

# 맵 입력
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 방문 순서가 정점 번호가 작은 순서여야 하므로 정렬
for adj in graph:
    adj.sort()

# DFS
visited_dfs = [False] * (N+1)
dfs_result = []

def dfs(v):
    visited_dfs[v] = True
    dfs_result.append(v)
    for nv in graph[v]:
        if not visited_dfs[nv]:
            dfs(nv)

# BFS
visited_bfs = [False] * (N+1)
bfs_result = []

def bfs(start):
    queue = deque([start])
    visited_bfs[start] = True
    while queue:
        v = queue.popleft()
        bfs_result.append(v)
        for nv in graph[v]:
            if not visited_bfs[nv]:
                visited_bfs[nv] = True
                queue.append(nv)
dfs(V)
bfs(V)
print(*dfs_result)
print(*bfs_result)

import sys
from collections import deque

input = sys.stdin.readline

n = int(input().strip())
m = int(input().strip())

adj = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

INF = -1
dist = [INF] * (n + 1)
dist[1] = 0

q = deque([1])
while q:
    v = q.popleft()
    if dist[v] == 2:
        continue
    for u in adj[v]:
        if dist[u] == INF:
            dist[u] = dist[v] + 1
            q.append(u)

ans = sum(1 for i in range(2, n + 1) if 1 <= dist[i] <= 2)
print(ans)

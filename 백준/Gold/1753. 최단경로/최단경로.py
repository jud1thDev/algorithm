import sys
import heapq

input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())

graph = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

d = [0] * (V + 1) 

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    d[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if d[now] and dist > d[now]:
            continue
        for next_node, weight in graph[now]:
            cost = dist + weight
            if d[next_node] == 0 or cost < d[next_node]:
                d[next_node] = cost
                heapq.heappush(q, (cost, next_node))

dijkstra(K)

for i in range(1, V + 1):
    if i == K:
        print(0)
    elif d[i] == 0:
        print("INF")
    else:
        print(d[i])
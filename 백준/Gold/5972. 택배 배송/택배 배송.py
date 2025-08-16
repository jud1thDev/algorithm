import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))  # 양방향

def dijkstra(start):
    q = []
    distance = [INF] * (n + 1)
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for neighbor, cost in graph[now]:
            new_cost = dist + cost
            if new_cost < distance[neighbor]:
                distance[neighbor] = new_cost
                heapq.heappush(q, (new_cost, neighbor))

    return distance

ans = dijkstra(1)
print(ans[n])

import heapq

INF = 10**15

def dijkstra(start, n, graph):
    dist = [INF] * (n + 1)
    dist[start] = 0
    pq = [(0, start)]  # (누적비용, 노드)
    while pq:
        cost, now = heapq.heappop(pq)
        if cost > dist[now]:
            continue
        for nxt, w in graph[now]:
            nc = cost + w
            if nc < dist[nxt]:
                dist[nxt] = nc
                heapq.heappush(pq, (nc, nxt))
    return dist

def solution(n, s, a, b, fares):
    graph = [[] for _ in range(n + 1)]
    for c, d, f in fares:
        graph[c].append((d, f))
        graph[d].append((c, f))

    distS = dijkstra(s, n, graph)
    distA = dijkstra(a, n, graph)
    distB = dijkstra(b, n, graph)

    ans = INF
    for k in range(1, n + 1):
        if distS[k] == INF or distA[k] == INF or distB[k] == INF:
            continue
        ans = min(ans, distS[k] + distA[k] + distB[k])
    return ans
import sys 
input = sys.stdin.readline

n = int(input())
connect = int(input())

graph = [[] for _ in range(n+1)] # 0번은 안 사용하므로 
for _ in range(connect):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

visited = [False]*(n+1)

dfs(graph, 1, visited) # 1번 컴퓨터에서 시작

print(sum(visited)-1)
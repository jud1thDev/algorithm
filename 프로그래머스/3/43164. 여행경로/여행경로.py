from collections import defaultdict

# 방문하는 공항 경로를 배열에 담아 return
def solution(tickets):
    graph = defaultdict(list) 
    for a, b in tickets: 
        graph[a].append(b) # 특정 출발지에서 어느 목적지로 가는지 그래프화
    
    # 스택은 LIFO이므로 사전 역순으로 정렬
    for i in graph:
        graph[i].sort(reverse=True)
    
    stack = ['ICN']
    route = []
    
    while stack:
        top = stack[-1]
        if graph[top]:
            stack.append(graph[top].pop())
        else: 
            route.append(stack.pop())
            
    return route[::-1]
            
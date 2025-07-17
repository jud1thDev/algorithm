import sys 
input = sys.stdin.readline

# 구하고자 하는 것: 최소의 배추흰지렁이 마리 수 줄별로 출력

t = int(input())

def dfs(x, y):
    stack = [(x,y)]
    while stack:
        cx, cy = stack.pop() # current
        # 종료: 범위 벗어남
        if cx<=-1 or cx>=n or cy<=-1 or cy>=m:
            continue
        # 성공
        if graph[cx][cy] == 1: # 배추가 있는 곳이면 상하좌우를 살피자
            graph[cx][cy] = 0
            stack.append((cx-1, cy))
            stack.append((cx+1, cy))
            stack.append((cx, cy-1))
            stack.append((cx, cy+1))

for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0]*m for _ in range(n)] # 전체 맵을 0으로 초기화
    # 배추 위치 맵에 표시
    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1 

    result = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                dfs(i, j)
                result += 1
    print(result)
   
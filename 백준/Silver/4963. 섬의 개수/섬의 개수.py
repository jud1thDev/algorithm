import sys 
input = sys.stdin.readline

result = []

while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0: # 입력 끝
        break 

    # 맵 입력받기
    graph = []
    for _ in range(h):
        line = list(map(int, input().split()))
        graph.append(line)

    visited = [[False]*w for _ in range(h)]
    cnt = 0
    
    def dfs(x, y):
        stack = [(x, y)]
        while stack:
            cx, cy = stack.pop() # 현재 x, y. current.
            # 종료: 범위 내 아님
            if cx <= -1 or cx >= h or cy <= -1 or cy >= w:
                continue
            # 방문 조건
            if not visited[cx][cy] and graph[cx][cy]==1:
                visited[cx][cy] = True
                stack.append((cx+1, cy))
                stack.append((cx, cy+1))
                stack.append((cx-1, cy))
                stack.append((cx, cy-1))
                stack.append((cx-1, cy-1))
                stack.append((cx-1, cy+1))
                stack.append((cx+1, cy-1))
                stack.append((cx+1, cy+1))

                

    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1 and visited[i][j] == False:
                dfs(i, j)
                cnt += 1

    result.append(cnt)
    
for r in result:
    print(r)
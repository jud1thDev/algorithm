import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
Ix, Iy = -1, -1

for i in range(n):
    line = list(input().rstrip())
    graph.append(line)
    if 'I' in line:
        Ix = i
        Iy = line.index('I')

visited = [[False]*m for _ in range(n)]
ans = 0

stack = [(Ix, Iy)]
visited[Ix][Iy] = True

while stack:
    x, y = stack.pop()
    if graph[x][y] == 'P':
        ans += 1

    for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m:
            if not visited[nx][ny] and graph[nx][ny] != 'X':
                visited[nx][ny] = True
                stack.append((nx, ny))

if ans == 0:
    print("TT")
else:
    print(ans)
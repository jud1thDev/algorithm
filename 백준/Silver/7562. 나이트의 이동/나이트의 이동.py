from collections import deque

T = int(input())
for _ in range(T):
    l = int(input())
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())

    board = [[0]*l for _ in range(l)]
    dx = [2, 1, -1, -2, -2, -1, 1, 2]
    dy = [1, 2, 2, 1, -1, -2, -2, -1]

    q = deque()
    q.append((sx, sy))

    while q:
        x, y = q.popleft()
        if (x, y) == (ex, ey):
            print(board[x][y])
            break

        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < l and 0 <= ny < l and board[nx][ny] == 0:
                board[nx][ny] = board[x][y] + 1
                q.append((nx, ny))
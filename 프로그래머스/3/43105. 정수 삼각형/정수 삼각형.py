def solution(triangle):
    n = len(triangle)
    d = [[0] * (i + 1) for i in range(n)]  

    def dfs(i, j):
        if i == n - 1:  # 바닥
            return triangle[i][j]
        if d[i][j] != 0:  # 이미 계산
            return d[i][j]
        d[i][j] = triangle[i][j] + max(dfs(i + 1, j), dfs(i + 1, j + 1))
        return d[i][j]

    return dfs(0, 0)

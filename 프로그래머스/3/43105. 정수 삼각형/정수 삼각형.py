def solution(triangle):
    n = len(triangle)
    d = [0] * n
    d[0] = triangle[0][0]

    for i in range(1, n):
        row = triangle[i]
        for j in range(i, -1, -1):
            if j == 0:
                d[j] = d[j] + row[j]
            elif j == i:
                d[j] = d[j - 1] + row[j]
            else:
                d[j] = max(d[j - 1], d[j]) + row[j]

    return max(d)

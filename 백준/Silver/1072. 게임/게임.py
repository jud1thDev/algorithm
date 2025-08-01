x, y = map(int, input().split())

def binary_search(x, y):
    z = (y * 100) // x # 이제 형택이는 앞으로의 모든 게임에서 지지 않는다. z는 승률
    if z >= 99: 
        return -1

    start = 1
    end = 10**9
    result = -1

    while start <= end:
        mid = (start + end) // 2
        new_z = ((y + mid) * 100) // (x + mid)

        if new_z > z:
            result = mid
            end = mid - 1
        else:
            start = mid + 1

    return result

ans = binary_search(x, y)
print(ans)
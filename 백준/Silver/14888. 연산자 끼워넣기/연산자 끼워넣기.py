import sys 
input = sys.stdin.readline

# 구하고자 하는 것: 첫째 줄에 만들 수 있는 식의 결과의 최댓값을, 둘째 줄에는 최솟값
# 곱셈이 젤 큰 수를 만들 수 있을 것 같은데.. 그 후 로직이 생각 안나니 dfs 해야하나...
def solution():
    n = int(input())
    arr = list(map(int, input().split()))
    ops = list(map(int, input().split()))
    max_val, min_val = dfs(1, arr[0], ops, arr, n)
    print(max_val, min_val)

def dfs(idx, result, ops, arr, n):
    if idx == n:
        return result, result
    
    max_val = -int(1e9)
    min_val = int(1e9)

    # + 연산자
    if ops[0] > 0:
        ops[0] -= 1
        tmp_max, tmp_min = dfs(idx+1, result + arr[idx], ops, arr, n)
        ops[0] += 1
        max_val = max(max_val, tmp_max)
        min_val = min(min_val, tmp_min)

    # - 연산자
    if ops[1] > 0:
        ops[1] -= 1
        tmp_max, tmp_min = dfs(idx+1, result - arr[idx], ops, arr, n)
        ops[1] += 1
        max_val = max(max_val, tmp_max)
        min_val = min(min_val, tmp_min)

    # * 연산자
    if ops[2] > 0:
        ops[2] -= 1
        tmp_max, tmp_min = dfs(idx+1, result * arr[idx], ops, arr, n)
        ops[2] += 1
        max_val = max(max_val, tmp_max)
        min_val = min(min_val, tmp_min)

    # / 연산자
    if ops[3] > 0:
        ops[3] -= 1
        if result < 0:
            val = -(-result // arr[idx])
        else:
            val = result // arr[idx]
        tmp_max, tmp_min = dfs(idx+1, val, ops, arr, n)
        ops[3] += 1
        max_val = max(max_val, tmp_max)
        min_val = min(min_val, tmp_min)
    
    return max_val, min_val

solution()
